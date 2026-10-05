---
id: "pyocd-command-reference-device"
type: "concept"
domain: "debug"
title: "Command reference: Device"
summary: "Command reference: Device"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/command_reference.md#device"
license: "Apache-2.0"
mode: "V"
---

##### `reset`

**Usage**: reset [halt|-halt|-h] [TYPE] \
Reset the target, optionally with halt and/or specifying the reset type. The reset type must be one of 'default', 'hardware', 'system', 'core', 'n_srst', 'sysresetreq', 'vectreset' or 'emulated'.


##### `unlock`

**Usage**: unlock  \
Unlock security on the target.
