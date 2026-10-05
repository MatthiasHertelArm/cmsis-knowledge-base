---
id: "alp-deploy-mobilesam-on-ethos-u-validate-the-results-inspect-the-visual-result"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Validate the MobileSAM segmentation result: Inspect the visual result"
summary: "Open fvp_comparison.png under arm_test/mobilesam/result/ in an image viewer. The image contains three panels:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results/#inspect-the-visual-result"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open `fvp_comparison.png` under `arm_test/mobilesam/result/` in an image viewer. The image contains three panels:

- The resized input image with the positive point prompt
- The host quantized segmentation overlay
- The FVP segmentation overlay

Compare the object boundaries in the two mask overlays. The FVP mask should select the dog at the positive point prompt and closely match the host quantized result.
