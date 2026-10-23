---
id: "pyocd-command-reference-bringup"
type: "concept"
domain: "debug"
title: "Command reference: Bringup"
summary: "These commands are meant to be used when starting up Commander in no-init mode. They are primarily useful for low-level debugging of debug infrastructure on a new chip."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#bringup"
license: "Apache-2.0"
mode: "V"
---

These commands are meant to be used when starting up Commander in no-init mode. They are primarily useful for low-level debugging of debug infrastructure on a new chip.

##### `initdp`

**Usage**: initdp  \
Init DP and power up debug.


##### `makeap`

**Usage**: makeap APSEL \
Creates a new AP object for the given APSEL. The type of AP, MEM-AP or generic, is autodetected.


##### `reinit`

**Usage**: reinit  \
Reinitialize the target object.
