---
id: "ethu-integration-step-1-characterize-the-target-hardware"
type: "concept"
domain: "edge-ai"
title: "Integration: Tutorial: Create an Ethos-U application / Step 1: Characterize the target hardware and create the project"
summary: "Part of: Tutorial: Create an Ethos-U application"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/main.md#step-1-characterize-the-target-hardware-and-create-the-project"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tutorial: Create an Ethos-U application_

For our application, we selected the Alif Semiconductor
[Ensemble E7 (`AE722F80F55D5LS`)](https://www.keil.arm.com/devices/alif-semiconductor-ae722f80f55d5ls/)
device and the related
[AppKit-E7-AIML](https://www.keil.arm.com/boards/alif-semiconductor-appkit-e7-aiml-d1-34b5d51/)
board. We target the Ethos-U55 NPU on this device and therefore start with
`Test-Ethos-U55.csolution.yml`.

#### Add a new target to the solution

Open `Test-Ethos-U55.csolution.yml` and add the DFP and BSP packs required by
the selected device and board. Use the information in the
[CMSIS-Pack catalog](https://www.keil.arm.com/packs/) to identify these packs.
Then add a hardware target to the `target-types:` node before the existing FVP
target. For the E7 device and AppKit, the relevant parts of the solution are:

```yaml
  packs:
    - pack: AlifSemiconductor::Ensemble
    # Keep the existing packs
    - pack: ARM::V2M_MPS3_SSE_300_BSP@1.5.0

  target-types:
    - type: AppKit-E7
      board: Alif Semiconductor::AppKit-E7-AIML
      device: Alif Semiconductor::AE722F80F55D5LS

    # Keep the existing target for validating with FVP simulation model.
    - type: SSE-300-U55
      board: ARM::V2M-MPS3-SSE-300-FVP
      device: ARM::SSE-300-MPS3

```

Save the solution. Keil Studio discovers compatible board layers in the
installed packs and prompts you to select one. The Alif E7 pack provides two
layers for the AppKit-E7-AIML board:

- `Board/AppKit-E7_M55_HE` configures the `M55_HE` processor.
- `Board/AppKit-E7_M55_HP` configures the `M55_HP` processor.

This example uses the `Board/AppKit-E7_M55_HP` layer.

> [!TIP]
> When no compatible board layer exists, create one based on the supplied FVP
> board layer. This example requires standard output and the Ethos-U driver. See
> [Board Layers](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#board-layer)
> in the CMSIS-Toolbox documentation.
