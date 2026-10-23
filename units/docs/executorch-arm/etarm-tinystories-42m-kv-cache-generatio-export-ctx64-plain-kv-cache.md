---
id: "etarm-tinystories-42m-kv-cache-generatio-export-ctx64-plain-kv-cache"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85: Export ctx64 plain KV cache"
summary: "Although the KV model consumes one token per invocation, max_seq_length=64 describes the exported sequence capacity. PT2E uses one 64-token Wikitext sample for the quick validation calibration."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/tinystories42m_example_ethos_u/README.md#export-ctx64-plain-kv-cache"
license: "BSD-3-Clause"
mode: "V"
---

```bash
bash examples/arm/tinystories42m_example_ethos_u/export_tinystories42m_ethosu.sh
```

The default export uses:

```text
model.use_kv_cache=True
model.quantize_kv_cache=False
model.enable_dynamic_shape=False
export.max_seq_length=64
export.max_context_length=64
quantization.pt2e_quantize=ethosu_16a8w
quantization.quantize_scope=linear
quantization.calibration_tasks=[wikitext]
quantization.calibration_limit=1
quantization.calibration_seq_length=64
debug.generate_full_logits=False
```

Although the KV model consumes one token per invocation, `max_seq_length=64`
describes the exported sequence capacity. PT2E uses one 64-token Wikitext
sample for the quick validation calibration.
