---
id: "pyocd-using-session-options-priority-layers"
type: "concept"
domain: "debug"
title: "Using session options: Priority layers"
summary: "Session options have a priority based on their source. The OptionsManager class implements these priorities as an ordered sequence of layers from front (high priority) to back (low priority). Each layer is a dict of option name to value."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/api/using_session_options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/api/using_session_options.md#priority-layers"
license: "Apache-2.0"
mode: "V"
---

Session options have a priority based on their source. The `OptionsManager` class implements these priorities as an ordered sequence of layers from front (high priority) to back (low priority). Each layer is a dict of option name to value. There is also an implicit lowest-priority layer derived from default values specified in the option definitions.

The priorities of the different sources, from front to back:

1. Keyword arguments to the `Session` constructor. Applies to most dedicated command-line arguments.
2. _options_ parameter to `Session` constructor. Applies to `-O` command-line arguments.
3. Options set by CMSIS-Toolbox Run and Debug Management (`cbuild-run`)
4. Probe-specific options from a config file.
5. Global options from a config file.
6. _option_defaults_ parameter to `Session` constructor. Used only in rare cases by subcommands to change the default value of options.
7. Default values from option definitions.

The `.set()` method simply modifies the value of the highest priority (aka front) copy of the option. Additional layers can be added to the front or back using the `.add_front()` and `.add_back()` methods. These methods take a dict of new option values.
