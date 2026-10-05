---
id: "alp-deploy-mobilesam-on-ethos-u-validate-the-results-reconstruct-the-target-mask"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Validate the MobileSAM segmentation result: Reconstruct the target mask"
summary: "Run the visualization tool from the ExecuTorch repository root without arguments. It reads the Fixed Virtual Platform (FVP) output tensor from output-0.bin under arm_test/mobilesam/io/ and thresholds its mask logits at zero. It compares the mask with quantized_mask.png under arm_test/mobilesam/export/:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results/#reconstruct-the-target-mask"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the visualization tool from the ExecuTorch repository root without arguments. It reads the Fixed Virtual Platform (FVP) output tensor from `output-0.bin` under `arm_test/mobilesam/io/` and thresholds its mask logits at zero. It compares the mask with `quantized_mask.png` under `arm_test/mobilesam/export/`:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime/visualize_fvp_output.py
```

The tool requires `112 × 112` float32 logits and exits with an error if the FVP and host masks have an intersection over union (IoU) below `0.9`. The threshold is fixed in the script.

On success, it prints `FVP/reference mask IoU:` with the measured score and a `Saved` line with the comparison image path. It writes `fvp_mask.png`, `fvp_comparison.png`, and `metrics.json` under `arm_test/mobilesam/result/`.
