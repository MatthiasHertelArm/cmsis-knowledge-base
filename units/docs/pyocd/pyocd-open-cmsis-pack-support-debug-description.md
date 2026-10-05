---
id: "pyocd-open-cmsis-pack-support-debug-description"
type: "concept"
domain: "debug"
title: "Open-CMSIS-Pack support: Debug description"
summary: "A Device Family Pack contains a description of the device's debug architecture. In pyOCD, this is used primarily to support debug access sequences."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/open_cmsis_pack_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/open_cmsis_pack_support.md#debug-description"
license: "Apache-2.0"
mode: "V"
---

A Device Family Pack contains a [description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html) of the device's debug architecture. In pyOCD, this is used primarily to support debug access sequences. For its own use, pyOCD automatically discovers the device's debug architecture via the Arm CoreSight discovery process (e.g., reading ROM tables) since this is usually more reliable and also works for devices without debug descriptions.

### Reset types

The debug description can set a target's default reset type and disable certain reset types.
