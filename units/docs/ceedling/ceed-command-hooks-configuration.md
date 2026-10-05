---
id: "ceed-command-hooks-configuration"
type: "concept"
domain: "test"
title: "Command Hooks: Configuration"
summary: "To connect utilties or scripts to build step hooks, Ceedling tools must be defined."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/command-hooks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/command-hooks/#configuration"
license: "MIT"
mode: "V"
---

### Overview

To connect utilties or scripts to build step hooks, Ceedling tools must be defined.

A Ceedling tool is just a YAML blob that gathers together a handful of settings and values that tell Ceedling how to build and execute a command line. Your tool can be a command line utility, a script, etc.

Example Ceedling tools follow. When enabled, this plugin ensures any tools you define are executed by the corresponding build step hook they are organized beneath. The configurtion of enabled hooks and tools happens in a top-level `:command_hooks:` block within your project configuration. One or more tools can be attached to a build step hook.

### Tool lists

A command hook can execute one or more tools.

If only a single tool is needed, its hash keys and value can be organized as a YAML sub-hash beneath the hook key. Alternatively, a single tool can exist as the only entry in a YAML list.

If multiple tools are needed, they must be organized as entries in a YAML list.

See the commented examples below.

### Tool definitions

Each Ceedling tool requires an `:executable` string and an optional `:arguments` list. See the [`:tools` configuration reference][tools-doc] to understand how to craft your argument list and other tool options.

This plugin passes one or two runtime parameters for use in a hook’s tool argument list depending on the hook. These parameters are referenced with Ceedling tool argument expansion identifiers `${1}`, `${2}`, etc. Wherever you place `${1}` or `${2}` in your tool argument list, they expand in the command line Ceedling constructs with the parameters this plugin provides for that build step hook. The list of build step hooks below documents which parameters are available for each hook.

Each tool may optionally include a `:name` — a simple nickname used in log and error messages. If omitted, the plugin forms a default name from the hook’s key (e.g. `pre_mock_generate`). For a hook configured with a list of tools, the default name additionally includes the tool’s position in the list (e.g. `post_link_execute_0`, `post_link_execute_1`). See the commented examples below.

[tools-doc]: ../configuration/reference/tools.md

### Hook logging

In addition to the standard Ceedling tool definition elements, a hook configuration entry may optionally include a `:logging` setting.

`:logging` may be set to `TRUE` or `FALSE`. An omitted setting is equivalent to `FALSE`.

When logging is enabled and logging conditions are appropriate, any output from the hook tool will be logged to the console with a brief header identifying the hook.

* Explicit command hook output logging only occurs at verbosity levels Normal and Obnoxious.
* Debug logging naturally displays hook output as part of normal tool execution logging. It is not duplicated by hook logging.
* At Normal verbosity, blank hook output is not logged at all; Obnoxious verbosity will display blank output as `<empty>`.

### Command Hooks example configuration YAML

```yaml
:command_hooks:
  # Hook called every time a mock is generated
  # Who knows what my_script.py does -- sky is the limit
  :pre_mock_generate:
    # This tool is organized as a sub-hash beneath the command hook key
    :executable: python
    :name: 'mock prep script' # Explicit nickname used in log/error messages
    :arguments:
      - my_script.py
      - --some-arg
      - ${1} # Replaced with the filepath of the header file that will be mocked
    :logging: TRUE # Log any tool output to console
      
  # Hook called for each linking operation
  # Here, we are performing two tasks for the same build step hook, converting a
  # binary executable to S-record format and, then, archiving with other artifacts.
  # Neither tool below is given a :name -- the plugin defaults them to
  # "post_link_execute_0" and "post_link_execute_1"
  :post_link_execute:
    # These tools are organized in a YAML list beneath the command hook key
    - :executable: objcopy.exe
      :arguments:
        - ${1} # Replaced with the filepath to the linker’s binary artifact output
        - output.srec
        - --strip-all
    - :executable: 
      :arguments: tar.exe
        - -acf
        - awesome_build.zip
        - ${1} # Replaced with the filepath to the linker’s binary artifact output
        - memory_report.txt
```
