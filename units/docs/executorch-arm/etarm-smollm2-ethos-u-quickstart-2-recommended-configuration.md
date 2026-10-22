---
id: "etarm-smollm2-ethos-u-quickstart-2-recommended-configuration"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 2. Recommended configuration"
summary: "These are the settings used by the main flow in this README:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/smollm2_example_ethos_u/README.md#2-recommended-configuration"
license: "BSD-3-Clause"
mode: "V"
---

These are the settings used by the main flow in this README:

- `quantization.pt2e_quantize=ethosu_16a8w`
- `quantization.quantize_scope=linear`
- `model.use_kv_cache=True`
- `export.max_seq_length=64`
- `export.max_context_length=64`
- `quantization.calibration_seq_length=64`
- `quantization.calibration_limit=1`
- `backend.ethosu.target=ethos-u85-256`
- `backend.ethosu.system_config=Ethos_U85_SYS_DRAM_High`
- `backend.ethosu.memory_mode=Dedicated_Sram_512KB`

Why these settings matter:

- `linear` scope means only the linear layers are quantized onto Ethos-U. This
  is the current validated path for meaningful output in this example.
- `model.use_kv_cache=True` exports the token and `input_pos` inputs used for
  step-wise decoding.
- `max_seq_length=64` and `max_context_length=64` set the documented 64-token
  generation context. In KV-cache mode, `generate_sampled.py` can derive the
  context length from `--window 64`; pass `--max-context-length 64` explicitly
  when you want the command line to make that relationship obvious.
- `calibration_limit=1` keeps this experimental KV-cache flow practical for
  local iteration. Increase it when you want more calibration coverage.
