---
id: "zep-system-calls-c-prototype"
type: "concept"
domain: "rtos"
title: "System Calls: C Prototype"
summary: "The C prototype represents how the API is invoked from either user or supervisor mode. For example, to initialize a semaphore:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

The C prototype represents how the API is invoked from either user or
supervisor mode. For example, to initialize a semaphore:

```c

__syscall void k_sem_init(struct k_sem *sem, unsigned int initial_count,
                          unsigned int limit);
```
The `__syscall` attribute is very special. To the C compiler, it
simply expands to 'static inline'. However to the post-build
parse_syscalls.py script, it indicates that this API is a system call.
The parse_syscalls.py script does some parsing of the function prototype,
to determine the data types of its return value and arguments, and has some
limitations:

* Array arguments must be passed in as pointers, not arrays. For example,
  `int foo[]` or `int foo[12]` is not allowed, but should instead be
  expressed as `int *foo`.

* Function pointers horribly confuse the limited parser. The workaround is
  to typedef them first, and then express in the argument list in terms
  of that typedef.

* `__syscall` must be the first thing in the prototype.

The preprocessor is intentionally not used when determining the set of system
calls to generate. However, any generated system calls that don't actually have
a verification function defined (because the related feature is not enabled in
the kernel configuration) will instead point to a special verification for
unimplemented system calls. Data type definitions for APIs should not have
conditional visibility to the compiler.

Any header file that declares system calls must include a special generated
header at the very bottom of the header file. This header follows the
naming convention `syscalls/<name of header file>`. For example, at the
bottom of `include/zephyr/drivers/sensor.h`:

```c

#include <zephyr/syscalls/sensor.h>
```
C prototype functions must be declared in one of the directories
listed in the CMake variable `SYSCALL_INCLUDE_DIRS`. This list
always contains `APPLICATION_SOURCE_DIR` when
`CONFIG_APPLICATION_DEFINED_SYSCALL` is set, or
`${ZEPHYR_BASE}/subsys/testsuite/ztest/include` when
`CONFIG_ZTEST` is set. Additional paths can be added to the list
through the CMake command line or in CMake code that is run before
`find_package(Zephyr ...)` is run. `${ZEPHYR_BASE}/include`
is always scanned for potential syscall prototypes.

Note that not all syscalls will be included in the final binaries.
CMake functions `zephyr_syscall_header` and
`zephyr_syscall_header_ifdef` are used to specify which header
files contain syscall prototypes where those syscalls must be
present in the final binaries. Note that header files inside
directories listed in CMake variable `SYSCALL_INCLUDE_DIRS`
will always have their syscalls present in final binaries.
To force all syscalls to be included in the final binaries,
turn on `CONFIG_EMIT_ALL_SYSCALLS`.


### Invocation Context


Source code that uses system call APIs can be made more efficient if it is
known that all the code inside a particular C file runs exclusively in
user mode, or exclusively in supervisor mode. The system will look for
the definition of macros `__ZEPHYR_SUPERVISOR__` or
`__ZEPHYR_USER__`, typically these will be added to the compiler
flags in the build system for the related files.

* If `CONFIG_USERSPACE` is not enabled, all APIs just directly call
  the implementation function.

* Otherwise, the default case is to make a runtime check to see if the
  processor is currently running in user mode, and either make the system call
  or directly call the implementation function as appropriate.

* If `__ZEPHYR_SUPERVISOR__` is defined, then it is assumed that
  all the code runs in supervisor mode and all APIs just directly call the
  implementation function. If the code was actually running in user mode,
  there will be a CPU exception as soon as it tries to do something it isn't
  allowed to do.

* If `__ZEPHYR_USER__` is defined, then it is assumed that all the
  code runs in user mode and system calls are unconditionally made.


### Implementation Details


Declaring an API with `__syscall` causes some code to be generated in
C and header files by the gen_syscalls.py script, all of which can be found in
the project out directory under `include/generated/`:

* The system call is added to the enumerated type of system call IDs,
  which is expressed in `include/generated/zephyr/syscall_list.h`. It is the name
  of the API in uppercase, prefixed with `K_SYSCALL_`.

* An entry for the system call is created in the dispatch table
  `_k_syscall_table`, expressed in `include/generated/zephyr/syscall_dispatch.c`

  * This table only contains syscalls where their corresponding
    prototypes are declared in header files when
    `CONFIG_EMIT_ALL_SYSCALLS` is enabled:

    * Indicated by CMake functions `zephyr_syscall_header` and
      `zephyr_syscall_header_ifdef`, or

    * Under directories specified in CMake variable
      `SYSCALL_INCLUDE_DIRS`.

* A weak verification function is declared, which is just an alias of the
  'unimplemented system call' verifier. This is necessary since the real
  verification function may or may not be built depending on the kernel
  configuration. For example, if a user thread makes a sensor subsystem
  API call, but the sensor subsystem is not enabled, the weak verifier
  will be invoked instead.

* An unmarshalling function is defined in `include/generated/zephyr/syscalls/<name>_mrsh.c`

The body of the API is created in the generated system header. Using the
example of `k_sem_init()`, this API is declared in
`include/zephyr/kernel.h`. At the bottom of
`include/zephyr/kernel.h` is::
```
#include <zephyr/syscalls/kernel.h>
```
Inside this header is the body of `k_sem_init()`::
```
static inline void k_sem_init(struct k_sem * sem, unsigned int initial_count, unsigned int limit)
{
#ifdef CONFIG_USERSPACE
        if (z_syscall_trap()) {
                arch_syscall_invoke3(*(uintptr_t *)&sem, *(uintptr_t *)&initial_count, *(uintptr_t *)&limit, K_SYSCALL_K_SEM_INIT);
                return;
        }
        compiler_barrier();
#endif
        z_impl_k_sem_init(sem, initial_count, limit);
}
```
This generates an inline function that takes three arguments with void
return value. Depending on context it will either directly call the
implementation function or go through a system call elevation. A
prototype for the implementation function is also automatically generated.

The final layer is the invocation of the system call itself. All architectures
implementing system calls must implement the seven inline functions
`_arch_syscall_invoke0` through `_arch_syscall_invoke6`. These
functions marshal arguments into designated CPU registers and perform the
necessary privilege elevation. Parameters of API inline function, before being
passed as arguments to system call, are C casted to `uintptr_t` which matches
size of register.
Exception to above is passing 64-bit parameters on 32-bit systems, in which case
64-bit parameters are split into lower and higher part and passed as two consecutive
arguments.
There is always a `uintptr_t` type return value, which may be neglected if
not needed.

Some system calls may have more than six arguments, but number of arguments
passed via registers is limited to six for all architectures.
Additional arguments will need to be passed in an array in the source memory
space, which needs to be treated as untrusted memory in the verification
function. This code (packing, unpacking and validation) is generated
automatically as needed in the stub above and in the unmarshalling function.

System calls return `uintptr_t` type value that is C casted, by wrapper, to
a return type of API prototype declaration. This means that 64-bit value may
not be directly returned, from a system call to its wrapper, on 32-bit systems.
To solve the problem the automatically generated wrapper function defines 64-bit
intermediate variable, which is considered **untrusted** buffer, on its stack
and passes pointer to that variable to the system call, as a final argument.
Upon return from the system call the value written to that buffer will be
returned by the wrapper function.
The problem does not exist on 64-bit systems which are able to return 64-bit
values directly.
