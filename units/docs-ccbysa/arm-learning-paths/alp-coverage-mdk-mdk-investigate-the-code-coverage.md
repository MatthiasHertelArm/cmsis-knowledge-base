---
id: "alp-coverage-mdk-mdk-investigate-the-code-coverage"
type: "concept"
domain: "debug"
title: "Get started with Keil MDK Code Coverage: Set up Code Coverage: Investigate the code coverage output"
summary: "Observe the report, which details the percentage of instructions that have been executed for each function. Browse for an interesting record, for example osRtxThreadDelayTick, within rtx_thread.c."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/coverage_mdk/mdk.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/coverage_mdk/mdk/#investigate-the-code-coverage-output"
license: "CC-BY-SA-4.0"
mode: "V"
---

Observe the report, which details the percentage of instructions that have been executed for each function. Browse for an interesting record, for example `osRtxThreadDelayTick`, within `rtx_thread.c`. You should see less than 100% of the instructions executed, including one or more instructions not fully executed.

Click on that function (in the `Code Coverage` window) to put the source and disassembly views in focus on that function.

Code that has been fully executed is highlighted in green.

Code that hasn't been executed (such as some of the switch-cases) isn't highlighted.

Code that hasn't been fully executed is highlighted in orange or blue. This means, for example, a conditional branch instruction where only one of the true and false conditions has been met, so the other branch path of that instruction hasn't been tested by that run. Orange means the branch is never taken, blue means it has always been taken.

It is also possible to output the code coverage information on the MDK command line. To show all, simply use:
```command
coverage
```
You can also filter the report by source file or function. In the `Code Coverage` view by the `Module` pulldown, else on the command line with, for example:
```command
coverage \blinky.c
coverage \blinky.c\main
```
