---
id: "alp-bare-metal-retarget"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Modify the example to use the UART for printf output"
summary: "You have been using printf() to output your message. A mechanism called semihosting was used to handle this output."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/retarget.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/retarget/"
license: "CC-BY-SA-4.0"
mode: "V"
---

You have been using `printf()` to output your message. A mechanism called [semihosting](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/FVP-debug) was used to handle this output. While this is supported in the FVP, it would not be available on real hardware (without a debugger being present), and so execution would simply stop when the `HLT` instruction that is used by the debugger/FVP to detect semihosting is executed.

Modify the example to send output to the [PL011 UART](https://developer.arm.com/documentation/ddi0183) of the FVP.

You can check if you are using semihosting by importing the symbol `__use_no_semihosting` to your project.

Modify `hello.c` to import the symbol:
#### hello.c
```C
#include <stdio.h>
__asm(".global __use_no_semihosting\n\t");

int main(void) {
  printf("Hello World!\n");
  return 0;
}
```
Rebuild the example:
```command
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello.c
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup_el3.s
armlink --scatter=scatter.txt hello.o startup_el3.o -o hello.axf --entry=el3_entry
```
The linker will error for any functions that use semihosting:
```output
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _sys_exit was referenced
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _sys_open was referenced
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _ttywrch was referenced
```
