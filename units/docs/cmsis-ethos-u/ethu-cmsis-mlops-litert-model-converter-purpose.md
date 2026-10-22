---
id: "ethu-cmsis-mlops-litert-model-converter-purpose"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Purpose"
summary: "model-converter.py wraps the Ethos-U Vela compiler. It converts one or more quantized LiteRT models (TensorFlow Lite) and generates their integration files. A generated .cbuild-mlops.yml file supplies model names, paths, and Vela configuration."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/examples/Test-Ethos-U/script/model-converter-specification.md#purpose"
license: "Apache-2.0"
mode: "V"
---

`model-converter.py` wraps the Ethos-U Vela compiler. It converts one or more
quantized LiteRT models (TensorFlow Lite) and generates their integration
files. A generated `*.cbuild-mlops.yml` file supplies model names, paths, and
Vela configuration.

The surrounding workflow and generated configuration are defined by the
CMSIS-Toolbox [MLOps integration documentation](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-integration).
