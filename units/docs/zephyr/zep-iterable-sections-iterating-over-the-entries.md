---
id: "zep-iterable-sections-iterating-over-the-entries"
type: "concept"
domain: "rtos"
title: "Iterable Sections: Iterating over the entries"
summary: "Once the section is in place, iterate over its entries with STRUCT_SECTION_FOREACH:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/iterable_sections/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/iterable_sections/index.rst"
license: "Apache-2.0"
mode: "V"
---

Once the section is in place, iterate over its entries with
`STRUCT_SECTION_FOREACH`:

```c

STRUCT_SECTION_FOREACH(my_data, data) {
        printk("%p: a: %d, b: %d\n", data, data->a, data->b);
}
```

**Note:** The linker is going to place the entries sorted by name, so the example above would visit `d1`, `d2` and `d3` in that order, regardless of how they were defined in the code.
