---
id: "helium-helium-optimization-topics-1-the-b-using-the-right-command-line-options-in"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #1 - the basics: Using the right command line options in compilation toolchain"
summary: "Because Helium and Floating-point unit (FPU) are optional features, the support for these features in the compiler can be enabled / disabled during compilation."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/basic_optimization_topics.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/basic_optimization_topics.md#using-the-right-command-line-options-in-compilation-toolchain"
license: "Apache-2.0"
mode: "V"
---

Because Helium and Floating-point unit (FPU) are optional features, the support for these features in the compiler can be enabled / disabled during compilation. As a result, software developers need to ensure that correct compilation options (or command line options if using the compiler in Command Line Interface)
For Arm Compiler 6.22, please refer to the following page for available options for Armv8.1-M processors: [Supported architecture feature combinations for specific processors](
https://developer.arm.com/documentation/101754/0622/armclang-Reference/Other-Compiler-specific-Features/Supported-architecture-feature-combinations-for-specific-processors)

Commonly used command line options are included here:

|Processor configuration|armclang / GCC option (-mcpu) | Armlink/fromelf options (--cpu)|
|---|---|---|
|No Helium, no FPU |# Cortex-M52 | # Cortex-M52 |
||-mcpu=cortex-m52+nomve+nofp|--cpu=cortex-m52.no_mve.no_fp|
||# Cortex-M55 | # Cortex-M55 |
||-mcpu=cortex-m55+nomve+nofp|--cpu=cortex-m55.no_mve.no_fp|
||# Cortex-M85 | # Cortex-M85 |
||-mcpu=cortex-m85+nomve+nofp|--cpu=cortex-m85.no_mve.no_fp|
|No Helium, have FPU |# Cortex-M52 | # Cortex-M52 |
||-mcpu=cortex-m52+nomve|--cpu=cortex-m52.no_mve|
||# Cortex-M55 | # Cortex-M55 |
||-mcpu=cortex-m55+nomve|--cpu=cortex-m55.no_mve|
||# Cortex-M85 | # Cortex-M85 |
||-mcpu=cortex-m85+nomve|--cpu=cortex-m85.no_mve|
|Full feature |# Cortex-M52 | # Cortex-M52 |
||-mcpu=cortex-m52|--cpu=cortex-m52|
||# Cortex-M55 | # Cortex-M55 |
||-mcpu=cortex-m55|--cpu=cortex-m55|
||# Cortex-M85 | # Cortex-M85 |
||-mcpu=cortex-m85|--cpu=cortex-m85|

Additional GCC options for Arm processors can be found in https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html.
