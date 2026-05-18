# Bash Scripting

## Quick Summary

Bash is both a command shell and a scripting language. In DevOps work, Bash is used for navigation, file operations, text processing, automation scripts, CI/CD steps, server troubleshooting, and glue logic between tools.

The practical mental model:

```text
command -> arguments -> input/output -> exit code
```

If you understand commands, streams, quoting, variables, conditions, loops, and exit codes, you can automate many everyday Linux tasks.

## Why It Matters

Bash is useful because:

- Most Linux servers provide a POSIX-like shell.
- CI/CD pipelines often run shell commands.
- Cloud and Kubernetes tooling commonly exposes CLI workflows.
- Logs, config files, and command output often need quick text processing.
- Small scripts can automate repeatable tasks without a full application.

Use Bash for small operational automation. For large programs, complex data structures, or heavy error handling, use a language such as Python, Go, or the project's primary language.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Shell | Program that reads and executes commands. |
| Command | Executable, shell builtin, function, or alias. |
| Argument | Value passed to a command. |
| Standard input | Input stream, usually keyboard or pipe. |
| Standard output | Normal output stream. |
| Standard error | Error output stream. |
| Exit code | Numeric result of a command; `0` means success. |
| Pipe | Sends output from one command into another. |
| Redirection | Sends input/output to or from files. |
| Variable | Named value in the shell. |

## Command Help

```bash
man ls
help cd
type cd
type -a python
compgen -b
```

Use:

- `man` for external command manuals.
- `help` for Bash builtins.
- `type` to see whether a command is an alias, function, builtin, or executable.

## File And Directory Commands

```bash
pwd
ls
ls -la
cd /path/to/dir
cd ..
touch file.txt
mkdir notes
mkdir -p parent/child
cp source.txt copy.txt
cp -r dir1 dir2
mv old.txt new.txt
rm file.txt
rm -i file.txt
rmdir empty-dir
```

Important:

- `.` means current directory.
- `..` means parent directory.
- `~` means current user's home directory.
- Use `rm -i` when learning or using risky patterns.

## Safer rm With Alias

Temporary alias:

```bash
alias rm='rm -i'
```

Show alias:

```bash
alias rm
```

Persist aliases in:

```text
~/.bashrc
```

Reload:

```bash
source ~/.bashrc
```

Do not rely only on aliases for safety in scripts. Scripts may run without interactive aliases.

## Viewing Files

```bash
cat file.txt
less file.txt
head file.txt
head -n 20 file.txt
tail file.txt
tail -n 50 file.txt
tail -f app.log
```

Use `less` for reading, `tail -f` for following logs.

## Searching With grep

```bash
grep 'error' app.log
grep -i 'error' app.log
grep -n 'error' app.log
grep -R 'TODO' .
grep '^START' file.txt
grep 'END$' file.txt
```

Context:

```bash
grep -A3 'error' app.log
grep -B3 'error' app.log
grep -C3 'error' app.log
```

Print only matches:

```bash
grep -o 'pattern' file.txt
```

For code searches, prefer `rg` when available:

```bash
rg "search term"
rg -n "function_name" .
```

## Redirection

| Syntax | Meaning |
| --- | --- |
| `>` | Redirect stdout, overwrite file. |
| `>>` | Redirect stdout, append file. |
| `2>` | Redirect stderr. |
| `2>&1` | Send stderr to stdout destination. |
| `<` | Read stdin from file. |

Examples:

```bash
echo hello > file.txt
echo another >> file.txt
command > output.log 2> error.log
command > combined.log 2>&1
sort < names.txt
```

## Pipes

Pipes send stdout from one command into stdin of another.

```bash
cat file.txt | grep 'jay'
```

Better:

```bash
grep 'jay' file.txt
```

Useful pipelines:

```bash
ps aux | grep nginx
cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr
journalctl -u nginx | tail -n 100
```

Avoid unnecessary pipes when a command can read files directly.

## Variables

```bash
name="jay"
echo "$name"
```

Rules:

- No spaces around `=`.
- Use quotes around variable expansions.
- Environment variables are inherited by child processes only when exported.

```bash
export APP_ENV=prod
```

## Quoting

| Quote | Behavior |
| --- | --- |
| Single quotes `'...'` | Literal text; variables are not expanded. |
| Double quotes `"..."` | Variables and command substitution expand. |
| No quotes | Word splitting and glob expansion can occur. |

Examples:

```bash
name="Jay"
echo '$name'
echo "$name"
```

Best practice: quote variables unless you intentionally want splitting/globbing.

```bash
rm "$file"
```

## Exit Codes

Show previous exit code:

```bash
echo $?
```

Meaning:

- `0` means success.
- Non-zero means failure or special condition.

Use in scripts:

```bash
if grep -q 'ready' status.txt; then
  echo "Ready"
else
  echo "Not ready"
fi
```

## Conditions

```bash
if [ -f app.log ]; then
  echo "log exists"
fi
```

Common tests:

| Test | Meaning |
| --- | --- |
| `-f file` | Regular file exists. |
| `-d dir` | Directory exists. |
| `-z "$var"` | String is empty. |
| `-n "$var"` | String is not empty. |
| `"$a" = "$b"` | Strings equal. |
| `$n -eq 5` | Numbers equal. |

## Loops

For loop:

```bash
for file in *.log; do
  echo "$file"
done
```

While loop:

```bash
while read -r line; do
  echo "$line"
done < file.txt
```

Use `read -r` to avoid backslash escape surprises.

## Functions

```bash
backup_file() {
  local file="$1"
  cp "$file" "$file.bak"
}

backup_file app.conf
```

Use `local` inside functions to avoid accidentally changing global variables.

## Script Header And Safety Options

Script:

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Hello"
```

Meaning:

| Option | Meaning |
| --- | --- |
| `-e` | Exit on many command failures. |
| `-u` | Treat unset variables as errors. |
| `-o pipefail` | Pipeline fails if any command in the pipe fails. |

Caveat: `set -e` has edge cases. Still handle expected failures explicitly.

## Command Substitution

```bash
today="$(date +%F)"
echo "$today"
```

Prefer `$(...)` over backticks for readability.

## Text Processing Basics

```bash
cut -d: -f1 /etc/passwd
sort names.txt
uniq -c
awk '{print $1}' access.log
sed 's/old/new/g' file.txt
tr ':' '\n'
```

Use structured parsers for structured formats when possible:

- Use `jq` for JSON.
- Use `yq` for YAML when available.
- Avoid fragile regex parsing for complex structured data.

## Useful DevOps Commands

```bash
env
printenv PATH
which bash
df -h
du -sh *
free -h
ps aux
ss -tulpen
curl -v https://example.com
journalctl -u service-name -f
```

## Benefits

- Available almost everywhere on Linux.
- Excellent for glue automation.
- Strong text-processing ecosystem.
- Good fit for CI/CD steps and operational scripts.

## Drawbacks / Limitations

- Quoting mistakes can be dangerous.
- Error handling can be subtle.
- Complex scripts become hard to maintain.
- Portability differs between Bash, sh, zsh, and different Unix tools.
- Not ideal for complex data structures or APIs.

## Hidden Details / Caveats

- Always quote variables unless you intentionally want splitting.
- Shell aliases usually do not apply inside non-interactive scripts.
- `cat file | grep pattern` is often unnecessary.
- `set -e` does not replace explicit error handling.
- `rm -rf "$dir"` is dangerous if `dir` is empty or wrong; validate before destructive operations.
- Newlines and spaces in filenames break careless loops.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Spaces around variable assignment | Use `name="value"`. |
| Unquoted variables | Use `"$var"`. |
| Parsing JSON with grep | Use `jq`. |
| Ignoring exit codes | Check command success. |
| Using Bash-only syntax in `sh` scripts | Use `#!/usr/bin/env bash` if Bash is required. |
| Running destructive commands without checks | Print/validate targets first. |

## Best Practices

- Start scripts with a clear shebang.
- Use `set -euo pipefail` where appropriate.
- Quote variables.
- Use `shellcheck` if available.
- Keep scripts small and focused.
- Add comments for non-obvious logic.
- Prefer arrays for lists in Bash.
- Validate inputs before acting.
- Avoid storing secrets in scripts.

## Troubleshooting

| Problem | Check |
| --- | --- |
| Command not found | PATH, installed package, shell builtin vs executable. |
| Permission denied | File permissions, executable bit, user, sudo needs. |
| Script exits early | `set -e`, failing command, unset variable. |
| Variable empty | Assignment, export, subshell, quoting. |
| Works interactively but not in CI | Shell type, working directory, env vars, installed tools. |

## Interview Notes

- `$?` stores the previous command's exit code.
- `0` means success; non-zero means failure/special condition.
- `>` overwrites; `>>` appends.
- Pipes connect stdout to stdin.
- Single quotes prevent variable expansion; double quotes allow it.
- `grep`, `awk`, `sed`, `cut`, `sort`, and `uniq` are common text tools.
- Use `chmod +x script.sh` to make a script executable.

## Related Topics

- [Learning GitHub Actions](Learning%20GitHub%20Actions.md)
- [Jenkins](Jenkins/INDEX.md)
- [Terraform CLI](Terraform/7%20-%20Terraform%20CLI.md)
