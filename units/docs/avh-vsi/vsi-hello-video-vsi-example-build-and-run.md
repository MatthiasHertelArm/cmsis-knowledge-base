---
id: "vsi-hello-video-vsi-example-build-and-run"
type: "concept"
domain: "debug"
title: "Hello Video VSI Example: Build and run"
summary: "The example is provided in csolution format and can be build in an IDE, or in command line interface using cbuild utility from CMSIS-Toolbox."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_video_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_video_vsi/README.md#build-and-run"
license: "Apache-2.0"
mode: "V"
---

The example is provided in [csolution format](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) and can be build in an IDE, or in command line interface using *cbuild* utility from [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/build-operation.md).

The example supports Corstone-310 and Corstone-300 targets and can be compiled with Arm Compiler 6 (AC6) or GCC.

The path to the input image/video file is specified in the `app.c` file as `INPUT_IMAGE` and by default is `./samples/typing.mp4`. The path is relative to the current location and assumes the execution from the `./hello_video_vsi/` folder.

Project build type `.lcd_out` uses model's lcd to display the file content. For example, to build and run the example on Corstone-310 FVP with GCC toolchaing use:

Compile:

```bash
cbuild hello_video_vsi.csolution.yml --packs --rebuild --toolchain GCC --context .lcd_out+Corstone_310
```

Run the program in .elf format when compiled in GCC:

```bash
FVP_Corstone_SSE-310 -a ./out/hello_video_vsi/Corstone_310/lcd_out/GCC/hello_video_vsi.elf -C mps3_board.v_path=./source/vsi/video_vsi_py/
```

To compile with Arm Compiler use `--toolchain AC6` option.  With Arm Compiler an .axf file is generated and should be loaded in the same way as shown above.
