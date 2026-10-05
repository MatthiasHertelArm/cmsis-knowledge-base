---
id: "etarm-smollm2-ethos-u-quickstart-6-optional-evaluate-wikitext-perplexity"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 6. Optional: evaluate Wikitext perplexity"
summary: "The KV-cache generation artifact can also be used for step-wise perplexity scoring over the same 64-token context."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/README.md#6-optional-evaluate-wikitext-perplexity"
license: "BSD-3-Clause"
mode: "V"
---

The KV-cache generation artifact can also be used for step-wise perplexity scoring over the same 64-token context.

### 6.1 Build the matching runner

```bash
bash examples/arm/smollm2_example_ethos_u/build_executor_runner_semihosting.sh \
  --pte=smollm2_ethosu_kv_seq64_w8a16_wikitext.pte \
  --output=smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out \
  --method_pool_size=0x01000000 \
  --scratch_pool_size=0x00800000 \
  --input_file_pool_size=0x00100000
```

The KV-cache artifact uses `--method_pool_size=0x01000000` (`16 MiB`).

### 6.2 Run perplexity

```bash
python examples/arm/smollm2_example_ethos_u/eval_wikitext_perplexity.py \
  --fvp examples/arm/arm-scratch/FVP-corstone320/models/Linux64_GCC-9.3/FVP_Corstone_SSE-320 \
  --runner-w8a8 smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --runner-w8a16 smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --prompts-file outputs/$(date +%F)/wikitext_prompts_kv_seq64.txt \
  --num-prompts 100 \
  --ppl-prompts 50 \
  --min-prompt-tokens 64 \
  --max-prompt-tokens 64 \
  --max-tokens-per-prompt 64 \
  --window 64 \
  --max-context-length 64 \
  --use-kv-cache \
  --timeout 2400 \
  --refresh-prompts
```

Why the prompt settings are all 64 here:

- `--window 64` and `--max-context-length 64` match the exported KV-cache
  context.
- `--min-prompt-tokens 64` and `--max-prompt-tokens 64` force every prompt to
  fill one scoring context, which makes the comparison easier to reason about.
- `--max-tokens-per-prompt 64` keeps scoring aligned with that same context.
- `--num-prompts 100` builds a reusable prompt file with enough samples for a
  stable comparison.
- `--ppl-prompts 50` keeps the FVP check manageable. Raise it when you want a
  fuller but slower run.

The evaluator script compares two runners, which is why it asks for both
`--runner-w8a8` and `--runner-w8a16`. In this simplified `w8a16`-only flow, it
is acceptable to pass the same runner to both options when you only want one
number from the validated artifact. A 50-prompt seq64 KV-cache run in this
branch completed with perplexity around 45.
