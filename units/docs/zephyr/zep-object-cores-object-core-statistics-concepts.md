---
id: "zep-object-cores-object-core-statistics-concepts"
type: "concept"
domain: "rtos"
title: "Object Cores: Object Core Statistics Concepts"
summary: "A variety of kernel objects allow for the gathering and reporting of statistics. Object cores provide a uniform means to retrieve that information via object core statistics."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/object_cores/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/object_cores/index.rst"
license: "Apache-2.0"
mode: "V"
---

A variety of kernel objects allow for the gathering and reporting of statistics.
Object cores provide a uniform means to retrieve that information via object
core statistics. When enabled, the object type contains a pointer to a
statistics descriptor that defines the various operations that have been
enabled for interfacing with the object's statistics. Additionally, the object
core contains a pointer to the "raw" statistical information associated with
that object. Raw data is the raw, unmanipulated data associated with the
statistics. Queried data may be "raw", but it may also have been manipulated in
some way by calculation (such as determining an average).

The following table indicates both what objects have been integrated into the
object core statistics as well as the structures used for both "raw" and
"queried" data.

=====================  ============================== ==============================
Object                 Raw Data Type                  Query Data Type
=====================  ============================== ==============================
struct mem_slab        struct mem_slab_info            struct sys_memory_stats
struct sys_mem_blocks  struct sys_mem_blocks_info      struct sys_memory_stats
struct k_thread        struct k_cycle_stats            struct k_thread_runtime_stats
struct _cpu            struct k_cycle_stats            struct k_thread_runtime_stats
struct z_kernel        struct k_cycle_stats[num CPUs]  struct k_thread_runtime_stats
=====================  ============================== ==============================
