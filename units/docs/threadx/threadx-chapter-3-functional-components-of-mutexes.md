---
id: "threadx-chapter-3-functional-components-of-mutexes"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Mutexes"
summary: "In addition to semaphores, ThreadX also provides a mutex object. A mutex is basically a binary semaphore, which means that only one thread can own a mutex at a time."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#mutexes"
license: "MIT"
mode: "V"
---

In addition to semaphores, ThreadX also provides a mutex object. A mutex is basically a binary semaphore, which means that only one thread can own a mutex at a time. In addition, the same thread may perform a successful mutex get operation on an owned mutex multiple times, 4,294,967,295 to be exact. There are two operations on the mutex object: ***tx_mutex_get*** and ***tx_mutex_put***. The get operation obtains a mutex not owned by another thread, while the put operation releases a previously obtained mutex. For a thread to release a mutex, the number of put operations must equal the number of prior get operations.

Each mutex is a public resource. ThreadX places no constraints on how mutexes are used.

ThreadX mutexes are used solely for *mutual exclusion*. Unlike counting semaphores, mutexes have no use as a method for event notification.

### Mutex Mutual Exclusion

Similar to the discussion in the counting semaphore section, mutual exclusion pertains to controlling the access of threads to certain application areas (also called *critical sections* or *application resources*). When available, a ThreadX mutex will have an ownership count of 0. After the mutex is obtained by a thread, the ownership count is incremented once for every successful get operation performed on the mutex and decremented for every successful put operation.

### Creating Mutexes

ThreadX mutexes are created either during initialization or during run-time by application threads. The initial condition of a mutex is always "available." A mutex may also be created with *priority inheritance* selected.

### Thread Suspension

Application threads can suspend while attempting to perform a get operation on a mutex already owned by another thread.

After the same number of put operations are performed by the owning thread, the suspended thread's get operation is performed, giving it ownership of the mutex, and the thread is resumed. If multiple threads are suspended on the same mutex, they are resumed in the same order they were suspended (FIFO).

However, priority resumption is done automatically if the mutex priority inheritance was selected during creation. Priority resumption is also possible if the application calls ***tx_mutex_prioritize*** prior to the mutex put call that lifts thread suspension. The mutex prioritize service places the highest priority thread at the front of the suspension list, while leaving all other suspended threads in the same FIFO order.

### Run-time Mutex Performance Information

ThreadX provides optional run-time mutex performance information. If the ThreadX library and application is built with **TX_MUTEX_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

- mutex puts

- mutex gets

- mutex get suspensions

- mutex get timeouts

- mutex priority inversions

- mutex priority inheritances

Total number for each mutex:

  - mutex puts

  - mutex gets

  - mutex get suspensions

  - mutex get timeouts

  - mutex priority inversions

  - mutex priority inheritances

This information is available at run-time through the services ***tx_mutex_performance_info_get*** and ***tx_mutex_performance_system_info_get***. Mutex performance information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of "mutex get timeouts" might
suggest that other threads are holding resources too long.

### Mutex Control Block TX_MUTEX

The characteristics of each mutex are found in its control block. It contains information such as the current mutex ownership count along with the pointer of the thread that owns the mutex. This structure is defined in the ***tx_api.h*** file. Mutex control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Deadly Embrace

One of the most interesting and dangerous pitfalls associated with mutex ownership is the *deadly embrace*. A deadly embrace, or *deadlock*, is a condition where two or more threads are suspended indefinitely while attempting to get a mutex already owned by the other threads. The discussion of *deadly embrace* and its remedies are completely valid for the mutex object as well.

### Priority Inversion

As mentioned previously, a major pitfall associated with mutual exclusion is priority inversion. This topic is discussed more fully in "[Thread Priority Pitfalls](#thread-priority-pitfalls)".

The basic problem results from a situation in which a lower priority thread has a semaphore that a higher priority thread needs. This in itself is normal. However, threads with priorities in between them may cause the priority inversion to last a nondeterministic amount of time. Unlike semaphores discussed previously, the ThreadX mutex object has optional *priority inheritance*. The basic idea behind priority inheritance is that a lower priority thread has its priority raised temporarily to the priority of a high priority thread that wants the same mutex owned by the lower priority thread. When the lower priority thread releases the mutex, its original priority is then restored and the higher priority thread is given ownership of the mutex. This feature eliminates nondeterministic priority inversion by bounding the amount of inversion to the time the lower priority thread holds the mutex. Of course, the techniques discussed earlier in this chapter to handle nondeterministic priority inversion are also valid with mutexes
as well.
