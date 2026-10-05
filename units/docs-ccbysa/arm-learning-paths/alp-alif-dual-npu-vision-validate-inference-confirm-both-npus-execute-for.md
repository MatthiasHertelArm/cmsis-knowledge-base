---
id: "alp-alif-dual-npu-vision-validate-inference-confirm-both-npus-execute-for"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Validate live parallel inference: Confirm both NPUs execute for each frame"
summary: "The coordinator wakes both Zephyr worker threads before waiting for their completion. Every tenth frame, the application prints the current and average timing values:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference/#confirm-both-npus-execute-for-each-frame"
license: "CC-BY-SA-4.0"
mode: "V"
---

The coordinator wakes both Zephyr worker threads before waiting for their completion. Every tenth frame, the application prints the current and average timing values:

```output
dual-et: PAR class=... frame=10 sample=10 U55=... U85=... span=... overlap=... us avg U55/U85/span/overlap=.../.../.../... us
```

Use the fields as follows:

| Field | Meaning |
| --- | --- |
| `U55` | SSD-Slim `Method::execute()` wall time on Ethos-U55 |
| `U85` | MobileNetV2 `Method::execute()` wall time on Ethos-U85 |
| `span` | Time from the first worker starting to the last worker finishing |
| `overlap` | Time during which both model executions overlap |

These are Cortex-M cycle-counter wall-time measurements around delegated `Method::execute()` rather than NPU PMU active-cycle counts. Input preparation and result decoding are outside these intervals. The two NPU interrupt counters also increase during live operation:

```output
dual-et: live frame=30 IRQs=.../...
```

Changing the scene changes the preview, tensor checksums, and detection results. If the image and results remain fixed, the application is still using the startup test input instead of live frames.

**Note:**
If the startup test completes but the live result doesn't change, confirm that `dual-et: live dual-NPU pipeline started` appears and that the live-frame messages and NPU interrupt counters continue to increase.

If capture errors repeat, power-cycle the board, flash the package again, and recheck the camera connector and overlay order.
