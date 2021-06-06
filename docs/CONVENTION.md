# Table of Contents
- [Table of Contents](#table-of-contents)
- [Convention for writing notes](#convention-for-writing-notes)
  - [Directory convention](#directory-convention)
    - [Directory structure](#directory-structure)
    - [Main directories](#main-directories)
  - [Note convention](#note-convention)
    - [Header](#header)
    - [Body](#body)
    - [Footer](#footer)

# Convention for writing notes
## Directory convention
All directories in the repository must obey the following conventions

[README](/README.md)  

### Directory structure
**Master note**. Each directory containing notes about a book or a field or something similar, must have a master note
* *Example*. Directory about OS should have a master note `Master note.md`
* *Master note content*. Master note contains links to notes in the directory with clear naming and explanation of each note

    $\to$ The naming and explanation of each note must be detail enough for readers to easily see what note they are seeking for

**Medias used in notes**. All medias used in a note must be put in the `media` directory, and be referenced with relative path from the project root

### Main directories
**`notes/`**. Knowledge notes directory

**`materials/`**. Books, slides, tutorials, and other materials

**`media/`**. Images, audio, etc. used in the notes

**`code/`**. Code snippets used in the notes, or for experimenting

## Note convention
All notes in the repository must obey the following conventions

### Header
**Title and tags**. Each note must include title and tags
* *Explain*. The first 4 lines of any note must be given as below (for example)

    ```
    ---
    title: Cache memory
    tags: Operating system
    ---
    ```

**Table of contents**. Each note must have ToC, except for draft notes. The ToC must be given right after the title and tags and before any note content
* *Example*.

    ```
    ---
    title: Cache memory
    tags: Operating system
    ---

    # Table of Contents
    - [Table of Contents](#table-of-contents)
    - [Convention for writing notes](#convention-for-writing-notes)
    - [Directory convention](#directory-convention)
    - [Note convention](#note-convention)
        - [Header](#header)
        - [Body](#body)
        - [Footer](#footer)
    ```

* *Auto-ToC*. You are allowed to use auto-ToC so long as this ToC can be displayed on all standard Markdown browsers, e.g. Github, HackMD, VScode, etc.

**H1 header**. After the ToC, each note must contain one and only one H1 header denoting the note title, e.g.

```
---
title: Cache memory
tags: Operating system
---

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Convention for writing notes](#convention-for-writing-notes)
  - [Directory convention](#directory-convention)
    - [Directory structure](#directory-structure)
    - [Main directories](#main-directories)
  - [Note convention](#note-convention)
    - [Header](#header)
    - [Body](#body)
    - [Footer](#footer)

# Cache memory
```

### Body

### Footer