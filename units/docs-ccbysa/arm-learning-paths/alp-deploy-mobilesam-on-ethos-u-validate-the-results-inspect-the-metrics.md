---
id: "alp-deploy-mobilesam-on-ethos-u-validate-the-results-inspect-the-metrics"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Validate the MobileSAM segmentation result: Inspect the metrics"
summary: "Confirm that fvp_reference_iou is at least 0.9."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results/#inspect-the-metrics"
license: "CC-BY-SA-4.0"
mode: "V"
---

Display the target comparison metrics:

```bash
python3 -m json.tool arm_test/mobilesam/result/metrics.json
```

Confirm that `fvp_reference_iou` is at least `0.9`.

The exporter already checked the floating-point and quantized host masks. Display that result if you want to inspect the earlier stage:

```bash
python3 -m json.tool arm_test/mobilesam/export/metrics.json
```

The `fp32_quantized_iou` value must also be at least `0.9`.

A reference run at the pinned commit produced these scores:

| Comparison | IoU |
| --- | --- |
| Floating-point and quantized host masks | 0.9550 |
| FVP and quantized host masks | 0.9809 |

This run used Python 3.12.13, PyTorch 2.14.0, Vela 5.1.0, and Corstone-320 FVP 11.31.28 on macOS 26.6.2 with Apple silicon. Treat these scores as examples; use the two `0.9` thresholds to check your own run.
