---
id: "zep-shell-alias-support"
type: "concept"
domain: "debug"
title: "Shell: Alias support"
summary: "The shell can expand aliases before executing a command when CONFIG_SHELL_ALIASES is enabled. Zephyr always provides the built-in alias ?, which expands to help."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The shell can expand aliases before executing a command when
`CONFIG_SHELL_ALIASES` is enabled. Zephyr always provides the
built-in alias `?`, which expands to `help`.

To load additional aliases from a host file, set
`CONFIG_SHELL_ALIASES_FILE` and generate the corresponding
include file from the application `CMakeLists.txt` file. When
`CONFIG_SHELL_ALIASES_FILE` is non-empty,
`CONFIG_SHELL_ALIASES_HAS_FILE` is enabled automatically.

```cmake

if(CONFIG_SHELL_ALIASES_HAS_FILE)
  set(gen_dir ${ZEPHYR_BINARY_DIR}/include/generated/)
  set(aliases_src ${CONFIG_SHELL_ALIASES_FILE})

  generate_shell_aliases_inc_file_for_target(
    app
    ${aliases_src}
    ${gen_dir}/generated-shell-aliases.inc
  )
endif()
```
The aliases file uses one `alias=command` entry per line. Lines beginning
with `#` are comments, and command strings containing spaces must be quoted.
The sample at `samples/net/sockets/echo_service/shell_aliases.txt`
uses the following format:

```none

# Example shell aliases file
stacks="kernel thread stacks"
scan="wifi scan"
connect="wifi connect"
```
Use the `aliases` command to inspect the aliases available in the
running shell.
