---
id: "ethu-test-ethos-u"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U"
summary: "This CMSIS-Toolbox integration test provides target solutions for Arm Ethos-U55, Ethos-U65, and Ethos-U85 NPUs. The project runs on the matching Corstone FVP simulation or hardware when used as a reference application."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/README.md"
license: "Apache-2.0"
mode: "V"
---

This CMSIS-Toolbox integration test provides target solutions for
Arm Ethos-U55, Ethos-U65, and Ethos-U85 NPUs. The project runs on
the matching Corstone FVP simulation or hardware when used as a
[reference application](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/).

The test demonstrates end-to-end TensorFlow Lite Micro (TFLM) integration for
Ethos-U systems. It builds and runs two Vela-compiled models, supplies a golden
input to each model, and compares the NPU output bit-for-bit with output captured
from the host TensorFlow Lite reference interpreter.

Key features include:

- **Full NPU offload:** both models contain zero CPU operators after Vela compilation.
- **Self-checking execution:** embedded host-reference vectors turn the example
  into an integration test with a clear `PASS` or `FAIL` result.
- **Layered CMSIS solution:** target-specific code is in a `Board` layer and
  ML specific content is in an `ML-Model` layer.
- **Model artifacts provided:** the original quantized `.tflite` files and the
  Vela-generated models can be recompiled.
- **Configurable integration:** the supplied `vela.ini` provides alternative
  memory modes, while the original models can be recompiled for other NPU
  configurations with the supplied model converter.
