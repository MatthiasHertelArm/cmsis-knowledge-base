---
id: "cet-executorch-on-ethos-u-component-selection"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Component selection"
summary: "The ExecuTorch pack provides the runtime, backends, and individual operators as selectable CMSIS components. create_ai_layer.py examines the exported program and writes ai_layer/ai_layer.clayer.yml so only the required components are linked."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#component-selection"
license: "Apache-2.0"
mode: "V"
---

The [ExecuTorch pack](https://www.keil.arm.com/packs/executorch-pytorch/)
provides the runtime, backends, and individual operators as selectable CMSIS
components. `create_ai_layer.py` examines the exported program and writes
`ai_layer/ai_layer.clayer.yml` so only the required components are linked.
Because the layer is complete before the build starts, an ML model change that
changes the operator set needs nothing more than re-running steps 2 and 3.
