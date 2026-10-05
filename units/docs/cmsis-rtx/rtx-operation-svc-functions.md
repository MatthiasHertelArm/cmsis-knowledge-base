---
id: "rtx-operation-svc-functions"
type: "concept"
domain: "rtos"
title: "operation: SVC Functions"
summary: "Supervisor Calls (SVC) are exceptions targeted at software and operating systems for generating system function calls. They are sometimes called software interrupts."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#svc-functions"
license: "Apache-2.0"
mode: "V"
---

Supervisor Calls (SVC) are exceptions targeted at software and operating systems for generating system function calls. They are sometimes called software interrupts. For example, instead of allowing user programs to directly access hardware, an operating system may provide access to hardware through an SVC. So when a user program wants to use certain hardware, it generates the exception using SVC instructions. The software exception handler in the operating system executes and provides the requested service to the user application. In this way, access to hardware is under the control of the OS, which can provide a more robust system by preventing the user applications from directly accessing the hardware.

SVCs can also make software more portable because the user application does not need to know the programming details of the underlying hardware. The user program will only need to know the application programming interface (API) function ID and parameters; the actual hardware-level programming is handled by device drivers.

SVCs run in **privileged handler** mode of the Arm Cortex-M core. SVC functions accept arguments and can return values. The functions are used in the same way as other functions; however, they are executed indirectly through the SVC instruction. When executing SVC instructions, the controller changes to the privileged handler mode.

Interrupts are **not disabled** in this mode. To protect SVC functions from interrupts, you need to include the disable/enable intrinsic functions `__disable_irq()` and `__enable_irq()` in your code.

You can use SVC functions to access protected peripherals, for example, to configure NVIC and interrupts. This is required if you run threads in unprivileged (protected) mode and you need to change interrupts from the within the thread.

To implement SVC functions in your Keil RTX5 project, you need to:

 1. Add the SVC User Table file **svc_user.c** to your project folder and include it into your project. This file is available as a user code template.
 2. Write a function implementation. Example:

  ```c
    uint32_t svc_atomic_inc32 (uint32_t *mem) {
      // A protected function to increment a counter. 
      uint32_t val;
        
      __disable_irq();
      val  = *mem;
      (*mem) = val + 1U;
      __enable_irq();
        
      return (val);
    }
  ```

 3. Add the function to the SVC function table in the **svc_user.c** module:

  ```c
    void * const osRtxUserSVC[1+USER_SVC_COUNT] = {
      (void *)USER_SVC_COUNT,
      (void *)svc_atomic_inc32,
    };
  ```

 4. Increment the number of user SVC functions:

  ```c
    #define USER_SVC_COUNT  1       // Number of user SVC functions
  ```

 5. Declare a function wrapper to be called by the user to execute the SVC call.
 **Code Example** (Arm Compiler 6):

  ```c
    __STATIC_FORCEINLINE uint32_t atomic_inc32 (uint32_t *mem) {
      register uint32_t val;
      
      __ASM volatile (
        "svc 1" : "=l" (val) : "l" (mem) : "cc", "memory"
      );
      return (val);
    }
  ```

> **Note**
>
> - The SVC function `0` is reserved for the Keil RTX5 kernel.
> - Do not leave gaps when numbering SVC functions. They must occupy a continuous range of numbers starting from 1.
> - SVC functions can still be interrupted.

\ifnot FuSaRTS
