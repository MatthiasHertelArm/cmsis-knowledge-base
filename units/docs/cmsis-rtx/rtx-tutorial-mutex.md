---
id: "rtx-tutorial-mutex"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Mutex"
summary: "Mutex stands for “Mutual Exclusion”. In reality, a mutex is a specialized version of semaphore. Like a semaphore, a mutex is a container for tokens."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#mutex"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

Mutex stands for “Mutual Exclusion”. In reality, a mutex is a specialized version of semaphore. Like a semaphore, a mutex is
a container for tokens. The difference is that a mutex can only contain one token which cannot be created or destroyed. The
principle use of a mutex is to control access to a chip resource such as a peripheral. For this reason a mutex token is
binary and bounded. Apart from this it really works in the same way as a semaphore. First of all we must declare the mutex
container and initialize the mutex:

```c
osMutexId_t uart_mutex;
 
osMutexAttr_t {
  const char *name;   ///< name of the mutex
  uint32_t attr_bits; ///< attribute bits
  void *cb_mem;       ///< memory for control block
  uint32_t cb_size;   ///< size of provided memory for control block
};
```

When a mutex is created its functionality can be modified by setting the following attribute bits:

| Bitmask                 | Description |
|-------------------------|-------------|
| osMutexRecursive   | The same thread can consume a mutex multiple times without locking itself.        |
| osMutexPrioInherit | While a thread owns the mutex it cannot be preempted by a higher priority thread. |
| osMutexRobust      | Notify threads that acquire a mutex that the previous owner was terminated.       |

Once declared the mutex must be created in a thread.

```c
uart_mutex = osMutexNew(&MutexAttr);
```

Then any thread needing to access the peripheral must first acquire the mutex token:

```c
osMutexAcquire(osMutexId_t mutex_id,uint32_t ticks);
```

Finally, when we are finished with the peripheral the mutex must be released:

```c
osMutexRelease(osMutexId_t mutex_id);
```

Mutex use is much more rigid than semaphore use, but is a much safer mechanism when controlling absolute access to
underlying chip registers.

#### Exercise 15 - Mutex

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 15 Mutex** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Mutex Caveats

Clearly, you must take care to return the mutex token when you are finished with the chip resource, or you will have
effectively prevented any other thread from accessing it. You must also be extremely careful about using the
osThreadTerminate call on functions which control a mutex token. Keil RTX5 is designed to be a small footprint RTOS
so that it can run on even the very small Cortex-M microcontrollers. Consequently, there is no thread deletion safety. This
means that if you delete a thread which is controlling a mutex token, you will destroy the mutex token and prevent any
further access to the guarded peripheral.
