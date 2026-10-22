---
id: "zep-built-in-commands-other-project-commands"
type: "concept"
domain: "project"
title: "Built-in commands: Other project commands"
summary: "West has a few more commands for managing the projects in the workspace, which are summarized here. Run west <command> -h for detailed help."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/built-in.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/built-in.rst"
license: "Apache-2.0"
mode: "V"
---

West has a few more commands for managing the projects in the
workspace, which are summarized here. Run `west <command> -h` for
detailed help.

- `west compare`: compare the state of the workspace against the manifest
- `west diff`: run `git diff` in local project repositories
- `west forall`: run an arbitrary command in local project repositories
- `west grep`: search for patterns in local project repositories
- `west list`: print a line of information about each project in the
  manifest, according to a format string
- `west manifest`: manage the manifest file. See west-manifest-cmd.
- `west status`: run `git status` in local project repositories
