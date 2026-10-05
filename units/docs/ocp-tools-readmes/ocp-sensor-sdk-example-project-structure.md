---
id: "ocp-sensor-sdk-example-project-structure"
type: "concept"
domain: "project"
title: "Sensor-SDK-Example: Project Structure"
summary: "This AWS MQTT Mutual Authentication example uses the CMSIS-Toolbox csolution project format with CMSIS software packs and software layers. The default configuration uses a AVH-FVP simulation model. No physical hardware is required to explore this example."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Sensor-SDK-Example@3cee161:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

This AWS MQTT Mutual Authentication example uses the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/)
*csolution project format* with CMSIS software packs and software layers. The default configuration uses a AVH-FVP simulation model.
No physical hardware is required to explore this example. By using different layers it can run on physical evaluation boards,
use different communication stacks, or WiFi modules.

Project File                                        | Description
:---------------------------------------------------|:------------------------------------------------
`*.csolution.yml`                                   | Specifies the target hardware, build types, and defines the actual software layers used.
`*.cproject.yml`                                    | Contains the source files and components that belong to one example. Note that the solution may contain multiple similar examples.
`Board/.../Board.clayer.yml`                        | Contains the hardware interfaces to the device and board peripherals.
`Shield/.../Shield.clayer.yml`                      | Contains the pin mapping to the Arduino Shield.
