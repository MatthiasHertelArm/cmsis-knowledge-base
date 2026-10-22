---
id: "etarm-tinystories-42m-kv-cache-generatio-alif-e8-deployment"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85: Alif E8 deployment"
summary: "The exported PTE is approximately 103 MiB, so it fits within the current 125 MiB model-storage budget for the Alif E8 Ethos-U85 configuration."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/tinystories42m_example_ethos_u/README.md#alif-e8-deployment"
license: "BSD-3-Clause"
mode: "V"
---

The exported PTE is approximately 103 MiB, so it fits within the current
125 MiB model-storage budget for the Alif E8 Ethos-U85 configuration. Deploy
the PTE with the Alif board-specific ExecuTorch firmware runner; the embedded
Corstone-320 semihosting runner below is only for FVP validation and is not the
Alif firmware image.

The board integration must provide the token and `input_pos` int32 inputs,
retain the KV-cache state between decoding steps, and perform token selection
and decoding in the application. Firmware, runtime arenas, KV-cache buffers,
and tokenizer storage are additional to the PTE size and must be checked
against the board's runtime memory configuration.
