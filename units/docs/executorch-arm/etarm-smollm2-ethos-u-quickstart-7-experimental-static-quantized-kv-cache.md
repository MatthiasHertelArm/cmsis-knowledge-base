---
id: "etarm-smollm2-ethos-u-quickstart-7-experimental-static-quantized-kv-cache"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 7. Experimental static quantized KV cache"
summary: "Ethos-U does not support the dynamic per-token quantization used by model.quantize_kv_cache=True. The static path instead calibrates fixed per-channel K/V scales from Wikitext before export, stores the cache as int8, and uses standard tensor cache updates."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/smollm2_example_ethos_u/README.md#7-experimental-static-quantized-kv-cache"
license: "BSD-3-Clause"
mode: "V"
---

Ethos-U does not support the dynamic per-token quantization used by
`model.quantize_kv_cache=True`. The static path instead calibrates fixed
per-channel K/V scales from Wikitext before export, stores the cache as int8,
and uses standard tensor cache updates. It does not link the Llama custom cache
operator, and runner inputs remain int32.

Export the seq64 `w8a16` static-KVQ artifact with one Wikitext calibration
sample:

```bash
bash examples/arm/smollm2_example_ethos_u/export_smollm2_ethosu.sh \
  --mode=w8a16 \
  --use-kv-cache \
  --static-quantize-kv-cache \
  --so_library=/path/to/cmake-out/kernels/quantized/libquantized_ops_aot_lib.so \
  --max_seq_length=64 \
  --max_context_length=64 \
  --calibration_limit=1 \
  --calibration_seq_length=64 \
  --quantize_scope=linear
```

`--so_library` is needed only during export to register portable QDQ out
variants. Build it with `EXECUTORCH_BUILD_KERNELS_QUANTIZED_AOT=ON` if your
ExecuTorch installation does not already provide it. The embedded runner uses
the standard `quantized_ops_lib`; it does not link Llama custom cache operators.

This produces:

```text
smollm2_ethosu_static_kvq_seq64_w8a16_wikitext.pte
```

Build it with the standard semihosting runner; no custom cache-op source or
linkage is required:

```bash
bash examples/arm/smollm2_example_ethos_u/build_executor_runner_semihosting.sh \
  --pte=smollm2_ethosu_static_kvq_seq64_w8a16_wikitext.pte \
  --output=smollm2_ethosu_static_kvq_seq64_w8a16_wikitext/cmake-out \
  --method_pool_size=0x01000000 \
  --scratch_pool_size=0x00800000 \
  --input_file_pool_size=0x00100000
```

Run the ten-token greedy smoke test:

```bash
python examples/arm/smollm2_example_ethos_u/generate_sampled.py \
  --fvp examples/arm/arm-scratch/FVP-corstone320/models/Linux64_GCC-9.3/FVP_Corstone_SSE-320 \
  --runner smollm2_ethosu_static_kvq_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --embedded-pte \
  --tokenizer data/tokenizers/smollm2/tokenizer.json \
  --prompt "Once upon a time in a small village," \
  --window 64 \
  --max-context-length 64 \
  --use-kv-cache \
  --max-new-tokens 10 \
  --temperature 0 \
  --top-p 0.9 \
  --repetition-penalty 1.1
```

Run all nine default prompts greedily and save the generated text:

```bash
python examples/arm/smollm2_example_ethos_u/generate_sampled.py \
  --fvp examples/arm/arm-scratch/FVP-corstone320/models/Linux64_GCC-9.3/FVP_Corstone_SSE-320 \
  --runner smollm2_ethosu_static_kvq_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --embedded-pte \
  --tokenizer data/tokenizers/smollm2/tokenizer.json \
  --prompt-file examples/arm/smollm2_example_ethos_u/default_prompts.txt \
  --prompt-all \
  --save-generations outputs/$(date +%F)/ethosu_static_kvq_seq64_generations.txt \
  --window 64 \
  --max-context-length 64 \
  --use-kv-cache \
  --max-new-tokens 64 \
  --temperature 0 \
  --top-p 0.9 \
  --repetition-penalty 1.1 \
  --timeout 2400
```

For a 50-prompt comparison, pass the plain-KV runner as `w8a8` and the
static-KVQ runner as `w8a16`; those labels are only result keys in this helper:

```bash
python examples/arm/smollm2_example_ethos_u/eval_wikitext_perplexity.py \
  --runner-w8a8 smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --runner-w8a16 smollm2_ethosu_static_kvq_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --prompts-file outputs/$(date +%F)/wikitext_prompts_kv_seq64.txt \
  --num-prompts 100 \
  --ppl-prompts 50 \
  --min-prompt-tokens 64 \
  --max-prompt-tokens 64 \
  --max-tokens-per-prompt 64 \
  --window 64 \
  --max-context-length 64 \
  --use-kv-cache \
  --timeout 24000
```
