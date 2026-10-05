---
id: "zep-system-calls-implementation-function"
type: "concept"
domain: "rtos"
title: "System Calls: Implementation Function"
summary: "The implementation function is what actually does the work for the API. Zephyr normally does little to no error checking of arguments, or does this kind of checking with assertions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

The implementation function is what actually does the work for the API.
Zephyr normally does little to no error checking of arguments, or does this
kind of checking with assertions. When writing the implementation function,
validation of any parameters is optional and should be done with assertions.

All implementation functions must follow the naming convention, which is the
name of the API prefixed with `z_impl_`. Implementation functions may be
declared in the same header as the API as a static inline function or
declared in some C file. There is no prototype needed for implementation
functions, these are automatically generated.
