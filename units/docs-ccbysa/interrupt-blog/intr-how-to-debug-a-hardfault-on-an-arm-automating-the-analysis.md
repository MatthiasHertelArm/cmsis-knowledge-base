---
id: "intr-how-to-debug-a-hardfault-on-an-arm-automating-the-analysis"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Automating the Analysis"
summary: "At this point we have gone over all the pieces of information which can be manually examined to determine what caused a fault."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#automating-the-analysis"
license: "CC-BY-SA-4.0"
mode: "V"
---

At this point we have gone over all the pieces of information which can be manually examined to determine what caused a fault. While this might be fun the first couple times, it can become a tiresome and error prone process if you wind up doing it often. In the following sections we'll explore how we can automate this analysis!

### Halting & Determining Core Register State

What if we are trying to debug an issue that is **not** easy to reproduce? Even if we have a debugger attached, useful state may be overwritten before we have a chance to halt the debugger and take a look.

The first thing we can do is to programmatically trigger a breakpoint when the system faults:

```c
// NOTE: If you are using CMSIS, the registers can also be
// accessed through CoreDebug->DHCSR & CoreDebug_DHCSR_C_DEBUGEN_Msk
#define HALT_IF_DEBUGGING()                              \
  do {                                                   \
    if ((*(volatile uint32_t *)0xE000EDF0) & (1 << 0)) { \
      __asm("bkpt 1");                                   \
    }                                                    \
} while (0)
```

[Above](#registers-prior-to-exception), we discussed how to hand unroll the register state prior to the exception taking place. Let's explore how we can instrument the code to make this a less painful process.

First, we can easily define a C struct to represent the register stacking:

```c
typedef struct __attribute__((packed)) ContextStateFrame {
  uint32_t r0;
  uint32_t r1;
  uint32_t r2;
  uint32_t r3;
  uint32_t r12;
  uint32_t lr;
  uint32_t return_address;
  uint32_t xpsr;
} sContextStateFrame;
```

We can determine the stack pointer that was active prior to the exception using a small assembly shim that applies the logic discussed [above](#determine-pre-exception-sp) and passes the active stack pointer as an argument into `my_fault_handler_c`:

```shell
#define HARDFAULT_HANDLING_ASM(_x)               \
  __asm volatile(                                \
      "tst lr, #4 \n"                            \
      "ite eq \n"                                \
      "mrseq r0, msp \n"                         \
      "mrsne r0, psp \n"                         \
      "b my_fault_handler_c \n"                  \
                                                 )
```

{: #my-fault-handler-c}
Finally, we can put together `my_fault_handler_c` that looks something like:

```c
// Disable optimizations for this function so "frame" argument
// does not get optimized away
__attribute__((optimize("O0")))
void my_fault_handler_c(sContextStateFrame *frame) {
  // If and only if a debugger is attached, execute a breakpoint
  // instruction so we can take a look at what triggered the fault
  HALT_IF_DEBUGGING();

  // Logic for dealing with the exception. Typically:
  //  - log the fault which occurred for postmortem analysis
  //  - If the fault is recoverable,
  //    - clear errors and return back to Thread Mode
  //  - else
  //    - reboot system
}
```

Now when a fault occurs and a debugger is attached, we will automatically hit a breakpoint and be able to look at the register state!
Re-examining our `illegal_instruction_execution` example we have:

```
0x00000244 in my_fault_handler_c (frame=0x200005d8 <ucHeap+1136>) at ./cortex-m-fault-debug/startup.c:94
94	  HALT_IF_DEBUGGING();
(gdb) p/a *frame
$18 = {
  r0 = 0x0 <g_pfnVectors>,
  r1 = 0x200003c4 <ucHeap+604>,
  r2 = 0x10000000,
  r3 = 0xe0000000,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x61 <illegal_instruction_execution+16>,
  return_address = 0xe0000000,
  xpsr = 0x80000000
}
```

Furthermore, we now have a variable we can read stack info from and a C function we can easily extend for postportem analysis!

### Fault Register Analyzers

#### Instrumenting the code

Many Real Time Operating Systems (**RTOS**) targeting Cortex-M devices will add options to dump
verbose fault register information to the console upon crash. Some examples include Arm Mbed OS[^2]
and Zephyr[^3]. For example, with Zephyr, the `illegal_instruction_execution()` crash looks like:

```
***** MPU FAULT *****
  Instruction Access Violation
***** Hardware exception *****
Current thread ID = 0x20000074
Faulting instruction address = 0xe0000000
Fatal fault in thread 0x20000074! Aborting.
```

This approach has a couple notable limitations:

- It bloats the code & data size of the binary image and consequently often gets turned off.
- It can increase the stack size requirements for the fault handler (due to printf calls)
- It requires a firmware update to improve or fix issues with the analyzers
- It requires a console session be active to see what fault occurred. Furthermore, this can be flaky if the system is in a crashed state.

#### Debugger Plugins

Many embedded IDEs expose a system view that can be used to look at registers. The registers will often be decoded into human readable descriptions. These implementations typically leverage the CMSIS _System View Description_ (**SVD**) format[^4], a standardized XML file format for describing the memory mapped registers in an ARM MCU. Most silicon vendors expose this information on their own website, ARM's website[^5], or provide the files upon request.

{: #pycortex-svd-gdb-setup}
You can even load these files in GDB using PyCortexMDebug[^6], a [GDB python](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api#getting-started-with-gdb-python) script .

To use the utility, all you need to do is update your `.gdbinit` to use PyPi packages from your environment (instructions [here](https://interrupt.memfault.com/blog/using-pypi-packages-with-GDB#3-append-syspath-to-gdbs-python)) and then run:

```shell
$ git clone git@github.com:bnahill/PyCortexMDebug.git
# Check out Python 2 compatible code
$ git checkout 77af54e
$ cd PyCortexMDebug
$ python setup.py install
```

When you next start gdb, you can source the `svd_gdb.py` script and use it to start inspecting registers. Here's some output for the svd plugin we will use in the examples [below](#svd-usage-example):

```
(gdb) source cmdebug/svd_gdb.py
(gdb) svd_load cortex-m4-scb.svd
(gdb) svd
Available Peripherals:
    ...
	SCB:        System control block
    ...
(gdb) svd SCB
Registers in SCB:
    ...
	CFSR_UFSR_BFSR_MMFSR:      524288  Configurable fault status register
    ...
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
	IACCVIOL:     0  Instruction access violation flag
	DACCVIOL:     0  Data access violation flag
	MUNSTKERR:    0  Memory manager fault on unstacking for a return from exception
	MSTKERR:      0  Memory manager fault on stacking for exception entry.
	MLSPERR:      0
	MMARVALID:    0  Memory Management Fault Address Register (MMAR) valid flag
	IBUSERR:      1  Instruction bus error
	PRECISERR:    0  Precise data bus error
	IMPRECISERR:  0  Imprecise data bus error
	UNSTKERR:     0  Bus fault on unstacking for a return from exception
	STKERR:       0  Bus fault on stacking for exception entry
	LSPERR:       0  Bus fault on floating-point lazy state preservation
	BFARVALID:    0  Bus Fault Address Register (BFAR) valid flag
	UNDEFINSTR:   0  Undefined instruction usage fault
	INVSTATE:     1  Invalid state usage fault
	INVPC:        0  Invalid PC load usage fault
	NOCP:         0  No coprocessor usage fault.
	UNALIGNED:    0  Unaligned access usage fault
	DIVBYZERO:    0  Divide by zero usage fault
```

### Postmortem Analysis

The previous two approaches are only helpful if we have a debug or physical connection to the device. Once the product has shipped and is out in the field these strategies will not help to triage what went wrong on devices.

One approach is to simply try and reproduce the issue on site. This is a guessing game (are you
actually reproducing the same issue the customer hit?), can be a huge time sink and in some cases is not even particularly feasible[^14].

Another strategy is to log the fault register and stack values to persistent storage and periocially collect or push the error logs. On the server side, the register values can be decoded and addresses can be symbolicated to try to root cause the crash.

Alternatively, an end-to-end firmware error analysis system, such as
[Memfault](https://memfault.com/features/error-analysis.html?utm_source=interrupt&utm_medium=link&utm_campaign=cortex-m-faults),
can be used to automatically collect, transport, deduplicate and surface the faults and crashes happening in the field. Here is some example output from Memfault for the bad memory read example we will walk through [below](#bad-address-read-example):



{: #recovering-from-a-fault}
