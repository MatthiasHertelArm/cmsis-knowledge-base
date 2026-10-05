---
id: "intr-a-guide-to-using-arm-stack-limit-r-limitations-and-further-improvements"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: Limitations and Further Improvements"
summary: "The MSPLIM and PSPLIM registers will help against most stack overflows. Unfortunately, they do not protect us from local buffers corrupting the stack. We will look at the most common; buffer overflow."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#limitations-and-further-improvements"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MSPLIM and PSPLIM registers will help against most stack overflows.
Unfortunately, they do not protect us from local buffers corrupting the stack.
We will look at the most common; buffer overflow. A buffer overflow occurs when
a fixed buffer is allocated on the stack, and the program starts writing to
memory addresses outside this boundary. This results in corrupted data and can
even change the return address of a function, causing undesired execution of
application code.

There are different ways to handle this condition on other architectures. For
example, Zephyr uses the MPU to guard the PSP on each thread. Here, we will
discuss stack canaries.

### Stack Canary

Stack Canaries are widely implemented as a means of code hardening. A function
will place a value (canary) on the end of a stack frame and will check the value
is intact before it returns. This mechanism protects against buffer overflow
attacks, where malicious source code could overflow the buffer to redirect the
return address to its function.

This same idea can also be used to guard against buffer overflows in our
application.

### FreeRTOS Buffer Overflow protection

FreeRTOS implements a means for overflow detection, as discussed in
[Initializing the PSPLIM Register](#initializing-the-psplim-register). This uses
the concept of a canary, which will periodically check the value during a
context switch.

FreeRTOS has two different configurations that follow this concept:

```c
#if( ( configCHECK_FOR_STACK_OVERFLOW > 1 ) && ( portSTACK_GROWTH < 0 ) )

    #define taskCHECK_FOR_STACK_OVERFLOW()                                                              \
    {                                                                                                   \
        const uint32_t * const pulStack = ( uint32_t * ) pxCurrentTCB->pxStack;                         \
        const uint32_t ulCheckValue = ( uint32_t ) 0xa5a5a5a5;                                          \
                                                                                                        \
        if( ( pulStack[ 0 ] != ulCheckValue ) ||                                                \
            ( pulStack[ 1 ] != ulCheckValue ) ||                                                \
            ( pulStack[ 2 ] != ulCheckValue ) ||                                                \
            ( pulStack[ 3 ] != ulCheckValue ) )                                             \
        {                                                                                               \
            vApplicationStackOverflowHook( ( TaskHandle_t ) pxCurrentTCB, pxCurrentTCB->pcTaskName );   \
        }                                                                                               \
    }

#endif /* #if( configCHECK_FOR_STACK_OVERFLOW > 1 ) */
/*-----------------------------------------------------------*/

#if( ( configCHECK_FOR_STACK_OVERFLOW > 1 ) && ( portSTACK_GROWTH > 0 ) )

    #define taskCHECK_FOR_STACK_OVERFLOW()                                                                                              \
    {                                                                                                                                   \
    int8_t *pcEndOfStack = ( int8_t * ) pxCurrentTCB->pxEndOfStack;                                                                     \
    static const uint8_t ucExpectedStackBytes[] = { tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE,     \
                                                    tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE,     \
                                                    tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE,     \
                                                    tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE,     \
                                                    tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE, tskSTACK_FILL_BYTE };   \
                                                                                                                                        \
                                                                                                                                        \
        pcEndOfStack -= sizeof( ucExpectedStackBytes );                                                                                 \
                                                                                                                                        \
        /* Has the extremity of the task stack ever been written over? */                                                               \
        if( memcmp( ( void * ) pcEndOfStack, ( void * ) ucExpectedStackBytes, sizeof( ucExpectedStackBytes ) ) != 0 )                   \
        {                                                                                                                               \
            vApplicationStackOverflowHook( ( TaskHandle_t ) pxCurrentTCB, pxCurrentTCB->pcTaskName );                                   \
        }                                                                                                                               \
    }

#endif /* #if( configCHECK_FOR_STACK_OVERFLOW > 1 ) */
```

Both methods check for an expected value at the end of the stack. If this value
is overwritten, then vApplicationStackOverflowHook is called, and the
application should record and reset. Unfortunately, the periodicity is
non-deterministic, as it relies on a context switch. Periodic checks lead to a
race condition when a task doesn't yield in time. You can test this from the
previous example by setting the following:

```c
#define dg_configARMV8_USE_STACK_GUARDS         (0)
#define #define TOGGLE_MSP_OVERFLOW             (0)
```

In this example, prvTestOverFlowTask will not yield, so FreeRTOS does not catch
this condition.

### Compiler Enabled Overflow Detection

Compilers have started enabling SSP (Stack Smashing Protection) libraries. The
library options will allow the compiler to use canaries within function calls.
We're going to look at GCC's implementation[^5] specifically. GCC provides the
following compiler flags:

- **-fstack-protector**: This includes functions that call **alloca** and
  functions with buffers larger than or equal to 8 bytes. The guards are
  initialized when a function is entered and then checked when the function
  exits.

- **-fstack-protector-strong** - Like -fstack-protector but includes additional
  functions to be protected — those that have local array definitions, or have
  references to local frame addresses.

- **-fstack-protector-all**: all functions are protected.

- **-fstack-protector-explicit**: protects those functions which have the
  stack_protect attribute

### GCC SSP Example

Let's take a look at using the ssp library in GCC. First, let's add the compiler
flag from the previous example: -fstack-protector. The ssp library has two
externs that we define as follows.

```c
uint32_t__stack_chk_guard = 0xDEADBEEF;

void __stack_chk_fail(void) { /* will be called if guard/canary gets corrupted */

    __ASM volatile ("cpsid i" : : : "memory");

    hw_watchdog_freeze();                           // Stop WDOG
    while(1){}
}
```

Let's also add the vulnerability in our application and add it to the
prvTestOverFlowTask:

```c
__attribute__((optimize("O0"))) static uint8_t stack_buffer_test(uint16_t iters)
{
    uint8_t buffer[16];
    uint16_t i;

    for(i = 0; i < iters; i++)
    {
            buffer[i] = 0xaa;
    }

    return buffer[8];
}

```

> **NOTE:** \_\_stack_chk_guard should be randomized on startup if using ssp for
> security reasons.

This function has a fixed buffer to pass a value larger than the local buffer.
Let's add a stack_buffer_test(17) to our task and look at the assembly.

```
(gdb) disassemble stack_buffer_test
Dump of assembler code for function stack_buffer_test:
   0x0000ccc8 <+0>: push    {r7, lr}
   0x0000ccca <+2>: sub sp, #32
   0x0000cccc <+4>: add r7, sp, #0
   0x0000ccce <+6>: mov r3, r0
   0x0000ccd0 <+8>: strh    r3, [r7, #6]
   0x0000ccd2 <+10>:    ldr r3, [pc, #68]   ; (0xcd18 <stack_buffer_test+80>)
   0x0000ccd4 <+12>:    ldr r3, [r3, #0]
   0x0000ccd6 <+14>:    str r3, [r7, #28]
   0x0000ccd8 <+16>:    mov.w   r3, #0
   0x0000ccdc <+20>:    movs    r3, #0
   0x0000ccde <+22>:    strh    r3, [r7, #10]
   0x0000cce0 <+24>:    b.n 0xccf4 <stack_buffer_test+44>
   0x0000cce2 <+26>:    ldrh    r3, [r7, #10]
   0x0000cce4 <+28>:    adds    r3, #32
   0x0000cce6 <+30>:    add r3, r7
   0x0000cce8 <+32>:    movs    r2, #170    ; 0xaa
   0x0000ccea <+34>:    strb.w  r2, [r3, #-20]
   0x0000ccee <+38>:    ldrh    r3, [r7, #10]
   0x0000ccf0 <+40>:    adds    r3, #1
   0x0000ccf2 <+42>:    strh    r3, [r7, #10]
   0x0000ccf4 <+44>:    ldrh    r2, [r7, #10]
   0x0000ccf6 <+46>:    ldrh    r3, [r7, #6]
   0x0000ccf8 <+48>:    cmp r2, r3
   0x0000ccfa <+50>:    bcc.n   0xcce2 <stack_buffer_test+26>
   0x0000ccfc <+52>:    ldrb    r3, [r7, #20]
   0x0000ccfe <+54>:    ldr r2, [pc, #24]   ; (0xcd18 <stack_buffer_test+80>)
   0x0000cd00 <+56>:    ldr r1, [r2, #0]
   0x0000cd02 <+58>:    ldr r2, [r7, #28]
   0x0000cd04 <+60>:    eors    r1, r2
   0x0000cd06 <+62>:    mov.w   r2, #0
   0x0000cd0a <+66>:    beq.n   0xcd10 <stack_buffer_test+72>
   0x0000cd0c <+68>:    bl  0xcdb0 <__stack_chk_fail>
   0x0000cd10 <+72>:    mov r0, r3
   0x0000cd12 <+74>:    adds    r7, #32
   0x0000cd14 <+76>:    mov sp, r7
   0x0000cd16 <+78>:    pop {r7, pc}
   0x0000cd18 <+80>:    strh    r4, [r6, #44]   ; 0x2c
   0x0000cd1a <+82>:    movs    r0, #0

```

Here we can see the compiler loading the canary at the end of the stack frame:

```
   0x0000ccd2 <+10>:    ldr r3, [pc, #68]   ; (0xcd18 <stack_buffer_test+80>)
   0x0000ccd4 <+12>:    ldr r3, [r3, #0]
   0x0000ccd6 <+14>:    str r3, [r7, #28]

(gdb) x /1a 0xcd18
0xcd18 <stack_buffer_test+80>:  0x200085b4 <__stack_chk_guard>
(gdb) x /1a 0x200085b4
0x200085b4 <__stack_chk_guard>: 0xdeadbeef
```

Before return, we can see the function checking the canary at the end of the
stack frame and calling \_\_stack_chk_fail if the value is corrupted:

```c
0x0000cd0a <+66>:   beq.n   0xcd10 <stack_buffer_test+72>
0x0000cd0c <+68>:   bl  0xcdb0 <__stack_chk_fail>
```

Running the rest of the example should confirm the call of \_\_stack_chk_fail.
