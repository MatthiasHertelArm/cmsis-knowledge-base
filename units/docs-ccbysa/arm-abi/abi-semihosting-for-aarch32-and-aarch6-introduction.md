---
id: "abi-semihosting-for-aarch32-and-aarch6-introduction"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Introduction"
summary: "Semihosting is a mechanism that enables code running on an ARM target or emulator to communicate with and use the Input/Output facilities on a host computer."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

Semihosting is a mechanism that enables code running on an ARM target or emulator to communicate with and use the Input/Output facilities on a host computer. The host must be running the emulator, or a debugger that is attached to the ARM target.

Examples of these facilities include keyboard input, screen output, and disk I/O. For example, you can use this mechanism to enable functions in the C library, such as `printf()` and `scanf()`, to use the screen and keyboard of the host instead of having a screen and keyboard on the target system.

This is useful because development hardware often does not have all the input and output facilities of the final system. Semihosting enables the host computer to provide these facilities.

Semihosting is implemented by a set of defined software instructions that generate exceptions from program control. The application invokes the appropriate semihosting call and the debug agent then handles the exception. The debug agent provides the required communication with the host.

The semihosting interface is common across all debug agents that are provided by ARM. Semihosted operations work when you are debugging applications on your development platform, as shown in the following figure:

In many cases, semihosting is invoked by code within library functions. The application can also invoke the semihosting operation directly.


**Note:** The instruction that is used to make semihosting calls can be `SVC`, `HLT`, or `BKPT`, depending on the processor. See The semihosting interface for more detail.

The following terms are used in the semihosting documentation:

Semihosting Implementation
   An agent (for example, a debugger or emulator) that services semihosting operation requests from a Semihosting Caller executing on an ARM target.

Semihosting Caller
   A program executing on an ARM target that sends requests to a Semihosting Implementation (for example, a debugger or emulator) to service semihosting operations.


### Related information


  - The semihosting interface

  - [The ARM C and C++ libraries](https://developer.arm.com/docs/dui0475/latest/the-arm-c-and-c-libraries)
