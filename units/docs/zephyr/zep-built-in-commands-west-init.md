---
id: "zep-built-in-commands-west-init"
type: "concept"
domain: "project"
title: "Built-in commands: west init"
summary: "This command creates a west workspace. It can be used in two ways:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/built-in.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/built-in.rst"
license: "Apache-2.0"
mode: "V"
---

This command creates a west workspace. It can be used in two ways:

1. Cloning a new manifest repository from a remote URL
2. Creating a workspace around an existing local manifest repository

**Option 1**: to clone a new manifest repository from a remote URL, use:

```none

west init [-m URL] [--mr REVISION] [--mf FILE] [directory]
```
The new workspace is created in the given `directory`, creating a new
`.west` inside this directory. You can give the manifest URL using
the `-m` switch, the initial revision to check out using `--mr`, and
the location of the manifest file within the repository using `--mf`.

For example, running:

```shell

west init -m https://github.com/zephyrproject-rtos/zephyr --mr v1.14.0 zp
```
would clone the upstream official zephyr repository into `zp/zephyr`,
and check out the `v1.14.0` release. This command creates
`zp/.west`, and set the `manifest.path` :ref:`configuration option
<west-config>` to `zephyr` to record the location of the manifest
repository in the workspace. The default manifest file location is used.

The `-m` option defaults to `https://github.com/zephyrproject-rtos/zephyr`.
The `--mf` option defaults to `west.yml`. Since west v0.10.1, west will use
the default branch in the manifest repository unless the `--mr` option
is used to override it. (In prior versions, `--mr` defaulted to `master`.)

If no `directory` is given, the current working directory is used.

**Option 2**: to create a workspace around an existing local manifest
repository, use:

```none

west init -l [--mf FILE] directory
```
This creates `.west` **next to** `directory` in the file
system, and sets `manifest.path` to `directory`.

As above, `--mf` defaults to `west.yml`.

**Reconfiguring the workspace**:

If you change your mind later, you are free to change `manifest.path` and
`manifest.file` using west-config-cmd after running `west init`.
Just be sure to run `west update` afterwards to update your workspace to
match the new manifest file.
