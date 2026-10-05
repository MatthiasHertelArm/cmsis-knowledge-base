---
id: "vsi-hello-vsi-example-run"
type: "concept"
domain: "debug"
title: "Hello VSI example: Run"
summary: "To run the application from command line, use corresponding AVH FVP and provide the path to the binary image as well as the VSI python scripts. Also see the main README for details."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/README.md#run"
license: "Apache-2.0"
mode: "V"
---

To run the application from command line, use corresponding AVH FVP and provide the path to the binary image as well as the VSI python scripts. Also see the main [README](https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/../README.md) for details.

For example:

To run on the Corstone-315 the event-based firmware built with GCC compiler, with exit after running 40 seconds (wall-time), use:

```bash
FVP_Corstone_SSE-315 -a ./out/hello_vsi/Corstone_315/event/GCC/hello_vsi.elf -C mps4_board.v_path=./source/vsi/data_sensor_py/ --timelimit 40
```

For a target Corstone-310 with gated fetch flow built with Arm Compiler 6 and exit after 60 seconds of execution:

```bash
FVP_Corstone_SSE-310 -a ./out/hello_vsi/Corstone_310/gated/AC6/hello_vsi.axf -C mps3_board.v_path=./source/vsi/data_sensor_py/ --timelimit 40
```
