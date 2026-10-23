---
id: "etarm-tinystories-42m-kv-cache-generatio"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85"
summary: "This example exports the stories42M.pt checkpoint as a static-shape, token-at-a-time KV-cache model with linear w8a16 PT2E quantization. It reuses the validated SmolLM2 Ethos-U semihosting runner and host generation helper."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/tinystories42m_example_ethos_u/README.md"
license: "BSD-3-Clause"
mode: "V"
---

This example exports the `stories42M.pt` checkpoint as a static-shape,
token-at-a-time KV-cache model with linear `w8a16` PT2E quantization. It reuses
the validated SmolLM2 Ethos-U semihosting runner and host generation helper.
