---
id: "etarm-tinystories-42m-kv-cache-generatio-kv-cache-configuration"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85: KV-cache configuration"
summary: "Use FP32 KV-cache buffers for Alif E8 deployment. These buffers retain the key and value tensors computed for earlier tokens and are updated for each new token."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/tinystories42m_example_ethos_u/README.md#kv-cache-configuration"
license: "BSD-3-Clause"
mode: "V"
---

Use FP32 KV-cache buffers for Alif E8 deployment. These buffers retain the key
and value tensors computed for earlier tokens and are updated for each new
token. Board measurements found decoding with FP32 KV-cache buffers
approximately 6x faster than with statically quantized int8 KV-cache buffers.
At ctx64, storing the KV-cache buffers as int8 reduces their runtime size from
approximately 2 MiB to 0.5 MiB, but does not reduce the PTE stored in OSPI. For
implementation details, see the
[SmolLM2 static KV-cache section](https://github.com/pytorch/executorch/blob/658390c/examples/arm/tinystories42m_example_ethos_u/../smollm2_example_ethos_u/README.md#7-experimental-static-quantized-kv-cache).
