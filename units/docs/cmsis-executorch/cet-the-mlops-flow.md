---
id: "cet-the-mlops-flow"
type: "concept"
domain: "edge-ai"
title: "The MLOps flow"
summary: "The mlops: node in cmsis-executorch.csolution.yml is the central definition of the initial Ethos-U target for this template. It follows the CMSIS-Toolbox MLOps information specification. This document explains how the three build steps use and propagate that information."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/mlops-flow.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md"
license: "Apache-2.0"
mode: "V"
---

The `mlops:` node in `cmsis-executorch.csolution.yml` is the central
definition of the initial Ethos-U target for this template. It follows the CMSIS-Toolbox
[MLOps information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information)
specification. This document explains how the three build steps use and
propagate that information.

```mermaid
flowchart TD
    A["cmsis-executorch.csolution.yml<br/><b>mlops:</b> node"] -->|"1. cbuild setup --active &lt;target&gt;"| B["cmsis-executorch.cbuild-mlops.yml<br/>npu, vela.options, model.clayer"]
    B -->|"2. create_ai_layer.py"| C["EthosUCompileSpec<br/>quantize, delegate, Vela"]
    D["model/model.py<br/>TinyCNN"] --> C
    C --> E["ai_layer/model_pte.c<br/>the program as a C array"]
    C --> F["ai_layer/ai_layer.clayer.yml<br/>component selection"]
    E --> G["3. cbuild --active &lt;target&gt;"]
    F --> G
    G --> H["cmsis-executorch.axf"]
```
