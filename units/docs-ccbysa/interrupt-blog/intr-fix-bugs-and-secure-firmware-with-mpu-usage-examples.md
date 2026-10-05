---
id: "intr-fix-bugs-and-secure-firmware-with-mpu-usage-examples"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU: MPU Usage Examples"
summary: "Now that we have a better grasp of what an MPU does and how to configure it, let's try a couple real world examples."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#mpu-usage-examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have a better grasp of what an MPU does and how to configure it, let's try a couple real world examples. For the purposes of this demo, I am using a [nRF52840 DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-DK) and running the blinky demo application compiled at `examples/peripheral/blinky/pca10056/blank/armgcc` in the [v15.2 SDK](https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v15.x.x/nRF5_SDK_15.2.0_9412b96.zip). However, you should be able to run similar code snippets on pretty much any _ARMv6-M_ or _ARMv7-M_ processor with an MPU!

The examples which follow will walk through building up a collection of MPU region configurations and example crashes but you can also look at the code in it's entirety [here](https://github.com/memfault/interrupt/tree/master/example/armv7-mpu/main.c) which is a drop-in replacement for the blinky `main.c` located at `examples/peripheral/blinky/main.c` in the SDK.

**NOTE** For convenience, the code makes use of a couple GCC extensions, notably some [function attributes](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Common-Function-Attributes.html#Common-Function-Attributes) and [binary constants](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Binary-constants.html) but could easily be modified to target other compilers as well.

### Examine NRF52 MPU Implementation

Let's read the `MPU_TYPE` register from GDB to sanity check that it _has_ a MPU implemented and determine the number of regions available! As mentioned above this is in the 8 bit `DREGION` field

```
(gdb) p/x (*(uint32_t*)0xE000ED90>>8)&0xff
$1 = 0x8
```

Great, we have 8 regions to work with!

Now let's check the minimum region size supported. As described in the `MPU_RBAR` section above this can be resolved by setting bits 32-5 to 1. If all the bits remain set, it means the smallest possible size of 32 bytes is supported. We can check this out in GDB as well and confirm the NRF52 supports a minimum region size of 32 bytes:

```
(gdb) set *(uint32_t*)0xE000ED9C=0xffffffe0
(gdb) p/x *(uint32_t*)0xE000ED9C
$3 = 0xffffffe0
```

### Enable MemManage Fault Handler

Let's override the default `MemManage` fault handler for the purposes of our example to just trigger a breakpoint. That way GDB will halt as soon as
a MemManage Fault is hit and we can investigate further.

```c
// The NRF52 fault handlers can be overridden because they are declared as weak
// Let's override the handler and insert a breakpoint when it's hit
__attribute__((naked))
void MemoryManagement_Handler(void) {
  __asm("bkpt 1");
}
```

The `MemManage` fault is off by default. (When it's off an MPU fault will immediately escalate to a hardfault). You will need to add the following code somewhere during init to enable the exception:

```c
  // Let's set MEMFAULTENA so MemManage faults get tripped
  // (otherwise we will immediately get a HardFault)
  volatile uint32_t *shcsr = (void *)0xE000ED24;
  *shcsr |= (0x1 << 16);
```

### Catch Stack Overflows with the MPU

For illustrative purposes, let's add a simple recursive function to `main.c`. We'll also disable optimizations in all our examples so it's easier to step through the code in a debugger.

```c
__attribute__((optimize("O0")))
int recursive_sum(int n) {
  if (n == 0) {
    return 0;
  }

  return n + recursive_sum(n-1);
}
```

From our `main` loop let's call `recursive_sum(600)`. If you compile and run the application, you should see the LEDs blink in a loop. Things _appear_ to be working. Let's use MPU Region 0 just to be sure we aren't overflowing our stack.

The NRF52 SDK defines a [linker script variable](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#variables), `__StackLimit`, which can be used to determine where the end of the stack is. We'll set up a `64 byte` MPU region at the bottom of the stack so we can catch a stack overflow as it is happening. Based on what we learned above, the configuration settings we need to add to our code will look something like:

```c
  volatile uint32_t *mpu_rbar = (void *)0xE000ED9C;
  volatile uint32_t *mpu_rasr = (void *)0xE000EDA0;

  extern uint32_t __StackLimit;
  // align base address to nearest 64 byte boundary
  // because it needs to match SIZE
  uint32_t mask = 64 - 1;
  const uint32_t base_addr = ((uint32_t)&__StackLimit + mask) & ~mask;

  // Let's set the base_address and use the 'VALID'
  // bit to make sure region 0 is active in 'MPU_RNR'
  *mpu_rbar = (base_addr | 1 << 4 | 0);

  // MPU_RASR settings:
  //  AP=0b000 because we don't want to allow _any_ access
  //  TEXSCB=0b000110 because the Stack is in "Internal SRAM"
  //  SIZE=5 because we want a 64 byte MPU region
  //  ENABLE=1
  *mpu_rasr = (0b000 << 24) | (0b000110 << 16) | (5 << 1) | 0x1;
```

Finally, let's activate the MPU:

```c
  // Finally, activate the MPU and default memory map (PRIVDEFENA)
  volatile uint32_t *mpu_ctrl = (void *)0xE000ED94;
  *mpu_ctrl = 0x5;
```

If we have a debugger attached, we should hit the breakpoint we set:

```
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
MemoryManagement_Handler () at ../../../main.c:20
20    __asm("bkpt 1");
```

When a MemManage fault is hit there are a couple registers that are very helpful to look at.

The first is the MemManage Status Register (`MMFSR`) - 0xE000ED28:


The second is the MemManage Fault Address Register (`MMFAR`) located at 0xE000ED34 which contains the address of the access which triggered the fault provided `MMFSR.MMARVALID` is set.

Let's look at this information in GDB and compare it to the bottom of the stack, `&__StackLimit`.

```
(gdb) p &__StackLimit
$1 = (uint32_t *) 0x2003e000
(gdb) p/x *(uint32_t*)0xE000ED28
$2 = 0x92
(gdb) p/x *(uint32_t*)0xE000ED34
$3 = 0x2003e038
```

We see our `MMARVALID` is set so we know the fault took place when the address `0x2003e038` was accessed. This is directly above the bottom of our stack, `0x2003e000`, at the top of the 64 byte MPU region we allocated! So our deep recursive routine _is_ overflowing. Even though things _appeared_ to be working we were silently corrupting the memory below our stack. This would almost _certainly_ cause subtle issues in the future when the linker placed a variable in that area or we moved a heap to that region.

### Catch Writes To Flash

On ARM processors, `0x0` is a _valid_ address. `0x00000000`-`0x1FFFFFFF` is specified as a `Code region` and usually maps to internal flash. On most processors writes to this address range are a no-op. This means a `NULL` pointer dereferences and write can go uncaught. We can try it out on our MCU by adding a function that looks something like this:

```c
__attribute__((optimize("O0")))
void invalid_write_to_flash(void) {
  volatile uint32_t *bad_pointer = (void *)0x0;
  *bad_pointer = 0xdeadbeef;
}
```

Running this in the main loop on the NRF52 blinky app, we see the LEDs happily blinking.

To help us catch nefarious NULL-pointer dereference bugs, let's extend our example app and use MPU Region 1 to make the flash space read-only. For the NRF52840, the code we need to add will look something like this:

```c
  // The NRF52840 internal flash is 1MB and starts at address 0x0
  // No need to mask the address since it's fixed and 1MB aligned
  base_addr = 0x0;
  // Let's use the 'VALID' bit to select region 1 in 'MPU_RNR'
  *mpu_rbar = (base_addr | 1 << 4 | 1);

  // MPU_RASR settings for flash write protection:
  //  AP=0b110 to make the region read-only regardless of privilege
  //  TEXSCB=0b000010 because the Code is in "Flash memory"
  //  SIZE=19 because we want to cover 1MB
  //  ENABLE=1
  *mpu_rasr = (0b110 << 24) | (0b000010 << 16) | (19 << 1) | 0x1;
```

Now when we run the example with a debugger attached we see clearly where the bad access took place and can fix the problem!

```
MemoryManagement_Handler () at ../../../main.c:26
26    __asm("bkpt 1");
(gdb) p/x *(uint32_t*)0xE000ED28
$1 = 0x82
(gdb) p/x *(uint32_t*)0xE000ED34
$2 = 0x0
(gdb) bt
#0  MemoryManagement_Handler () at ../../../main.c:26
#1  <signal handler called>
#2  0x000002fe in invalid_write_to_flash () at ../../../main.c:19
#3  0x00000358 in main () at ../../../main.c:81
(gdb) frame 2
#2  0x000002fe in invalid_write_to_flash () at ../../../main.c:19
19    *bad_pointer = 0xdeadbeef;
```

### Catch Execution of Data Array As Code

Now let's look at an example where an array of data is getting executed as if it's valid code. In this example, we just so happen to have an array of "random" data that has a valid _SVC_ instruction within it. The _SVC_ instruction is used for switching between [privileged and unprivileged](https://blog.stratifylabs.co/device/2013-10-12-Effective-Use-of-ARM-Cortex-M3-SVCall/) mode so on a real world system that runs third party code this could be the start of a serious security exploit!

```c
// An array of data that "happens" to have a pattern of valid
// ARM instructions.
//
// Note: We are aligning the data along a boundary that matches its
// size for simplicity in our MPU configuration example
static const uint16_t s_data[64] __attribute__((aligned(128))) = {
  0xbf00, // nop
  0xbf00, // nop
  0xdf00, // svc 0
  0x4770, // bx lr
};

__attribute__((optimize("O0")))
void execute_data_array_as_code(void) {
  uint32_t func_addr = (uint32_t)&s_data[0];
  // bit[0] of a function pointer must be set to 1 per per
  // "ARMv7-M and interworking support" section of reference manual
  func_addr |= 0x1;

  // perform a read/write
  s_data[5] |= 0xabab;

  // execute the array like it's a function
  void (*data_as_function)(void) = (void *)func_addr;
  data_as_function();
}
```

On the NRF52840, the default `SVC_Handler` is a `while (1)` loop so calling `execute_data_array_as_code()` wedges the system in an infinite loop in an interrupt which isn't great either! Let's guard the data region with MPU Region 2 and set the _Execute Never_ (`XN`) bit to intercept this kind of attack! The MPU configuration will look something like:

```c
  // The s_data struct is 128 bytes in size and is already 128 byte aligned
  base_addr = (uint32_t)&s_data[0];
  // Let's use the 'VALID' bit to select region 2 in 'MPU_RNR'
  *mpu_rbar = (base_addr | 1 << 4 | 2);

  // MPU_RASR settings for flash write protection:
  //  XN=1 to block _any_ attempts to execute the region as code
  //  AP=0b011 to allow full read/write access to the region
  //  TEXSCB=0b000110 because the Stack is in "Internal SRAM"
  //  SIZE=6 because we want to cover 128 bytes
  //  ENABLE=1
  *mpu_rasr =
      (0b1 << 28) | (0b011 << 24) | (0b000110 << 16) | (6 << 1) | 0x1;
```

Let's run the code with a debugger and see what we get this time:

```
MemoryManagement_Handler () at ../../../main.c:53
53    __asm("bkpt 1");
(gdb) p/x *(uint32_t*)0xE000ED28
$3 = 0x1
(gdb) bt
#0  MemoryManagement_Handler () at ../../../main.c:53
#1  <signal handler called>
#2  0x20000000 in s_data ()
#3  0x00000318 in execute_data_array_as_code () at ../../../main.c:46
#4  0x0000037c in main () at ../../../main.c:132
```

You'll notice `MMARVALID` is _not_ set so `MMFAR` is not valid but bit 1 is set, telling us an instruction access violation (`IACCVIOL`) took place. The backtrace clearly shows our array getting executed in frame 2. We've caught the attempted attack!
