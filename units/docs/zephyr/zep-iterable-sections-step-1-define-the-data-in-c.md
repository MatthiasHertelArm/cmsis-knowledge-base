---
id: "zep-iterable-sections-step-1-define-the-data-in-c"
type: "concept"
domain: "rtos"
title: "Iterable Sections: Step 1: Define the data in C"
summary: "Define the struct in a common header and provide a helper macro that instantiates entries with STRUCT_SECTION_ITERABLE:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/iterable_sections/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/iterable_sections/index.rst"
license: "Apache-2.0"
mode: "V"
---

Define the struct in a common header and provide a helper macro that
instantiates entries with `STRUCT_SECTION_ITERABLE`:

```c

struct my_data {
         int a, b;
};

#define DEFINE_DATA(name, _a, _b) \
         STRUCT_SECTION_ITERABLE(my_data, name) = { \
                 .a = _a, \
                 .b = _b, \
         }

...

DEFINE_DATA(d1, 1, 2);
DEFINE_DATA(d2, 3, 4);
DEFINE_DATA(d3, 5, 6);
```
For ROM-resident iterables, the instances must be declared `const` so the
compiler emits them into a read-only input section. The C declaration and the
CMake placement (see Step 2) must agree on RAM vs. ROM placement.
