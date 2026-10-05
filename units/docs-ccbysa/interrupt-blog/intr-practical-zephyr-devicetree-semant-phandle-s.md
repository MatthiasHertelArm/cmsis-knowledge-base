---
id: "intr-practical-zephyr-devicetree-semant-phandle-s"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API / `phandle`s"
summary: "We've seen that properties of the types phandle and phandles produce the same output, with the only difference being that the output of phandle only generates a single set of macros."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#phandle-s"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr's Devicetree API_

We've seen that properties of the types [`phandle` and `phandles`](#path-phandle-and-phandles) produce the same output, with the only difference being that the output of `phandle` only generates a single set of macros. Since the values of _phandle_ macros are still just _node identifiers_, we need to make a tiny adaption for our referenced `/node_a` to show how they are used; we're adding the property `dummy-value` of type `int` in the overlay:

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_a: node_a {
    compatible = "custom-cells-a";
    #phandle-array-of-ref-cells = <2>;
    dummy-value = <0xc0ffee>;
  };
  label_b: node_b {
    compatible = "custom-cells-b";
    #phandle-array-of-ref-cells = <1>;
  };

  node_refs {
    compatible = "custom-props-phandles";
    // --snip--
    phandle-by-path = <&{/node_a}>;
    phandle-by-label = <&label_a>;
    phandles = <&{/node_a} &label_b>;
    // --snip--
  };
};
```

An update of the binding is also necessary since otherwise Zephyr's generator won't produce any output:

`dts/bindings/custom-cells-a.yaml`
```yaml
description: Dummy for matching "cells"
compatible: "custom-cells-a"

properties:
  dummy-value:
    type: int
# --snip--
```

For _phandles_ from properties of type `phandle` or `phandles` it is possible to retrieve the node identifier using the `DT_PHANDLE` and `DT_PHANDLE_BY_IDX` Devicetree macros. The former can only be used for `phandle` types, whereas the latter is usable by both since both types provide the required macros including indices `_IDX`:

```c
// Identifier of /node_refs.
#define NODE_REFS DT_PATH(node_refs)

// Identifiers of /node_a and /node_b via the phandle properties in /node_refs.
#define NODE_A_PHANDLE_BY_LABEL DT_PHANDLE(NODE_REFS, phandle_by_label)
#define NODE_A_PHANDLE_BY_PATH  DT_PHANDLE(NODE_REFS, phandle_by_path)
#define NODE_A_PHANDLES         DT_PHANDLE_BY_IDX(NODE_REFS, phandle_array, 0)
#define NODE_B_PHANDLES         DT_PHANDLE_BY_IDX(NODE_REFS, phandle_array, 1)
```

The macros with the prefix `NODE_A_` resolve to `DT_N_S_node_a`, and `NODE_B_PHANDLES` to `DT_N_S_node_b`. Once you have the node's identifier, you can access its properties as usual, e.g., our newly added `dummy-value`, using the `DT_PROP` macro:

```c
uint32_t val_from_prop = DT_PROP(NODE_A_PHANDLE_BY_LABEL, dummy_value);
```

Since this is a very common use case, Zephyr's Devicetree API also contains the macros `DT_PROP_BY_PHANDLE` and `DT_PROP_BY_PHANDLE_IDX`, which allow reading a property's value without having to retrieve the node identifier using the corresponding `DT_PHANDLE` macros first - which is the recommended approach:

```c
uint32_t val_from_phandle_by_label = DT_PROP_BY_PHANDLE(NODE_REFS, phandle_by_label, dummy_value);
uint32_t val_from_phandle_by_path  = DT_PROP_BY_PHANDLE(NODE_REFS, phandle_by_path, dummy_value);
uint32_t val_from_phandles         = DT_PROP_BY_PHANDLE_IDX(NODE_REFS, phandles, 0, dummy_value);
```
