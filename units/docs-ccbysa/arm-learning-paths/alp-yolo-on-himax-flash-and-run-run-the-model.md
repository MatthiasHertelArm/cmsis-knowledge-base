---
id: "alp-yolo-on-himax-flash-and-run-run-the-model"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Flash firmware onto the microcontroller: Run the model"
summary: "After the reset button is pressed, the board starts inference with the object detection automatically. Observe the output in the terminal to verify that the image is built correctly."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/flash-and-run/#run-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

After the reset button is pressed, the board starts inference with the object detection automatically. Observe the output in the terminal to verify that the image is built correctly. If a person is in front of the camera, you should see the `person_score` value exceed `100`.

```output
b'SENSORDPLIB_STATUS_XDMA_FRAME_READY 240'
b'write frame result 0, data size=15284,addr=0x340e04e0'
b'invoke pass'
b'person_score:113'
b'EVT event = 10'
b'SENSORDPLIB_STATUS_XDMA_FRAME_READY 241'
b'write frame result 0, data size=15296,addr=0x340e04e0'
b'invoke pass'
b'person_score:112'
b'EVT event = 10'
```

This means the image works correctly on the device, and the end-to-end flow is complete.
