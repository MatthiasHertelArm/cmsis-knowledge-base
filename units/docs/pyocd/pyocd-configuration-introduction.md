---
id: "pyocd-configuration-introduction"
type: "concept"
domain: "debug"
title: "configuration: Introduction"
summary: "pyOCD allows you to control many aspects of its behaviour by setting session options. There are multiple ways to set these options."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuration.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuration.md#introduction"
license: "Apache-2.0"
mode: "V"
---

pyOCD allows you to control many aspects of its behaviour by setting
_session options_. There are multiple ways to set these options.

- Many of the most commonly used session options have dedicated command line arguments.
- Options can be placed in a YAML config file.
- Arbitrary options can be set individually with the `-O_option_=_value_` command line argument.
- If you are using the Python API, see the [session options developer documentation]({% link _docs/api/using_session_options.md %}) for information about using session options.

The priorities of the different session option sources, from highest to lowest:

1. Dedicated command-line arguments.
2. `-O` command-line arguments.
3. Probe-specific options from a config file.
4. Global options from a config file.
5. Changes to an option's default value. Used only in rare cases for certain subcommands.
6. The option's default value.





The full set of session options is documented in the
Session options list reference.
