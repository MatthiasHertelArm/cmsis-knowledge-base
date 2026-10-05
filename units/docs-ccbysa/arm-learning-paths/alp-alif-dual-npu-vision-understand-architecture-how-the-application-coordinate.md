---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-coordinate"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application coordinates the workers"
summary: "The coordinator uses three synchronization stages:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-coordinates-the-workers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The coordinator uses three synchronization stages:

1. Each worker signals that its `Program` and `Method` are prepared.
2. The coordinator gives both execute semaphores for the current frame.
3. Each worker signals after it has copied the input and again after inference completes.

The early input-copy signal lets the coordinator return the camera buffer to the ISP queue without waiting for both NPUs. The later completion signal protects result processing and timing calculations.

The application records execution start and end cycles inside each worker, close to `Method::execute()`. It derives four live metrics:

| Metric | Calculation |
| --- | --- |
| U55 | U55 end minus U55 start |
| U85 | U85 end minus U85 start |
| Span | Latest end minus earliest start |
| Overlap | Earlier end minus later start, or zero when executions don't overlap |

These measurements isolate delegated execution from camera capture and UART output. They don't represent complete camera-to-display latency.
