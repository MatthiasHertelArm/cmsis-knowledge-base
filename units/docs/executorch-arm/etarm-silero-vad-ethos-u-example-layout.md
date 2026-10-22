---
id: "etarm-silero-vad-ethos-u-example-layout"
type: "concept"
domain: "edge-ai"
title: "Silero VAD Ethos-U Example: Layout"
summary: "Silero VAD Ethos-U Example: Layout"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/silero_vad_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/silero_vad_example_ethos_u/README.md#layout"
license: "BSD-3-Clause"
mode: "V"
---

- `model_export/README.md` — Model loading, quantization, Ethos-U85
  lowering, `.pte` generation, and reference probability generation.
- `runtime/README.md` — Building the bare-metal app, generating headers
  from the `.pte` and WAV file, running on FVP, and comparing serial
  probability output.
