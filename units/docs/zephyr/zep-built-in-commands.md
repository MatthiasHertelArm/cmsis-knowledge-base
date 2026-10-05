---
id: "zep-built-in-commands"
type: "concept"
domain: "project"
title: "Built-in commands"
summary: "This page describes west's built-in commands, some of which were introduced in west-basics, in more detail."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/built-in.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/built-in.rst"
license: "Apache-2.0"
mode: "V"
---

This page describes west's built-in commands, some of which were introduced in
west-basics, in more detail.

Some commands are related to Git commands with the same name, but operate
on the entire workspace. For example, `west diff` shows local changes in
multiple Git repositories in the workspace.

Some commands take projects as arguments. These arguments can be project
names as specified in the manifest file, or (as a fallback) paths to them
on the local file system. Omitting project arguments to commands which
accept them (such as `west list`, `west forall`, etc.) usually defaults
to using all projects in the manifest file plus the manifest repository
itself.

For additional help, run `west <command> -h` (e.g. `west init -h`).
