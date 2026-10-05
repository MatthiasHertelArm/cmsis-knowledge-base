---
id: "pyocd-session-options-list-picoprobe-options"
type: "concept"
domain: "debug"
title: "Session options list: Picoprobe options"
summary: "These session options are available when the Picoprobe debug probe plugin is active."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#picoprobe-options"
license: "Apache-2.0"
mode: "V"
---

These session options are available when the Picoprobe debug probe plugin is active.



| Option Name | Type | Default | Description |
|---|---|---|---|
| picoprobe.safeswd | bool | False | Use safer but slower SWD transfer function with Picoprobe. Default is False, so possible WAIT or FAULT SWD acknowledges and protocol errors will not be caught immediately. |
