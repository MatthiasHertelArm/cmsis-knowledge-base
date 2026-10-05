---
id: "alp-alif-dual-npu-vision-validate-inference-check-the-live-camera-ui"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Validate live parallel inference: Check the live camera UI"
summary: "After 5 seconds, the application clears the test image and starts the MT9M114 stream. Confirm the following results:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/validate-inference/#check-the-live-camera-ui"
license: "CC-BY-SA-4.0"
mode: "V"
---

After 5 seconds, the application clears the test image and starts the MT9M114 stream. Confirm the following results:

- The MW405 display shows a 480 x 352 live preview.
- The preview is in color and updates when you move the camera.
- Green boxes track faces in the live frame.
- The classification label and confidence change with the scene.
- Face boxes appear when SSD-Slim detects a face.
- The lower status area shows rolling U55, U85, span, and overlap values.

The log confirms the transition:

```output
dual-et: live dual-NPU pipeline started
```

**Note:**
If the preview is grainy or monochrome, the application is displaying packed sensor data as RGB565. Confirm that the build includes both ISP overlays and that the selected video endpoint is `isp@49046000`. The native pipeline requests planar RGB888 output from the ISP before it creates the display preview and model inputs.
