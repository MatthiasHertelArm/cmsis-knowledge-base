---
id: "avh-useful-hints-and-tips-execution-timing"
type: "concept"
domain: "test"
title: "Useful Hints and Tips: Execution timing"
summary: "FVP simulation models are targeted to software development and functional testing, and are not suitable for accurate performance comparisons on the CPU level."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/hints_and_tips.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/hints_and_tips.md#execution-timing"
license: "Apache-2.0"
mode: "V"
---

FVP simulation models are targeted to software development and functional testing, and are not  suitable for accurate
performance comparisons on the CPU level. However, they can be well used to analyze timing on the program level, such
as for scheduling RTOS tasks, detecting deadlocks, but also identifying overall performance trends.

Following mechanisms and settings can be used for timing control and measurements:

- FVP models can be started with command-line option `--stat` to print the execution statistics on simulation
  exit. Here is an example of such statistics output:

  ```txt
  --- cpu_core statistics: ------------------------------------------------------
  Simulated time                          : 0.651964s
  User time                               : 0.843750s
  System time                             : 0.109375s
  Wall time                               : 1.503559s
  Performance index                       : 0.43
  cpu_core.cpu0                           :  68.40 MIPS (    65196784 Inst)
  -------------------------------------------------------------------------------
  ```

Also see section
[Displaying the total execution time](https://developer.arm.com/documentation/100965/latest/Timing-Annotation/Timing-annotation-tutorial/Setting-up-the-environment/Displaying-the-total-execution-time-of-the-simulation)
in the Fast Models User Guide.

- [CMSIS-View](https://github.com/ARM-software/CMSIS-View) utility can be used to measure and analyze timing between
  events in the program, including statistical data. To store the log files on FVPs, semihosting
  should be enabled. CMSIS-View annotations can also be reused for event analysis and time measurement on real
  hardware.
- Config parameters can be used to control and impact the execution timing:
    - With Cycle Per Instruction (CPI) settings `cpi_div` and `cpi_mul`.
    - With clock configurations such as Clock Rate Multiplier, for example `core_clk.mul` on Corstone-300.
    - With pipeline-impacting parameters such as for memory caches, Floating-Point-Unit (FPU) or M-Profile Vector
      Extensions (MVE), etc.

The [Timing Annotations](https://developer.arm.com/documentation/100965/latest/Timing-Annotation) chapter in the Fast
Models User Guide explains the performance estimation concept as implemented in the underlying Fast Models technology.
Note that the FVPs are built with Timing Annotations enabled (`FASTSIM_DISABLE_TA` set to 0).

For interaction with the external world such as via arm_vsi or semihosting, the timing differences need to be
taken into account as explained in
[Timing-considerations-for-FVPs](https://developer.arm.com/documentation/100966/1126/Getting-Started-with-Fixed-Virtual-Platforms/Timing-considerations-for-FVPs).
