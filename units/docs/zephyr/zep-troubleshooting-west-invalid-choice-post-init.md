---
id: "zep-troubleshooting-west-invalid-choice-post-init"
type: "concept"
domain: "project"
title: "Troubleshooting West: \"invalid choice: 'post-init'\""
summary: "If you see this error when running west init:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

If you see this error when running `west init`:

```none

west: error: argument <command>: invalid choice: 'post-init'
(choose from 'init', 'update', 'list', 'manifest', 'diff',
'status', 'forall', 'config', 'selfupdate', 'help')
```
Then you have an old version of west installed, and are trying to use it in a
workspace that requires a more recent version.

The easiest way to resolve this issue is to upgrade west and retry as follows:

#. Install the latest west with the `-U` option for `pip3 install` as shown
   in west-install.

#. Back up any contents of `zephyrproject/.west/config` that you want to
   save. (If you don't have any configuration options set, it's safe to skip
   this step.)

#. Completely remove the `zephyrproject/.west` directory (if you don't,
   you will get the "already in a workspace" error message discussed next).

#. Run `west init` again.
