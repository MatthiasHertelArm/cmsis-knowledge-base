---
id: "nn-cmsis-nn-building-cmsis-nn-as-a-library"
type: "concept"
domain: "optimization"
title: "CMSIS NN: Building CMSIS-NN as a library"
summary: "It is recommended to use toolchain files from Arm Ethos-U Core Platform project. These are supporting TARGET_CPU, which is a required argument. Note that if not specifying TARGET_CPU, these toolchains will set some default."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@71cbe3d:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/71cbe3d/README.md#building-cmsis-nn-as-a-library"
license: "Apache-2.0"
mode: "V"
---

It is recommended to use toolchain files from [Arm Ethos-U Core Platform](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform) project. These are supporting TARGET_CPU, which is a required argument. Note that if not specifying TARGET_CPU, these toolchains will set some default. The format must be TARGET_CPU=cortex-mXX, see examples below.

Here is an example:

```
cd </path/to/CMSIS_NN>
mkdir build
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=</path/to/ethos-u-core-platform>/cmake/toolchain/arm-none-eabi-gcc.cmake -DTARGET_CPU=cortex-m55
make
```

Some more examples:

```
cmake .. -DCMAKE_TOOLCHAIN_FILE=</path/to/ethos-u-core-platform>/cmake/toolchain/armclang.cmake -DTARGET_CPU=cortex-m55
cmake .. -DCMAKE_TOOLCHAIN_FILE=</path/to/ethos-u-core-platform>/cmake/toolchain/arm-none-eabi-gcc.cmake -DTARGET_CPU=cortex-m7
cmake .. -DCMAKE_TOOLCHAIN_FILE=</path/to/ethos-u-core-platform>/cmake/toolchain/armclang.cmake -DTARGET_CPU=cortex-m3
```
