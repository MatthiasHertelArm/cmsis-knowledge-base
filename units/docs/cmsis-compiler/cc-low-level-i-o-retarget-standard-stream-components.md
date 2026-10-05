---
id: "cc-low-level-i-o-retarget-standard-stream-components"
type: "concept"
domain: "core"
title: "Low-Level I/O Retarget: Standard Stream Components"
summary: "Software components that retarget the standard C library input/output streams are as follows:"
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_io.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_io.md#standard-stream-components"
license: "Apache-2.0"
mode: "V"
---

Software components that retarget the standard C library input/output streams are as follows:

 Component  |  Description
:-----------|:--------------------
 **STDERR** | Standard error stream of the application to output diagnostic messages.
 **STDIN**  | Standard input stream going into the application (`scanf` etc.).
 **STDOUT** | Standard output stream of the application (`printf` etc.).
 **TTY**    | Teletypewriter, which is the last resort for error output.

> **Note**
> - **TTY** is only available for Arm Compiler toolchain.

Each component can have various rt_io_subcomponents.

### Standard Stream Subcomponents

The subcomponent selection allows you to change the target hardware interface of the I/O stream.

#### STDERR/STDIN/STDOUT Subcomponents

(figure: STDERR/STDIN/STDOUT subcomponents)

The following subcomponents are available:

 Variant           | Description
:------------------|:-------------------
**Breakpoint**     | When the I/O stream is used, the application stops with [BKPT](https://developer.arm.com/documentation/100073/latest/The-Arm-C-and-C---Libraries/Support-for-building-an-application-with-the-C-library/Using-the-C-and-C---libraries-with-an-application-in-a-semihosting-environment?lang=en) instruction. No additional code is required.
**Event Recorder** | STDOUT and STDERR can be redirected using the [Event Recorder](https://arm-software.github.io/CMSIS-View/main/evr.html) (especially interesting for targets without ITM (such as Cortex-M0/M0+/M23)).
**ITM**            | Use [Instrumentation Trace Macrocell (ITM)](https://developer.arm.com/documentation/ddi0314/h/Instrumentation-Trace-Macrocell?lang=en) for I/O communication via the debugger (only available for Cortex-M3/M4/M7/M33/M55/M85 processors).
 Usually, data is shown in a dedicated window.
 No additional code is required to output or input data through the ITM channel. However, you have to configure the ITM channel for tracing.
**RTT**            | Retarget I/O streams to SEGGER RTT Channel 0.
**UART**           | Retarget I/O streams to UART. Default implementation variant uses CMSIS-Driver USART.
**Custom**         | Retarget I/O stream to a user defined interface (such as custom UART implementation or other application specific interface).
See custom_subcomponent for further details.


> **Note**
> - Depending on the selected subcomponent, certain `#define` are set in the header file **RTE_Components.h** that enable the appropriate code sections in the retarget core implementation.
> - Retargeting **STDOUT** and **STDERR** using the *Event Recorder* variant is available for all Cortex-M based devices.
> - The [microlib](https://developer.arm.com/documentation/100073/latest/The-Arm-C-Micro-library?lang=en) of Arm Compiler C run-time library interfaces to the hardware via low-level functions. It implements a reduced set of high-level functions and therefore does not implement system I/O functions. Thus, in case of using the microlib, you cannot redefine the system I/O functions. Using any of the features of the Arm Compiler component provides the [assert](https://developer.arm.com/documentation/101754/latest/armasm-Legacy-Assembler-Reference/armasm-Directives-Reference/ASSERT-directive?lang=en) facility for microlib.

### "Custom" Subcomponent

The **Custom** component provides code template that helps you to implement the retarget interface functionality for custom interfaces that are not mentioned above.

The following user code templates are available:

 Component     | Name                 | File Name
:--------------|:---------------------|:-----------------------------------
 STDOUT:Custom | STDOUT User template | stdout_user.c
 STDIN:Custom  | STDIN User template  | stdin_user.c
 STDERR:Custom | STDERR User template | stderr_user.c
 TTY:Custom    | TTY User template    | tty_user.c
