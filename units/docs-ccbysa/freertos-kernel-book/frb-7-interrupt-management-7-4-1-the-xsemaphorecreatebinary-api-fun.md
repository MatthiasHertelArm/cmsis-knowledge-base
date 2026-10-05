---
id: "frb-7-interrupt-management-7-4-1-the-xsemaphorecreatebinary-api-fun"
type: "concept"
domain: "rtos"
title: "7 Interrupt Management: 7.4 Binary Semaphores Used for Synchronization / 7.4.1 The xSemaphoreCreateBinary() API Function"
summary: "Part of: 7.4 Binary Semaphores Used for Synchronization"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch07.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch07.md#7-4-1-the-xsemaphorecreatebinary-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 7.4 Binary Semaphores Used for Synchronization_

FreeRTOS also includes the `xSemaphoreCreateBinaryStatic()`
function, which allocates the memory required to create a binary
semaphore statically at compile time: Handles to all the various types
of FreeRTOS semaphore are stored in a variable of type
`SemaphoreHandle_t`.

Before a semaphore can be used, it must be created. To create a binary
semaphore, use the `xSemaphoreCreateBinary()` API function[^15].

[^15]: Some Semaphore API functions are actually macros, not functions.
For simplicity, they are all referred to as functions throughout
this book.




```c
SemaphoreHandle_t xSemaphoreCreateBinary( void );
```
***Listing 7.3*** *The xSemaphoreCreateBinary() API function prototype*

**xSemaphoreCreateBinary() Return Value**

- Return value

  If NULL is returned, then the semaphore cannot be created because
  there is insufficient heap memory available for FreeRTOS to allocate the
  semaphore data structures.

  If a non-NULL value is returned, it indicates that the semaphore has been
  created successfully. The returned value should be stored as the handle
  to the created semaphore.
