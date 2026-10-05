---
id: "intr-practical-zephyr-devicetree-semant-labels-and-paths"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example / Labels and paths"
summary: "Before we move on to properties using phandle types, let's have a look at labels and paths."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#labels-and-paths"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Bindings by example_

Before we move on to properties using `phandle` types, let's have a look at labels and paths. In the previous article, we've seen that the [Devicetree specification](https://www.devicetree.org/specifications/) allows _labels_ not only to refer to _nodes_ but also to other positions in the Devicetree, e.g., in front of property _values_. In our example, we have three labels:

- One label `label_with_props` for our node `/node_with_props`,
- Two labels `second_value` and `string_value` for some property values.

`dts/playground/props-basics.overlay`
```dts
/ {
  label_with_props: node_with_props {
    compatible = "custom-props-basics";
    /* ... */
    array = <1 second_value: 2 3>;
    /* ... */
    string = string_value: "foo bar baz";
    string-array = "foo", "bar", "baz";
    /* ... */
  };
};
```

Zephyr's DTS generator accepts this input and - as we've seen - won't complain about the labels `second_value` and `string_value` referring to the property values. However, Zephyr simply ignores any label that doesn't refer to a _node_ and therefore doesn't generate anything usable for the property labels. Only the _node_ label `label_with_props` has a macro:

```bash
$ grep second_value ../build/zephyr/include/generated/devicetree_generated.h
$ grep string_value ../build/zephyr/include/generated/devicetree_generated.h
$ grep label_with_props ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_NODELABEL_label_with_props DT_N_S_node_with_props
```

> **Note:** In case you want some practice, look at the [Devicetree specification](https://www.devicetree.org/specifications/) and try to use references to value labels in your Devicetree. I promise it won't work either.

The following macros are generated to represent a node and its labels:

`build/zephyr/include/generated/devicetree_generated.h`
```c
/*
 * Devicetree node: /node_with_props
 *
 * Node identifier: DT_N_S_node_with_props
 * --snip--
 */
/* Node's full path: */
#define DT_N_S_node_with_props_PATH "/node_with_props"
/* Node's name with unit-address: */
#define DT_N_S_node_with_props_FULL_NAME "node_with_props"
// --snip--
/* Existence and alternate IDs: */
#define DT_N_S_node_with_props_EXISTS 1
#define DT_N_INST_0_custom_props_basics DT_N_S_node_with_props
#define DT_N_NODELABEL_label_with_props DT_N_S_node_with_props
```

The _node identifier_ that is used for our `/node_with_props` is `DT_N_S_node_with_props`, which is exactly what we'd expect knowing the node's path and from what we've learned about [understanding Devicetree macro names](#understanding-devicetree-macro-names). This _node identifier_ is itself just a _token_: No macro with the name `DT_N_S_node_with_props` exists!

_Identifiers_ are used by the macros of the [Devicetree API](#zephyrs-devicetree-api). As we'll see, these macros essentially do nothing but paste together different _tokens_. E.g., accessing a node's property's value, all we need to do is paste together _tokens_:

- Using the node identifier `DT_N_S_node_with_props`,
- and knowing that `_P_` is used for property names,
- we end up with `DT_N_S_node_with_props_P_int` for the property `int`.

In turn, a _label_ is nothing else than a different name for our node's identifier, as we can see in the above snippet of `devicetree_generated.h`. Labels use the format `DT_N_NODELABEL_<label_in_lowercase>` as the macro name and the node's identifier as the value.

In addition, the generator also produces macros with the suffix `_PATH` and `_FULL_NAME` that contain the node's full path and name including the unit address as string literals.

#### `/aliases` and `/chosen`

In the previous article about Devicetree basics, we've also seen the standard nodes `/aliases` and `/chosen`, defined by the [Devicetree specification](https://www.devicetree.org/specifications/). These nodes allow referring to a node using a _phandle_ (either using a reference to its label or the `${/full/path}` syntax), or the node's full path as a plain string. Let's try this out in our overlay file:

`dts/playground/props-basics.overlay`
```dts
/ {
  aliases {
    alias-by-label = &label_with_props;
    alias-by-path = &{/node_with_props};
    alias-as-string = "/node_with_props";
  };

  chosen {
    chosen-by-label = &label_with_props;
    chosen-by-path = &{/node_with_props};
    chosen-as-string = "/node_with_props";
  };
  /* ... previous content ... */
};
```

The node's aliases are translated to macros with the format `DT_N_ALIAS_<alias_in_lowercase>` in the node's section _"Existence and alternate IDs"_ that we've seen just before. Looking at the generated output it is now also clear why Zephyr makes no clear distinction between the terms _"references"_ and _"phandle"_:

```c
/* Existence and alternate IDs: */
#define DT_N_S_node_with_props_EXISTS 1
#define DT_N_ALIAS_alias_by_label       DT_N_S_node_with_props
#define DT_N_ALIAS_alias_by_path        DT_N_S_node_with_props
#define DT_N_ALIAS_alias_as_string      DT_N_S_node_with_props
#define DT_N_INST_0_custom_props_basics DT_N_S_node_with_props
#define DT_N_NODELABEL_label_with_props DT_N_S_node_with_props
```

Whether we reference a node using its label, a path reference, or its path as a string, it all translates to the node's _identifier_ token. The only difference is [the Devicetree API macro](#zephyrs-devicetree-api) that we use to obtain this token (or _node identifier_), as we'll see later.

Finally, `/chosen` nodes are listed in their own output section in `devicetree_generated.h`. The only difference to `/aliases` is, that each macro also gets its own `_EXISTS` pair:

```c
/*
 * Chosen nodes
 */
// --snip--
#define DT_CHOSEN_chosen_by_label         DT_N_S_node_with_props
#define DT_CHOSEN_chosen_by_label_EXISTS  1
#define DT_CHOSEN_chosen_by_path          DT_N_S_node_with_props
#define DT_CHOSEN_chosen_by_path_EXISTS   1
#define DT_CHOSEN_chosen_as_string        DT_N_S_node_with_props
#define DT_CHOSEN_chosen_as_string_EXISTS 1
```
