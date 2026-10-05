---
id: "etarm-smollm2-ethos-u-quickstart"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart"
summary: "This document focuses on one validated flow:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/README.md"
license: "BSD-3-Clause"
mode: "V"
---

> **Heads-up:** This Ethos-U post-training quantization flow is still
> experimental. The current recommended path is `w8a16` with
> `quantization.quantize_scope=linear`, which places the linear layers on
> Ethos-U while the remaining FP32 operators still run on the Corstone-320 FVP
> host CPU. That hybrid setup is deliberate: it is the simplest path in this
> example that still produces meaningful text.
>
> This example exports the base `HuggingFaceTB/SmolLM2-135M` checkpoint via
> `base.model_class=smollm2`, so fetch the matching tokenizer from the same
> model family. Do not mix this flow with the `SmolLM2-135M-Instruct`
> tokenizer/checkpoint pair unless you intentionally change the exported model.

This document focuses on one validated flow:

1. Export one generation-ready KV-cache `w8a16` PTE with a 64-token context.
2. Build one runner that embeds that PTE and uses semihosting for host-side
   input/output tensor exchange.
3. Run a short prompt-generation smoke test on Corstone-320 FVP.
4. Optionally evaluate Wikitext perplexity with the same KV-cache artifact.

In this example, semihosting is mainly a convenient FVP integration path for
passing meaningful input tensors into the runner and reading output tensors back
out. The Python host script does the tokenization and prompt preprocessing, then
uses semihosting to provide the resulting input tensor to the model and collect
the output logits. Embedding the PTE is a separate convenience that avoids
copying the model file at runtime. On real silicon, the same preprocessing would
more likely populate the model input buffer directly from software rather than
via semihosting.

The primary path below uses KV-cache decoding with a 64-token context. Each
runtime step executes one token plus its `input_pos`, while the exported context
length controls the KV-cache capacity. The older static non-KV seq32 full-logits
flow remains the safest fallback when debugging full-window execution. Larger
non-KV windows are experimental: they are more expensive at runtime and require
retuning the runner allocator pools. For example, a seq48 embedded-PTE smoke run
needed a scratch pool just under 5 MiB instead of the 4 MiB pool used by the
seq32 non-KV commands.
