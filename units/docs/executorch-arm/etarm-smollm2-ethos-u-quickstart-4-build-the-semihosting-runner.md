---
id: "etarm-smollm2-ethos-u-quickstart-4-build-the-semihosting-runner"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 4. Build the semihosting runner"
summary: "Build one runner that embeds the generation artifact:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/README.md#4-build-the-semihosting-runner"
license: "BSD-3-Clause"
mode: "V"
---

Build one runner that embeds the generation artifact:

```bash
bash examples/arm/smollm2_example_ethos_u/build_executor_runner_semihosting.sh \
  --pte=smollm2_ethosu_kv_seq64_w8a16_wikitext.pte \
  --output=smollm2_ethosu_kv_seq64_w8a16_wikitext/cmake-out \
  --method_pool_size=0x01000000 \
  --scratch_pool_size=0x00800000 \
  --input_file_pool_size=0x00100000
```

What this command does:

- Builds a semihosting `arm_executor_runner` ELF so the host can pass
  preprocessed input tensors in and read output tensors back out easily on FVP.
  In this flow the PTE is embedded in that runner as a separate convenience.
- Uses the validated `Ethos_U85_SYS_DRAM_High` and `Dedicated_Sram_512KB`
  defaults from the build helper, so you do not need to pass them explicitly in
  the common case.
- Sets three allocator pool sizes that keep the embedded-PTE KV-cache runner
  inside a practical Corstone-320 DDR budget.

How to read the pool sizes:

- `method_pool_size` stores long-lived runtime objects such as the loaded
  method and model state.
- `scratch_pool_size` is temporary workspace used during execution.
- `input_file_pool_size` is the buffer used to load semihosted input files such
  as `i0.bin`.

These values are not universal tuning rules. They are simply the validated pool
sizes for this example's seq64 KV-cache embedded-PTE runner. Start with them
unless you are actively changing the export shape or runtime integration.
