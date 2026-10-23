---
id: "vela-vela-cli-options-ignore-ops"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Ignore Ops"
summary: "Lets the specified TFLite builtin operator types fall back to the CPU so they remain as CPU operators in the output .tflite model."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#ignore-ops"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Lets the specified TFLite builtin operator types fall back to the CPU so they
remain as CPU operators in the output `.tflite` model.

This option is only supported when using the Regor core. For TOSA input networks,
the option is accepted but ignored. The value is a comma-separated list of
TFLite builtin operator names and the option can be specified multiple times.
Operator names are case-insensitive.

**Type: String**  
**Default: None**  
**Format: `OP[,OP...]`**

```bash
vela network.tflite --ignore-ops ADD,ARGMAX --ignore-ops CONV_2D
```
