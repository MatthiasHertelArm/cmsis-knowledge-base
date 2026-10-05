---
id: "rtx-operation-arm-c-library-multi-threading-protection"
type: "concept"
domain: "rtos"
title: "operation: Arm C library multi-threading protection"
summary: "RTX5 provides an interface to the Arm C libraries to ensure static data protection in a multi-threaded application."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#arm-c-library-multi-threading-protection"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides an interface to the [Arm C libraries](https://developer.arm.com/documentation/100073) to ensure static data protection in a multi-threaded application.

The Arm C libraries use static data to store errno, floating-point status word for software floating-point operations, a pointer to the base of the heap, and other variables. The Arm C micro-library (i.e. microlib) does not support protection for multi-threaded applications. See the [Differences between microlib and the default C library](https://developer.arm.com/documentation/100073/latest/The-Arm-C-Micro-library/Differences-between-microlib-and-the-default-C-library).

By default, RTX5 uses the Arm C libraries multi-thread protection for:

- all user threads if Object specific Memory allocation is enabled.
- the number of threads defined by `OS_THREAD_LIBSPACE_NUM` if Object specific Memory allocation is disabled. The definition `OS_THREAD_LIBSPACE_NUM` defines the number of threads that can safely call Arm C library functions and can be found in `RTX_Config.h` file or can be defined on the global scope.

The default, Arm C libraries use mutex functions to [protect shared resources from concurrent access](https://developer.arm.com/documentation/100073/0621/The-Arm-C-and-C---Libraries/Multithreaded-support-in-Arm-C-libraries/Management-of-locks-in-multithreaded-applications). RTX5 implements these functions and uses resources from the Global Dynamic Memory to allocate mutex objects.

\endif
