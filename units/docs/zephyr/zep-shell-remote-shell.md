---
id: "zep-shell-remote-shell"
type: "concept"
domain: "debug"
title: "Shell: Remote Shell"
summary: "The shell module supports remote shell. Remote shell allows to execute commands on the remote core using the main core shell interface. User interface features like Tab autocompletion or history navigation are supported on the remote shell client."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The shell module supports remote shell. Remote shell allows to execute commands
on the remote core using the main core shell interface. User interface features
like `Tab` autocompletion or history navigation are supported on the remote
shell client. There can be multiple remote clients connected to the main core shell.
Each remote client has its own tree of commands. Remote client commands are executed
in the context of the remote client core. Remote shell is using ipc_service to
communicate with the remote core.

If only a single remote client is enabled then `remote_shell` command is registered as a root
command for the remote core tree of commands. If multiple remote clients are enabled
then `remote_shell <core_name>` is used as a root for the given remote client.

Remote client implementation supports case where threads are disabled
(`CONFIG_MULTITHREADING` set to `n`).

This approach has two main benefits:

1. It allows to use the same shell interface for both the main and the remote cores.
2. Full shell implementation is present only on the host core, significantly reducing the
   memory footprint of the remote cores. Implementation uses less than 3 kB per remote client.
   Half of the memory is used for string formatting and can be shared with other
   modules that use string formatting (for example, logging).

See shell-module for details on how to enable remote shell.


### Configuration


Following Kconfig options are available for remote shell host configuration:

`CONFIG_SHELL_REMOTE`: Enables remote shell on the host core.

`CONFIG_SHELL_REMOTE_MULTI_CLI`: Enables multiple remote clients.

`CONFIG_SHELL_REMOTE_TMP_BUF_SIZE`: Size of the temporary buffer for remote shell
command data. Need to be large enough to hold the command and its arguments.

Following Kconfig options are available for remote shell client configuration:

`CONFIG_SHELL_REMOTE_CLI`: Enables remote shell client on the remote core.

`CONFIG_SHELL_REMOTE_CLI_BUF_SIZE`: Size of the internal buffer used for
remote messages. Need to be large enough to hold the command syntax and help text.
Help text is truncated if the buffer is too small. It is also used to hold data for
shell print messages. If it is too small then the print message is replaced with
the error message.

`CONFIG_SHELL_REMOTE_CLI_KWORK`: Use kwork context for command execution.

`CONFIG_SHELL_REMOTE_CLI_STACK_SIZE`: Thread stack size for remote shell client.

If a single client is used then IPC service device is automatically chosen based on the devicetree
configuration. User can specify the IPC device tree node using chosen node. If not specified then
if there is only a single IPC device available that one is used.

IPC service device tree node configuration example:

```dts

chosen {
    zephyr,ipc_shell = &ipc0;
};
```

### Limitations


Some shell features are not supported on the remote shell client:

* Bypass mode is not supported on the remote shell client.
* Select mode is not supported on the remote shell client.

IPC communication assumes same endianness and alignment of the data on both sides. It has been
tested on the following core pairs:

* Cortex-M33 (host) and Cortex-M33 (client)
* Cortex-M33 (host) and RISC-V 32 (client)
