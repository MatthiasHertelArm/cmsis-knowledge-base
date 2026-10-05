---
id: "intr-how-to-debug-a-hardfault-on-an-arm-relevant-status-registers"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Relevant Status Registers"
summary: "This 32 bit register contains a summary of the fault(s) which took place and resulted in the exception. The register is comprised of three different status registers -- UsageFault, BusFault & MemManage Fault Status Registers:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#relevant-status-registers"
license: "CC-BY-SA-4.0"
mode: "V"
---

{: #cfsr}

### Configurable Fault Status Registers (CFSR) - 0xE000ED28

This 32 bit register contains a summary of the fault(s) which took place and resulted in the exception. The register is comprised of three different status registers -- UsageFault, BusFault & MemManage Fault Status Registers:



The register can be accessed via a 32 bit read at `0xE000ED28` or each register can be read individually. For example, in GDB it would look something like this:

- Entire CFSR - `print/x *(uint32_t *) 0xE000ED28`
- [UsageFault Status Register (UFSR)](#ufsr) - `print/x *(uint16_t *)0xE000ED2A`
- [BusFault Status Register (BFSR)](#bfsr) - `print/x *(uint8_t *)0xE000ED29`
- [MemManage Status Register (MMFSR)](#mmfsr) - `print/x *(uint8_t *)0xE000ED28`

> NOTE: If multiple faults have occurred, bits related to several faults may be set. Fields are only cleared by a system reset or by writing a 1 to them.

{: #ufsr}

#### UsageFault Status Register (UFSR) - 0xE000ED2A

This register is a 2 byte register which summarizes any faults that are not related to memory access failures, such as executing invalid instructions or trying to enter invalid states.



where,

- `DIVBYZERO` - Indicates a divide instruction was executed where the denominator was zero. This fault is [configurable](#configurable-usage-faults).
- `UNALIGNED` - Indicates an unaligned access operation occurred. Unaligned multiple word accesses, such as accessing a `uint64_t` that is not `8-byte` aligned, will _always_ generate this fault. With the exception of Cortex-M0 MCUs, whether or not unaligned accesses below 4 bytes generate a fault is also [configurable](#configurable-usage-faults).
- `NOCP` - Indicates that a Cortex-M coprocessor instruction was issued but the coprocessor was
  disabled or not present. One common case where this fault happens is when code is compiled to use the Floating Point extension (`-mfloat-abi=hard` `-mfpu=fpv4-sp-d16`) but the coprocessor was not [enabled](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#fpu-config-options) on boot.
- `INVPC` - Indicates an integrity check failure on `EXC_RETURN`. We'll explore an example [below](#coprocessor-fault-example). [`EXC_RETURN`](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#exc-return-info) is the value branched to upon return from an exception. If this fault flag is set, it means a reserved `EXC_RETURN` value was used on exception exit.
- `INVSTATE` - Indicates the processor has tried to execute an instruction with an invalid
  _Execution Program Status Register_ (**EPSR**) value. Among other things the ESPR tracks whether or not the processor is in thumb mode state. Instructions which use "interworking addresses"[^1] (`bx` & `blx` or `ldr` & `ldm` when loading a `pc`-relative value) must set `bit[0]` of the instruction to 1 as this is used to update `ESPR.T`. If this rule is violated, a `INVSTATE` exception will be generated. When writing C code, the compiler will take care of this automatically, but this is a common bug which can arise when hand-writing assembly.
- `UNDEFINSTR` - Indicates an undefined instruction was executed. This can happen on exception exit if the stack got corrupted. A compiler may emit undefined instructions as well for code paths that _should_ be unreachable.

{: #configurable-usage-faults}

##### Configurable UsageFault

It is worth noting that some classes of UsageFaults are configurable via the _Configuration and Control Register_ (**CCR**) located at address `0xE000ED14`.

- Bit 4 (`DIV_0_TRP`) - Controls whether or not divide by zeros will trigger a fault.
- Bit 3 (`UNALIGN_TRP`) - Controls whether or not unaligned accesses will always generate a fault.

> NOTE: On reset both of these optional faults are disabled. It is generally a good idea to enable `DIV_0_TRP` to catch mathematical errors in your code.

{: #bfsr}

#### BusFault Status Register (BFSR) - 0xE000ED29

This register is a 1 byte register which summarizes faults related to instruction prefetch or memory access failures.



- `BFARVALID` - Indicates that the _Bus Fault Address Register_ (**BFAR**), a 32 bit register located at `0xE000ED38`, holds the address which triggered the fault. We'll walk through an example using this info [below](#bad-address-read-example).
- `LSPERR` & `STKERR` - Indicates that a fault occurred during lazy state preservation or during exception entry, respectively. Both are situations where the hardware is [automatically saving state on the stack](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#context-state-stacking). One way this error may occur is if the stack in use overflows off the valid RAM address range while trying to service an exception. We'll go over an example [below](#stkerr-example).
- `UNSTKERR` - Indicates that a fault occurred trying to return from an exception. This typically arises if the stack was corrupted while the exception was running or the stack pointer was changed and its contents were not initialized correctly.
- `IMPRECISERR` - This flag is _very_ important. It tells us whether or not the hardware was able to determine the exact location of the fault. We will explore some debug strategies when this flag is set in the [next section](#imprecise-error-debug) and walk through a code exampe [below](#imprecise-error-code-example).
- `PRECISERR` - Indicates that the instruction which was executing prior to exception entry triggered the fault.

{: #imprecise-error-debug}

##### Imprecise Bus Error Debug Tips

Imprecise errors are one of the hardest classes of faults to debug. They result asynchronously to instruction execution flow. This means the registers stacked on exception entry will **not** point to the code that caused the exception.

Instruction fetches and data loads should always generate _synchronous_ faults for Cortex-M devices and be precise. Conversely, store operations can generate _asynchronous_ faults. This is because writes will sometimes be buffered prior to being flushed to prevent pipeline stalls so the program counter will advance before the actual data store completes.

When debugging an imprecise error, you will want to inspect the code around the area reported by the exception for a store that looks suspicious. If the MCU has support for the ARM _Embedded Trace Macrocell_ (**ETM**), the history of recently executed instructions can be viewed by some debuggers[^8].

##### Auxiliary Control Register (ACTLR) - 0xE000E008

This register allows for some hardware optimizations or features to be disabled typically at the cost of overall performance or interrupt latency. The exact configuration options available are specific to the Cortex-M implementation being used.

{: #cortex-m3-m4-debug-trick}
For the Cortex M3 & Cortex M4 **only**, there is a trick to make all `IMPRECISE` accesses `PRECISE` by disabling any write buffering. This can be done by setting bit 1 (`DISDEFWBUF`) of the register to 1.

For the Cortex M7, there is **no** way to force all stores to be synchronous / precise.

##### Auxiliary Bus Fault Status Register (ABFSR) - 0xE000EFA8

This register **only** exists for Cortex-M7 devices. When an `IMPRECISE` error occurs it will at least give us an indication of what memory bus the fault occurred on[^7]:



A full discussion of memory interfaces is outside the scope of this article but more details can be found in the reference manual [^7].

{: #mmfsr}

#### MemManage Status Register (MMFSR) - 0xE000ED28

This register reports Memory Protection Unit faults.

Typically MPU faults will only trigger if the MPU has been [configured and enabled](https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu) by the firmware. However, there are a few memory access errors that will always result in a MemManage fault -- such as trying to execute code from the system address range (`0xExxx.xxxx`).

The layout of the register looks like this:



where,

- `MMARVALID` - Indicates that the _MemManage Fault Address Register_ (**MMFAR**), a 32 bit register located at `0xE000ED34`, holds the address which triggered the MemManage fault.
- `MLSPERR` & `MSTKERR` - Indicates that a MemManage fault occurred during lazy state preservation or exception entry, respectively. For example, this could happen if an MPU region is being used to detect [stack overflows](https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu).
- `MUNSTKERR` - Indicates that a fault occurred while returning from an exception
- `DACCVIOL` - Indicates that a data access triggered the MemManage fault.
- `IACCVIOL` - Indicates that an attempt to execute an instruction triggered an MPU or Execute Never (XN) fault. We'll explore an example [below](#bad-pc-mpu-fault).

### HardFault Status Register (HFSR) - 0xE000ED2C

This registers explains the reason a HardFault exception was triggered.



There's not too much information in this register but we will go over the fields real quickly

- `DEBUGEVT` - Indicates that a debug event (i.e executing a breakpoint instruction) occurred while the debug subsystem was not enabled
- `FORCED` - This means a configurable fault (i.e. the fault types we discussed in previous sections) was escalated to a HardFault, either because the configurable fault handler was not enabled or a fault occurred within the handler.
- `VECTTBL` - Indicates a fault occurred because of an issue reading from an address in the vector table. This is pretty atypical but could happen if there is a bad address in the vector table and an unexpected interrupt fires.

{: #registers-prior-to-exception}
