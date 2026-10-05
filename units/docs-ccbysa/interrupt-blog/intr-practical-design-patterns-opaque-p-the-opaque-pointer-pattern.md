---
id: "intr-practical-design-patterns-opaque-p-the-opaque-pointer-pattern"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: The Opaque Pointer Pattern"
summary: "In traditional OOP, an object has state (data) and behavior (functions) coupled together in one class."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#the-opaque-pointer-pattern"
license: "CC-BY-SA-4.0"
mode: "V"
---

*opaque: not able to be seen through; not transparent.*

In traditional OOP, an object has state (data) and behavior (functions) coupled together in
one class.

If you want to have something resembling objects in C, you can:

1. Define a struct with your state data
2. Define functions which take a pointer to the struct as the first parameter
3. Declare a variable with that struct type to create an instance of the "object"

Need another object instance? Declare another variable with that struct type.
Boom! Objects in C, baby!

Of course, there's a little more to it than that (but not much).

Before getting into the details, let me show you the complete pattern first, using a ring buffer
that stores `uint8_t` as an example.
This is not a complete ringbuffer implementation.
It's just enough to show you the general pattern.

`ringbuffer.h`

```c
#pragma once

#include <stdint.h>
#include <stdbool.h>

// Opaque pointer type to represent a ringbuffer instance
typedef struct ringbuffer_instance_t* ringbuffer_t;

// Functions that operate on an instance
ringbuffer_t ringbuffer_create(uint32_t capacity);
uint32_t ringbuffer_capacity(ringbuffer_t instance);
bool ringbuffer_enqueue(ringbuffer_t instance, uint8_t item);
bool ringbuffer_dequeue(ringbuffer_t instance, uint8_t* item);
void ringbuffer_destroy(ringbuffer_t instance);
```

`ringbuffer.c`

```c
#include "ringbuffer.h"
#include <stdlib.h>

// Private struct, only accessible from within this file
struct ringbuffer_instance_t {
    volatile uint32_t wr_pos;
    volatile uint32_t rd_pos;
    uint8_t* data;
    uint32_t capacity;
};

ringbuffer_t ringbuffer_create(uint32_t capacity) {
    ringbuffer_t inst = calloc(1, sizeof(struct ringbuffer_instance_t));
    inst->data = calloc(capacity, sizeof(uint8_t));
    inst->capacity = capacity;
    inst->wr_pos = 0;
    inst->rd_pos = 0;
    return inst;
}

uint32_t ringbuffer_capacity(ringbuffer_t instance) {
    return instance->capacity;
}

bool ringbuffer_enqueue(ringbuffer_t instance, uint8_t item) {
    // implementation omitted
    return true;
}

bool ringbuffer_dequeue(ringbuffer_t instance, uint8_t* item) {
    // implementation omitted
    return true;
}

void ringbuffer_destroy(ringbuffer_t instance) {
    if (instance) {
        if (instance->data) {
            free(instance->data);
        }
        free(instance);
    }
}
```
