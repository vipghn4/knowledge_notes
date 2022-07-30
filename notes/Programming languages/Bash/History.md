<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [History](#history)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# History
**Erase all shell history**. `rm ~/.bash_history`
* *`.bash_history`*. A hidden file for bash to keep the shell history
    * *Location*. This file is located in the home directory
    * *Consequence*. To get rid of the history, delete `.bash_history`
* *Recording of history erase*. If we logout after erasing the shell history, this last `rm ~/.bash_history` command will be logged

**Stop logging history for the current session**. `unset HISTFILE` or `HISTFILE=/dev/null`

$\to$ We can change `HISTFILE` to whatever file we want
* *`HISTFILE`*. Special bash variable pointing to the file, where the shell history should be saved

**Run command without logging history**. ` command`, i.e. the command starts with an extra space

**Show the history**. `history`

**Execute last command**. 
* *Execute the previous command quickly*. `!!`
* *Execute the most recent command starting with the given string*. `!string`
    * *Explain*. The first bang starts history substitution, and the second one refers to the most recent command starting with `string`
* *Open the previous executed command in a text editor*. `fc`

# Appendix
## References
* https://catonmat.net/bash-one-liners-explained-part-four