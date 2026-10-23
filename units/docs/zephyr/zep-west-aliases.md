---
id: "zep-west-aliases"
type: "concept"
domain: "project"
title: "West aliases"
summary: "West allows to add alias commands to the local, global or system configuration files. These aliases make it easy to add shortcuts for frequently used, or hard to memorize commands for ease of development."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/alias.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/alias.rst"
license: "Apache-2.0"
mode: "V"
---

West allows to add alias commands to the local, global or system configuration files.
These aliases make it easy to add shortcuts for frequently used, or hard to memorize
commands for ease of development.

Similar to how `git` aliases work, the alias command is replaced with the alias'
full text and parsed as a new shell argument list (using the Python function
shlex.split() internally to split the value). This enables adding argument
parameters as they were passed to the original command. Spaces are considered
argument separators; use proper escaping if arguments shouldn't be split.

.. _shlex.split(): https://docs.python.org/3/library/shlex.html#shlex.split

To add a new alias simply call the `west config` command:

```shell

west config alias.mylist "list -f '{name} {revision}'"
```
To list aliases, use `west help {some_alias}`.

Recursive aliases are allowed as an alias command can contain other aliases, effectively
building more complex but easy-to-remember commands.

It is possible to override an existing command, for example to pass default arguments:

```shell

west config alias.update "update -o=--depth=1 -n"
```

**Warning:** Overriding/shadowing other or built-in commands is an advanced use case, it can lead to strange side-effects and should be done with great care.
