---
id: "zep-shell-usage"
type: "concept"
domain: "debug"
title: "Shell: Usage"
summary: "The following code shows a simple use case of this library:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The following code shows a simple use case of this library:

```c

int main(void)
{

}

static int cmd_demo_ping(const struct shell *sh, size_t argc,
             char **argv)
{
    ARG_UNUSED(argc);
    ARG_UNUSED(argv);

    shell_print(sh, "pong");
    return 0;
}

static int cmd_demo_params(const struct shell *sh, size_t argc,
               char **argv)
{
    int cnt;

    shell_print(sh, "argc = %d", argc);
    for (cnt = 0; cnt < argc; cnt++) {
        shell_print(sh, "  argv[%d] = %s", cnt, argv[cnt]);
    }
    return 0;
}

/* Creating subcommands (level 1 command) array for command "demo". */
SHELL_STATIC_SUBCMD_SET_CREATE(sub_demo,
    SHELL_CMD(params, NULL, "Print params command.",
                           cmd_demo_params),
    SHELL_CMD(ping,   NULL, "Ping command.", cmd_demo_ping),
    SHELL_SUBCMD_SET_END
);
/* Creating root (level 0) command "demo" without a handler */
SHELL_CMD_REGISTER(demo, &sub_demo, "Demo commands", NULL);

/* Creating root (level 0) command "version" */
SHELL_CMD_REGISTER(version, NULL, "Show kernel version", cmd_version);
```
Users may use the `Tab` key to complete a command/subcommand or to see the
available subcommands for the currently entered command level.
For example, when the cursor is positioned at the beginning of the command
line and the `Tab` key is pressed, the user will see all root (level 0)
commands:

```none

clear  demo  shell  history  log  resize  version
```

**Note:** To view the subcommands that are available for a specific command, you must first type a `space` after this command and then hit

These commands are registered by various modules, for example:

* `clear`, `shell`, `history`, and `resize`
  are built-in commands which have been registered by
  `subsys/shell/shell.c`
* `demo` and `version` have been registered in example code
  above by main.c
* `log` has been registered by `subsys/logging/log_cmds.c`

Then, if a user types a `demo` command and presses the `Tab` key,
the shell will only print the subcommands registered for this command:

```none

params  ping
```
