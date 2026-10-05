---
id: "alp-deploy-mobilesam-on-ethos-u-export-the-model-export-the-executorch-program"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Export MobileSAM for Ethos-U85: Export the ExecuTorch program"
summary: "Export the example image and positive point prompt for the ethos-u85-256 target:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model/#export-the-executorch-program"
license: "CC-BY-SA-4.0"
mode: "V"
---

Export the example image and positive point prompt for the `ethos-u85-256` target:

```bash
python3 examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py
```

The exporter loads the prepared checkpoint, calibrates post-training quantization with the example image, checks the quantized mask against the floating-point mask, and lowers the graph to Ethos-U85.

This script uses one fixed configuration: `examples/models/dinov2/dog.jpg`, positive point `(219, 193)`, input size `448`, target `ethos-u85-256`, and memory mode `Dedicated_Sram_384KB`. These values are set in the Python source rather than through command-line arguments.

Export requires a host mask intersection over union (IoU) of at least `0.9` and exactly one Ethos-U delegated subgraph. It writes `mobilesam.pte` to `arm_test/mobilesam/export/`.
