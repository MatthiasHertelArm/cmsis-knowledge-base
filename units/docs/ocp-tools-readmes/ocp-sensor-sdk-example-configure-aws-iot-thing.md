---
id: "ocp-sensor-sdk-example-configure-aws-iot-thing"
type: "concept"
domain: "project"
title: "Sensor-SDK-Example: Configure AWS IoT Thing"
summary: "Use Build solution to translate the application."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Sensor-SDK-Example@3cee161:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/README.md#configure-aws-iot-thing"
license: "Apache-2.0"
mode: "V"
---

Use **Build solution** to translate the application.

### Manual Configuration

Refer to [CMSIS-Toolbox - Reference Applications - Usage](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications#usage) for use command line tools to obtain above information.  However you may also use the CMSIS-Toolbox command `csolution list layers` to obtain information about the layers that are available in the installed packs. These layers may be copied to your project directory and defined as shown above.

```bash
csolution list layers
.../Sensor-SDK-Example/shields/a8974/Shield.clayer.yml (layer type: Shield)
.../Sensor-SDK-Example/shields/agm01/Shield.clayer.yml (layer type: Shield)
.../Sensor-SDK-Example/shields/agmp03/Shield.clayer.yml (layer type: Shield)
.../Sensor-SDK-Example/shields/p3115/Shield.clayer.yml (layer type: Shield)
.../Arm/Packs/Keil/STM32F469I-DISCO_BSP/1.0.0/Layers/Default/Board.clayer.yml (layer type: Board)
```

Use **cbuild** to translate the application.

```bash
cbuild xxx.csolution.yml --context .Debug+MyBoard --packs
```
