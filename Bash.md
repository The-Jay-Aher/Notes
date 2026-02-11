# Bash Scripting

## Chapter 01 - Basics

## Basic File Manipulation

### Create, Move, and Remove Files

- `touch file.txt`
  - Creates `file.txt` if it does not exist.
  - If the file already exists, it updates the file timestamp (modification/access time) instead of changing content.

- `mv <source> <destination>`
  - Moves a file or directory to a new location.
  - Also renames items when source and destination are in the same folder (example: `mv old.txt new.txt`).
  - If destination exists, it can be overwritten depending on shell settings/options.

- `rm -i lesson*`
  - Deletes files that match `lesson*` (for example, `lesson1`, `lesson_notes.txt`).
  - `-i` enables interactive mode, so Bash prompts for confirmation before each removal.
  - Useful when wildcards are involved and you want to reduce accidental deletion risk.

### Safe `rm` Alias

- `alias rm='rm -i'`
  - Makes `rm` run in interactive mode by default for the current shell session.
  - This adds a safety prompt to normal `rm` usage.
  - To keep it permanently, add it to your shell startup file (like `~/.bashrc`).

- `alias rm`
  - Prints the current alias for `rm` if one exists.
  - Use this to verify whether your safe alias is active.

## Directory Navigation

- `cd .`
  - Changes directory to the current directory (`.` means "here").
  - Functionally no movement; mostly used in scripts where a path variable may resolve to `.`.

- `cd ..`
  - Moves from the current directory to its parent directory.
  - Example: from `/home/jay/projects/app` to `/home/jay/projects`.

## Searching in Files (`grep`)

- `grep 'jay' /usr/share/dict/words`
  - Prints every line in `/usr/share/dict/words` that contains the text `jay`.
  - Match is case-sensitive by default.

- `grep '^jay' file.txt`
  - `^` anchors the match to the start of the line.
  - This finds lines beginning with `jay` only.

- `grep 'jay$' file.txt`
  - `$` anchors the match to the end of the line.
  - This finds lines that end with `jay` only.

- `grep -i 'jay' file.txt`
  - Performs a case-insensitive search (`jay`, `Jay`, `JAY`, etc.).
  - Helpful when text case is inconsistent.

### Context Around Matches

- `grep -A1 'jay' file.txt`
  - Shows each matching line plus `1` line After it.
  - Good for quickly viewing nearby output context.

- `grep -B2 'jay' file.txt`
  - Shows each matching line plus `2` lines Before it.
  - Useful for checking what led up to a match.

- `grep -C1 'jay' file.txt`
  - Shows each matching line plus `1` line of Context on both sides.
  - Equivalent to combining `-B1` and `-A1`.

### Print Only Matched Text

- `grep -o '^j.' file.txt`
  - `-o` prints only the part that matches, not the full line.
  - Pattern `^j.` returns the first two characters of lines that start with `j` (for example, `ja`, `jo`).

- `grep -oi '^j.' file.txt`
  - Same as above, but `-i` makes matching case-insensitive.
  - So lines starting with `j` or `J` are both included.

## Redirection and Appending

- `echo hello > file.txt`
  - Writes `hello` to `file.txt`.
  - `>` overwrites the file if it exists, or creates it if missing.
  - Use carefully to avoid replacing existing content by mistake.

- `echo a >> file.txt`
  - Appends `a` to the end of `file.txt`.
  - `>>` preserves current content and adds new output on a new line.
  - Creates the file if it does not exist.

## Pipes

- `cat file.txt | grep 'jay'`
  - Sends output of `cat file.txt` to `grep` through a pipe (`|`).
  - In this case, it is equivalent to `grep 'jay' file.txt`.
  - Direct form is shorter, but piping is useful when chaining multiple commands.

## Paging Files

Useful for viewing large files one screen at a time:

- `less file.txt`
  - Opens an interactive viewer for large files.
  - Supports forward/backward navigation, `/pattern` search, and quit with `q`.
  - Preferred over `more` for flexibility.

- `more file.txt`
  - Opens a basic pager for reading output page by page.
  - Simpler than `less`, with limited backward movement on many systems.
