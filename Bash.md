# Bash Scripting

## Chapter 01 - Basics

### Basic File Manipulation

- `touch file.txt`
    - Creates `file.txt` if it does not exist.
    - If it exists, updates file timestamps.

- `mv <source> <destination>`
    - Moves files/directories.
    - Also renames files (for example, `mv old.txt new.txt`).

- `rm -i lesson*`
    - Removes files matching `lesson*` with interactive confirmation.
    - Safer when using wildcards.

### Safer `rm` with Alias

- `alias rm='rm -i'`
    - Makes `rm` interactive for the current shell session.

- `alias rm`
    - Displays the current alias for `rm`.

- To persist aliases, add them to `~/.bashrc` and reload:

```bash
source ~/.bashrc
```

### Directory Navigation

- `cd .`
    - Stay in current directory (`.` means current path).

- `cd ..`
    - Move to parent directory.

### Searching in Files (`grep`)

- `grep 'jay' /usr/share/dict/words`
    - Finds lines containing `jay` (case-sensitive).

- `grep '^jay' file.txt`
    - Finds lines that start with `jay`.

- `grep 'jay$' file.txt`
    - Finds lines that end with `jay`.

- `grep -i 'jay' file.txt`
    - Case-insensitive search.

#### Match Context

- `grep -A1 'jay' file.txt`
    - Match + 1 line after.

- `grep -B2 'jay' file.txt`
    - Match + 2 lines before.

- `grep -C1 'jay' file.txt`
    - Match + 1 line before and after.

#### Print Only Matches

- `grep -o '^j.' file.txt`
    - Prints only matched text.
    - Example pattern: first two characters for lines starting with `j`.

- `grep -oi '^j.' file.txt`
    - Same as above, case-insensitive.

### Redirection

- `echo hello > file.txt`
    - Overwrites `file.txt` with `hello`.

- `echo a >> file.txt`
    - Appends `a` to `file.txt`.
    - Creates file if it does not exist.

### Pipes

- `cat file.txt | grep 'jay'`
    - Sends `cat` output into `grep`.
    - Equivalent here: `grep 'jay' file.txt`.

### Paging Files

- `less file.txt`
    - Interactive pager with search/navigation.
    - Quit with `q`.

- `more file.txt`
    - Simpler pager with limited navigation.

---

## Chapter 02 - Commands and Help System

### Command Documentation

- `man <command>`
    - Opens manual page for a command.

- `help <builtin>`
    - Shows help for Bash built-in commands.

- `type <command>`
    - Shows whether command is alias, built-in, function, or executable.

- `type -a <command>`
    - Shows all command resolutions in search order.

- `compgen -b`
    - Lists Bash built-in commands.

### Programs and Utilities

- `file <filename>`
    - Detects file type based on content/signatures.
    - More reliable than extension alone.
    - But can be spoffed

- `tr ':' '\n'`
    - Translates characters from first set to second set.
    - Example above converts `:` into newlines.

## Quick Tips

1. Prefer direct commands over unnecessary pipes when possible.
2. Use `-i` options and aliases carefully for safer deletions.  
3. Learn `man`, `help`, and `type` early for faster troubleshooting.

## Chapter 03 - Scripting

- `echo $?`
    - Gives the exit code of the previous command
    - 0 is success
    - Anything non-zero is a fail
