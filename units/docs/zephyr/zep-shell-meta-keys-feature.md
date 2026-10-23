---
id: "zep-shell-meta-keys-feature"
type: "concept"
domain: "debug"
title: "Shell: Meta Keys Feature"
summary: "The shell module supports the following meta keys:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The shell module supports the following meta keys:


* - Meta keys
  - Action
* - `Ctrl+a`
  - Moves the cursor to the beginning of the line.
* - `Ctrl+b`
  - Moves the cursor backward one character.
* - `Ctrl+c`
  - Preserves the last command on the screen and starts a new command in
    a new line.
* - `Ctrl+d`
  - Deletes the character under the cursor.
* - `Ctrl+e`
  - Moves the cursor to the end of the line.
* - `Ctrl+f`
  - Moves the cursor forward one character.
* - `Ctrl+k`
  - Deletes from the cursor to the end of the line.
* - `Ctrl+l`
  - Clears the screen and leaves the currently typed command at the top of
    the screen.
* - `Ctrl+n`
  - Moves in history to next entry.
* - `Ctrl+p`
  - Moves in history to previous entry.
* - `Ctrl+t`
  - Toggles logs output on the shell when `CONFIG_SHELL_LOG_BACKEND` is set.
* - `Ctrl+u`
  - Clears the currently typed command.
* - `Ctrl+w`
  - Removes the word or part of the word to the left of the cursor. Words
    separated by period instead of space are treated as one word.
* - `Alt+b`
  - Moves the cursor backward one word.
* - `Alt+f`
  - Moves the cursor forward one word.
This feature is activated by `CONFIG_SHELL_METAKEYS` set to `y`.
