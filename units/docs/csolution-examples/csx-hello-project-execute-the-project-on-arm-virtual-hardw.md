---
id: "csx-hello-project-execute-the-project-on-arm-virtual-hardw"
type: "concept"
domain: "project"
title: "Hello project: Execute the project on Arm Virtual Hardware"
summary: "The project is configured for execution on Arm Virtual Hardware which removes the requirement for a physical hardware board."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:Hello/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/Hello/README.md#execute-the-project-on-arm-virtual-hardware"
license: "Apache-2.0"
mode: "V"
---

The project is configured for execution on [**Arm Virtual Hardware**](https://developer.arm.com/Tools%20and%20Software/Arm%20Virtual%20Hardware) which removes the requirement for a physical hardware board.  

### Execute this project via command line

#### For debug type

```bash
> FVP_Corstone_SSE-300 -f ../FVP/FVP_Corstone_SSE-300/fvp_config.txt -a ./out/Hello/CS300/Debug/Hello.axf --simlimit 10
```

#### For release type

```bash
> FVP_Corstone_SSE-300 -f ../FVP/FVP_Corstone_SSE-300/fvp_config.txt -a ./out/Hello/CS300/Release/Hello.axf --simlimit 10
```

### Use this project with Keil Studio

Install [Keil Studio](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) from the Visual Studio Marketplace, clone this repository, and open `Hello.csolution.yml` in VS Code. Keil Studio provides the CMSIS solution, build, and debug tooling required to work with the project.
