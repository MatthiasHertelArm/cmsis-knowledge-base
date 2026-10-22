---
id: "etarm-smollm2-ethos-u-quickstart-5-run-a-generation-smoke-test"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 5. Run a generation smoke test"
summary: "Use generate_sampled.py to tokenize the prompt on the host, write the input tensor file expected by the semihosting runner, launch FVP, read back the output logits, and decode the generated token IDs into text:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/smollm2_example_ethos_u/README.md#5-run-a-generation-smoke-test"
license: "BSD-3-Clause"
mode: "V"
---

Use `generate_sampled.py` to tokenize the prompt on the host, write the input
tensor file expected by the semihosting runner, launch FVP, read back the
output logits, and decode the generated token IDs into text:

```bash
python examples/arm/smollm2_example_ethos_u/generate_sampled.py \
  --fvp examples/arm/arm-scratch/FVP-corstone320/models/Linux64_GCC-9.3/FVP_Corstone_SSE-320 \
  --runner smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out/arm_executor_runner \
  --embedded-pte \
  --tokenizer data/tokenizers/smollm2/tokenizer.json \
  --prompt "Once upon a time in a small village," \
  --window 64 \
  --max-context-length 64 \
  --use-kv-cache \
  --max-new-tokens 2 \
  --temperature 0 \
  --top-p 0.9 \
  --repetition-penalty 1.1
```

How to interpret the main options:

- `--embedded-pte` tells the script not to copy a separate `program.pte`,
  because the runner already contains the model.
- `--window 64` provides the main context length used by the script.
- `--max-context-length 64` makes the KV-cache capacity explicit; omitting it
  would use `--window`.
- `--use-kv-cache` runs the two-input token/position path and keeps one FVP
  process alive in semihosting server mode for step-wise decoding.
- `--max-new-tokens 2` keeps the smoke test short. The goal here is to show the
  end-to-end path works, not to benchmark long decoding.
- `--temperature 0` switches to greedy decoding, which is the most stable way
  to compare short smoke runs.
- `--top-p 0.9` is kept for consistency with the broader sampling interface,
  but it does not affect greedy decoding when `--temperature 0`.
- `--repetition-penalty 1.1` still matters in greedy mode because it modifies
  the logits before `argmax`.

### 5.1 Profile prompt processing and decoding

The runner exposes Ethos-U85 PMU counters for every server-mode inference.
Capture those counters with FVP fast mode disabled:

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
  --max-new-tokens 2 \
  --temperature 0 \
  --no-topk-print \
  --profile-output outputs/ethosu_u85_profile.json \
  --timeout 24000
```

`--profile-output` accepts `.json` or `.csv` and automatically removes the
Ethos-U `--fast` FVP option. The report contains one NPU PMU sample per model
execution, split into `prefill` and `decode` phases. Passing
`--npu-frequency-mhz` also reports an estimated NPU-only token rate.

This KV-cache demo processes the prompt one token at a time; its prefill result
is therefore the aggregate and average of those token executions, not a
batched-prefill measurement. The final prompt execution supplies the logits for
the first generated token, so steady-state decode executions start with the
second generated token.

CS-320 provides useful Ethos-U85 NPU cycle and event estimates when its timing
adapters match the target configuration. Cortex-M85 CPU timing and simulator
wall time are not cycle accurate, so the report must not be interpreted as
end-to-end latency or measured device tokens/s. Use FPGA or hardware for those
measurements.
