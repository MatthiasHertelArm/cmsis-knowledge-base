---
id: "rtx-tutorial-memory-management"
type: "concept"
domain: "rtos"
title: "tutorial: Memory Management"
summary: "When each thread is created, it is assigned its own stack for storing data during the context switch."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#memory-management"
license: "Apache-2.0"
mode: "V"
---

When each thread is created, it is assigned its own stack for storing data during the context switch. This should not be confused with the native Cortex-M processor stack; it is really a block of memory that is allocated to the thread.

A default stack size is defined in the RTOS configuration file (we will see this later) and this amount of memory will be allocated to each thread unless we override it to allocate a custom size. The default stack size will be assigned to a thread if the stack size value in the thread definition structure is set to zero. If necessary a thread can be given additional memory resources by defining a bigger stack size in the thread structure.

Keil RTX5 supports several memory models to assign this thread memory. The default model is a global memory pool. In this model each RTOS object that is created (threads, message queues, semaphores etc.) are allocated memory from a single block of memory.

If an object is destroyed the memory it has been assigned is returned to the memory pool. This has the advantage of memory reuse but also introduces the possible problem of memory fragmentation.

The size of the global memory pool is defined in the configuration file:

```c
#define OS_DYNAMIC_MEM_SIZE         4096
```

And the default stack size for each thread is defined in the threads section:

```c
#define OS_STACK_SIZE               256
```

It is also possible to define object specific memory pools for each different type of RTOS object. In this model you define the maximum number of a specific object type and its memory requirements. The RTOS then calculates and reserves the required memory usage.

The object specific model is again defined in the RTOS configuration file by enabling the "object specific memory" option provided in each section of the configuration file:

```c
#define OS_SEMAPHORE_OBJ_MEM        1
#define OS_SEMAPHORE_NUM            1
```

In the case of simple object which requires a fixed memory allocation we just need to define the maximum number of a given object type. In the case of more complex objects such as threads we will need to define the required memory usage:

```c
#define OS_THREAD_OBJ_MEM           1
#define OS_THREAD_NUM               1
#define OS_THREAD_DEF_STACK_NUM     0
#define OS_THREAD_USER_STACK_SIZE   1024
```

To use the object specific memory allocation model with threads we must provide details of the overall thread memory usage.

Finally it is possible to statically allocate the thread stack memory. This is important for safety related systems where memory usage has to be rigorously defined.

### Exercise 3 - Memory Model

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 03 Memory Model** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
