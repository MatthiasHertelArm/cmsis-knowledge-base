---
id: "etarm-mobilesam-prompt-segmentation-on-e-what-it-does"
type: "concept"
domain: "edge-ai"
title: "MobileSAM Prompt Segmentation on Ethos-U: What It Does"
summary: "The Python installer uses this source checkout and installs the dependencies needed for ahead-of-time Ethos-U export. The Arm setup script installs the cross compiler and FVP. Do not install a separate PyPI executorch wheel for this source example."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md#what-it-does"
license: "BSD-3-Clause"
mode: "V"
---

1. Fetches the pinned official MobileSAM source and checkpoint outside the
   repository.
2. Runs `torch.export`, PT2E quantization, and `EthosUPartitioner` to create a
   `.pte` containing one Ethos-U delegate.
3. Builds the standard Arm ExecuTorch runner and runs one inference on FVP.
4. Compares the FVP mask with the host quantized mask and requires `0.9` IoU.

Successful completion creates:

- Program: `arm_test/mobilesam/export/mobilesam.pte`
- Host masks: `arm_test/mobilesam/export/fp32_mask.png` and
  `arm_test/mobilesam/export/quantized_mask.png`
- FVP log: `arm_test/mobilesam/fvp.log`
- Comparison: `arm_test/mobilesam/result/fvp_comparison.png`
- FVP validation: `arm_test/mobilesam/result/metrics.json`
- TOSA and Vela artifacts: `arm_test/mobilesam/export/artifacts`

The Python installer uses this source checkout and installs the dependencies
needed for ahead-of-time Ethos-U export. The Arm setup script installs the
cross compiler and FVP. Do not install a separate PyPI `executorch` wheel for
this source example.

On macOS, Docker must be running and the
[FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac) wrapper must be on
`PATH`.
