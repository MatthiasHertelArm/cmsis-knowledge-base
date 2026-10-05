---
id: "rtx-configure-rtx-v5-thread-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Thread Configuration"
summary: "The RTX5 provides several parameters to configure the CMSISRTOSThreadMgmt functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#thread-configuration"
license: "Apache-2.0"
mode: "V"
---

The RTX5 provides several parameters to configure the CMSIS_RTOS_ThreadMgmt functions.

**Thread Configuration Options**

(figure: RTX_Config.h: Thread Configuration)

Option                                          | \#define               | Description
:--------------------------------------------------------------------------|:-------------------------------|:---------------------------------------------------------------
Object specific Memory allocation               | `OS_THREAD_OBJ_MEM`   | Enables object specific memory allocation. See ObjectMemoryPool.
Number of user Threads                          | `OS_THREAD_NUM`       | Defines maximum number of user threads that can be active at the same time. Applies to user threads with system provided memory for control blocks. Default value is `1`. Value range is `[1-1000]`.
Number of user Threads with default Stack size  | `OS_THREAD_DEF_STACK_NUM`     | Defines maximum number of user threads with default stack size and applies to user threads with `0` stack size specified. Value range is `[0-1000]`.
Total Stack size [bytes] for user Threads with user-provided Stack size    | `OS_THREAD_USER_STACK_SIZE` | Defines the combined stack size for user threads with user-provided stack size. Default value is `0`. Value range is `[0-1073741824]` Bytes, in multiples of `8`.
Default Thread Stack size [bytes]               | `OS_STACK_SIZE`    | Defines stack size for threads with zero stack size specified. Default value is `3072`. Value range is `[96-1073741824]` Bytes, in multiples of `8`.
Idle Thread Stack size [bytes]                  | `OS_IDLE_THREAD_STACK_SIZE`  | Defines stack size for Idle thread. Default value is `512`. Value range is `[72-1073741824]` bytes, in multiples of `8`.
Idle Thread TrustZone Module ID                 | `OS_IDLE_THREAD_TZ_MOD_ID`   | Defines the TrustZone Module ID the Idle Thread shall use. This needs to be set to a non-zero value if the Idle Thread need to call secure functions. Default value is `0`.
Idle Thread Safety Class                        | `OS_IDLE_THREAD_CLASS`       | Defines the the Safety Class for the Idle thread. Applied only if Safety Class functionality is enabled in systemConfig. Default value is `0`.
Idle Thread Zone                                | `OS_IDLE_THREAD_ZONE`        | Defines the MPU Protected Zone for the Idle thread. Applied only if MPU protected Zone functionality is enabled in systemConfig. Default value is `0`.
Stack overrun checking                          | `OS_STACK_CHECK`             | Enable stack overrun checks at thread switch.
Stack usage watermark                           | `OS_STACK_WATERMARK`         | Initialize thread stack with watermark pattern for analyzing stack usage. Enabling this option increases significantly the execution time of thread creation.
Processor mode for Thread execution             | `OS_PRIVILEGE_MODE`          | Controls the default processor mode when not specified through thread attributes osThreadUnprivileged or osThreadPrivileged. Default value is `Privileged` mode. Value range is `[0=Unprivileged; 1=Privileged]` mode.

### Configuration of Thread Count and Stack Space

The RTX5 kernel uses a separate stack space for each thread and provides two methods for defining the stack requirements:

- **Static allocation**: when osThreadAttr_t::stack_mem and osThreadAttr_t::stack_size specify a memory area
  which is used for the thread stack. **Attention**: The stack memory provided must be 64-bit aligned, i.e. by using uint64_t for declaration.
- **Dynamic allocation**: when osThreadAttr_t is NULL or osThreadAttr_t::stack_mem is NULL, the system
  allocates the stack memory from:
  - Object-specific Memory Pool (default Stack size) when "Object specific Memory allocation" is enabled and "Number of
    user Threads with default Stack size" is not `0` and osThreadAttr_t::stack_size is `0` (or
    osThreadAttr_t is NULL).
  - Object-specific Memory Pool (user-provided Stack size) when "Object specific Memory allocation" is enabled and "Total
    Stack size for user..."  is not `0` and osThreadAttr_t::stack_size is not `0`.
  - Global Memory Pool when "Object specific Memory allocation" is disabled or (osThreadAttr_t::stack_size is not
    `0` and "Total Stack size for user..." is `0`) or (osThreadAttr_t::stack_size is `0` and
    "Number of user Threads with default Stack size" is `0`).

osThreadAttr_t is a parameter of the function osThreadNew.

> **Note**
>
> - Before the RTX kernel is started by the osKernelStart function, the main stack defined in startup__device_.s is used.
>   The main stack is also used for:
>   - user application calls to RTX functions in **thread mode** using SVC calls
>   - interrupt/exception handlers.
### Stack Overflow Checking

RTX5 implements a software stack overflow checking that traps stack overruns. Stack is used for return addresses and automatic variables. Extensive usage or incorrect stack configuration may cause a stack overflow. Software stack overflow checking is controlled with the define `OS_STACK_CHECK`.

If a stack overflow is detected, the function osRtxErrorNotify with error code osRtxErrorStackOverflow is called. By default, this function is implemented as an endless loop and will practically stop code execution.
### Stack Usage Watermark

RTX5 initializes thread stack with a watermark pattern (0xCC) when a thread is created. This allows the debugger to determine the maximum stack usage for each thread. It is typically used during development but removed from the final application. Stack usage watermark is controlled with the define `OS_STACK_WATERMARK`.

Enabling this option significantly increases the execution time of osThreadNew (depends on thread stack size).
### Processor Mode for Thread Execution

RTX5 allows to execute threads in unprivileged or privileged processor mode. The processor mode is configured for all threads with the define `OS_PRIVILEGE_MODE`.

It is also possible to specify the privilege level for individual threads. For that use osThreadUnprivileged and osThreadPrivileged defines in the *attr_bits* of osThreadAttr_t argument when creating a thread with osThreadNew.

In **unprivileged** processor mode, the application software:

- has limited access to the MSR and MRS instructions, and cannot use the CPS instruction.
- cannot access the system timer, NVIC, or system control block.
- might have restricted access to memory or peripherals.

In **privileged** processor mode, the application software can use all the instructions and has access to all resources.
