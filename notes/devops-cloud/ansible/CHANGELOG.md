# Ansible Changelog

## 2026-11-21

- Fixed `KodeCloud Ansible Course.md`, the course notes:
  - Corrected the config file search order: the third location is `~/.ansible.cfg` in the home directory, not `./.ansible.cfg`. Added that only the first file found is used and nothing is merged.
  - Corrected section names to their real spelling (`[privilege_escalation]`, `[colors]`) and fixed typos such as `ANSILBE_`.
  - Replaced "an environment variable takes the highest priority" with the actual chain: environment variables beat `ansible.cfg`, but command-line options, playbook keywords and variables beat both.
  - Noted that not every environment variable is `ANSIBLE_<KEY>` (for example `ANSIBLE_COLOR_ERROR`), explained what `gathering = explicit` does, and showed the project `ansible.cfg` as an ini file instead of a mixed shell block.
  - Fixed heading levels, lists, code fence languages and blank lines to match the Linter rules.
  - Added a config-search diagram, YAML spacing and indentation rules, a "Small Details That Matter Later" section and self-test questions with hidden answers.
  - Linked it from `INDEX.md`.
  - Facts checked against the Ansible configuration, precedence and installation docs on docs.ansible.com.
- Rewrote the Config Precedence section of `2 - Inventory and Configuration.md`. It said only that Ansible "looks for config in several places", so it now:
  - Separates the two questions: which config file is read, and which value wins when a setting is given several ways.
  - Explains why the search order exists, that only the first file found is used (unlike Git, nothing is layered) and why a world-writable directory is skipped, with the WSL `/mnt/c` case and its fixes.
  - Lays out the precedence ladder (configuration settings, command-line options, playbook keywords, variables), with the remote-user example across all five forms and the tie-break rule inside each category.
  - Shows how to check what Ansible actually used (`ansible --version`, `ansible-config dump --only-changed`, `ansible-config list`) and what `ansible-config` cannot see.
  - Adds a worked "personal settings vanish" example and two self-test questions with hidden answers.
  - Adds matching rows to Hidden Details, Troubleshooting and Interview Notes, two official references, and links between this note and the course notes.

## 2026-05-27

- Refreshed source assumptions against current Ansible community documentation.
- Added `7 - Idempotency Infrastructure Labs and Operational Runbooks.md`.
- Added `10 - Cheatsheet.md` and `11 - Glossary.md`.
- Marked ansible-core 2.19 / Ansible 12 templating changes as version-sensitive.

