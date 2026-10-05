---
id: "alp-deploy-mobilesam-on-ethos-u-validate-the-results-confirm-ethos-u-delegation"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Validate the MobileSAM segmentation result: Confirm Ethos-U delegation"
summary: "Display the delegation report written during export:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/validate-the-results/#confirm-ethos-u-delegation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Display the delegation report written during export:

```bash
sed -n '1,120p' arm_test/mobilesam/export/delegation.txt
```

Confirm that `Total delegated subgraphs` is `1`. The exporter checks this before writing the `.pte`. The reference run above produced:

```output
Total delegated subgraphs: 1
Number of delegated nodes: 5076
Number of non-delegated nodes: 3
```

Node counts can vary with dependency versions. Use the values from your export when reporting delegation.
