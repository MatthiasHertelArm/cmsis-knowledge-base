---
id: "cc-i-o-retarget-example-project-execute-project-2"
type: "concept"
domain: "core"
title: "I/O Retarget example project: Execute Project"
summary: "The project is configured for execution on Arm Virtual Hardware which removes the requirement for a physical hardware board."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:example/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/example/README.md#execute-project"
license: "Apache-2.0"
mode: "V"
---

The project is configured for execution on Arm Virtual Hardware which removes the requirement for a physical hardware board.

To execute application image on Arm Virtual Hardware use below command:

```bash
FVP_MPS2_Cortex-M3 -f fvp-config.txt out/retarget/FVP_MPS2_CM3/Debug/retarget.axf
```

> **Note**
>
> - For GCC and CLANG, the application image file has extension `.elf` and extension `.out` for IAR.

This command will execute the simulation model and in the default terminal window you should see the following output:

```txt
Starting ...
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

Finished
```

The simulation model will automatically terminate after the above output.
