---
id: "vela-vela-cli-options-cop-format"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / COP format"
summary: "Set the COP (custom operator payload) format version to use. This is metadata that is prepended to the command stream. It contains information that describes the target a command stream has been compiled for. The option --separate-io-region requires --cop-format COP2."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#cop-format"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Set the COP (custom operator payload) format version to use. This is metadata
that is prepended to the command stream. It contains information that describes
the target a command stream has been compiled for. The option
`--separate-io-region` requires `--cop-format COP2`.  
**Type: String**  
**Default: COP1**  
**Choices: [COP1, COP2]**

```bash
vela network.tflite --cop-format COP2
```
