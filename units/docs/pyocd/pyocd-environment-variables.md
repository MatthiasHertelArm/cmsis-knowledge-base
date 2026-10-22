---
id: "pyocd-environment-variables"
type: "concept"
domain: "debug"
title: "Environment variables"
summary: "Environment variables"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/env_vars.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/env_vars.md"
license: "Apache-2.0"
mode: "V"
---

| Variable | Description |
|---|---|
|  `PYOCD_COLOR`  | Changes the default color output setting. Must be one of `auto`, `always`, or `never`. If not defined, the default is `auto`, which will enable color only when outputting to a tty. Overridden by `--color` on the command line. |
|  `PYOCD_HISTORY`  | Path to the `pyocd commander` command history file. The default is `~/.pyocd_history`. |
|  `PYOCD_HISTORY_LENGTH`  | Maximum number of entries in the command history file. Set to -1 for unlimited. Default is 1000. |
|  `PYOCD_PROJECT_DIR`  | Sets the path to pyOCD's project directory. This variable acts as a fallback if the `project_dir` session option is not specified. |
|  `PYOCD_USB_BACKEND`  | This variable overrides the default selection of the USB backend for CMSIS-DAP v1 probes. The accepted values are `hidapiusb`, `pyusb`, and `pywinusb`. An empty value is the same as unset. CMSIS-DAP v2 probes are unaffected by the environment variable; pyusb is always used. Forcing the USB backend is really only useful on Windows, because both `hidapiusb` and `pywinusb` backends are available. Note that pyOCD only installs the `hidapiusb` backend by default. |
