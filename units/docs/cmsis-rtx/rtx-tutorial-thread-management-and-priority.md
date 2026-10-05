---
id: "rtx-tutorial-thread-management-and-priority"
type: "concept"
domain: "rtos"
title: "tutorial: Thread Management and Priority"
summary: "When a thread is created it is assigned a priority level. The RTOS scheduler uses a thread’s priority to decide which thread should be scheduled to run."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#thread-management-and-priority"
license: "Apache-2.0"
mode: "V"
---

When a thread is created it is assigned a priority level. The RTOS scheduler uses a thread’s priority to decide which thread should be scheduled to run. If a number of threads are ready to run, the thread with the highest priority will be placed in the run state. If a high priority thread becomes ready to run it will preempt a running thread of lower priority.

Importantly, a high priority thread running on the CPU will not stop running unless it blocks on an RTOS API call or is preempted by a higher priority thread. A thread's priority is defined in the thread structure and the following priority definitions are available. The default priority is `osPriorityNormal`. The osPriority_t value specifies the priority for a thread.

Once the threads are running, there are a small number of RTOS system calls which are used to manage the running threads. It is also then possible to elevate or lower a thread’s priority either from another function or from within its own code.

```c
osStatus   osThreadSetPriority(threadID, priority);
osPriority osThreadGetPriority(threadID);
```

As well as creating threads, it is also possible for a thread to delete another active thread from the RTOS. Again, we use the thread ID rather than the function name of the thread.

```c
osStatus = osThreadTerminate (threadID1);
```

If a thread wants to terminate itself then there is a dedicated exit function.

```c
osThreadExit (void)
```

Finally, there is a special case of thread switching where the running thread passes control to the next ready thread of the same priority. This is used to implement a third form of scheduling called co-operative thread switching.

```c
osStatus osThreadYield();      //switch to next ready to run thread at the same priority
```
