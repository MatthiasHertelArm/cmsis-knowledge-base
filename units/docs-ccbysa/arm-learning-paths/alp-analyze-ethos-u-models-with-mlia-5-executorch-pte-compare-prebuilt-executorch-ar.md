---
id: "alp-analyze-ethos-u-models-with-mlia-5-executorch-pte-compare-prebuilt-executorch-ar"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze ExecuTorch artifacts with MLIA and Corstone: Compare prebuilt ExecuTorch "
summary: "The model artifacts repository includes prebuilt Ethos-U .pte files:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/5-executorch-pte.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/5-executorch-pte/#compare-prebuilt-executorch-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

The model artifacts repository includes prebuilt Ethos-U `.pte` files:

```output
pte/toy_conditional_select_int8_ethos_u55_256.pte
pte/toy_conditional_select_int8_ethos_u85_256.pte
```

These are synthetic learning artifacts rather than benchmark models. The artifacts use a small convolution plus a conditional selection pattern to make target-dependent delegation easier to see. A model can be packaged for different Ethos-U targets and show different delegation and runtime-counter behavior.

For supported `.pte` workloads, MLIA performance analysis uses a Corstone backend. In this context, Corstone refers to an Arm reference subsystem platform. The backend uses a Fixed Virtual Platform (FVP).

An FVP is a software model of a hardware platform. You can use an FVP to run a packaged artifact in a target-like environment and collect performance counters without needing a physical board on your desk.

For `.pte` artifacts, MLIA currently supports only performance analysis. The artifact has already been packaged for an ExecuTorch deployment path. Corstone is used to run the packaged program on an FVP and collect NPU performance counters for the whole model run.

Corstone doesn't provide per-layer estimates or operator breakdowns. Perform a Vela-backed analysis similar to earlier when you need layer-level performance estimates or compatibility checks.

Run the Ethos-U55 artifact with the Corstone-300 backend:

```bash
mlia check pte/toy_conditional_select_int8_ethos_u55_256.pte \
  --target-profile ethos-u55-256 \
  --performance \
  --backend corstone-300
```

Running the check installs any required Corstone backends that weren't previously installed.

**Note:**
Corstone backend installation requires accepting a license. You'll be prompted in the terminal to agree.


Run the Ethos-U85 artifact with the Corstone-320 backend:

```bash
mlia check pte/toy_conditional_select_int8_ethos_u85_256.pte \
  --target-profile ethos-u85-256 \
  --performance \
  --backend corstone-320
```

The reports show Corstone running each `.pte` artifact and collecting NPU performance counters for the whole model run. Read the Corstone report as runtime counter evidence:

| Field | What it tells you |
| --- | --- |
| `NPU active cycles` | Cycles where the NPU was doing work. |
| `NPU idle cycles` | Cycles where the NPU was present but not active. A very small value means this run kept the NPU busy after work was issued. |
| `NPU total cycles` | Active plus idle cycles for the NPU portion of the run. |
| `NPU AXI0 RD/WR data beat` | Memory traffic on the AXI0 port, configured as SRAM for this target profile. |
| `NPU AXI1 RD/WR data beat` | Memory traffic on the AXI1 port, configured as DRAM for this target profile. |

Use the reports to compare the NPU counters for each packaged artifact:

| Artifact | Target profile | Backend | NPU total cycles |
| --- | --- | --- | --- |
| `toy_conditional_select_int8_ethos_u55_256.pte` | `ethos-u55-256` | `corstone-300` | `273,088` |
| `toy_conditional_select_int8_ethos_u85_256.pte` | `ethos-u85-256` | `corstone-320` | `19,056` |

The comparison uses `ethos-u55-256` and `ethos-u85-256`, so both target profiles use 256 MACs per cycle. However, Ethos-U85 is a newer and higher performance NPU than Ethos-U55. The target information in the reports also shows other platform differences, such as accelerator clock and memory configuration.

The Ethos-U55 report shows `271,725` NPU active cycles and `1,363` NPU idle cycles. The Ethos-U85 report shows `18,183` NPU active cycles and `873` NPU idle cycles, for `19,056` total NPU cycles. This difference reflects the combined effect of improvements in Ethos-U85 over Ethos-U55.

Use the Corstone counters to compare packaged artifacts under the same target profile and backend. If part of the graph runs outside the NPU delegate, the CPU-side cost isn't fully represented by the NPU cycle table.
