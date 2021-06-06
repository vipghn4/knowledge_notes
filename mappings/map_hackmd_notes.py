import os
import glob
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParsrer()
    parser.add_argument("--raw_note_dir", type=str,
                        help="Path to downloaded HackMD note directory")
