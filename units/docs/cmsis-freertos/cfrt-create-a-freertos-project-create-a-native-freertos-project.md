---
id: "cfrt-create-a-freertos-project-create-a-native-freertos-project"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project: Create a Native FreeRTOS Project"
summary: "In your IDE, open the Manage software components dialog."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md#create-a-native-freertos-project"
license: "Apache-2.0"
mode: "V"
---

### In the Arm CMSIS Solution extension

In your IDE, open the
[Manage software components](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html#software-components)
dialog.

1. If you cannot see the **RTOS:CORE** component in the **FreeRTOS** variant, select to display **All installed packs**.
2. Select the **RTOS:CORE&FreeRTOS** component. Also, add **RTOS:Config** (**FreeRTOS** variant) and an applicable
   **RTOS:Heap** scheme.
3. **Save** the selection.

(figure: Native FreeRTOS component selection)

### In uVision

- In the Manage Run-Time Environment window, select **::Device:Startup**, **::RTOS:CORE** and
  **::RTOS:Config** in the **FreeRTOS** variant and an applicable **::RTOS:Heap** scheme
  (for more information on the heap schemes, visit the FreeRTOS documentation):

  (figure: Manage RTE FreeRTOS Native)

  \n
- If the **Validation Output** requires other components to be present, try to use the **Resolve** button.
- Click **OK**.

### Configure FreeRTOS

When you have created the native FreeRTOS project, you can configure the real-time operating system
using the **FreeRTOSConfig.h** file. Please refer to the
[FreeRTOS documentation](https://www.freertos.org/a00110.html) for more information on the specific settings.

### Interrupt Priority Configuration

FreeRTOS implements critical sections using the
[BASEPRI](https://developer.arm.com/documentation/dui0552/a/the-cortex-m3-processor/programmers-model/core-registers?lang=en)
register (available in Armv7-M and Armv8-M architecture-based devices) which masks only a subset of interrupts.
This is configured via the `configMAX_SYSCALL_INTERRUPT_PRIORITY` setting. Therefore, it is needed to properly
configure this setting. It is also needed to set appropriate interrupt priorities for interrupt service routines (ISR)
that use RTOS functions. This can especially impact drivers which typically use peripheral interrupts. Normally,
these use the RTOS directly or indirectly through registered callbacks.

Arm Cortex-M cores store interrupt priority values in the most significant bits of the interrupt priority registers
which can have a maximum of eight bits. Many implementations offer only three priority bits. These three bits are
shifted up to be bits five, six and seven respectively. `configMAX_SYSCALL_INTERRUPT_PRIORITY` must not be 0 and can
be xxx00000. This results in the following table:

| configMAX_SYSCALL_INTERRUPT_PRIORITY    | Upper three bits | Priority    |
|:---------------------------------------:|:----------------:|:-----------:|
| 32                                      | 001              | 1 (Highest) |
| 64                                      | 010              | 2           |
| 96                                      | 011              | 3           |
| 128                                     | 100              | 4           |
| 160                                     | 101              | 5           |
| 196                                     | 110              | 6           |
| 224                                     | 111              | 7 (Lowest)  |

#### Example

If you set `configMAX_SYSCALL_INTERRUPT_PRIORITY` to 32, then the priority of an interrupt service routine that uses
RTOS functions must then be higher or equal to 1. This ensures that this interrupt will be masked during a critical section.

A WiFi driver using the SPI interface registers a callback to SPI which is executed in an interrupt context.
The callback function in the WiFi driver uses RTOS functions. Therefore, the SPI interrupt priority must be
set to a value equal or higher to the FreeRTOS preempt priority, for example 1.

> **Note:**
>
> - For a detailed description of how FreeRTOS is using Cortex-M code registers, refer to
>   [Running the RTOS on an ARM Cortex-M Core](https://www.freertos.org/RTOS-Cortex-M3-M4.html).

### Add Event Recorder Visibility

- To use the Event Recorder together with FreeRTOS, add the software component **::Compiler:Event Recorder** to your project.
- Open [FreeRTOSConfig.h](#configure_native_freertos) and
  - verify the header file **freertos_evr.h** is included
  - add Event Recorder configuration definitions (see [Event Recorder Configuration](#configure_evr))
- Call **EvrFreeRTOSSetup()** in your application code (ideally in `main()`).
- If you are using simulation mode, add an initialization file with the following content:
  ```plaintext
  MAP 0xE0001000, 0xE0001007 READ WRITE
  signal void DWT_CYCCNT (void) {
  while (1) {
    rwatch(0xE0001004);
    _WWORD(0xE0001004, states);
    }
  }
  DWT_CYCCNT()
  ```
- Build the application code and download it to the debug hardware or run it in simulation.

Once the target application generates event information, it can be viewed in the µVision debugger using the **Event Recorder**.
