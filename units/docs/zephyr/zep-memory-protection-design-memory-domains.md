---
id: "zep-memory-protection-design-memory-domains"
type: "concept"
domain: "rtos"
title: "Memory Protection Design: Memory Domains"
summary: "The kernel ensures that any user thread will have access to its own stack buffer, plus program text and read-only data. The memory domain APIs are the way to grant access to additional blocks of memory to a user thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel ensures that any user thread will have access to its own stack
buffer, plus program text and read-only data. The memory domain APIs are the
way to grant access to additional blocks of memory to a user thread.

Conceptually, a memory domain is a collection of some number of memory
partitions. The maximum number of memory partitions in a domain
is limited by the number of available MPU regions. This is why it is important
to minimize the number of boot-time MPU regions.

Memory domains are *not* intended to control access to memory from supervisor
mode. In some cases this may be unavoidable; for example some architectures do
not allow for the definition of regions which are read-only to user mode but
read-write to supervisor mode. A great deal of care must be taken when working
with such regions to not unintentionally cause the kernel to crash when
accessing such a region. Any attempt to use memory domain APIs to control
supervisor mode access is at best undefined behavior; supervisor mode access
policy is only intended to be controlled by boot-time memory regions.

Memory domain APIs are only available to supervisor mode. The only control
user mode has over memory domains is that any user thread's child threads
will automatically become members of the parent's domain.

All threads are members of a memory domain, including supervisor threads
(even though this has no implications on their memory access). There is a
default domain `k_mem_domain_default` which will be assigned to threads if
they have not been specifically assigned to a domain, or inherited a memory
domain membership from their parent thread. The main thread starts as a
member of the default domain.


### Memory Partitions


Each memory partition consists of a memory address, a size,
and access attributes. It is intended that memory partitions are used to
control access to system memory. Defining memory partitions are subject
to the following constraints:

- The partition must represent a memory region that can be programmed by
  the underlying memory management hardware, and needs to conform to any
  underlying hardware constraints. For example, many MPU-based systems require
  that partitions be sized to some power of two, and aligned to their own
  size. For MMU-based systems, the partition must be aligned to a page and
  the size some multiple of the page size.

- Partitions within the same memory domain may not overlap each other. There is
  no notion of precedence among partitions within a memory domain.  Partitions
  within a memory domain are assumed to have a higher precedence than any
  boot-time memory regions, however whether a memory domain partition can
  overlap a boot-time memory region is architecture specific.

- The same partition may be specified in multiple memory domains. For example
  there may be a shared memory area that multiple domains grant access to.

- Care must be taken in determining what memory to expose in a partition.
  It is not appropriate to provide direct user mode access to any memory
  containing private kernel data.

- Memory domain partitions are intended to control access to system RAM.
  Configuration of memory partitions which do not correspond to RAM
  may not be supported by the architecture; this is true for MMU-based systems.

There are two ways to define memory partitions: either manually or
automatically.


#### Manual Memory Partitions


The following code declares a global array `buf`, and then declares
a read-write partition for it which may be added to a domain:

```c

uint8_t __aligned(32) buf[32];

K_MEM_PARTITION_DEFINE(my_partition, buf, sizeof(buf),
                       K_MEM_PARTITION_P_RW_U_RW);
```
This does not scale particularly well when we are trying to contain multiple
objects spread out across several C files into a single partition.


#### Automatic Memory Partitions


Automatic memory partitions are created by the build system. All globals
which need to be placed inside a partition are tagged with their destination
partition. The build system will then coalesce all of these into a single
contiguous block of memory, zero any BSS variables at boot, and define
a memory partition of appropriate base address and size which contains all
the tagged data.

Automatic memory partitions are only configured as read-write
regions. They are defined with `K_APPMEM_PARTITION_DEFINE()`.
Global variables are then routed to this partition using
`K_APP_DMEM()` for initialized data and `K_APP_BMEM()` for
BSS.

```c

#include <zephyr/app_memory/app_memdomain.h>

/* Declare a k_mem_partition "my_partition" that is read-write to
 * user mode. Note that we do not specify a base address or size.
 */
K_APPMEM_PARTITION_DEFINE(my_partition);

/* The global variable var1 will be inside the bounds of my_partition
 * and be initialized with 37 at boot.
 */
K_APP_DMEM(my_partition) int var1 = 37;

/* The global variable var2 will be inside the bounds of my_partition
 * and be zeroed at boot size K_APP_BMEM() was used, indicating a BSS
 * variable.
 */
K_APP_BMEM(my_partition) int var2;
```
The build system will ensure that the base address of `my_partition` will
be properly aligned, and the total size of the region conforms to the memory
management hardware requirements, adding padding if necessary.

If multiple partitions are being created, a variadic preprocessor macro can be
used as provided in `app_macro_support.h`:

```c

FOR_EACH(K_APPMEM_PARTITION_DEFINE, part0, part1, part2);
```

##### Automatic Partitions for Static Library Globals


The build-time logic for setting up automatic memory partitions is in
`scripts/build/gen_app_partitions.py`. If a static library is linked into Zephyr,
it is possible to route all the globals in that library to a specific
memory partition with the `--library` argument.

For example, if the Newlib C library is enabled, the Newlib globals all need
to be placed in `z_libc_partition`. The invocation of the script in the
top-level `CMakeLists.txt` adds the following:

```none

gen_app_partitions.py ... --library libc.a z_libc_partition ..
```
For pre-compiled libraries there is no support for expressing this in the
project-level configuration or build files; the toplevel `CMakeLists.txt` must
be edited.

For Zephyr libraries created using `zephyr_library` or `zephyr_library_named`
the `zephyr_library_app_memory` function can be used to specify the memory
partition where all globals in the library should be placed.


#### Pre-defined Memory Partitions


There are a few memory partitions which are pre-defined by the system:

 - `z_malloc_partition` - This partition contains the system-wide pool of
   memory used by libc malloc(). Due to possible starvation issues, it is
   not recommended to draw heap memory from a global pool, instead
   it is better to define various sys_heap objects and assign them
   to specific memory domains.

 - `z_libc_partition` - Contains globals required by the C library and runtime.
   Required when using either the Minimal C library or the Newlib C Library.
   Required when `CONFIG_STACK_CANARIES` is enabled.

Library-specific partitions are listed in `include/zephyr/app_memory/partitions.h`.
For example, to use the MBEDTLS library from user mode, the
`k_mbedtls_partition` must be added to the domain.


### Memory Domain Usage



#### Create a Memory Domain


A memory domain is defined using a variable of type
`k_mem_domain`. It must then be initialized by calling
`k_mem_domain_init`.

The following code defines and initializes an empty memory domain.

```c

struct k_mem_domain app0_domain;

k_mem_domain_init(&app0_domain, 0, NULL);
```

#### Add Memory Partitions into a Memory Domain


There are two ways to add memory partitions into a memory domain.

This first code sample shows how to add memory partitions while creating
a memory domain.

```c

/* the start address of the MPU region needs to align with its size */
uint8_t __aligned(32) app0_buf[32];
uint8_t __aligned(32) app1_buf[32];

K_MEM_PARTITION_DEFINE(app0_part0, app0_buf, sizeof(app0_buf),
                       K_MEM_PARTITION_P_RW_U_RW);

K_MEM_PARTITION_DEFINE(app0_part1, app1_buf, sizeof(app1_buf),
                       K_MEM_PARTITION_P_RW_U_RO);

struct k_mem_partition *app0_parts[] = {
    app0_part0,
    app0_part1
};

k_mem_domain_init(&app0_domain, ARRAY_SIZE(app0_parts), app0_parts);
```
This second code sample shows how to add memory partitions into an initialized
memory domain one by one.

```c

/* the start address of the MPU region needs to align with its size */
uint8_t __aligned(32) app0_buf[32];
uint8_t __aligned(32) app1_buf[32];

K_MEM_PARTITION_DEFINE(app0_part0, app0_buf, sizeof(app0_buf),
                       K_MEM_PARTITION_P_RW_U_RW);

K_MEM_PARTITION_DEFINE(app0_part1, app1_buf, sizeof(app1_buf),
                       K_MEM_PARTITION_P_RW_U_RO);

k_mem_domain_add_partition(&app0_domain, &app0_part0);
k_mem_domain_add_partition(&app0_domain, &app0_part1);
```

**Note:** The maximum number of memory partitions is limited by the maximum number of MPU regions or the maximum number of MMU tables.


#### Memory Domain Assignment


Any thread may join a memory domain, and any memory domain may have multiple
threads assigned to it. Threads are assigned to memory domains with an API
call:

```c

k_mem_domain_add_thread(&app0_domain, app_thread_id);
```
If the thread was already a member of some other domain (including the
default domain), it will be removed from it in favor of the new one.

In addition, if a thread is a member of a memory domain, and it creates a
child thread, that thread will belong to the domain as well.


#### Remove a Memory Partition from a Memory Domain


The following code shows how to remove a memory partition from a memory
domain.

```c

k_mem_domain_remove_partition(&app0_domain, &app0_part1);
```
The k_mem_domain_remove_partition() API finds the memory partition
that matches the given parameter and removes that partition from the
memory domain.


#### Available Partition Attributes


When defining a partition, we need to set access permission attributes
to the partition. Since the access control of memory partitions relies on
either an MPU or MMU, the available partition attributes would be architecture
dependent.

The complete list of available partition attributes for a specific architecture
is found in the architecture-specific include file
`include/zephyr/arch/<arch name>/arch.h`, (for example, `include/zephyr/arch/arm/arch.h`.)
Some examples of partition attributes are:

```c

/* Denote partition is privileged read/write, unprivileged read/write */
K_MEM_PARTITION_P_RW_U_RW
/* Denote partition is privileged read/write, unprivileged read-only */
K_MEM_PARTITION_P_RW_U_RO
```
In almost all cases `K_MEM_PARTITION_P_RW_U_RW` is the right choice.
