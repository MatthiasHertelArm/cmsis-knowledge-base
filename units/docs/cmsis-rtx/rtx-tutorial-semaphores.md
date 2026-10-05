---
id: "rtx-tutorial-semaphores"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Semaphores"
summary: "Like thread flags, semaphores are a method of synchronizing activity between two or more threads. Put simply, a semaphore is a container that holds a number of tokens."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#semaphores"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

Like thread flags, semaphores are a method of synchronizing activity between two or more threads. Put simply, a semaphore is
a container that holds a number of tokens. As a thread executes, it will reach an RTOS call to acquire a semaphore token. If
the semaphore contains one or more tokens, the thread will continue executing and the number of tokens in the semaphore will
be decremented by one. If there are currently no tokens in the semaphore, the thread will be placed in a waiting state until
a token becomes available. At any point in its execution, a thread may add a token to the semaphore causing its token count
to increment by one.

The diagram above illustrates the use of a semaphore to synchronize two threads. First, the semaphore must be created and
initialized with an initial token count. In this case the semaphore is initialized with a single token. Both threads will
run and reach a point in their code where they will attempt to acquire a token from the semaphore. The first thread to reach
this point will acquire the token from the semaphore and continue execution. The second thread will also attempt to acquire
a token, but as the semaphore is empty it will halt execution and be placed into a waiting state until a semaphore token is
available.

Meanwhile, the executing thread can release a token back to the semaphore. When this happens, the waiting thread will
acquire the token and leave the waiting state for the ready state. Once in the ready state the scheduler will place the
thread into the run state so that thread execution can continue. While semaphores have a simple set of OS calls they can be
one of the more difficult OS objects to fully understand. In this section, we will first look at how to add semaphores to an
RTOS program and then go on to look at the most useful semaphore applications.

To use a semaphore in the CMSIS-RTOS you must first declare a semaphore attributes:

```c
osSemaphoreAttr_t {
  const char *name;   ///< name of the semaphore
  uint32_t attr_bits; ///< attribute bits (none)
  void *cb_mem;       ///< memory for control block
  uint32_t cb_size;   ///< size of provided memory for control block
};
```

Next declare the semaphore handle:

```c
osSemaphoreId_t sem1;
```

Then within a thread the semaphore container can be initialised with a number of tokens:

```c
sem1 = osSemaphoreNew(maxTokenCount,initalTokencount,&osSemaphoreAttr_t);
```

It is important to understand that semaphore tokens may also be created and destroyed as threads run. So for example you can
initialise a semaphore with zero tokens and then use one thread to create tokens into the semaphore while another thread
removes them. This allows you to design threads as producer and consumer threads.

Once the semaphore is initialized, tokens may be acquired and sent to the semaphore in a similar fashion to event flags. The
osSemaphoreAcquire call is used to block a thread until a semaphore token is available. A timeout period may also be
specified with 0xFFFF being an infinite wait.

```c
osStatus osSemaphoreAcquire(osSemaphoreId_t semaphore_id, uint32_t ticks);
```

Once the thread has finished using the semaphore resource, it can send a token to the semaphore container:

```c
osStatus osSemaphoreRelease(osSemaphoreId_t semaphore_id);
```

All semaphore functions are listed in the API reference.

#### Using Semaphores

Although semaphores have a simple set of OS calls, they have a wide range of synchronizing applications. This makes them
perhaps the most challenging RTOS object to understand. In this section we, will look at the most common uses of semaphores.
These are taken from free book [The Little Book Of Semaphores](https://greenteapress.com/wp/semaphores/) by Allen B. Downey.

#### Signalling

Synchronizing the execution of two threads is the simplest use of a semaphore:

```c
osSemaphoreId_t sem1;
static const osSemaphoreAttr_t semAttr_SEM1 = {
    .name = "SEM1",
};
 
void thread1(void) {
  sem1 = osSemaphoreNew(5, 0, &semAttr_SEM1);
  while (1) {
    FuncA();
    osSemaphoreRelease(sem1)
  }
}
 
void task2(void) {

  while (1) {
    osSemaphoreAcquire(sem1, osWaitForever) FuncB();
  }
}
```

In this case the semaphore is used to ensure that the code in `FuncA()` is executed before the code in `FuncB()`.

#### Exercise 11 - Semaphore Signalling

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 11 Semaphore Signalling** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Multiplex

A multiplex is used to limit the number of threads that can access a critical section of code. For example, this could be a
routine that accesses memory resources and can only support a limited number of calls.

```c
osSemaphoreId_t multiplex;
static const osSemaphoreAttr_t semAttr_Multiplex = {
    .name = "SEM1",
};
 
void thread1(void) {
  multiplex = osSemaphoreCreate(5, 5, &semAttr_Multiplex);
  while (1) {
    osSemaphoreAcquire(multiplex, osWaitForever);
    processBuffer();
    osSemaphoreRelease(multiplex);
  }
}
```

In this example we initialise the multiplex semaphore with five tokens. Before a thread can call the `processBuffer()`
function, it must acquire a semaphore token. Once the function has completed, the token is sent back to the semaphore. If
more than five threads are attempting to call `processBuffer()`, the sixth must wait until a thread has finished with
`processBuffer()` and returns its token. Thus, the multiplex semaphore ensures that a maximum of five threads can call the
`processBuffer()` function "simultaneously".

#### Exercise 12 - Multiplex

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 12 Multiplex** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Rendezvous

A more generalised form of semaphore signalling is a rendezvous. A rendezvous ensures that two threads reach a certain point
of execution. Neither may continue until both have reached the rendezvous point.

```c
osSemaphoreId_t arrived1, arrived2;
static const osSemaphoreAttr_t semAttr_Arrived1 = {
    .name = "Arr1",
};
 
static const osSemaphoreAttr_t semAttr_Arrived2 = {
    .name = "Arr2",
};
 
void thread1(void) {
  arrived1 = osSemaphoreNew(2, 0);
  arrived1 = osSemaphoreNew(2, 0);
  while (1) {
    FuncA1();
    osSemaphoreRelease(arrived1);
    osSemaphoreAcquire(arrived2, osWaitForever);
    FuncA2();
  }
}
 
void thread2(void) {
  while (1) {
    FuncB1();
    os_sem_Release(arrived2);
    os_sem_Acquire(arrived1, osWaitForever);
    FuncB2();
  }
}
```

In the above case, the two semaphores will ensure that both threads will rendezvous and then proceed to execute `FuncA2()`
and `FuncB2()`.

#### Exercise 13 - Rendezvous

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 13 Rendezvous** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Barrier Turnstile

Although a rendezvous is very useful for synchronising the execution of code, it only works for two functions. A barrier is
a more generalised form of rendezvous which works to synchronise multiple threads.

```c
osSemaphoreId_t count, barrier;
static const osSemaphoreAttr_t semAttr_Counter = {
    .name = "Counter",
};
 
static const osSemaphoreAttr_t semAttr_Barier = {
    .name = "Barrier",
};
 
unsigned int count;
 
void thread1(void) {
  Turnstile_In = osSemaphoreNew(5, 0, &semAttr_SEM_In);
  Turnstile_Out = osSemaphoreNew(5, 1, &semAttr_SEM_Out);
  Mutex = osSemaphoreNew(1, 1, &semAttr_Mutex);
  while (1) {
    osSemaphoreAcquire(Mutex, osWaitForever); // Allow one task at a time to
                                              // access the first turnstile
    count = count + 1; // Increment count
    if (count == 5) {
      osSemaphoreAcquire(Turnstile_Out,
                         osWaitForever); // Lock the second turnstile
      osSemaphoreRelease(Turnstile_In);  // Unlock the first turnstile
    }
    osSemaphoreRelease(Mutex); // Allow other tasks to access the turnstile
    osSemaphoreAcquire(Turnstile_In, osWaitForever); // Turnstile Gate
    osSemaphoreRelease(Turnstile_In);
    critical_Function();
  }
}
```

In this code, we use a global variable to count the number of threads which have arrived at the barrier. As each function
arrives at the barrier it will wait until it can acquire a token from the counter semaphore. Once acquired, the count
variable will be incremented by one. Once we have incremented the count variable, a token is sent to the counter semaphore
so that other waiting threads can proceed. Next, the barrier code reads the count variable. If this is equal to the number
of threads which are waiting to arrive at the barrier, we send a token to the barrier semaphore.

In the example above we are synchronising five threads. The first four threads will increment the count variable and then
wait at the barrier semaphore. The fifth and last thread to arrive will increment the count variable and send a token to the
barrier semaphore. This will allow it to immediately acquire a barrier semaphore token and continue execution. After passing
through the barrier, it immediately sends another token to the barrier semaphore. This allows one of the other waiting
threads to resume execution. This thread places another token in the barrier semaphore which triggers another waiting thread
and so on. This final section of the barrier code is called a turnstile because it allows one thread at a time to pass the
barrier. In our model of concurrent execution this means that each thread waits at the barrier until the last arrives then
the all resume simultaneously. In the following exercise we create five instances of one thread containing barrier code.
However, the barrier could be used to synchronise five unique threads.

#### Exercise 14 - Semaphore Barrier

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 14 Barrier** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Semaphore Caveats

Semaphores are an extremely useful feature of any RTOS. However semaphores can be misused. You must always remember that the
number of tokens in a semaphore is not fixed. During the runtime of a program semaphore tokens may be created and destroyed.
Sometimes this is useful, but if your code depends on having a fixed number of tokens available to a semaphore you must be
very careful to always return tokens back to it. You should also rule out the possibility of accidently creating additional
new tokens.
