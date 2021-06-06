---
title: Practical VIM
tags: Editor
---

# Table of Contents

[toc]

# Introduction
## Philosophy of Vim - Repeat!
**Philosophy of Vim**. Don't repeat yourself! Let's Vim does it for you!

**Basic commands and their repeats**.

| Intent | Act | Repeat | Reverse |
| --- | --- | --- | --- |
| Make a change | `{edit}` | `.` | `u` |
| Scan line for next character | `f{char}` | `;` | `,` |
| Scan document for next match of current word | `*` | `n` | `N` |

>**NOTE**. From the moment we enter Insert mode, e.g. pressing `i`, until we return to Normal mode, e.g. pressing `<Esc>`, Vim records every keystroke for repetition purpose
>* *Trick*. Vim prefers small insertion!

>**NOTE**. When we use the `.` command to repeat a change made to a visual selection, it repeats the change on the same range of text

**More advanved commands and their repeats**
| Intent | Act | Repeat | Reverse |
| --- | --- | --- | --- |
| Scan line for previous character | `F{char}` | `;` | `,` |
| Scan document for next match | `/{pattern}` | `n` | `N` |
| Scan document for previous match | `?{pattern}` | `n` | `N` |
| Substitution | `:s/target/replacement` | `&` | `u` |

# Modes
**Vim modes**. 
* *Insert mode* (hot key `i`). To enter / edit text
* *Command line mode* (hot key `:`). To enter commands
* *Visual mode* (hot key `v`). Visually select text and run commands upon
    * *Ordinary visual mode*. `v`
    * *Linewise visual mode*. `Shift + v`
    * *Blockwise visual mode*. `Ctrl + v`

## Normal mode
**Philosophy**. Pause with your brush off the page!
* *Explain*. Most of the time, you will not spend on Insert mode, but Normal mode instead

### Changes
**Chunking undos**. In nonmodal text editors, the editor could chunk a set of characters together so that each undo operation removed a word instead of a character
* *Default Vim undo chunk*. From the moment we enter Insert mode until we return to Normal mode, everything we do counts as a single change
    * *Consequence*. We can make the undo command operate on words, sentences, or paragraphs by moderating the use of `<Esc>`
* *How often should we leave Insert mode?*. Make each undoable chunk correspond to a thought
    * *Explain*. Each pause forms to a natural breaking thought
* *Tips*. Use `Esc + o` rather than `<Enter>` to break thoughts

>**NOTE**. Moving around, e.g. `hjkl`, in Insert mode resets the change

**Compose repeatable changes**. Compose our changes so that they can be repeated with the dot command
* *Example*. Use `daw` or `diw` (sing-step change) rather than `edbx` (three-step changes) to exploit `.` (repeat last change)

**Use counts to do simple arithmetic**. `<n_repeats><command>`

>**NOTE**. Don't count if we can repeat

## Insert mode
### Best practice for correction in Insert mode
**Instant corrections in Insert mode**. If we make a mistake while composing text in Insert mode, we can fix it immediately
* *Default correction manner*.
    1. Use backspace to erase
    2. Make a correction
* *Export corretion manner*.
    1. Delete the entire word
    2. Type the word out again

**Delete commands in Insert mode**.
* *Delete one character (backspace)*. `<C-h>`
* *Delete back one word*. `<C-w>`
* *Delete back to start of line*. `<C-u>`

### Best practice for getting back to Normal mode
**Commands to switch to normal mode**.

| Key strokes | Effects |
| --- | --- |
| `<Esc>` | Switch to Normal mode |
| `<C-]>` | Switch to Normal mode |
| `<C-o>` | Switch to Insert Normal mode |

**Insert Normal mode**. A special version of Normal mode
* *Usage*. When we are in Insert mode and we want to run only one Normal mode command, then continue where we left off in Insert mode

### Replace mode
**Replace mode**. Identical to Insert mode, excep that it overwrites existing text in the document
* *Engage Replace mode*. `R` (in Normal mode)
* *Exit Replace mode*. `<Esc>`

**Virtual Replace mode**. Identical to Replace mode, but treating tab character as though it consisted of spaces
* *Engage Virtual Replace mode*. `gR`
* *Explain*. We overwrite characters of screen real estate rather than dealing with the actual characters in the file

>**NOTE**. We should  use Virtual Replace mode rather than Replace mode

### Pasting from a register without leaving Insert mode
**Steps**.
1. Yank the text to be pasted
2. Go to the position to paste
3. `<C-r>{register}` to paste the text to current cursor position

>**NOTE**. By default, text are copied to register `0`

>**NOTE**. If we want to paste multiple lines of text, we should switch to Normal mode

**Back-of-the-envelope calculations in place**.
1. `<C-r>=` to enter expression register
2. Enter the expression to be evaluated
3. Press `<CR>` to finish the evaluation and insert the result to the cursor position

## Visual mode
**Visual mode**. Allow us to select a range of text, then operate upon it
* *Types of visual modes*.
    * *Character-wise visual mode*. We can select anything from a single character up to a range of characters within a line, or spanning multiple lines
    * *Line-wise visual mode*. Used when we want to operate on entire lines
    * *Block-wise visual mode*. Allow us to work with columnar regions of the document
* *Changes in Visual mode*. Any change in Normal mode, which changes only one character, will change all selected characters in the similar way for Visual mode

**Enabling visual modes**

| Mode | Enable command |
| --- | --- |
| Character-wise visual mode | `v` |
| Line-wise visual mode | `V` |
| Block-wise visual mode | `<C-v>` |
| Back to Normal mode | `<Esc>` |

**Toggling the free end of a selection**. `o`, i.e. jump between two ends of the selected range of text

**Insert mode within Visual mode**. As we change a word in block-wise Visual mode, all selected words in other lines are changed in the same way once we exit the Visual mode, e.g. `<Esc>`

## Command mode
### Introduction
**Command-line mode**. Prompt us to enter an Ex command, a search pattern, or an expression
* *Move to command-line mode and execute command*.
    1. Enter command-line mode by pressing `:`
    2. Type the name of a command
    3. Execute it by pressing `<CR>`
* *Exit command-line mode*. `<Esc>`
* *Other ways to enable command-line mode*.
    * *Enable command-line for searching*. `/`
    * *Enable command-line for accessing expression register*. `<C-r>=`

**Range in Vim**. `start,end` implies position, or line, from `start` to `end`
* *Special characters*. `$` (end), `.` (currrent line), `.+1` (line after current line)

>**NOTE**. We can use `%` to mean all the lines in the current file, i.e. `0,$`

**Common commands**.

| Command | Effect |
| --- | --- |
| `:[range]delete [x]` | Delete specified lines (into register x) |
| `:[range]yank [x]` | Yank specified lines (into register x) |
| `:[line]put [x]` | Put the text from register x after the specified line |
| `:[range]copy {address}` | Copy the specified lines to below the line specified by `{address}` |
| `:[range]move {address}` | Move the specified lines to below the line specified by `{address}` |
| `:[range]join` | Join the specified lines |
| `:[range] normal {commands}` | Execute Normal mode `{commands}` on each specified line |
| `:[range]substitute/{pattern}/{string}/[flags]` | Replace occurrences of `{pattern}` with `{string}` on each specified line |
| `:[range]global/{pattern}/[cmd]` | Execute the Ex command `[cmd]` on all specified lines where `{pattern}` matches |

**Other commands**.
* *Read and write files*. `:edit` and `:write`
* *Create tabs*. `:tabnew`
* *Switch tabs*.
    * *Switch to previous tab*. `gt`
    * *Switch to next tab*. `gt`
    * *Switch to specific tab*. `{tab_idx}gt`
* *Split windows*. `:split`
* *Interact with the argument list*. `:prev` or `:next`
* *Interact with the buffer list*. `:bprev` or `:bnext`

**Shared keys of Insert mode and Command-line mode**.
* `<C-w>` (delete backward to start of word)
* `<C-u>` (delete backward to start of line)
* `<C-r>{register}` (insert contents of a register to command)

**Normal mode vs Command-line mode**. Ex commands are long range and have the capacity to modify many lines in a single move 
* It can sometimes be quicker to use an Ex command than to get the same job done with Vim's Normal commands
* The greatest feature, which distinguishes Ex commands is their ability to be executed across many lines at the same time

### Execute a command on one or more consecutive lines
**Principle**. Many Ex commands can be given a `[range]` of lines to act upon. We can specify the start and end of a range with either a line number, a mark, or a pattern

**Use line numbers as an address**. If we enteran Ex command consisting only of a number


$\to$ Vim will interpret that as an address and move our cursor to the specified line

**Specify a range of lines by address**. We can specify a range of line by `{start_line},{end_line}`, where `{start}` and `{end}` are addresses

**Specify a range of lines by visual selection**. If we have selected a range of lines with line-wise Visual mode

$\to$ The command-line prompt will be prepopulated with the range `:'<,'>`, i.e. a range standing for the visual selection

**Specify a range of lines by patterns**. `:/<pattern>/,/<pattern>/`

**Modify an address using an offset**. `:{start+offset},{end+offset}`

**Discussion**. The syntax for defining a range is very flexible

### Duplicate or move lines using `:t` and `:m` commands
**Fast copy**. `:[range]t{address}`, i.e. short of `:[range]co[py]{address}`
* *Explain*. Equivalent to
    1. Select `[range]` in line-wise visual mode
    2. Yank, i.e. `y`
    3. Jump back to current line and paste, i.e. `p`

>**NOTE**. `:t` duplicates the current line, i.e. equivalent to `yyp`

* *Difference between `:t` and `yyp`*. `yyp` uses a register, while `:t` does not

    $\to$ We use `:t` to duplicate a line without overwriting the current value in the default register

**Move lines with `:m` command**. `:[range]move {address}`
* *Explain*. Equivalent to
    1. Select `[range]` with line-wise Visual mode
    2. Cut the chosen range, i.e. `d`
    3. Move to `{address}` and paste, i.e. `p`

### Run Normal mode commands across a range
**Syntax**. `:[range]normal {command}`

$\to$ We can combine expressive nature of Vim's Normal mode commands with the range of Ex commands

### Repeat the last Ex command
**Repeat the last Ex command**. `@:`

>**NOTE**. Once running `@:`, we can subsequently repeat it with `@@`
>$\to$ This obeys the mantra of Vim, i.e. act, repeat, and reverse

### Tab-complete the Ex commands
**Principle**. Just like in the shell, we can use `<Tab>` key to autocomplete commands at the prompt
* *List all command suggestions*. `<C-d>`, e.g. `:col<C-d>`
* *Scroll forward through the suggestions*. `<Tab>`
* *Scroll backward through the suggestions*. `<S-Tab>`

### Insert the current word at the command prompt
**Syntax**. `<C-r><C-w>`, i.e. copy the word under the cursor and insert it at the command-line prompt

### Run commands in the shell
**Syntax**. `:!{command}`

**Putting Vim in the background**. We can use `:shell` to switch to an interactive shell

>**NOTE**. When operating Vim, we are never more than a couple of keystrokes away from the shell

# Getting around faster
**Principle**. Motions are some of the most important commands for operating Vim

## Navigate inside files with motions
### Keep our fingers on the Home row
**How row positioning**. Our fingers should rest on the home row
* *Home row*. When poised in home row position, we can reach for any other key on the keyboard, withou having to move our hands or look at our fingers
    * Left fingers on `a`, `s`, `d`, `f`
    * Right fingers on `j`, `k`, `l`, `;`

>**NOTE**. Home row is the ideal posture for touch typing

**Basic moves in Vim**. `hjkl`
* *Pros*. Moving with `hjkl`, we do not need to move our hand away from its resting place on the home row
* *Cons*. When we are used to moving with `hjkl`, using other editor depending on arrow keys will be strange

**Leave our right hand where it belongs**.
* *QWERTY keyboard right hand positioning*. We show follow this manner
    * *Description*.
        * `jkl` fall directly below the index, middle, and ring fingers of the right hand
        * Use index finger to press `h` key, i.e. we have to reach for it
    * *Explain*. Vim provides much quicker ways of moving around

        $\to$ We are wasting keystrokes if we press `h` more than two times in a row
* *Bad practice*. To avoid reaching for `h` with index finger
    * *Description*. `hjkl` are each covered by a finger
* *Tricks*. 
    * Use `h` and `l` for off-by-one errors, when we narrowly miss our target
        
        $\to$ Otherwise, we should rarely touch them
    * Use character search commands often, i.e. `f{character}`

### Distinguish between real lines and display lines
**Moving based on display lines**. Use `g` prefix

**Basic moves between real lines and display lines**.
* *Moving up and down* 
    * *Between real lines*. `jk`
    * *Between display lines*, `g{move}` where `{move}` can be `jk`
* *Moving to start and end of lines*.
    * *Between real lines*. `0`, `^`, and `$`
    * *Between display lines*. `g{move}` where `{move}` can be `0`, `^`, and `$`

>**NOTE**. Most other text editors have no notion of the concept of real lines, i.e. they interact with display lines only

### Move word-wise
| Command | Move cursor |
| --- | --- |
| `w` | Forward to start of next word |
| `b` | Backward to start of current word / previous word |
| `e` | Forward to end of current / next word |
| `ge` | Forward to end of previous word |

>**NOTE**. We can think of the motions as coming in pairs, i.e. `w` and `b` (both target the start of a word), and `e` and `ge` (both target the end of a word)

>**NOTE**. Trying to memorize all of these commands is not easy and we should not do it
>$\to$ Start by using `w` and `b` commands, then `e` and `ge` optionally

**Combo with motion commands**. `ea`, i.e. move to the end of word then append, or `gea`

**Know our words from our WORDS**.
* *Word and WORD*.
    * *Word*. A sequence of letters, digits, and underscores, or a sequence of other nonblank characters separated with whitespace
    * *WORD*. A sequence of nonblank characters separated with whitespace
* *Motions for word and WORD*. Use WORD-wise motions if we want to move faster, and word-wise motion if we want a more fine-grained traversal
    * *Word-wise motion*. `w`, `b`, `e`, `ge`
    * *WORD-wise motion*. `W`, `B`, `E`, `gE`

### Find by character
**Syntax**. `f{char}`

>**NOTE**. This is one of the quickest methods of moving around in Vim

* *Repeat and search forward*. `;`
* *Repeat and search backward*. `,`

**Character search can include or exclude the target**.
| Command | Effect |
| --- | --- |
| `f{char}` | Forward to the next occurrence of `{char}` |
| `F{char}` | Backward to the previous occurrence of `{char}` |
| `t{char}` | Forward to the character before the next occurrence of `{char}` |
| `T{char}` | Forward to the character after the previous occurrence of `{char}` |
| `;` | Repeat the last character-search command |
| `,` | Reverse the last character-search command |

>**NOTE**. We should use `f{char}` and `F{char}` in Normal mode, when we want to move the cursor quickly within the current line

>**NOTE**. We should use `t{char}` and `T{char}` in combination with `d{motion}`or `c{motion}`, i.e. in Operator-Pending mode

**Think like a Scrabble player**. Some letter appear more frequently than others

$\to$ We should choose less common characters for use with `f{char}`

### Search to navigate
**Recommended behavior**. If we want to search for more than one character, or move beyond the current line, we can use the search command instead
* *Limitations of `f{char}`*.
    * `f{char}` can only search for a single character at a time
    * `f{char}` can only search within the current line

**Operate with a search motion**. We can use the search command from Visual and Operator-Pending modes also

### Trace our selection with precision text objects
**Text object**. Allow us to interact with parentheses, quotes, XML tags, etc. which appear in text
* *Definition*. Regions of text by structure
* *Explain*. Each opening `{` character is balanced by a closing `}` character. This is the same for `[`, `<`

**Vim for text objects**. Vim understands the structure of the well-formed patterns and it allows us to operate on the regions of text which they delimit
* *Syntax*. 
    * `{operator}i{closing_char}` to choose text within the text object, i.e. `i` is *inside*
        * `{operator}` are VIM operators, e.g. `d`, `c`, `v`, etc.
        * `closing_char` is the closing character of the text object
    * `{operator}a{closing_char}` to choose the whole text object, i.e. `a` is *around*, or *all*

**Performing operations with text objects**. We can use text objects in Visual mode and in Operator-pending mode

**Discussion**. Text objects are the next level up of `f{char}` and `/pattern<CR>` commands
* *Explain*.
    * `f{char}` and `/pattern<CR>` commands are flying kick to the head
    * Text objects are scissors kick which strikes two targets with a single move

### Delete around, or change inside
**Principle**. We can use keystrokes to choose a word or a sentence or a paragraph, i.e.

* *Bounded text objects*.
    
    | Keystrokes | Buffer contents |
    | --- | --- |
    | `w` | Current word |
    | `W` | Current WORD |
    | `s` | Current sentence |
    | `p` | Current paragraph |

    >**NOTE**. For bounded text objects, `i` includes the text itself, and `a` includes the text plus one space after or before the word

### Mark our place and snap back to it
**Mark**. Vim's mark allow us to jump quickly to locations of interest within a document

>**NOTE**. We can set marks manually, but Vim also keeps track of certain points of interest for us automatically

* *Syntax*. `m{a-zA-Z}`
    * *Lowercase marks*. Local marks of each individual buffer
    * *Uppercase marks*. Global marks
* *Jumping between marks*.
    * *Move to the line where a mark was set*. `'{mar}`
        * *Explain*. Position the cursor on the first non-whitespace character
        * *Usage*. Only when we want to use Ex command
    * *Move to the exact position of the mark*. ``{mark}`
        * *Usage*. If we care about restoring the exact position, or just getting to the right line

>**NOTE**. Letting the mark name `m` will give us a handy pair

**Automatic marks**.

| Keystrokes | Buffer contents                                       |
| ---------- | ----------------------------------------------------- |
| \`         | Position before the last jump within the current file |
| `.`        | Location of last change                               |
| `^`        | Location of last insertion                            |
| `[`        | Start of last change or yank                          |
| `]`        | End of last change or yank                            |
| `>`        | End of last visual selection                          |
| `<`        | Start of last visual selection                        |

# Files
## Manage multiple files
### Track open files with the buffer list
**Files and buffers**. When we are editting a file with Vim, we are not actually editting a file

$\to$ We are editting an in-memory representation of a file, i.e. a buffer in Vim's terminology
* *Locations*. Files are stored on disk, whereas buffers exist in memory
* *How a file is editted in Vim*. 
    1. When we open a file in Vim

        $\to$ Its contents are read into a buffer taking the same name as the file
    2. Initially, the contents of the buffer will be identical to the file

        $\to$ But the two will diverge as we make changes to the buffer
    3. If we decide to keep our changes

        $\to$ We can write the contents of the buffer back into the file
    
    >**NOTE**. Most Vim commands operate on buffers, but a few operate on files

**Buffer list**. Vim allows us to work on multiple buffers simultaneously
* *Start Vim with a buffer list*. `vim [pattern]`

    $\to$ This will open Vim with a buffer list corresponding to files whose names match `pattern`

    >**NOTE**. When Vim starts up, it shows a single window with a buffer representing the first file

* *List all buffers*. `:ls`
    * *The `%` symbol*. Indicate which of the buffers is visible in the current window
    * *The `#` symbol*. Indicate the alternate file

* *Switch between buffers*.
    * *Previous and next buffers*. `:bp` and `:bn`
    * *$i$th buffer*. `:b {i}`
    * *First and last buffers*. `:bfirst` and `:blast`
    * *Buffer with specific name*. `:b [buffer name]`

    >**NOTE**. We should map these commands to something easier to reach

**Deleting buffers**.
* *Buffer creattion*. Vim creates a new buffer any time we open a file
* *Buffer deletion*. `:bdelete {i}` or `:[range] bdelete`

>**NOTE**. Searching for buffer indices and deleting them is time-consuming
>$\to$ Unless we have a good reason to delete a buffer, we usually should not bother

>**NOTE**. Vim's built-in controls for managing the buffer list lack flexibility
>$\to$ If we want to arrange buffers in a way that makes sense for our workflow, attempting to organize the buffer list is not the way to go
>* *Altenative solution*. Divide our workspace using split windows, tab pages, or argument list

### Group buffers into a collection with argument list
**Group buffers into a collection with argument list**. The argument list is easily managed and can be useful for grouping a collection of files for easy navigation

$\to$ We can run an Ex command on each item in the argument list using `:argdo` comman

>**NOTE**. We can change the contents of argument list anytime we want
>$\to$ `:args` listing does not necessarily reflect the values passed to `vim` when we launched the editor

**Populate the argument list**. 
* *`:args`*. List files which was passed as an argument when we ran the `vim` command

>**NOTE**. `[ ]` indicating which of the files in the argument list is active

* *`:args {arglist}`*. Set the contents of the argument list
* *`{arglist}`*. Can include filenames, wildcards, or even the output from a shell command
* *Example*. `:args index.html app.js`

>**NOTE**. We can use backtick expansion, i.e. `:args `expansion``
>$\to$ Vim executes the text inside the backtick, using the output from it as the argument for `:args`

**Use argument list**.
* *Traverse files in argument list*. `:next` and `:prev`
* *Execute the same command on each buffer in the set*. `:argdo {cmd}` where `cmd` is any Ex command
    
    >**NOTE**. We can use `:bufdo {cmd}` to do the same thing to buffer list

**Argument list and buffer**.
* *Buffer*. Like the desktop, i.e. always messy
* *Argument list*. Like a tidy workspace

### Manage hidden files
**Buffers with hidden files**. When a buffer has been modified, Vim gives it special treatment to ensure that we do not accidentally quit the editor without saving our changes
* *Recognize modified buffers with `:ls`*. When we `:ls`, buffers marked with `+` are modified buffers, e.g.

    ```bash
    :ls

    1 %a + "a.txt"            line 1
    2      "b.txt"            line 0
    ```

* *Buffer switching with unsaved changes*. We cannot switch to another buffer, e.g. `:bn`, without saving the currently modified buffer
* *Hidden files*. If we force Vim to switch to another buffer without saving the currently modified buffer, e.g. `:bn!`

    $\to$ The new buffer will be marked `%a`, i.e. active, and the buffer with unsaved changes is marked `#h`, i.e. hidden

**Handling hidden buffers on quit**. If we leave hidden buffers with unsaved changes and quit Vim

$\to$ Vim will warn us about the hidden buffers, then load the first hidden buffer with modifications into the currrent window, so that we can decide what to do with it

>**NOTE**. If we have more than one hidden buffer with modifications, Vim activates the next unsaved buffer each time we enter  `:q` command

* *Quit Vim without reviewing hidden buffers*. `:qall!`
* *Write all modified buffers without reviewing them*. `:wall`

### Other techniques
We can use tabs and windows in combination with buffers and arguments

# Appendix
## Quick commands
### Normal mode
**Vim grammar**.
* *Command combination*. `<n_repeats><verb_command><noun_command>`
* *Current line command*. When duplicate a command, it acts upon the current line

**Editting**
* *Delete current word*. `daw` (delete a word)

    >**NOTE**. This command is single-step, thus very nice to be combined with `.`
    
    >**NOTE**. `daw` (delete a word) and `diw` (delete inside word) is that `diw` only deletes the word, but `daw` also deletes the space surrounding the word
* *Convert selected text to upper case*. `U`

**Quick scroll**. `zz`, i.e. redraw the screen with the current line in the middle of the window
* *Redraw in Insert mode*. `<C-o>zz`

**Last visual selection**. `gv`, i.e. reselect the range of text, which was last selected in Visual mode

**Jump between files**.
* *Jump to last visited file*. `<C-o>`
* *Jump to next visited file*. `<C-i>`
* *List all jumps*. `:jumps`

## Discussions
**Difference between substitution methods**.
* `s` (substitute)
    * Delete the current character
    * Place the cursor at the place of the removed character
    * Enter insert mode
* `c` (change) 
    * Take a vi/vim motion (such as w, j, b, etc.)
    * Delete the characters from the current cursor position up to the end of the movement
    
    >**NOTE**. `s` is equivalent to `cl`
* `r` (replace) never enters insert mode at all. Instead, it expects another character, which it will then use to replace the character currently under the cursor

**Multiple-line comment**.
1. Enter blockwise visual mode
2. Select lines to comment with arrow keys or `Ctrl + <direction>` (whole line)
3. Enter Insert mode with `Shift + I`
4. Type `#` (Python) then `Esc` to insert `#` to every selected line

**Insert mode vs Normal mode**. Insert mode is specialized for one task, i.e. entering text, whereas Normal mode is where we spend most of our time

**Remap the CapsLock key**.
* *Why CapsLock key is danger*. If CapLock key is engaged and we try `k` and `j` to move around, we may instead trigger `K` and `J`
* *Solution*. Map CapsLock to Ctrl key

**Buffer, tab and window in Vim**.
* *Buffers*. Used when we need to process hundreds of files without worring about spatial distribution

    $\to$ Buffers are for files
* *Windows*. Used when we need to compare two files, or work in one part of the current buffer while keeping an1other as reference
    
    $\to$ Windows are for visually comparing information
* *Tabs*. Used when we need to work for a while on a separate part of the project, without messing with their current view

    $\to$ Tabs are for differentiating truly unrelated files

# References
* Practical Vim: Edit Text at the Speed of Thought
* [Tutorialspoint](http://tutorialspoint.com/vim