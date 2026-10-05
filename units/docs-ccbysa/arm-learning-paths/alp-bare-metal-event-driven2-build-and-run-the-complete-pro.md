---
id: "alp-bare-metal-event-driven2-build-and-run-the-complete-pro"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (2): Build and run the complete project"
summary: "You are now ready to test the application. Build the project with:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2/#build-and-run-the-complete-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

You are now ready to test the application. Build the project with:
```command
armclang -c -g --target=aarch64-arm-none-eabi startup_el3.s
armclang -c -g --target=aarch64-arm-none-eabi uart.c
armclang -c -g --target=aarch64-arm-none-eabi vectors.s
armclang -c -g --target=aarch64-arm-none-eabi gic.s
armclang -c -g --target=aarch64-arm-none-eabi timer.s
armclang -c -g --target=aarch64-arm-none-eabi hello.c
armlink --scatter=scatter.txt --entry=el3_entry startup_el3.o uart.o vectors.o gic.o timer.o hello.o -o hello.axf
```
To enable the timer in the FVP, add the `-C bp.refcounter.non_arch_start_at_default=1` option to the command line.
```command
FVP_Base_AEMvA -C bp.refcounter.non_arch_start_at_default=1 -a hello.axf
```
Observe the application reporting that the exception occurred.
```output
Hello World!
Waiting for interrupt...
Interrupt 29 occurred
Returned from interrupt!
In _sys_exit. Use Ctrl+C to quit.
```
