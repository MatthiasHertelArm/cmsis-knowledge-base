---
id: "vela-vela-cli-options-separate-io-regions"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Separate IO regions"
summary: "Control where to allocate the Ethos-U Custom operator inputs and outputs. Default behaviour is to allocate inputs and outputs in the scratch region."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#separate-io-regions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Control where to allocate the Ethos-U Custom operator inputs and outputs.
Default behaviour is to allocate inputs and outputs in the scratch region. This
flag changes that so that inputs are allocated linearly in the input region and
outputs are allocated linearly in the output region. Each Ethos-U Custom
operator has a local address space for inputs and outputs, which means that the
first input and output to a Ethos-U Custom operator will always be allocated at
offset 0.

```bash
vela network.tflite --separate-io-regions --cop-format COP2
```
