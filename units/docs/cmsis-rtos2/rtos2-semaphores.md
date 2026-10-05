---
id: "rtos2-semaphores"
type: "concept"
domain: "rtos"
title: "Semaphores"
summary: "Access shared resources simultaneously from different threads."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

Access shared resources simultaneously from different threads.
 
Semaphores are used to manage and protect access to shared resources. Semaphores are very similar to
Mutexes. Whereas a Mutex permits just one thread to access a shared resource at a
time, a semaphore can be used to permit a fixed number of threads/ISRs to access a pool of shared resources. Using
semaphores, access to a group of identical peripherals can be managed (for example multiple DMA channels).

" "CMSIS-RTOS Semaphore"

A semaphore object should be initialized to the maximum number of available tokens. This number of available resources is
specified as parameter of the osSemaphoreNew function. Each time a semaphore token is obtained with osSemaphoreAcquire
(in **available** state), the semaphore count is decremented. When the semaphore count is 0 (i.e. **depleted** state), no
more semaphore tokens can be obtained. The thread/ISR that tries to obtain the semaphore token needs to wait until the next
token is free. Semaphores are released with osSemaphoreRelease incrementing the semaphore count.

" "CMSIS-RTOS Semaphore States"

**Note:** The functions osSemaphoreAcquire, osSemaphoreGetCount, and osSemaphoreRelease can be called from
Interrupt Service Routines.

Semaphore Use Cases
-------------------
Due to their flexibility, semaphores cover a wide range of synchronizing applications. At the same time, they are perhaps the
most challenging RTOS object to understand. The following explains a use case for semaphores, taken from the book
The Little Book Of Semaphores by Allen B. Downey which
is available for free download.

**Non-binary Semaphore (Multiplex)**

A multiplex limits the number of threads that can access a critical section of code. For example, this could be a function
accessing DMA resources which can only support a limited number of calls.

To allow multiple threads to run the function, initialize a semaphore to the maximum number of threads that can be allowed.
The number of tokens in the semaphore represents the number of additional threads that may enter. If this number is zero,
then the next thread trying to access the function will have to wait until one of the other threads exits and releases its
token. When all threads have exited the token number is back to n. The following example shows the code for one of the
threads that might access the resource:

```
osSemaphoreId_t multiplex_id;
 
void thread_n (void) {
 
  multiplex_id = osSemaphoreNew(3U, 3U, NULL);
  while(1) {
    osSemaphoreAcquire(multiplex_id, osWaitForever);
    // do something
    osSemaphoreRelease(multiplex_id);
  }
}
```

**Producer/Consumer Semaphore**

The producer-consumer problem can be solved using two semaphores.

A first semaphore (`empty_id`) counts down the available (empty) buffers, i.e.
the producer thread can wait for available buffer slots by acquiring from this one.

A second semaphore (`filled_id`) counts up the used (filled) buffers, i.e.
the consumer thread can wait for available data by acquiring from this one.

It is crucial for the correct behaviour that the threads acquire and release on both
semaphores in the given sequence. According to this example one can have multiple
producer and/or consumer threads running concurrently.

```
#define BUFFER_SIZE 10U
 
osSemaphoreId_t empty_id = osSemaphoreNew(BUFFER_SIZE, BUFFER_SIZE, NULL);
osSemaphoreId_t filled_id = osSemaphoreNew(BUFFER_SIZE, 0U, NULL);
 
void producer_thread (void) {
  while(1) {
    osSemaphoreAcquire(empty_id, osWaitForever);
    // produce data
    osSemaphoreRelease(filled_id);
  }
}

void consumer_thread (void) {
 
  while(1){
    osSemaphoreAcquire(filled_id, osWaitForever);
    // consume data
    osSemaphoreRelease(empty_id);
  }
}
```
