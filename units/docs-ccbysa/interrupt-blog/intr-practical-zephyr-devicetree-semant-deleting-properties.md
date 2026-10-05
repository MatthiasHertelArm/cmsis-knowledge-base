---
id: "intr-practical-zephyr-devicetree-semant-deleting-properties"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example / Deleting properties"
summary: "In our props-basics.overlay example we've seen the boolean property existent-boolean. We've learned that a boolean is set to true if it exists in the Devicetree, otherwise, it is false."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#deleting-properties"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Bindings by example_

In our `props-basics.overlay` example we've seen the boolean property `existent-boolean`. We've learned that a boolean is set to _true_ if it exists in the Devicetree, otherwise, it is _false_. Let's assume that a boolean property exists in some include file, how could you set this property to _false_ in your overlay? You'd somehow need to be able to tell the compiler to _remove_ the property since that is the only way to set it to _false_.

We can try this in our existing `dts/playground/props-basics.overlay`, where `node_with_props` has `existent-boolean` in its properties and thus sets its value to _true_. Without modifying `node_with_props` directly, we can _delete_ the property after the node's declaration using `/delete-property/`. We'll do this for both, `existent-boolean` and `string`, as follows:

`dts/playground/props-basics.overlay`
```dts
/ {
  label_with_props: node_with_props {
    compatible = "custom-props-basics";
    existent-boolean;
    /* --snip-- */
  };
};

&label_with_props {
  /delete-property/ existent-boolean;
  /delete-property/ string;
}
```

This leads to the same generated output as if the properties were not defined in the node at all. As we've seen, for `boolean`s the property's value is simply set to _0_. For the property `string`, no more macros are generated.

```c
#define DT_N_S_node_with_props_P_existent_boolean 0
#define DT_N_S_node_with_props_P_existent_boolean_EXISTS 1
/* No macros DT_N_S_node_with_props_P_string ... */
```
