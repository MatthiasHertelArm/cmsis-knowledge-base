---
id: "pyocd-using-session-options-adding-new-options"
type: "concept"
domain: "debug"
title: "Using session options: Adding new options"
summary: "Session options are defined by an instance of OptionInfo (from pyocd.core.options) that specifies the name, type(s), default value, and a help string. At runtime, the complete set of options is in the pyocd.core.options.OPTIONS_INFO dict."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/api/using_session_options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/api/using_session_options.md#adding-new-options"
license: "Apache-2.0"
mode: "V"
---

Session options are defined by an instance of `OptionInfo` (from `pyocd.core.options`) that specifies the name, type(s), default value, and a help string. At runtime, the complete set of options is in the `pyocd.core.options.OPTIONS_INFO` dict. Be sure to define any new options so they're documented and get a default and help text.

For example, this is the definition of the `frequency` option:

```py
OptionInfo('frequency', int, 1000000, "SWD/JTAG frequency in Hertz.")
```

There are several places to define a new option.

- Global and gdb server options should be added to the `BUILTIN_OPTIONS` list in `pyocd/core/options.py`
- Plugins can return a list of `OptionInfo` objects from the `.options` property of the `Plugin` subclass.
- Python scripts, including [user scripts]({% link _docs/user_scripts.md %}), can add new option definitions by calling `add_option_set()` (from `pyocd.core.options`) and passing a list of `OptionInfo` objects.

Supported types for options are *bool*, *int*, *float*, and *str*. An option that allows multiple types is specified with a tuple of those types. The `convert_session_options()` function from `pyocd.utility.cmdline` will convert the *bool*, *int*, and *float* options from a string value. However, there is not automatic type conversion when setting options directly on the `OptionsManager`.
