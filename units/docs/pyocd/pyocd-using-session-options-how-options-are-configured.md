---
id: "pyocd-using-session-options-how-options-are-configured"
type: "concept"
domain: "debug"
title: "Using session options: How options are configured"
summary: "Loading of options from YAML files is handled automatically when the Session object is created. Probe-specific options are automatically set, too."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api/using_session_options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api/using_session_options.md#how-options-are-configured"
license: "Apache-2.0"
mode: "V"
---

Loading of options from YAML files is handled automatically when the `Session` object is created. Probe-specific options are automatically set, too.

Options set through command line arguments, both dedicated arguments and `-O`, are passed into the `Session` constructor and added as their own layer. The `ConnectHelper` methods that are most often used to create sessions will pass through options related arguments to `Session`.
