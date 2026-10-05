---
id: "helium-helium-optimization-topics-1-the-b-using-optimized-software-libraries"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #1 - the basics: Using optimized software libraries"
summary: "Arm provides CMSIS-DSP, CMSIS-NN and Arm-2D libraries that are already optimized for Helium instructions. Recent releases of CMSIS-DSP libraries are delivered as source code. For best performance with Arm toolchains (e.g."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/basic_optimization_topics.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/basic_optimization_topics.md#using-optimized-software-libraries"
license: "Apache-2.0"
mode: "V"
---

Arm provides [CMSIS-DSP](https://github.com/ARM-software/CMSIS-DSP), [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN) and [Arm-2D](https://github.com/ARM-software/Arm-2D)  libraries that are already optimized for Helium instructions. Recent releases of CMSIS-DSP libraries are delivered as source code. For best performance with Arm toolchains (e.g. Keil Studio, Keil MDK, Arm DS) please compile the CMSIS-DSP with -Ofast optimization level.
In addition, when porting applications from previous Cortex-M projects, please visit [CMSIS-DSP library documentation](https://arm-software.github.io/CMSIS-DSP/latest/index.html) to check:

1) if the DSP functions you are using have Helium specific variant. For example, the biquad initialization function “arm_biquad_cascade_df1_init_f32” has a Helium variant “arm_biquad_cascade_df1_mve_init_f32”
2) if the DSP functions you are using have specific recommendations for data alignment.

CMSIS-DSP is optimized to work on block of data. Those blocks must be big enough so that most of the cycles are spent in the main body of the function. If you work with too small blocks, there won't be any acceleration. In that case, it is probably better to manually write a dedicated function.

If you can't find the needed feature in the existing libraries, you'll need to vectorize the code yourself.
The source codes in the CMSIS-DSP libraries are written with intrinisic functions. In some cases, additional performance gain is possible using inline assembly. Arm provides a selection of optimized DSP functions in the following location: https://github.com/ARM-software/EndpointAI/tree/master/Kernels/ARM-Optimized/DSP/Source

The CMSIS-NN libraries are used by ML software runtime such as TensorFlow Lite for Microcontroller. It is very unlikely that the CMSIS-NN library functions are being called in application code directly. To use CMSIS-NN, you need to ensure that the ML runtime libraries are compiled with CMSIS-NN option enabled. For example, [this page](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/cortex_m_corstone_300) contains information about compiling TensorFlow Lite Micro with CMSIS-NN enabled (Note the " OPTIMIZED_KERNEL_DIR=cmsis_nn " option).
