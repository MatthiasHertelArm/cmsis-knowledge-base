---
id: "ethu-cmsis-mlops-litert-model-converter-dependencies"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Dependencies"
summary: "It works on Windows, Linux, and macOS and uses pathlib for path handling. It does not import LiteRT or TensorFlow because it operates directly on existing quantized .tflite files."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/script/model-converter-specification.md#dependencies"
license: "Apache-2.0"
mode: "V"
---

The script requires:

- Python 3.10 or newer;
- PyYAML; and
- a Vela executable on `PATH`.

It works on Windows, Linux, and macOS and uses `pathlib` for path handling. It
does not import LiteRT or TensorFlow because it operates directly on existing
quantized `.tflite` files.
