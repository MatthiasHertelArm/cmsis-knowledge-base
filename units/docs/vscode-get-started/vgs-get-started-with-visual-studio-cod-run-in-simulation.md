---
id: "vgs-get-started-with-visual-studio-cod-run-in-simulation"
type: "concept"
domain: "project"
title: "Get started with Visual Studio Code: Run in simulation"
summary: "The project is configured for execution on the Corstone-300 Arm FVP running an Arm Cortex-M55 processor. This model is available free-of-charge and removes the requirement for a physical hardware board. It can be used with the MDK-Community edition."
status: "draft"
collection: "vscode-get-started"
source: "Open-CMSIS-Pack/vscode-get-started@675c86f:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/README.md#run-in-simulation"
license: "Apache-2.0"
mode: "V"
---

The project is configured for execution on the Corstone-300 Arm FVP running an Arm Cortex-M55 processor.
This model is available free-of-charge and removes the requirement for a physical hardware board. It can be used with
the [MDK-Community](https://keil.arm.com/mdk-community) edition.

In the **CMSIS** view, press the **Load & Run application** button (the play icon). In the background,
the following will be run:

```txt
 *  Executing task: FVP_Corstone_SSE-300 -f fvp-config.txt --simlimit 60 -a out/hello/Corstone-300-FVP/debug/hello.axf  

Info: FVP_MPS3_Corstone_SSE_300: telnetterminal0: Listening for serial connection on port 5000
Info: FVP_MPS3_Corstone_SSE_300: telnetterminal1: Listening for serial connection on port 5001
Info: FVP_MPS3_Corstone_SSE_300: telnetterminal2: Listening for serial connection on port 5002
Info: FVP_MPS3_Corstone_SSE_300: telnetterminal5: Listening for serial connection on port 5003

Hello World 0
Hello World 1
Hello World 2
Hello World 3
Hello World 4
Hello World 5
Hello World 6
Hello World 7
Hello World 8
Hello World 9
Hello World 10
Hello World 11
...

Info: Simulation is stopping. Reason: Simulated time has been exceeded.

Info: /OSCI/SystemC: Simulation stopped by user.
```
