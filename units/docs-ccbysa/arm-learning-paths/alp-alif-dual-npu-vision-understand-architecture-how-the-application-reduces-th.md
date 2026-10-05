---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-reduces-th"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application reduces the system power cost"
summary: "Power-constrained embedded products often need more than one machine learning workload, but adding another microcontroller unit (MCU) also adds its active and idle power. Adding another MCU can also add external memory, interprocessor communication, and board-level power domains."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-reduces-the-system-power-cost"
license: "CC-BY-SA-4.0"
mode: "V"
---

Power-constrained embedded products often need more than one machine learning
workload, but adding another microcontroller unit (MCU) also adds its active and idle power. Adding another MCU can
also add external memory, interprocessor communication, and board-level power
domains. The E8 avoids that duplication by letting one Cortex-M55 coordinate
both on-chip NPUs. Camera capture, preprocessing, result fusion, and the user
interface stay on one MCU, while each NPU runs the workload it handles best.

This arrangement doesn't make two active NPUs consume less instantaneous
power than one active NPU. It reduces system-level overhead compared with a
design that needs a separate MCU or application processor for each NPU. It can
also finish concurrent workloads sooner, allowing the system to return to an
idle or lower-power state earlier. Measure energy on the final hardware to
quantify the saving for a specific duty cycle.

The application uses the native Zephyr drivers in the Alif SDK `main` branch.
The MT9M114, image signal processor (ISP), and MW405 changes were merged through pull request 879. The
following diagram extends the original multi-NPU prototype with the live
camera, ISP, and display pipeline used by this demo.

(figure: System diagram showing the MT9M114 camera and ISP feeding parallel U55 and U85 ExecuTorch workers before results are composed on the MW405 display.#center)
