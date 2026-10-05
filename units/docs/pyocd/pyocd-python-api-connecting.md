---
id: "pyocd-python-api-connecting"
type: "concept"
domain: "debug"
title: "python api: Connecting"
summary: "pyOCD provides a handful of helper routines that make it very easy to enumerate and connect to available debug probes. These routines are all available as static methods on the ConnectHelper class in pyocd.core.helpers."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md#connecting"
license: "Apache-2.0"
mode: "V"
---

pyOCD provides a handful of helper routines that make it very easy to enumerate and connect to
available debug probes. These routines are all available as static methods on the `ConnectHelper`
class in `pyocd.core.helpers`.

`ConnectHelper.session_with_chosen_probe()` is the primary connection helper. This method returns
a single `Session` object, or None. If only a single probe is available, a new session for that
probe is returned immediately. But if there are multiple probes available, then by default, it will
present a simple console UI that lets the user select which probe they want to use. Other options
allow automatically picking the first available probe.

One of the most useful parameters for `session_with_chosen_probe()` is `unique_id`. Pass whole or
part of a probe's unique ID (aka serial number) to programmatically select a specific probe.

Session options may be passed to `session_with_chosen_probe()` in two ways. The `options`
parameter accepts a dictionary of session options. Or, you may pass options as keyword parameters.
The two methods may be combined.
