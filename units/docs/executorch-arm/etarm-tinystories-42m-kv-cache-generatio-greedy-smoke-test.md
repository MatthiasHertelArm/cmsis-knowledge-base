---
id: "etarm-tinystories-42m-kv-cache-generatio-greedy-smoke-test"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85: Greedy smoke test"
summary: "This smoke test validates export, runner integration, stateful token/position inputs, and decoding. Add prompt-set generation and perplexity only after this path produces a coherent continuation."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/tinystories42m_example_ethos_u/README.md#greedy-smoke-test"
license: "BSD-3-Clause"
mode: "V"
---

```bash
ARTIFACT_DIR="${TINYSTORIES42M_ARTIFACT_DIR:-data/tinystories42m}"

python examples/arm/smollm2_example_ethos_u/generate_sampled.py \
  --fvp=examples/arm/arm-scratch/FVP-corstone320/models/Linux64_GCC-9.3/FVP_Corstone_SSE-320 \
  --runner=tinystories42m_ethosu_ctx64/cmake-out/arm_executor_runner \
  --embedded-pte \
  --tokenizer="${ARTIFACT_DIR}/tokenizer.model" \
  --prompt="Once upon a time in a small village," \
  --window=64 \
  --max-context-length=64 \
  --use-kv-cache \
  --max-new-tokens=2 \
  --temperature=0 \
  --top-p=0.9 \
  --repetition-penalty=1.1 \
  --timeout=1200
```

This smoke test validates export, runner integration, stateful token/position
inputs, and decoding. Add prompt-set generation and perplexity only after this
path produces a coherent continuation.
