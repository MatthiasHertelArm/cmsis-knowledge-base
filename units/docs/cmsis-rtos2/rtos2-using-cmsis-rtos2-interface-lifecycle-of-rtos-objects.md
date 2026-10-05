---
id: "rtos2-using-cmsis-rtos2-interface-lifecycle-of-rtos-objects"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Lifecycle of RTOS Objects"
summary: "All RTOS objects share a common design concept. The overall life-cycle of an object can be summarized as created -> in use -> destroyed."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#lifecycle-of-rtos-objects"
license: "Apache-2.0"
mode: "V"
---

All RTOS objects share a common design concept. The overall life-cycle of an object can be summarized as created -> in use -> destroyed.

### Create Objects

An RTOS object (thread, timer, flags, mutex, etc.) is created by calling its `osXxxNew` function (for example osThreadNew, osTimerNew, osEventFlagsNew, etc). The new function returns a numeric identifier that can be used to operate with the new object.

The actual state of an object is typically stored in an object specific control block. The memory layout (and size needed) for the control block is implementation specific. One should not make any specific assumptions about the control block. The control block layout might change and hence should be seen as an implementation internal detail.

In order to expose control about object specific options all `osXxxNew` functions provide an optional `attr` argument, which can be left as `NULL` by default. It takes a pointer to an object specific attribute structure, commonly containing the fields:

 - `name` to attach a human readable name to the object for identification,
 - `attr_bits` to control object-specific options,
 - `cb_mem` to provide memory for the control block manually, and
 - `cb_size` to quantify the memory size provided for the control block.

The `name` attribute is only used for object identification, e.g. using RTOS-aware debugging. The attached string is not used for any other purposes internally.

The `cb_mem` and `cb_size` attributes can be used to provide memory for the control block manually instead of relying on the implementation internal memory allocation. One has to assure that the amount of memory pointed to by `cb_mem` is sufficient for the objects control block structure. If the size given as `cb_size` is not sufficient the `osXxxNew` function returns with an error, i.e. returning `NULL`. Furthermore providing control block memory manually is less portable. Thus one has to take care about implementation specific alignment and placement requirements for instance. Refer to CMSIS_RTOS_MemoryMgmt for further details.

### Object Usage

After an object has been created successfully it can be used until it is destroyed. The actions
defined for an object depends on its type. Commonly all the `osXxxDoSomething` access function
require the reference to the object to work with as the first `xxx_id` parameter.

The access function can be assumed to apply some sort of sanity checking on the id parameter. So that it is assured one cannot accidentally call an access function with a `NULL` object reference. Furthermore the concrete object type is verified, i.e. one cannot call access functions of one object type with a reference to another object type.

All further parameter checks applied are either object and action specific or may even be implementation specific. Thus one should always check action function return values for `osErrorParameter` to assure the provided arguments were accepted.

As a rule of thumb only non-blocking access function can be used from Interrupt Service Routines (ISR). This incorporates `osXxxWait` functions (and similar) limited to be called with parameter `timeout` set to `0`, i.e. usage of try-semantics.

### Object Destruction

Objects that are not needed anymore can be destructed on demand to free the control block memory. Objects are not destructed implicitly. Thus one can assume an object id to be valid until `osXxxDelete` is called explicitly. The delete function finally frees the control block memory. In case of user provided control block memory, see above, the memory must be freed manually as well.

The only exception one has to take care of are Threads which do not have an explicit `osThreadDelete` function. Threads can either be `detached` or `joinable`. Detached threads are automatically destroyed on termination, i.e. call to osThreadTerminate or osThreadExit or return from thread function. On the other hand joinable threads are kept alive until one explicitly calls osThreadJoin.
