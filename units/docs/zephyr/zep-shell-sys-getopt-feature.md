---
id: "zep-shell-sys-getopt-feature"
type: "concept"
domain: "debug"
title: "Shell: sys_getopt Feature"
summary: "Some shell users apart from subcommands might need to use options as well. the arguments string, looking for supported options. Typically, this task is accomplished by the getopt family functions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

Some shell users apart from subcommands might need to use options as well.
the arguments string, looking for supported options. Typically, this task
is accomplished by the `getopt` family functions.

For this purpose shell supports a variant of the getopt and getopt_long libraries from
the FreeBSD project called sys_getopt and sys_getopt_long. This feature is activated by:
`CONFIG_GETOPT` set to `y` and `CONFIG_GETOPT_LONG`
set to `y`.

This feature can be used in thread safe as well as non thread safe manner.
The former is full compatible with regular getopt usage while the latter
a bit differs.

An example non-thread safe usage:

```c

char *cvalue = NULL;
while ((char c = sys_getopt(argc, argv, "abhc:")) != -1) {
      switch (c) {
      case 'c':
              cvalue = sys_getopt_optarg;
              break;
      default:
              break;
      }
}
```
An example thread safe usage:

```c

char *cvalue = NULL;
struct sys_getopt_state *state;
while ((char c = sys_getopt(argc, argv, "abhc:")) != -1) {
      state = sys_getopt_state_get();
      switch (c) {
      case 'c':
              cvalue = state->optarg;
              break;
      default:
              break;
      }
}
```
Thread safe sys_getopt functionality is activated by
`CONFIG_SHELL_GETOPT` set to `y`.
