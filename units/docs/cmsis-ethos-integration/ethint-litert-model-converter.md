---
id: "ethint-litert-model-converter"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter"
summary: "model-converter.py wraps the Arm Ethos-U Vela compiler. It reads target settings and model information from a generated .cbuild-mlops.yml file and converts one or more quantized LiteRT (TensorFlow Lite) input model files."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:script/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md"
license: "Apache-2.0"
mode: "V"
---

`model-converter.py` wraps the Arm Ethos-U Vela compiler. It reads target settings
and model information from a generated `*.cbuild-mlops.yml` file and converts one
or more quantized LiteRT (TensorFlow Lite) input model files.

For the overall workflow and configuration format, see the CMSIS-Toolbox
[MLOps integration documentation](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-integration).

For every input model, the converter generates:

- a Vela-optimized `.tflite` model;
- a C source file containing the optimized model as a byte array; and
- a Markdown file containing the Vela report.
