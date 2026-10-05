---
id: "etarm-smollm2-ethos-u-quickstart-3-export-the-generation-artifact"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 3. Export the generation artifact"
summary: "This command produces the KV-cache PTE used for the generation smoke test and optional perplexity evaluation."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/README.md#3-export-the-generation-artifact"
license: "BSD-3-Clause"
mode: "V"
---

This command produces the KV-cache PTE used for the generation smoke test and optional perplexity evaluation.

```bash
bash examples/arm/smollm2_example_ethos_u/export_smollm2_ethosu.sh \
  --mode=w8a16 \
  --use-kv-cache \
  --max_seq_length=64 \
  --max_context_length=64 \
  --calibration_limit=1 \
  --calibration_seq_length=64 \
  --quantize_scope=linear
```

What this command does:

- `--mode=w8a16` selects the 16-bit activation, 8-bit weight Ethos-U quantizer.
- By default the helper writes the exported `.pte` into the repository root, so
  the runner build commands below can reference the artifact by filename.
- `--use-kv-cache` exports token and `input_pos` inputs and disables full-logits
  output naming.
- `--max_seq_length=64` and `--max_context_length=64` set the documented
  64-token KV-cache context.
- `--calibration_limit=1` is the quick validation setting used for this
  experimental KV-cache path.
- `--calibration_seq_length=64` calibrates with the same context length used at
  runtime.
- `--quantize_scope=linear` keeps the validated hybrid setup where linear layers
  run on Ethos-U and the rest of the graph remains FP32.

The output artifact is named:

```text
smollm2_ethosu_kv_seq64_w8a16_wikitext.pte
```
