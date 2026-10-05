---
id: "intr-a-guide-to-using-arm-stack-limit-r-implementing-the-limit-registers"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: Implementing the Limit Registers"
summary: "For an implementation example on the DA1469x, you can access this at Renesas's Github [^ARMV8_Guards]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#implementing-the-limit-registers"
license: "CC-BY-SA-4.0"
mode: "V"
---

For an implementation example on the DA1469x, you can access this at Renesas's
Github [^ARMV8_Guards].

### Initializing the MSPLIM Register

We use the MSR instruction to write to these registers, which requires us to be
in privileged mode. In this case, we will set the MSP Limit in the
Reset_Handler:

```c
Reset_Handler:

        ldr     r0, =__StackLimit
        add     r0, r0, #dg_configMSP_PADDING
        msr     MSPLIM, r0
```

Specifically to the DA1469x, we also need to place the same initialization in
the Wakeup_Reset_Handler:

```c
Wakeup_Reset_Handler:

    ldr     r0, =__StackLimit
    add     r0, r0, #dg_configMSP_PADDING
    msr     MSPLIM, r0

```

The DA1469x sleep architecture doesn't pertain to all Cortex-M33 architectures.
After initialization, the DA1469x replaces the Reset_Handler with the
Wakeup_Reset_Handler to handle the restoration of Cortex-M33 registers.

There are two definitions provided elsewhere in the project. \_\_StackLimit is
defined in vector_table_da1469x.S:

```c
.section .stack
                .align  3
                .globl  __StackTop
                .globl  __StackLimit
__StackLimit:
                .space  Stack_Size
                .size   __StackLimit, . - __StackLimit
__StackTop:
                .size   __StackTop, . - __StackTop
```

This definition helps us find the stack limit for setting the MSP.

We also added padding to this value. You will find this value in a configuration
file:

```c
#define dg_configMSP_PADDING                    (16)
```

When the MSPLIM is equal to the MSP, the UsageFault exception is triggered. The
padding is required to enable pushing items to the stack on Exception entry. If
we don't make space for the fault handler, nested exceptions can occur as the
MSPLIM register would be continuously exceeded, usually resulting in a LOCKUP.

The alternative would be to use a naked function[^gcc_attributes]. However, I
prefer to add padding as it provides more flexibility in the fault handler and
allows for Memfault hooks!

### Initializing the PSPLIM Register

On the DA1469x SDK, it makes use of FreeRTOS. The psp is used for each task's
stack so we can set up the PSPLIM register to protect against a task overflow.
This implementation is superior to FreeRTOS's stack overflow check[^1] for the
following reasons:

1.  FreeRTOS only checks the watermark on a context switch. Therefore, if a
    thread overflows the stack and isn't yielding, it can corrupt memory, access
    null pointers, etc.

2.  FreeRTOS does not recommend using this feature in production environments
    because of the context switch overhead[^2].

Implementing this is more straightforward. First, we must adjust the PSPLIM
during a context switch in FreeRTOS.

In tasks.c we create the following above vTaskSwitchContext:

```c
void vTaskSwitchStackGuard(void)
{
    volatile uint32_t end_of_stack_val = (uint32_t)pxCurrentTCB->pxStack;
     __set_PSPLIM( end_of_stack_val);
}
```

Next, we add the call immediately after the context switch:

```c
void xPortPendSVHandler( void ){

...

"   bl vTaskSwitchContext               \n"
"   bl vTaskSwitchStackGuard                        \n"

...
}
```

That's all we need to do for the PSP.

### Setting up the UsageFault_Handler

All that's left is doing some work in the UsageFault_Handler. We will declare
the UsageFault_Handler in exceptions_handler.s and call a separate handler
afterward.

First, we declare an application handler:

```c
__RETAINED_CODE void UsageFault_HandlerC(uint8_t stack_pointer_mask)
{

    volatile uint16_t usage_fault_status_reg __UNUSED;

    usage_fault_status_reg = (SCB->CFSR &         SCB_CFSR_USGFAULTSR_Msk) >> SCB_CFSR_USGFAULTSR_Pos;

    hw_watchdog_freeze();

    if(usage_fault_status_reg & (SCB_CFSR_STKOF_Msk >> SCB_CFSR_USGFAULTSR_Pos))
    {

        while(1){}
    }

        while (1) {}
}

```

Next, let's add our UsageFault_Handler into the exceptions_handler.S:

```c
#if (dg_configCODE_LOCATION == NON_VOLATILE_IS_FLASH)
            .section text_retained
#endif
    .align  2
    .thumb
    .thumb_func
    .globl  UsageFault_Handler
    .type   UsageFault_Handler, %function
UsageFault_Handler:
    ldr     r2,=UsageFault_HandlerC
    mrs     r1, msp
    mrs     r0, MSPLIM
    cmp     r0, r1
    beq     UsageFault_with_MSP_Overflow
    mrs     r1, psp
    mrs     r0, PSPLIM
    cmp     r0, r1
    beq     UsageFault_with_PSP_Overflow
    mov     r0, #0
    bx      r2
UsageFault_with_PSP_Overflow:
    mov     r0, #2
    bx      r2
UsageFault_with_MSP_Overflow:
    ldr     r1, =__StackLimit
    msr     MSPLIM, r1
    mov     r0, #1
    bx      r2
```

Since the USFR does not indicate if the psp or the msp caused the fault, I
decided to add some detection in assembly. I prefer doing this in assembly to
ensure no stack pushes before the application handler call.

- 0 - General UsageFault
- 1 - MSP Overflow
- 2 - PSP Overflow (Task Overflow)

In this function, we are checking the MSP and the PSP registers against the
limit registers. If the MSP matches the MSPLIM register, we restore the MSPLIM
to `__StackLimit` (Removing the padding we placed initially) and then call our
application fault handler.

### Testing our Implementation

We need a small piece of code to test the implementation. In our example, there
is a macro provided for causing an overflow for the MSP or the PSP:

```c
#define TOGGLE_MSP_OVERFLOW (0)     //0 Creates an application overflow in FreeRTOS task, 1 creates it on the MSP
```

When the button is pressed, depending on this macro setting, it calls a
recursive function either in interrupt context or in our main task.

```c
static void test_overflow_func(void)
{
        test_overflow_func();
}

static void _wkup_key_cb(void)
{
    BaseType_t need_switch;
    /* Clear the WKUP interrupt flag!!! */
    hw_wkup_reset_interrupt();

#if TOGGLE_MSP_OVERFLOW > 0
    test_overflow_func();
#endif


    xTaskNotifyFromISR(overFlow_handle, BUTTON_PRESS_NOTIF, eSetBits, &need_switch);
    portEND_SWITCHING_ISR(need_switch);
}

...

void prvTestOverFlowTask( void *pvParameters )
{
    _wkup_init();

    overFlow_handle = xTaskGetCurrentTaskHandle();

    for ( ;; ) {
        uint32_t notif;
        /*
        * Wait on any of the notification bits, then clear them all
        */
        xTaskNotifyWait(0, 0xFFFFFFFF, &notif, portMAX_DELAY);

        /* Notified from BLE manager? */
        if (notif & BUTTON_PRESS_NOTIF) {
                test_overflow_func();
        }
    }
}
```

After pressing the button, we should see the UsageFault_HandlerC get called in
our application code.
