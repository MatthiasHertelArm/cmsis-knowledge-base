---
id: "zep-tracing-object-tracking"
type: "concept"
domain: "debug"
title: "Tracing: Object tracking"
summary: "The kernel can also keep track of the kernel objects in the system. Enabling CONFIG_TRACING_OBJECT_TRACKING enables the object core framework, which enumerates the objects of each kernel object type. For instance, to visit every mutex, one can write::"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel can also keep track of the kernel objects in the system. Enabling
`CONFIG_TRACING_OBJECT_TRACKING` enables the
object core framework, which enumerates the objects of
each kernel object type. For instance, to visit every mutex, one can write::
```
static int visit_mutex(struct k_obj_core *obj_core, void *data)
{
    struct k_mutex *mutex = CONTAINER_OF(obj_core, struct k_mutex, obj_core);

    /* Do something */

    return 0;
}

k_obj_type_walk_locked(k_obj_type_find(K_OBJ_TYPE_MUTEX_ID), visit_mutex, NULL);
```
Each object type can be excluded through its `CONFIG_OBJ_CORE_*` option. The
object_cores sample can be built with object tracking
enabled.
