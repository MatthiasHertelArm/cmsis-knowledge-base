---
id: "zep-object-cores-implementation"
type: "concept"
domain: "rtos"
title: "Object Cores: Implementation"
summary: "An object type is a global variable of type k_obj_type. When the object struct has statically defined instances in an iterable section, the type is defined at build time with K_OBJ_TYPE_DEFINE and those instances become its permanent objects."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/object_cores/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/object_cores/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a New Object Type


An object type is a global variable of type `k_obj_type`. When the
object struct has statically defined instances in an iterable section, the
type is defined at build time with `K_OBJ_TYPE_DEFINE` and those
instances become its permanent objects. The following code shows how a new
object type can be defined for use with object cores and object core
statistics.

```c

/* Unique object type ID */

#define K_OBJ_TYPE_MY_NEW_TYPE  K_OBJ_TYPE_ID_GEN("UNIQ")

struct my_obj_type_raw_info {
    ...
};

struct my_obj_type_query_stats {
    ...
};

struct my_new_obj {
    ...
    struct k_obj_core obj_core;
    struct my_obj_type_raw_info  info;
};

struct k_obj_core_stats_desc my_obj_type_stats_desc = {
    .raw_size = sizeof(struct my_obj_type_raw_stats),
    .query_size = sizeof(struct my_obj_type_query_stats),
    .raw = my_obj_type_stats_raw,
    .query = my_obj_type_stats_query,
    .reset = my_obj_type_stats_reset,
    .disable = NULL,    /* Stats gathering is always on */
    .enable = NULL,     /* Stats gathering is always on */
};

K_OBJ_TYPE_DEFINE_STATS(my_obj_type, my_new_obj, K_OBJ_TYPE_MY_NEW_TYPE,
                        &my_obj_type_stats_desc, info);
```
A type whose objects are not in an iterable section is initialized at run
time instead, before any of its objects. A permanent array of objects can be
registered as the type's range so that its objects need no registry entry.

```c

struct k_obj_type  my_obj_type;
struct my_new_obj  my_objects[8];

void my_obj_type_init(void)
{
    z_obj_type_init(&my_obj_type, K_OBJ_TYPE_MY_NEW_TYPE,
                    offsetof(struct my_new_obj, obj_core));
    k_obj_type_init_range(&my_obj_type, my_objects,
                          &my_objects[ARRAY_SIZE(my_objects)],
                          sizeof(struct my_new_obj), false);
    k_obj_type_stats_init(&my_obj_type, &my_obj_type_stats_desc);
}
```

### Initializing a New Object Core


Kernel objects that have already been integrated into the object core framework
automatically have their object cores initialized when the object is
initialized. However, developers that wish to add their own objects into the
framework need to both initialize the object core and register it. Registering
an object that belongs to the type's permanent range has no effect, as it is
reported from the range. The following code builds on the example above and
initializes the object core.

```c

void my_new_obj_init(struct my_new_obj *new_obj)
{
    ...
    k_obj_core_init(K_OBJ_CORE(new_obj), &my_obj_type);
    k_obj_core_link(K_OBJ_CORE(new_obj));
    k_obj_core_stats_register(K_OBJ_CORE(new_obj), &new_obj->raw_stats,
                              sizeof(struct my_obj_type_raw_info));
}
```

### Walking a List of Object Cores


Two routines exist for walking the object cores of an object type. These are
`k_obj_type_walk_locked` and `k_obj_type_walk_unlocked`. Both
visit the permanent objects of the type first and the registered objects next.
The following code builds upon the example above and prints the addresses of
all the objects of that new object type.

```c

int walk_op(struct k_obj_core *obj_core, void *data)
{
    uint8_t *ptr;

    ptr = obj_core;
    ptr -= obj_core->type->obj_core_offset;

    printk("%p\n", ptr);

    return 0;
}

void print_object_addresses(void)
{
    struct k_obj_type *obj_type;

    /* Find the object type */

    obj_type = k_obj_type_find(K_OBJ_TYPE_MY_NEW_TYPE);

    /* Walk the list of objects */

    k_obj_type_walk_unlocked(obj_type, walk_op, NULL);
}
```

### Object Core Statistics Querying


The following code builds on the examples above and shows how an object
integrated into the object core statistics framework can both retrieve queried
data and reset the stats associated with the object.

```c

struct my_new_obj my_obj;

...

void my_func(void)
{
    struct my_obj_type_query_stats  my_stats;
    int  status;

    my_obj_type_init(&my_obj);

    ...

    status = k_obj_core_stats_query(K_OBJ_CORE(&my_obj),
                                    &my_stats, sizeof(my_stats));
    if (status != 0) {
        /* Failed to get stats */
        ...
    } else {
        k_obj_core_stats_reset(K_OBJ_CORE(&my_obj));
    }

    ...
}
```
