import os
import glob
import argparse

import numpy as np
import requests
from bs4 import BeautifulSoup

TITLE_LENGTH = len("title: ")
TAG_LENGTH = len("tags: ")

def refactor_md_file(path, image_dir):
    r"""Refactor the MD note"""
    with open(path) as f:
        lines = [line[:-1] for line in f.readlines()]
    lines = _truncate_note(path, lines)
    lines, title, tags = _extract_title_and_tags(path, lines)
    lines = _save_all_images_to_local(lines, image_dir)
    return lines, title, tags

def _truncate_note(path, lines):
    r"""Truncate empty lines in the header and footer of the note"""
    while lines[0] == "":
        del lines[0]
    while lines[-1] == "":
        del lines[-1]
    return lines

def _extract_title_and_tags(path, lines):
    r"""Get title ang tags from MD file"""
    assert lines[0] == "---", "{}: {} is not \"---\"".format(path, lines[0])
    assert lines[3] == "---", "{}: {} is not \"---\"".format(path, lines[3])

    # Get title
    if lines[1][:TITLE_LENGTH] == "title: ":
        title = lines[1][TITLE_LENGTH:]
    elif lines[2][:TITLE_LENGTH] == "title: ":
        title = lines[2][TITLE_LENGTH:]
    else:
        raise RuntimeError("Invalid note: {}".format(path))

    # Get tag
    if lines[1][:TAG_LENGTH] == "tags: ":
        tags = lines[1][TAG_LENGTH:]
    elif lines[2][:TAG_LENGTH] == "tags: ":
        tags = lines[2][TAG_LENGTH:]
    else:
        raise RuntimeError("Invalid note: {}".format(path))
    
    # Reformat note
    lines[1], lines[2] = "title: {}".format(title), "tags: {}".format(tags)
    return lines, title, tags

def _save_all_images_to_local(lines, image_dir):
    r"""Get all images in the note and save it to local

    Lines containing image link must be of the form
    * <img src="..." ...>
    * ![](...)
    """
    for i, line in enumerate(lines):
        if "<img src=" in line:
            image_link = _get_image_link_from_html_tag(line)
            pref = line[:line.find("<img src=")]
            suf = line[line.find("<img src="):]
            save_path = _save_image_from_link(image_link, image_dir)
            lines[i] = pref + "<img src=\"/{}\">".format(save_path)
        elif "![]" in line:
            image_link = _get_image_link_from_md_link(line)
            pref = line[:line.find("(")]
            suf = line[line.find("("):]
            save_path = _save_image_from_link(image_link, image_dir)
            lines[i] = pref + "(/{})".format(save_path)
    return lines

def _get_image_link_from_md_link(line):
    link = line[line.find("(")+1:line.rfind(")")]
    return link

def _get_image_link_from_html_tag(line):
    soup = BeautifulSoup(line, features="lxml")
    return soup.img["src"]

def _save_image_from_link(image_link, image_dir):
    r"""Download image from image_link and save to image_dir"""
    basename = os.path.basename(image_link)
    save_path = os.path.join(image_dir, basename)

    image_data = requests.get(image_link).content
    with open(save_path, 'wb') as handler:
        handler.write(image_data)
    return save_path

def save_md_file(lines, title, tags, path, dest_note_dir):
    r"""Save MD file to destination directory"""
    # Get save path
    basename = os.path.splitext(os.path.basename(path))[0]
    if basename[-1] == ")":
        basename = basename[:basename.rfind("(")-1]
    basename = basename + ".md"
    save_path = os.path.join(dest_note_dir, tags, basename)
    save_dir = os.path.dirname(save_path)

    # Check for duplication
    if os.path.exists(save_dir):
        to_save = not os.path.exists(save_path)
    else:
        os.makedirs(save_dir, exist_ok=True)
        to_save = True

    # Save file
    if to_save:
        with open(save_path, "w") as f:
            for i, line in enumerate(lines):
                if i != len(lines) - 1:
                    f.write(line+"\n")
                else:
                    f.write(line)
    else:
        raise RuntimeError("Cannot save file {}".format(save_path))

def print_unique_tags(all_tags):
    r"""Print all unique tags and their counts in HackMD raw note directory"""
    unique_tags, tag_counts = np.unique(all_tags, return_counts=True)
    for tag, count in zip(unique_tags, tag_counts):
        print("Tag {}: {} files".format(tag, count))

if __name__ == "__main__":
    r"""Process and map HackMD notes to their desired locations according
    to the convention for writing notes in `docs/CONVENTION.md`
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_note_dir", type=str,
                        help="Path to downloaded HackMD note directory")
    parser.add_argument("--dest_note_dir", type=str,
                        help="Path to destination HackMD note directory")
    parser.add_argument("--dest_image_dir", type=str,
                        help="Path to destination image directory")
    args = parser.parse_args()

    md_paths = []
    for path in os.listdir(args.raw_note_dir):
        if path.endswith('.md'):
            md_paths.append(os.path.join(args.raw_note_dir, path))

    all_tags = []
    for path in md_paths:
        print("Processing {}".format(path))
        lines, title, tags = refactor_md_file(path, args.dest_image_dir)
        save_md_file(lines, title, tags, path, args.dest_note_dir)
        all_tags.append(tags)
