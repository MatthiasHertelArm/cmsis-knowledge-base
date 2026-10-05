---
id: "ethu-integration-step-5-validate-and-tune"
type: "concept"
domain: "edge-ai"
title: "Integration: Tutorial: Create an Ethos-U application / Step 5: Validate and tune"
summary: "Part of: Tutorial: Create an Ethos-U application"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/main.md#step-5-validate-and-tune"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tutorial: Create an Ethos-U application_

Verify correctness, memory use, and performance on the target hardware.

- Run representative inputs and compare every output with known-good reference
  data. Check that Vela placed the expected operators on the NPU.
- Inspect the linker map and exercise the maximum expected tensor-arena, stack,
  and heap usage. Confirm that no region overlaps or exceeds its allocation.
- Measure several inference iterations on hardware, including warm-up behavior,
  and use the driver PMU
  to investigate NPU activity and stalls.
- Repeat inference under the intended RTOS, cache, and power conditions. Verify
  that timeout and fault paths terminate cleanly and report useful diagnostics.

When tuning, change one parameter at a time, such as the Vela memory mode,
`arena_cache_size`, or optimization strategy, then recompile and repeat the
checks. Use Read the Vela reports
and Compare Ethos-U configurations
to record and compare the results.
