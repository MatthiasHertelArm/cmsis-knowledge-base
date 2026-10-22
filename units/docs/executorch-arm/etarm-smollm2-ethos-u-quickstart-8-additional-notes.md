---
id: "etarm-smollm2-ethos-u-quickstart-8-additional-notes"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 8. Additional notes"
summary: "The full-logits export returns one logits row per position in the fixed window. Short prompts therefore need padding so the runtime still receives a tensor with exactly 32 token slots."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/smollm2_example_ethos_u/README.md#8-additional-notes"
license: "BSD-3-Clause"
mode: "V"
---

### Non-KV fallback: why padding is needed for full-logits evaluation

The full-logits export returns one logits row per position in the fixed window.
Short prompts therefore need padding so the runtime still receives a tensor with
exactly 32 token slots. For perplexity, the evaluator right-pads the prompt so
the real tokens stay at the front of the causal window and each target token is
scored against the matching row. This preserves the usual left-to-right causal
ordering even though the deployed runtime works with fixed-size inputs.

### What `full` quantization scope means

`quantization.quantize_scope=full` asks the export stack to quantize more than
just the linear layers. That path exists for experimentation, but it is not the
validated path in this README because the linear-only setup is the one that
currently produces the clearest end-to-end result on Ethos-U FVP.

### Non-KV fallback: can calibration be faster?

Yes. The quickest way to iterate is to lower `--calibration_limit`. The tradeoff
is that you are collecting activation statistics from fewer samples, which can
hurt perplexity and generation quality. Keep `--calibration_seq_length` aligned
with `--max_seq_length`; if they differ, the calibration run is no longer
measuring the same tensor shapes that the deployed model will execute. In the
older non-KV path, calibration was especially slow because it often replayed
many partial prefixes position by position. The newer full-logits path can
observe a whole 32-token window in one pass, so larger limits are now much more
practical.

In the saved seq32 runs in this branch, `--calibration_limit=62` is now
bearable as the fuller-calibration setting, while `--calibration_limit=2`
remains the fast validation option. On the 100-prompt perplexity check, `2`
scored best, but `62` was still competitive and is the more conservative
default when export turnaround is less important than fuller calibration.

### Clean-checkout checklist

If the example fails on a clean checkout, the most common missing pieces are:

- `huggingface_hub[cli]` for the `hf download` command.
- `datasets` for rebuilding Wikitext prompts in the perplexity script.
- `pytorch_tokenizers`, installed from `./extension/llm/tokenizers/`.
- `backends/arm/scripts/build_executorch.sh`, which populates the default
  `arm_test` build root used by the runner wrappers.
