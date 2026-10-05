---
id: "cfrt-create-a-freertos-project-debug-a-cmsis-freertos-project"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project: Debug a CMSIS-FreeRTOS Project"
summary: "Apart from the debug capabilities that Event Recorder offers, Keil MDK also supports thread-aware breakpoints, just like for the standard CMSIS-RTOS."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md#debug-a-cmsis-freertos-project"
license: "Apache-2.0"
mode: "V"
---

**Note:** The following only applies when used with [Arm Keil MDK](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK). If you are using a different toolchain, please consult its user's manual.

Apart from the debug capabilities that [Event Recorder](#configure_evr) offers, Keil MDK also supports thread-aware breakpoints, just like for the standard CMSIS-RTOS.

#### Code Example

```plaintext
BS FuncN1, 1, "break = (CURR_TID == tid_phaseA) ? 1 : 0"
BS FuncN1, 1, "break = (CURR_TID == tid_phaseA || CURR_TID == tid_phaseD) ? 1 : 0"
BS \\Blinky\Blinky.c\FuncN1\179, 1, "break = (CURR_TID == tid_phaseA || CURR_TID == tid_phaseD) ? 1 : 0"
```

> **Note:**
>
> - For more information on conditional breakpoints in Keil MDK, consult the [user's manual](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Windows-and-Dialogs/Breakpoints-Window).
> - Enabling [Periodic Window Update](https://developer.arm.com/documentation/101407/latest/User-Interface/View-Menu)
>   is required to capture register values for active running threads while executing. When turned off, only the current
>   FreeRTOS thread can be unwound after execution has been stopped.

#### Caveats

- You cannot specify individual breakpoints on the same address. The following is not possible:
  ```plaintext
  BS ThCallee, 1, "break = (CURR_TID==tid_phaseA) ? 1 : 0"
  BS ThCallee, 1, "break = (CURR_TID==tid_phaseD) ? 1 : 0"
  ```
  Instead, use this:
  ```plaintext
  BS ThCallee, 1, "break= (CURR_TID==tid_phaseA || CURR_TID==tid_phaseD) ? 1 : 0"
  ```

- If you don't want to use [Periodic Window Update](https://developer.arm.com/documentation/101407/latest/User-Interface/View-Menu), obtain the thread and unwind information by adding a function that gets called from each thread of interest:
  ```c
  _attribute_((noinline)) int FuncN1 (int n1) {
    ...
  }
  ```
  Then, specify a thread-aware breakpoint using an "invalid" thread ID:
  ```plaintext
  BS FuncN1, 1, "break = (CURR_TID == tid_phaseA + 1) ? 1 : 0"
  ```
  `'tid_phaseA'` would be valid, `'tid_phaseA + 1'` is not but will still capture the most recent registers and store them to the actual thread context each time a thread-aware breakpoint is checked.

- Function inlining typically causes thread-aware breakpoints to fail. To avoid this, prepend the `'noinline'` attribute to the function that is used to stop when the current FreeRTOS thread id matches:
  ```c
  _attribute_((noinline)) int FuncN1 (int n1) {
    ...
  }
  ```
  This helps to make thread-aware breakpoints far less dependent on the compiler optimization level.

- Thread-aware breakpoints should be setup using a [debug script](https://developer.arm.com/documentation/101407/latest/Debugging/Debug-Scripting). Reason being that thread-aware breakpoints are of a 'hybrid' type, that is a combined address and condition expression that works best when run from a debug script.
