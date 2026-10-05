---
id: "pyocd-configuring-logging-color-logging"
type: "concept"
domain: "debug"
title: "Configuring logging: Color logging"
summary: "By default, log output to a tty is colorised. Control over colorised log output is possible two ways."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuring_logging.md#color-logging"
license: "Apache-2.0"
mode: "V"
---

By default, log output to a tty is colorised. Control over colorised log output is possible two ways.

The command-line `--color` argument accepts an optional parameter that must be one of `auto`, `always`, or `never`.
The default is `auto`, which will enable color only when outputting to a tty.

Another option for controlling color output is the `PYOCD_COLOR` environment variable. It should be set to one of the
same values supported by `--color`. This environment variable changes the default color output setting, and is
overridden by `--color` on the command line.
