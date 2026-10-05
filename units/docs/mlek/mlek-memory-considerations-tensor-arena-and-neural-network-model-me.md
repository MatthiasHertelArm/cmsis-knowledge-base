---
id: "mlek-memory-considerations-tensor-arena-and-neural-network-model-me"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Tensor arena and neural network model memory placement"
summary: "The evaluation kit uses the name activation buffer for the tensor arena in the TensorFlow Lite Micro framework and compute buffer region in the ExecuTorch framework."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/memory_considerations.md#tensor-arena-and-neural-network-model-memory-placement"
license: "Apache-2.0"
mode: "V"
---

The evaluation kit uses the name `activation buffer` for the `tensor arena` in the TensorFlow Lite Micro framework
and compute buffer region in the ExecuTorch framework.
Every use-case application has a corresponding `<use_case_name>_ACTIVATION_BUF_SZ` parameter that governs the maximum
available size of the `activation buffer` for that particular use-case.

The linker script is set up to place this memory region in SRAM for *Ethos-U55* or in flash for *Ethos-U65* and *Ethos-U85*
(following the default memory modes of `Shared_Sram` and `Dedicated_Sram` respectively).

The neural network model is always placed in the flash region (even in case of `Sram_Only` memory mode as mentioned earlier).
