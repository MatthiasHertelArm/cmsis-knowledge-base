---
id: "cet-the-mlops-flow-3-cbuild-builds-the-application"
type: "concept"
domain: "edge-ai"
title: "The MLOps flow: 3. `cbuild` builds the application"
summary: "cbuild cmsis-executorch.csolution.yml --active SSE-320-U85 is a plain CMSIS build without any Python."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/mlops-flow.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md#3-cbuild-builds-the-application"
license: "Apache-2.0"
mode: "V"
---

`cbuild cmsis-executorch.csolution.yml --active SSE-320-U85` is a plain
CMSIS build without any Python. The cproject knows nothing about the model: it
lists the application source and the two layers, and the AI layer contributes
both the component selection and the model data.

Because the layer is complete before CMSIS-Toolbox resolves components, a model
change that changes the operator set is just another run of step 2 followed by
step 3.
