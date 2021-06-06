---
title: Linux terminal commands
tags: Operating system
---

[toc]

# Basic commands
### Basic commands
* *Display previous commands* 

    ```bash
    $ history
    ```    

* *Display file system*. Display information about the disk space usage of all mounted file systems

    ```bash
    $ df
    ```

* *Display directory usage*. Display the size of a directory and all of its subdirectories

    ```bash
    $ du
    ```

* *Display free space on the system*

    ```bash
    $ free
    ```

* *Display processes using the most resources*.

    ```bash
    $ top
    ```

* *Display process status*.

    ```bash
    $ ps
    ```

* *Instructions about other commands*.
    * `man`. Display manual page, i.e. very detailed, for any command we are unfamiliar with
    * `info`. Display more detailed or precise information than `man`
    * `command -h`. Display quick overview of the command and its uses
    * `whatis command`. Display a brief description of what is the functionality of specific built-in Linux command

### Utilities
**Pipeline and redirect**.
* *Pipeline*. Pass output to another program or utility
    * *Example*. `thing1 > thing2`
* *Redirect*. Pass output to either a file or stream
    * *Example*. `thing1 | thing2`

**`grep` (Globally search for REgular expression and Print out) command**. Search a file for a particular pattern of characters, then display all lines containing the searched pattern

```bash=
grep [options] pattern [files]
```
    
* *Options*.
    
    | Option | Description |
    | --- | --- |
    | `-c` (count) | Print a count of lines which match a pattern |
    | `-h` (hide) | Display the matched lines without filenames |
    | `-H` | Display the matched lines with filenames |
    | `-i` (ignore) | Ignore case for matching |
    | `-l` (list) | Display list of a filenames only |
    | `-n` (number) | Display the matched lines with their line numbers |
    | `-r` (recursive) | Recursively search for string within some folder |
    | `-w` | Match the whole word |
    | `--include=<pattern>` | Only search through files with pattern `<pattern>` |
    | `--exclude=<pattern>` | Exclude searching through files with pattern `<pattern>` |

**`xargs`**. Build and execute command lines from standard input

>**NOTE**. When combined with `grep` and `find`, the three commands form a very powerful toolset

```bash=
xargs [options] [command [initial-arguments]]
```

* *Common options*.

    | Option | Description |
    | --- | --- |
    | `-d [delim]` | Input items are terminated by specified character |
    | `-a [file]` | Read items from file instead of stdin |
    | `-I [replacte-str] ` | Replace occurrences of `replate-str` in initial arguments with names read from standard input |
    | `-i [replace-str]` | Synonym for `-I [replace-str]` if `replace-str` is spcified, otherwise as `-I{}` |
    | `-L [number]` | Read `number` lines from the stdin and concatenates them into one long string, then append this string to the command template and execute the resulting command. This is repeated until `xargs` reaches to the end of stdin |
    | `-l [number]` | Act like `L [number]`. If `number` is absent, it acts like `L1` |
    | `-n [number]` | Read a maximum of `number` arguments from stdin and puts them on the end of command template |

* *Examples*.
    
    ```bash=
    xargs -I {} mv dir1/{} dir2/{} # Replace `{}` with names from standard input
    ```

**`curl`**. Transfer data from or to a server, using one of supported protocols

### Hot keys
#### Terminal
<table>
    <tr>
        <th>Key</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Ctrl + Alt + T</td>
        <td>new terminal window</td>
    </tr>
    <tr>
        <td>Ctrl + Shift + T</td>
        <td>new terminal tab</td>
    </tr>
    <tr>
        <td>Ctrl + Shift + W</td>
        <td>close terminal window / tab</td>
    </tr>
    <tr>
        <td>Alt + <number></td>
        <td>switch to a particular terminal tab</td>
    </tr>
</table>

# Permissions
### Users and groups
#### Introduction
**User permissions** are used to provide the system with greater security

**Group permission** are useful for allowing multiple independent users to collaborate and share files

**Best practices**
* Give each user their own login to the system, i.e.
    * Protect each user's files form all other users
    * Allow more accurate system logging, particularly when combined with sudo

#### User
**User management**. 
* *Add user*. `useradd username`
    * *Options*.

    <table>
        <tr>
            <th>Option</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>-d home_dir</td>
            <td>login directory of the user</td>
        </tr>
        <tr>
            <td>-e date</td>
            <td>the date when the account will expire</td>
        </tr>
        <tr>
            <td>-f inactive</td>
            <td>the number of days before the account expires</td>
        </tr>
        <tr>
            <td>-s shell</td>
            <td>the default shell type</td>
        </tr>
    </table>
* *Set password*. `passwd username`
* *Remove user*. `userdel username`
    * *Option*. `-r` to remove the user, their home folder, and their files

**Sudo** allows users and groups access to commands they normally would not be able to use

#### Group
**Group**. In Unix-like systems, multiple users can be put into *groups*, which allows additional abilities to delegated in an organized fashion
* *Purpose*. Manage a collection of users
* *Control of group membership*. See `/etc/group`

**A group identifier (GID)** is a numeric value to represent a specific group

**Commands**
* *Create a group*.

```
newgrp group_name
```


### Change modes
#### `chmod`

**Description**. Change the access permissions of the file system objects, i.e. files and directories

**Show access mode**. `ls -ld files ...`
* `-l`. Use a long listing format
* `-d` List directories, not their contents

##### Syntax
**Octal modes**. Display results of `ls -ld`
* *Example*. `drwxrwx---`
* *Explain*.
    * The first character defines the file type
        *  `-` (file)
        *  `d` (directory)
        *  `l` (symlink)
    * The three leftmost character define permissions for the user class
    * The middle three characters define permissions for the group class
    * The last three characters define permissions for other class

**Symbolic modes**. Commonly used to run command `chmod`

```bash
chmod [options] [references][operator][modes] file ...
```

* *Options*
    * `-R` Recursive
    * `-v` verbose
* *Basic modes*. `r` (read), `w` (write) and `x` (execute)
* *Reference*.

<table>
    <tr>
        <th>Reference</th>
        <th>Class</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>u</td>
        <td>user</td>
        <td>file owner</td>
    </tr>
    <tr>
        <td>g</td>
        <td>group</td>
        <td>members of the group owning the file</td>
    </tr>
    <tr>
        <td>o</td>
        <td>others</td>
        <td>users who are neither the file's owner nor members of the file's group</td>
    </tr>
    <tr>
        <td>a</td>
        <td>all</td>
        <td>the same as ugo, i.e. all 3 types</td>
    </tr>
</table>

* *Operator*.

<table>
    <tr>
        <th>Operator</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>+</td>
        <td>adds the specified modes to the specified classes</td>
    </tr>
    <tr>
        <td>-</td>
        <td>removes the specified modes from the specified classes</td>
    </tr>
    <tr>
        <td>=</td>
        <td>the modes specified are to be made the exact modes for the specified classes</td>
    </tr>
</table> 

* *Other modes*

<table>
    <tr>
        <th>Mode</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>s</td>
        <td>set user or group ID on execution</td>
    </tr>
    <tr>
        <td>t</td>
        <td>save program text on swap device</td>
    </tr>
</table> 

* *Examples*.
    * `chmod a+rx file.txt`. Adds read and execution permissions for all classes
    * `chmod u=rw,g=r,o= file.txt`. Sets read and write permission for user, set read for group, and denies access for other

#### `chown`

**Description**. Change the owner of a file

**Syntax**.

```
chown new_owner file_name
```

or

```
chown newuser:newgroup file_name
```

**Permissions**.
* The ownership of any file may only be altered by a super-user, not not by any user, or even the owner of the file
* Only a member of a group can change a file's group ID to that group

#### `chgrp`

**Description**. Used by unprivileged users to change the group associated with a file system object to one of which they are a member

**Options**.
* `-R`. Recursive
* `-v` Verbose
* `-f`. Force if an error is encountered

### Common practices
**Fast-executed Python file**.
1. `chmod +x src.py` to allow execution mode
2. Add shebang line `#!/usr/bin/env python3` as the first line of `src.py` to tell the location of the interpreter
    * *General*. `#/path/to/interpreter/dir interpreter_name --option_name value`
    * *Example*. `#!/usr/bin/env python --output_dir ./results`
4. Run `./src.py` to run the file, rather than `python src.py`


**Execute with specific environment variable values**.
```bash
VAR_NAME=value command_to_execute
```

# Resource limitations
**Limit by users**. Exploit `/etc/security/limits.conf`

**Limit by processes**. Use control groups, i.e. `cgroups`
* *Install `cgroup`*. `sudo apt-get install cgroup-bin`
* *Control groups*. Feature provided by the Linux kernel to manage, restrict, and audit groups of processes
* *Inspectation of processes*.
    * *Show current `cgroup` hierarchy*. `systemctl status`
    * *Find `cgroup` of a process*. `cat /proc/{PID}/cgroup`
    * *Show `cgroup` resource usage*. `systemd-cgtop`
* *Persisten group configuration*. Define groups in `/etc/cgconfig.conf`, e.g.
    * *Example 1*.

        ```bash
        group groupname {
          perm {
        # who can manage limits
            admin {
              uid = $USER;
              gid = $GROUP;
            }
        # who can add tasks to this group
            task {
              uid = $USER;
              gid = $GROUP;
            }
          }
        # create this group in cpu and memory controllers
          cpu { }
          memory { }
        }

        group groupname/foo {
          cpu {
            cpu.shares = 100;
          }
          memory {
            memory.limit_in_bytes = 10000000;
          }
        }
        ```
    
    * *Example 2*.

        ```bash
        group matlab {
            perm {
                admin {
                    uid = username;
                }
                task {
                    uid = username;
                }
            }

            cpuset {
                cpuset.mems="0";
                cpuset.cpus="0-5";
            }
            memory {
                memory.limit_in_bytes = 5000000000;
            }
        }
        ```
* *Run command with restricted resource*.

    ```bash
    cgexec -g <controllers>:<group_name> <command>
    ```
    
    * *Example*.

        ```bash
        cgexec -g memory,cpuset:matlab /opt/MATLAB/2012b/bin/matlab bash
        ```

* *List all controllers*. See `/sys/fs/cgroup`
    * *Mechanism of group creation*. By creating a controller of group `groupname`
        
        $\to$ A directory named `groupname` would be created inside the corresponding controller directory in `/sys/fs/cgroup`

# Files and directories
### File system
#### inode

**The inode (index node)**. Each file is associated with an *inode*, which is identified by an integer called *i-number* or *inode number*
* *Information stored in an inode*. An inode stores metadata of a file or directory
    * File ownership
    * Access mode, i.e. `rwx`
    * File type
    * Link count, i.e. the number of hard links to the inode
    * User ID, i.e. the file owner
    * Group ID, i.e. the file's owner group
    * File size
    * Time stamp, i.e. access time, modificiation time, and change time
    * Attributes
    * Link to file location
    * Other metadata

>**NOTE**. The maximum number of inodes limiting the maximum number of files the system can hold

>**NOTE**. The identity of a file is its inode number, not its name

**Commands**.
* *Display inode data*.

    ```bash
    $ stat file_name
    ```
* *Display inode number*.

    ```bash
    $ ls -i
    ```

**inode structure for directory**.
* *Directory*. A special file mapping a file name to its inode number
    * *Directory entry (dentry)*. A mapping from a file name to its inode number
        * *Explain*. "A directory contains files and directories" means that the directory is mapping those files and directories to their inode numbers
    * *Consequence*. A directory cannot hold two files with the same name
* *inode number of `/` directory*. 2 (fixed)

>**NOTE**. We care about inode number of `/` directory since there is no directory mapping this directory to its inode number

#### `ln` command

**Description**. A standard Unix command to create a hard link or a symbolic link to an existing 

**Symbolic link (symlink)**. A separate file, whose contents point to the linked-to file
* *Symlink and original file*. 
    * The original file is a name connected directry to the inode
    * The symlink refers to the name
* *Usage*. Special files which refer to other files by name
* *Create symbolic link*. 


    ```bash
    $ ln -s file_to_be_linked symlink_file 
    ```
>**NOTE**. We can think of a symlink as a shortcut
* *Other details*.
    * *Symlink content*. The name of the target file only
    * *Permission*. All open, i.e. no permission management here

**Hard link**. A directory entry, which associates a name with a file on a file system
* *Usage*. Allow multiple filenames to be associated with the same file
* *Hard link and original file*. The hard link is a name, which refers an inode
    * *Example*. if `file1` has a hard link named `file2`, then they both refer to the same inode
    * *Consequences*. A hard link and the original file are two names connected to the same inode
* *Create a hard link*. Creating a hard link is adding a new name to an inode

    ```bash
    $ ln file_to_be_linked hardlink_file
    ```
* *Retrieve all filenames to an inode number*.

    ```bash
    $ find / -inum inode_number
    ```

# Packages
### Package management
#### `dpkg`

**`dpkg`**. The Linux Debian packages manager, i.e. add or remove applications
* *Usage*. Install or remove programs, list them or retrieve specific information about them

>**NOTE**. When `apt` or `apt-get` are used, they invoke the `dpkg` program to install or remove applications 

**Commands**.
* *Install software using `dpkg`*.

    ```bash
    $ dpkg -i package_name.deb
    ```
* *Removing software using `dpkg`*.

    ```bash
    $ dpkg --remove <package_name.deb|package_name>
    ```
* *List all programs*.

    ```bash
    $ dpkg -l
    ```
* *Search for programs*.

    ```bash
    $ dpkg -s package_name
    ```
* *List files of a program*.

    ```bash
    $ dpkg -L package_name
    ```
* *Show installation directories*.

    ```bash
    $ dpkg -c package_name
    ```

#### `apt` and `apt-get`

**`apt`**. Advantageous over `dpkg` since it resolves dependencies and downloads updated software automatically

>**NOTE**. `apt` uses `dpkg` to manage packages

**Commands**
* *List all packages managed by `apt`*.

    ```bash
    $ cat /etc/apt/sources.list
    ```
* *Install software with `apt`*.
    * *Install a new software*
        ```bash
        $ apt install package_name
        ```
    * *Reinstall a new software*.

        ```bash
        $ apt --reinstall install package_name 
        ```
* *Remove software with `apt`*.
    * *Remove software without removing configuration files*
        ```bash
        $ apt-get remove package_name
        ```
    * *Remove software with its configuration files*
        ```bash
        $ apt-get purge package_name
        ```
        or
        ```bash
        $ apt-get --purge remove package_name
        ```
* *Update package index files from `sources.list`*. All available packages are fetched and re-indexed from the locations specified in `/etc/apt/sources.list`

    ```bash
    $ apt-get update
    ```
* *Update all debian system packages*. Install all of the latest versions of each package installed on the system

    ```bash
    $ apt-get upgrade
    ```
* *Clear `apt-cache`*.

    ```bash
    $ apt-get clean
    ```
* *Remove uselss files from `apt-cache`*.

    ```bash
    apt-get autoclean
    ```
* *Search for package*.

    ```bash
    $ apt search package_name
    ```
* *List all packages*.

    ```bash
    $ apt list
    ```
* *`apt` troubleshooting*

    ```bash
    $ apt-get clean
    $ apt-get autoclean
    $ apt-get -f install
    $ apt-get --fix-missing install
    $ apt-get --purge autoremove
    $ apt-get update
    ```

### C/C++ Builder
#### C compilation process
**C program files**. A common convention in C programs is to write a header file for each source file, which we link to our main source code.
* *Source files*. Contains *declarations*, i.e. prototypes
    * *Suffices*. `.c`, `.cc`, `.cpp`, `.CPP`, `.c++`, `.cp`, or `.cxx`
* *Header files*. Contains *definitions*
    * *Suffices*. `.hh`, `.hpp`, or `.H`
* *Preprocessed files*.
    * *Suffices*. `.ii`

**GCC (GNU C Compiler)**. A compiler-driver of GNU Compiler Collection ([*source*](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html))

<div style="text-align:center">
    <img src="/media/mrDLHrq.png">
    <figcaption>GCC compilation process</figcaption>
</div>

* *Preprocessing*. GCC includes the headers, i.e. `#include`, and expands the macros, i.e. `#define`
    * *Command*. 

        ```bash
        $ cpp src.c > src.i
        ```
    * *Input*. Source code, e.g. `src.c`
    * *Output*. Extended source code, e.g. `src.c`

* *Compilation*. GCC compiles the preprocessed source code to assembly code for a specific processor
    * *Command*.

        ```bash
        $ gcc -S src.i
        ```

        where `-S` specifies to produce assembly code
* *Assembly*. The assembler, i.e. `as.exe`, converts the assembly code into machine code in the object file `src.o`
    * *Command*.

        ```bash
        $ as -o src.o src.s
        ```
    * *Input*. Assembly code, e.g. `src.s`
    * *Output*. Object file, e.g. `src.o`
* *Linker*. The linker, i.e. `ld.exe`, links the object code with the library code to produce an executable file, e.g. `src.exe`
    * *Command*.

        ```bash
        $ ld -o src.exe src.o ..libraries...
        ```

**Headers (`.h`), static libraries (`.lib`, `.a`), and shared library (`.dll`, `.so`)**.
* *Library*. A collection of pre-compiled object files, which can be linked into a program via the linker, e.g. `printf()`, `sqrt()`
    * *Static library*. When a program is linked against a static library, the machine code of the external functions in the program is copied into the executable
        * *Extensions*. `.a` (archive file) or `.lib` (library)
        * *Create static library*. Use archive program, i.e. `ar.exe`
    * *Shared library*. When a program is linked against a shared library, only a small table is created in the executable
        * *Dynamic linking*. Before execution, the OS loads the machine code needed for the external functions
        * *Expansions*. `.so` (shared object) or `.dll` (dynamic link library)
    * *Discussions*. 
        * Dynamic linking makes executable files smaller and saves disk space
        * Most OS allows one copy of a shared library in memory to be used by all running programs, i.e. save memory
        * Shared library codes can be upgraded without recompiling the linked programs
* *Searching for header files and libraries*.
    * *Prerequisites for compilation*.
        * *Compiler* needs the header files to compile the source codes
        * *Linker* needs the libraries to resolve external references from toher object files or libraries
    * *Guilding the search of header files and libraries*.
        * *Header files*. Use environment variable `CPATH` 
        * *Libraries*. Use environment variable `LIBRARY_PATH`

**Other environment variables**.
* `PATH`. For searching the executables and run-time shared libraries, e.g. `dll`, `.so`, etc.
* `CPATH`. For searching the include-paths for headers
* `LIBRARY_PATH`. For searching library-paths for link libraries

**Related commands**.
* `ldconfig`. Create the necessary links and cache to the most recent shared libraries
    * *Places to check for shared libraries*. 
        * In the directories specified in the command line
        * In the `/etc/ld.so.conf` file
        * In the trusted directories, i.e. `/lib` and `/usr/lib` (32-bit OS) or `/lib64` and `/usr/lib64` (64-bit OS)
    
    >**NOTE**. For details, please run `man ldconfig`

### `tmux`
**Start and terminate**.
* *Start `tmux`*. `tmux`
* *Start new session*. `tmux new -s <session_name>`
* *Detach tmux session*. `Ctrl + d`
* *Attach tmux session*. `tmux attach-session -t <session_name>`
* *Delete session*. `tmux kill-session -t <session_name>`

**Working with windows and panes**.
* *Windows*.
    * *Create a new window*. `Ctrl + b + c`
    * *Close tmux window*. `Ctrl + d`
    * *Choose window from a list*. `Ctrl + b + w`
    * *Switch to window*. `Ctrl + b + <window_number>`
* *Panes*.
    * *Horizontal split*. `Ctrl + b + %`
    * *Vertical split*. `Ctrl + b + "`
    * *Move between panes*. `Ctrl + b + <arrow key>`
    * *Close current pane*. `Ctrl + b + x`

**Misc**.
* *List all sessions*. `tmux ls`

**References**.
* https://man.cx/tmux

# Root directory structure
**`/etc/` directory**.
* *`/etc/alternatives`*. Contain symblic links determining default commands
    * *`update-alternatives`*. Update symbolic links determining default commands
* *`/etc/fstab`*. List file systems mounted automatically at startup by `mount -a` command
* *`/etc/apt/sources.list`*. Contain information about sources to `apt-get install` from
* *`/etc/passwd`*. The user database, with fields giving the username, realname, home directory, and other information

    $\to$ See `man passwd` for details
* *`/etc/group`*. Similar to `/etc/passwd` but for groups
* *`/etc/bash.bashrc`*. Bash script at login or startup time
* *`/etc/security/limits.conf`*. Set resource limits for each users of the system

**`/dev/` directory**. Contain information about devices

**`/var/` directory**. Contain data which is changed when the system is running normally
* *`/var/cache/man`*. Cached `man` pages
* *`/var/lib`*. Files which change while the system is running normally
* *`/var/lock`*. Lock files, i.e. many programs follow a convention to create a lock file here to indicate that they are using a particular device or file
* *`/var/log`*. Log files from various programs, especially login, i.e. `/var/log/wtmp`, and syslog, i.e. `/var/log/messages`

    $\to$ We need to clean this directory regularly
* *`/var/run`*. Files containing information about the system, which is valid until the system is next booted
* *`/var/tmp`*. Temporary files which are large or need to exist for a longer time that what is allowed for `/tmp`

**`/tmp` directory**. Contain temporary data which will be removed if shutdow