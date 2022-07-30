<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Redirection](#redirection)
  - [Introduction](#introduction)
  - [Redirection operators](#redirection-operators)
  - [Other stuffs with redirection](#other-stuffs-with-redirection)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Redirection
## Introduction
**File descriptors**. Working with redirections is all about manipulating file descriptors
* *Standard file descriptors*. When bash starts it opens the three standard file descriptors, i.e.
    * `stdin` with file descriptor `0`
    * `stdout` with file descriptor `1`
    * `stderr` with file descriptor `2`
* *Additional file descriptors*. We can 
    * Open more file descriptors, e.g. `3`, `4`, `5`, etc., and close them
    * Copy file descriptors
    * Write to and read from file descriptors
* *Command execution of bash*. When bash runs a command
    1. Bash forks a child process, i.e. see `man 2 fork`, inheriting all the file descriptors from the parent process
    2. Bash sets up the specified redirections
    3. Bash execs the command, i.e. `man 3 exec`

>**NOTE**. To understand bash redirections, we should visualize how the file descriptors get changed when redirections happen

**Options for redirection**.
* Redirect `stdout` to a file
* Redirect `stderr` to a file
* Redirect `stdout` to `stderr`
* Redirect `stderr` to `stdout`
* Redirect `stderr` and `stdout` to a file
* Redirect `stderr` and `stdout` to `stdout`
* Redirect `stderr` and `stdout` to `stderr`

**Special files for redirection**. Bash handles several filenames specially when they are used in redirections
* *Specification of special files*. If the OS on which Bash is running provides these special files, bash will use them
    
    $\to$ Otherwise it will emulate them internally with the behavior described below
* *Defailt special files*.
    * *`/dev/fd/fd`*. If `fd` is a valid integer, file descriptor `fd` is duplicated
    * *`/dev/stdin`*. File descriptor `0` is duplicated
    * *`/dev/stdout`*. File descriptor `1` is duplicated
    * *`/dev/stderr`*. File descriptor `2` is duplicated
    * *`/dev/tcp/host/port`*. If `host` is a valid hostname or Internet address, and `port` is an integer port number or service name
        
        $\to$ Bash attempts to open the corresponding TCP socket
    * *`/dev/udp/host/port`*. If `host` is a valid hostname or Internet address, and `port` is an integer port number or service name
        
        $\to$ Bash attempts to open the corresponding UDP socket

>**NOTE**. A failure to open or create a file causes the redirection to fail

>**NOTE**. Redirections using file descriptors greater than 9 should be used with care
>
>* *Explain*. They may conflict with file descriptors the shell uses internally

**Location of redirections**. Redirections can be put anywhere in the command we want, e.g.

```bash
echo hello >/tmp/example
echo >/tmp/example hello
>/tmp/example echo hello
```

## Redirection operators
**Operator `>` (output redirection)**. Redirect the contents of a command or file to another by overwriting the target file

<div style="text-align:center">
    <img src="https://i.imgur.com/Wx2gyrf.png">
    <figcaption>File descriptor table after output redirection</figcaption>
</div>

* *Example*.

    ```bash
    #!/bin/bash
    echo "hello world" > file.txt
    ```

* *Data flow*.
    1. Bash tries to open the file for writing and if it succeeds it sends the `stdout` of command to the newly opened file
    2. If it fails opening the file, the whole command fails
* *Redirection with specific file descriptors*. `command n>file`, i.e. redirect the file descriptor `n` to `file`
    * *Example*. 
        * `command >file` is the same as `command 1>file`, i.e. `1` stands for `stdout`
        * `command 2>file` reditects `stderr` to `file` 
* *Redirection of both `stdout` and `stderr`*. `&>` operator redirects both output streams, i.e. `stdout` and `stderr`, from `command` to `file`

    $\to$ This is bash's shortcut for quickly redirecting both streams to the same destination
* *Redirection from a file descriptor to another file descriptor*. `n&>m` redirects streams from file descriptor `n` to file descriptor `m`
    * *Example*. `command >file 2>&1` redirect `stderr` to `stdout` after redirecting `stdout` to `file`

        >**NOTE**. This is a much more common way to redirect both streams to a file

    >**NOTE**. In bash, writing `command &>file` is the same as `command >&file`

* *Discard streams from a file descriptor*. Redirect the file descriptor to `/dev/null`, i.e. `/dev/null` discards all data written to it
    * *Example*. `command > /dev/null`

**Operator `>>`**. The same as `>` but appending rather than overwriting, e.g.

```bash
#!/bin/bash
echo "hello world" >> file.txt
```

**Operator `<` (input redirection)**. Used for input redirection, e.g.

```bash
#!/bin/bash
cat < file.txt
```

**Operator `<<` (here-document)**. Allow to put a line of input into a command in many

```bash
#!/bin/bash
cat << EOF
```

**Operator `|`**. Redirect the output of the first command as the input of the second one, e.g.

```bash
#!/bin/bash
ls -la | sed `s/bash/redirection_operator/`
```

**Operator `<>`**. Open a file for reading and writing, e.g.

```bash
command n<>file # open `file` for rw and assign it fd n
```

**Processing order**. Redirections are processed in the order they appear, from left to right
* *Examples*.
    
    ```bash
    ls > dirlist 2>&1
    ```
    
    directs both `stdout` and `stderr` to `dirlist`, while the command

    ```bash
    ls 2>&1 > dirlist
    ```
    
    directs only `stdout` to `dirlist`, since `stderr` was made a copy of `stdout` before `stdout` was redirected to `dirlist`

## Other stuffs with redirection
**Redirect a file descriptor `n` to `file` in the current shell**. `exec n>file`

**Redirect multiple commands**. `(commands)` runs the commands a sub-shell, i.e. a child process launched by the current cell

```bash
(command1; command2) >file
```

**Execute commands in a shell via a file**.

```bash
exec < command_file
```

**Access a website via bash**.

```bash
exec n<>/dev/tcp/www.google.com/80
echo -e "GET / HTTP/1.1\n\n" >& 3
cat <& 3
```

* *Data flow*. 
    1. Open file descriptor `3` for reading and writing and point it to `/dev/tcp/www.google.com/80` special file, i.e. a connection to `www.google.com` on port `80`
    2. Write `GET / HTTP/1.1\n\n` to file descriptor `3`
    3. Read the response back from the same file descriptor by using `cat`

**Redirect `stdin` to a file and print it to `stdout`**. `command | tee file`

**Redirect `stdout` and `stderr` of one process to `stdin` of another**. `command1 |& command2` or `command1 2>&1 | command2`

**Swap `stdout` and `stderr`**. `command 3>&1 1>&2 2>&3`

**Send `stdout` to one process and `stderr` to another**. `command > >(stdout_cmd) 2> >(stderr_cmd)`
* *`>(...)` operator*. Run the commands in `...` with `stdin` connected to the read part of an anonymous named pipe
    * *Returned values*. Bash replaces the operator with the filename of the anonymous pipe
* *Examples*. `>(stdout_cmd)` may return `/dev/fd/60`, and `>(stderr_cmd)` may return `/dev/fd/61`
    
    $\to$ Both files are named pipes created by bash on the fly
* *Consequence*. Both named pipes have the commands as readers, which wait for someone to write to the pipes so they can read the data

    $\to$ The command then looks like

    ```bash
    command > /dev/fd/60 2> /dev/fd/61
    ```

# Appendix
## Concepts
**HereDoc**. A file literal or input stream literal, i.e. it is a section of a source code file treated as if it were a separate file
* *Syntax*. The syntax for writing a HereDoc is

    ```bash
    [COMMAND] <<[-] 'DELIMITER'
        Line 1
        Line 2
        ...
    DELIMITER
    ```

    * *`COMMAND` (optional)*. Works for any command accepting redirection
    * *`<<`*. The redirection operator for forwarding a HereDoc to the `COMMAND`
    * *`-`*. A parameter for tab suppression
    * *`DELIMITER` in the first line*. Define a HereDoc delimiter token, e.g. END, EOT, or EOF
        
        >**NOTE**. Any multicharacter word not in the body works
        
        >**NOTE**. Omit single quotes on the first line to allow command and variable expansion.
    * *`DELIMITER` in the last line*. Indicate the end of a HereDoc, i.e. use the same word from the first line without the leading whitespaces
* *Explain*. `COMMAND < file.txt`, where `file.txt` is a file with content `<file content>`, is the same as 
    
    ```bash
    COMMAND << DELIMITER
        <file content>
    DELIMITER
    ```

## References
* https://catonmat.net/bash-one-liners-explained-part-three