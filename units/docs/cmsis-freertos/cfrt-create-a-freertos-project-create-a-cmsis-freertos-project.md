---
id: "cfrt-create-a-freertos-project-create-a-cmsis-freertos-project"
type: "concept"
domain: "rtos"
title: "Create a FreeRTOS Project: Create a CMSIS-FreeRTOS Project"
summary: "In your IDE, open the Manage software components dialog."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/create_project.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/create_project.md#create-a-cmsis-freertos-project"
license: "Apache-2.0"
mode: "V"
---

### CMSIS-FreeRTOS in the Arm CMSIS Solution extension

In your IDE, open the
[Manage software components](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html#software-components)
dialog.

1. If you cannot see the **CMSIS:RTOS2 (API):FreeRTOS**, select to display **All installed packs**.
2. Select the **CMSIS:RTOS2 (API):FreeRTOS** component.
3. Also, add **RTOS:Config** (**CMSIS RTOS2** variant), **RTOS:Timers**, **RTOS:Event Groups**, and an applicable
   **RTOS:Heap** scheme.
4. **Save** the selection.

(figure: CMSIS-FreeRTOS component selection)

### CMSIS-FreeRTOS in uVision

- In the Manage Run-Time Environment window, select **::Device:Startup**, **::CMSIS::RTOS2 (API)::FreeRTOS**,
  **::RTOS:CORE** in the **FreeRTOS** variant, **::RTOS:Config** in the **CMSIS RTOS2** variant, **::RTOS:Timers**,
  **::RTOS:Event Groups**, and an applicable **::RTOS:Heap** scheme (for more information on the heap schemes,
  visit the FreeRTOS documentation):

  (figure: Manage RTE FreeRTOS RTOS2)

  \n
- If the **Validation Output** requires other components to be present, try to use the **Resolve** button.
- Click **OK**.

### Configure CMSIS-FreeRTOS

When you have created the CMSIS-FreeRTOS project, you can configure the real-time operating system using the **FreeRTOSConfig.h** file. It can be opened using the Configuration Wizard view:

(figure: FreeRTOS Config H CMSIS RTOS)

The following main settings are available:

| Name                           | Configuration define                 | Description                                                           |
|--------------------------------|--------------------------------------|-----------------------------------------------------------------------|
| Minimal stack size [words]     | configMINIMAL_STACK_SIZE             | Stack for idle task and default task stack in words.                  |
| Total heap size [bytes]        | configTOTAL_HEAP_SIZE                | Heap memory size in bytes.                                            |
| Kernel tick frequency [Hz]     | configTICK_RATE_HZ                   | Kernel tick rate in Hz.                                               |
| Timer task stack depth [words] | configTIMER_TASK_STACK_DEPTH         | Stack for timer task in words.                                        |
| Timer task priority            | configTIMER_TASK_PRIORITY            | Timer task priority.                                                  |
| Timer queue length             | configTIMER_QUEUE_LENGTH             | Timer command queue length.                                           |
| Preemption interrupt priority  | configMAX_SYSCALL_INTERRUPT_PRIORITY | Maximum priority of interrupts that are safe to call FreeRTOS API.    |
| Use time slicing               | configUSE_TIME_SLICING               | Enable setting to use time slicing.                                   |
| Use tickless idle              | configUSE_TICKLESS_IDLE              | Enable low power tickless mode that stops tick interrupt when idle.   |
| Idle should yield              | configIDLE_SHOULD_YIELD              | Control Yield behavior of the idle task.                              |
| Check for stack overflow       | configCHECK_FOR_STACK_OVERFLOW       | Enable or disable stack overflow checking.                            |
| Use idle hook                  | configUSE_IDLE_HOOK                  | Enable callback function call on each idle task iteration.            |
| Use tick hook                  | configUSE_TICK_HOOK                  | Enable callback function call during each tick interrupt.             |
| Use daemon task startup hook   | configUSE_DAEMON_TASK_STARTUP_HOOK   | Enable callback function call when timer service starts.              |
| Use malloc failed hook         | configUSE_MALLOC_FAILED_HOOK         | Enable callback function call when out of dynamic memory.             |
| Queue registry size            | configQUEUE_REGISTRY_SIZE            | Define maximum number of queue objects registered for debug purposes. |

> **Note**
>
> - Refer to [Interrupt Priority Configuration](#interrupt_priority_config) for more information on the usage of `configMAX_SYSCALL_INTERRUPT_PRIORITY`.

#### Event Recorder Configuration

The following settings are available (see [Event Recorder Configuration](#configure_evr) for details):

| Name                           | Configuration define                 | Description                                                                             |
|--------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------|
| Initialize Event Recorder      | configEVR_INITIALIZE                 | Initialize Event Recorder before FreeRTOS kernel start.                                 |
| Setup recording level filter   | configEVR_SETUP_LEVEL                | Enable configuration of FreeRTOS events recording level.                                |
| Task functions                 | configEVR_LEVEL_TASKS                | Define event recording level bitmask for events generated from Tasks functions.         |
| Queue functions                | configEVR_LEVEL_QUEUE                | Define event recording level bitmask for events generated from Queue functions.         |
| Timer functions                | configEVR_LEVEL_TIMERS               | Define event recording level bitmask for events generated from Timer functions.         |
| Event Groups functions         | configEVR_LEVEL_EVENTGROUPS          | Define event recording level bitmask for events generated from Event Groups functions.  |
| Heap functions                 | configEVR_LEVEL_HEAP                 | Define event recording level bitmask for events generated from Heap functions.          |
| Stream Buffer functions        | configEVR_LEVEL_STREAMBUFFER         | Define event recording level bitmask for events generated from Stream Buffer functions. |

#### Memory Allocation Configuration

The following settings are available:

| Name                                   | Configuration define                 | Description                                                                        |
|----------------------------------------|--------------------------------------|------------------------------------------------------------------------------------|
| Support static memory allocation       | configSUPPORT_STATIC_ALLOCATION      | Enable or disable support for static memory allocation.                            |
| Support dynamic memory allocation      | configSUPPORT_DYNAMIC_ALLOCATION     | Enable or disable support for dynamic memory allocation.                           |
| Use kernel provided static memory      | configKERNEL_PROVIDED_STATIC_MEMORY  | When enabled, FreeRTOS kernel provides static memory for Idle and Timer tasks.     |
| Use application allocated heap         | configAPPLICATION_ALLOCATED_HEAP     | When enabled, application must provide heap buffer externally.                     |
| Use separate heap for stack allocation | configSTACK_ALLOCATION_FROM_SEPARATE_HEAP | Enable or disable stack allocation for any task from a separate heap.         |
| Use heap protector                     | configENABLE_HEAP_PROTECTOR          | Enable or disable bounds checking and obfuscation to heap block pointers.          |

#### Port Specific Configuration

The following settings are available:

| Name                              | Configuration define           | Description                                                                        |
|-----------------------------------|--------------------------------|------------------------------------------------------------------------------------|
| Use Floating Point Unit           | configENABLE_FPU                | Enable or disable support for FPU when switching execution context.                |
| Use M-Profile Vector Extension    | configENABLE_MVE                | Enable or disable support for MVE when switching execution context.                |
| Use Memory Protection Unit        | configENABLE_MPU                | Enable or disable support for MPU on ARMv8-M MPU enabled ports.                    |
| Use TrustZone Secure Side Only    | configRUN_FREERTOS_SECURE_ONLY  | Enable this setting when FreeRTOS runs on the Secure side only.                    |
| Use TrustZone Security Extension  | configENABLE_TRUSTZONE          | Enable TrustZone when FreeRTOS runs on the Non-Secure side and calls functions from the Secure side.|
| Minimal secure stack size [words] | configMINIMAL_SECURE_STACK_SIZE | Stack for idle task Secure side context in words.                                  |

#### Interrupt Controller Configuration

**Note:** Settings related to interrupt controller are relevant only on ARMv7-A ports where it is necessary to configure Arm Generic Interrupt Controller (GIC).

The following settings are available:

| Name                                      | Configuration define                           | Description                                                   |
|-------------------------------------------|------------------------------------------------|---------------------------------------------------------------|
| Interrupt controller base address         | configINTERRUPT_CONTROLLER_BASE_ADDRESS         | Sets the base address of the interrupt controller peripheral. |
| Interrupt controller CPU interface offset | configINTERRUPT_CONTROLLER_CPU_INTERFACE_OFFSET | Sets the offset from interrupt controller base address at which the CPU interface starts.          |
| Interrupt controller unique priorities    | configUNIQUE_INTERRUPT_PRIORITIES               | Sets the number of unique priorities that can be specified in the interrupt controller peripheral. |

#### Symmetric Multiprocessing Configuration

**Note:** Symmetric Multiprocessing Configuration (SMP) settings are only relevant if FreeRTOS port implementation supports SMP.

The following settings are available:

| Name                        | Configuration define        | Description                                                      |
|-----------------------------|-----------------------------|------------------------------------------------------------------|
| Number of processor cores   | configNUMBER_OF_CORES       | Sets the number of available processor cores.                    |
| Use processor core affinity | configUSE_CORE_AFFINITY     | Enables the control for task to run on specific processor cores. |
| Use passive idle hook       | configUSE_PASSIVE_IDLE_HOOK | Enable callback function call on each idle task iteration.       |

### Add Event Recorder Visibility

- To use the Event Recorder together with FreeRTOS, add the software component **::Compiler:Event Recorder** to your project.
- Open [FreeRTOSConfig.h](#configure_cmsis_freertos) and
  - verify the header file **freertos_evr.h** is included
  - modify Event Recorder configuration definitions (see [Event Recorder Configuration](#configure_evr)) to change default configuration
- Call **osKernelInitialize()** in your application code (ideally in `main()`) to setup Event Recorder according to configuration settings.
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

Once the target application generates event information, it can be viewed in the µVision debugger
using the **Event Recorder**.
