---
id: "vela-vela-cli-options-arena-cache-size"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Arena Cache Size"
summary: "Set the size of the arena cache memory area, in bytes. If specified, this option overrides the memory mode attribute with the same name in a Vela configuration file."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#arena-cache-size"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Set the size of the arena cache memory area, in bytes.  If specified, this
option overrides the memory mode attribute with the same name in a Vela
configuration file.  If neither this nor the memory mode attribute are specified
then a size equal to the maximum address supported by the Ethos-U is used.

How this value is used depends on both the optimisation strategy and the selected
memory mode; see [Memory Modes](#memory-modes).  Vela prints a warning when
--arena-cache-size is explicitly specified together with --optimise Size.

**Type: Integer**  
**Choices: [ >= 0]**  

```bash
vela network.tflite --optimise Performance --arena-cache-size 2097152
```
