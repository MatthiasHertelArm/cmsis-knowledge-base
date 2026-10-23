---
id: "zep-stacks-implementation"
type: "concept"
domain: "rtos"
title: "Stacks: Implementation"
summary: "A stack is defined using a variable of type k_stack. It must then be initialized by calling k_stack_init or k_stack_alloc_init. In the latter case, a buffer is not provided and it is instead allocated from the calling thread's resource pool."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/stacks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/stacks.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Stack


A stack is defined using a variable of type `k_stack`.
It must then be initialized by calling `k_stack_init` or
`k_stack_alloc_init`. In the latter case, a buffer is not
provided and it is instead allocated from the calling thread's resource
pool.

The following code defines and initializes an empty stack capable of holding
up to ten word-sized data values.

```c

#define MAX_ITEMS 10

stack_data_t my_stack_array[MAX_ITEMS];
struct k_stack my_stack;

k_stack_init(&my_stack, my_stack_array, MAX_ITEMS);
```
Alternatively, a stack can be defined and initialized at compile time
by calling `K_STACK_DEFINE`.

The following code has the same effect as the code segment above. Observe
that the macro defines both the stack and its array of data values.

```c

K_STACK_DEFINE(my_stack, MAX_ITEMS);
```

### Pushing to a Stack


A data item is added to a stack by calling `k_stack_push`.

The following code builds on the example above, and shows how a thread
can create a pool of data structures by saving their memory addresses
in a stack.

```c

/* define array of data structures */
struct my_buffer_type {
    int field1;
    ...
};
struct my_buffer_type my_buffers[MAX_ITEMS];

/* save address of each data structure in a stack */
for (int i = 0; i < MAX_ITEMS; i++) {
    k_stack_push(&my_stack, (stack_data_t)&my_buffers[i]);
}
```

### Popping from a Stack


A data item is taken from a stack by calling `k_stack_pop`.

The following code builds on the example above, and shows how a thread
can dynamically allocate an unused data structure.
When the data structure is no longer required, the thread must push
its address back on the stack to allow the data structure to be reused.

```c

struct my_buffer_type *new_buffer;

k_stack_pop(&buffer_stack, (stack_data_t *)&new_buffer, K_FOREVER);
new_buffer->field1 = ...
```
