---
id: "etarm-introduction"
type: "concept"
domain: "edge-ai"
title: "Introduction"
summary: "As you have seen in the Arm® Ethos™-U NPU backend tutorial, ExecuTorch has two distinct parts: - Ahead-of-time(AoT) compile flow - Ethos-U on-device runtime"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/ethos-u-porting-guide.md"
license: "BSD-3-Clause"
mode: "V"
---

As you have seen in the [Arm® Ethos™-U NPU backend tutorial](https://github.com/pytorch/executorch/blob/658390c/examples/arm/../../docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md), ExecuTorch has two distinct parts:
- Ahead-of-time(AoT) compile flow
- Ethos-U on-device runtime

In the porting guide, we guide you through the main steps to port your SoC with an Ethos-U to the ExecuTorch Ethos-U backend in order to leverage the ExecuTorch Ethos-U enablement. We assume
you are familiar with the concepts introduced in `backends-arm-ethos-u-overview.md`, you have already generated a pte in the AoT flow and want to deploy the ML model on device.
Fundamentally, there are two big approaches you can take in porting a SoC with an Ethos-U NPU towards the ExecuTorch runtime.
- You can use the enablement we have done in ExecuTorch for the Arm® Corstone™-300(Arm® Cortex®-M55 and Arm® Ethos™-U55 reference design) and
Arm® Corstone™-320(Arm® Cortex®-M85 and Arm® Ethos™-U85 reference design) and migrate from the Corstone platform towards a new platform.
- If the SoC comes with an SDK that is not based on ExecuTorch, you can replace the runtime SDKs with the corresponding APIs from ExecuTorch runtime.

It is important to understand that irrespective of whether the SoC comes with or without SDK, there is
[a single Ethos-U driver](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver) that any SoC with Ethos-U relies on. For that reason, there will be
overlap between the two approaches when it comes to the enablement of the Ethos-U NPU.
