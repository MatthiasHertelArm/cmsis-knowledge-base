---
id: "rtx-tutorial-threads"
type: "concept"
domain: "rtos"
title: "tutorial: Threads"
summary: "The building blocks of a typical 'C' program are functions which we call to perform a specific procedure and which then return to the calling function. In CMSIS-RTOS2, the basic unit of execution is a \"Thread\"."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#threads"
license: "Apache-2.0"
mode: "V"
---

The building blocks of a typical 'C' program are functions which we call to perform a specific procedure and which then return to the calling function. In CMSIS-RTOS2, the basic unit of execution is a "Thread". A Thread is very similar to a 'C' procedure but has some very fundamental differences.

```c
unsigned int procedure (void) {
  ...
    return(ch);
}
 
void thread (void) {
  while(1) {
    ...
    }
}
 
__NO_RETURN void Thread1(void*argument) {
  while(1) {
    ...
  }
}
```

While we always return from our 'C' function, once started an RTOS thread must contain a loop so that it never terminates and thus runs forever. You can think of a thread as a mini self-contained program that runs within the RTOS. With the Arm Compiler, it is possible to optimize a thread by using a `__NO_RETURN` macro. This attribute reduces the cost of calling a function that never returns.

An RTOS program is made up of a number of threads, which are controlled by the RTOS scheduler. This scheduler uses the SysTick timer to generate a periodic interrupt as a time base. The scheduler will allot a certain amount of execution time to each thread. So `thread1` will run for 5 ms then be de-scheduled to allow `thread2` to run for a similar period; `thread2` will give way to `thread3` and finally control passes back to `thread1`. By allocating these slices of runtime to each thread in a round-robin fashion, we get the appearance of all three threads running in parallel to each other.

Conceptually we can think of each thread as performing a specific functional unit of our program with all threads running simultaneously. This leads us to a more object-orientated design, where each functional block can be coded and tested in isolation and then integrated into a fully running program. This not only imposes a structure on the design of our final application but also aids debugging, as a particular bug can be easily isolated to a specific thread. It also aids code reuse in later projects. When a thread is created, it is also allocated its own thread ID. This is a variable which acts as a handle for each thread and is used when we want to manage the activity of the thread.

```c
osThreadId_t id1, id2, id3;
```

In order to make the thread-switching process happen, we have the code overhead of the RTOS and we have to dedicate a CPU hardware timer to provide the RTOS time reference. In addition, each time we switch running threads, we have to save the state of all the thread variables to a thread stack. Also, all the runtime information about a thread is stored in a thread
control block, which is managed by the RTOS kernel. Thus the “context switch time”, that is, the time to save the current thread state and load up and start the next thread, is a crucial figure and will depend on both the RTOS kernel and the design of the underlying hardware.

The Thread Control Block contains information about the status of a thread. Part of this information is its run state. In a given system, only one thread can be running and all the others will be suspended but ready to run. The RTOS has various methods of inter-thread communication (signals, semaphores, messages). Here, a thread may be suspended to wait to be signaled by another thread or interrupt before it resumes its ready state, whereupon it can be placed into running state by the RTOS scheduler.

| State   | Description |
|---------|-------------|
| Running | The currently running thread |
| Ready   | Threads ready to run |
| Wait    | Blocked threads waiting for an OS event |

At any given moment a single thread may be running. The remaining threads will be ready to run and will be scheduled by the kernel. Threads may also be waiting pending an OS event. When this occurs they will return to the ready state and be scheduled by the kernel.
