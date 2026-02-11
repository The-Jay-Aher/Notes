# Bash Scripting

# Chapter 01

## Basic File Manipulation

`touch` - Create a file
`mv $sourceFileorLocation $destinationFileorLocation` - Move a File from one location to another, it can also rename the files

`rm -i lesson*` - Interactively asks to delete all the files which have lesson at the start

`alias rm='rm -i'` -> This will set and alias for the rm package, so that when you do `rm` it runs `rm -i`
You can check if a command has been alias'ed by running `alias $command` E.g. `alias rm` will show `alias rm='rm -i'`
