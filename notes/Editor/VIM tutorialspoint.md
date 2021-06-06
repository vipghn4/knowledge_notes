---
title: VIM tutorialspoint
tags: Editor
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Tutorialspoint](#tutorialspoint)
  * [Basic](#basic)
  * [Edit](#edit)
  * [Navigation](#navigation)
  * [Buffering](#buffering)
  * [Search](#search)
  * [Working with multiple things](#working-with-multiple-things)
  * [Markers (bookmarks)](#markers-bookmarks)
  * [Folding](#folding)
  * [Remote editing](#remote-editing)
<!-- /TOC -->

# Tutorialspoint
## Basic
**Basic commands**.
* *Run VIM*. type `vi` or `vim`
    * *Open as read-only*. `vi -R filename`
* *Command line mode*.
    * *Edit existing file*. `:edit filename`
    * *Save changes*. `:w`
    * *Quit VIM*. `:q`
    * *Force quit*. `:q!`
    * *Save and quit VIM*. `:x` or equivalently `:wq`

**Help**. `:help`
* *Help on specific topic*. `:help <topic-name>`
* *Help without knowing topic name*. `:helpgrep <phrase>`

## Edit
**Edit commands**.
* *Insert new text*.
    * *Insert*.
        * *Insert text before cursor*. `i`
        * *Insert text at the beginning of line*. `I`
    * *Append*.
        * *Append text after cursor*. `a`
        * *Append text at the end of line*. `A`
* *Change existing text*.
    * *Remove then edit*.
        * *Remove characeter then edit*. `s`
        * *Remove text from cursor to EOL then edit*. `C` or `cc`
    * *Replace text*.
        * *Replace character*. `r`
        * *Replace text from cursor* (like `insert` in Windows). `R`
* *Remove text*.
    * *Remove character*. `x`
    * *Remove with direction*. `d{direction}`

* *Misc*.
    * *Insert blankline below and enter edit mode*. `o`
    * *Insert blankline above and enter edit mode*. `O`
    * *Join current line and next line*. `J`

**Quick editting**.
* *Change inner*. `ci*` where `i` can be
    * `w`, i.e. change inner word
    * `"`, i.e. change inner `"..."`
    * `t)`, i.e. change inner `(...)`
* *Move cursor*.
    * *To beginning*. `gg`
    * *To end*. `G`

## Navigation
**Basic navigation**. `h` (left), `l` (down), `k` (up), `j` (right)

**Useful navigation**.
* *Move cursor to the BOL or EOL*. `0` or `$`
* *Scroll up or down entire page*. `Ctrl + f` or `Ctrl + b`
* *Jump to line `n`*. `:n`
    * *Jump to first line*. `:0`
    * *Jump to last line*. `:$`
* *Word navigation*.
    * *Move to the beginning of the next word*. `w`
    * *Move to the end of the current word*. `e`
    * *Move cursor to the beginning of the previous word*. `b`
* *List all previous navigation (jumps)*. `:jumps`
    * *Jump back to the previous position*. `Ctrl + o`
    * *Jump back to the next position*. `Ctrl + i`

## Buffering
**Buffer**. Temporary memory used by Vim to carry out cut, copy, delete, undo, redo, etc.

**Swap**. A file created by Vim to store buffer contents periodically
* *Get swap file name*. `:swapname`

**Cut, copy, and paste**.
* *Single-position commands*.
    * *Delete current character*. `x`
    * *Delete previous character*. `X`
    * *Copy current character*. `y` (yank)
    * *Paste character at cursor position*. `p`
    * *Paste character before cursor position*. `P`
* *Multi-position commands*.
    * *Delete a word from cursor position*. `dw`
    * *Delete entire line from cursor position*. `D`
    * *Delete entire line*. `dd`
    * *Copy entire line*. `yy`
* *Misc*.
    * *Auto indent when paste*. `:set paste`

**Undo and redo**.
* *Undo*. `:u` or `:<number>u`
* *Redo*. `Ctrl + r`

## Search
**Search settings**.
* *Incremental search*.
    * *Enable*. `:set incsearch`
    * *Disable*. `:set noincsearch`
* *Highlight search*.
    * *Enable*. `:set hlsearch`
    * *Disable*. `:set nohlsearch`

**Search commands**.
* *Forward search*. `/<expression>`
    * *Repeat previous forward search*. `//`
* *Backward search*. `?<expression>`
    * *Repeat previous backward search*. `??`
* *Traverse results*.
    * *Next occurrence*. `n`
    * *Previous occurrence*. `N`

**Multiple-file search**. `:vimgrep <expression> <files-by-regular-expression>`
* *Next occurrence*. `cn`
* *Next file*. `cnf`
* *Previous occurrence*. `cN`
* *Previous file*. `cNf`

## Working with multiple things
**Multiple files**.
* *Load some file for editing*. `:e <filename>` or `:edit <filename>`

**Multiple buffers (or tabs)**.
* *Basic commands*.
    * *Add file into new buffer*. `:badd <filename>`
    * *Remove buffer*. `:bd` or `:bw`
    * *Load all buffers*. `:ball`
    * *List all buffers*. `:buffers`
* *Switch buffer*.
    * *Switch to `i`th buffer*. `:bi`
    * *Switch to next buffer*. `:bnext`, or `:bn`
    * *Switch to previous buffer*. `:bprevious`, `:bp`, or `:bN`
    * *Move to first buffer*. `:bf` or `:bfirst`
    * *Move to last buffer*. `:bl` or `:blast`

**Multiple tabs**.
* *New tab*. `:tabnew`
* *Open new file in tab*. `:tabnew <filename>`
* *Close current tab*. `:tabclose`
* *Move to next tab*. `:tabnext`
* *Move to previous tab*. `:tabprevious`
* *Move to first tab*. `:tabfirst`
* *Move to last tab*. `:tablast`

**Multiple windows**.
* *New window*.
    * `:new` or `:new <filename>`, or
    * `:sp` (horizontal split) or `:sp <filename>`
    * `:vsp` (vertical split) or `:vsp <filename>`
* *Close window*. `:close`
* *Switch between windows*.
    * `:winc <direction>` where `<direction>` can be `h, j, k, l`

**Multi-cursor**.
* *Start multi-cursor and add a virtual cursor + selection on the match of current word*. `Ctrl + n`
    * *Select next match*. `Ctrl + n`
    * *Skip next match*. `Ctrl + x`
    * *Select prev match*. `Ctrl + p`
* *Back to regular cursor*. `Esc `

## Markers (bookmarks)
**Create bookmark**.
* *Create local bookmark at the cursor position*. `m<lowercase>`, e.g. `ma`
* *Create global bookmark at the cursor position*. `m<uppercase>`
    * *Global bookmark*. Bookmarks among opened files

**Misc**.
* *List all bookmarks*. `:marks`
* *Remove bookmarks*.`:delm[arks] <bookmark_name>`
* *Jump to bookmark*.
    * *Jump to bookmark location*. ``<bookmark_name>`
    * *Jump to BOL of bookmark line*. `'<bookmark_name>`

## Folding
**Basic commands**.
* *Fold*
    * *Fold current code block*. `zc` (close)
    * *Close all next-level folds*. `zm`
    * *Close all folds*. `zM`
* *Unfold*
    * *Open current fold*. `zo` (open)
    * *Open all next-level folds*. `zr`
    * *Open all folds*. `zR`
* *Moving between folds*. `z<direction>` where `<direction>` is `j` or `k`

## Remote editing
**Basic commands**.
* *Open Vim with remote file*. `vi <file_location>`
* *Open new remote file in Vim*.
    * *Open for reading*. `Nread <file_location>`, i.e. Network read
    * *Open for writing*. `Nwrite <file_location>`, i.e. Network write

**Supported protocols**. FTP, SFTP, HTTP (read-only), rsync, SCP
