---
id: "intr-practical-zephyr-devicetree-semant-node-identifiers"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API / Node identifiers"
summary: "Let's review how we can reference a node in the Devicetree using our props-basics.overlay:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#node-identifiers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr's Devicetree API_

Let's review how we can reference a node in the Devicetree using our `props-basics.overlay`:

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

  label_with_props: node_with_props {
    /* ... */
  };
};
```

> **Note:** We're deliberately skipping references to a node using `phandle` properties since those are _properties_, and properties are accessed differently, as we'll see in the next section (yes, technically node references in `/chosen` and `/aliases` are properties too, but those nodes are predefined by the [Devicetree specification](https://www.devicetree.org/specifications/)).

Having thoroughly explored Devicetree, we know that we have the following possibilities to refer to a node:
- Using the `/aliases` or `/chosen` nodes,
- using a globally unique _node label_,
- or via the node's full _path_.

In the previous article, we've learned that it is up to you to decide which way to reference nodes in your application. It typically makes sense to use `/aliases` or `/chosen` nodes, since paths and even node labels can be different for, e.g., different boards.

How can we reference nodes? We know that nodes as such do not exist in Zephyr's generated Devicetree: Nodes are translated into _tokens_ and thus do not have any value on their own. In Zephyr, these tokens are referred to as _node identifiers_ and they are used as parameters by other macros, e.g., to retrieve a property value. Such tokens are practically just prefixes for property macros.

Enough talk. Let's start with `/aliases`: Zephyr provides the `DT_ALIAS` macro to get a node's identifier via its alias:

```c
// Node identifier by /aliases node.
// DT_ALIAS(alias) = DT_N_ALIAS_ ## alias
#define NODE_PROPS_ALIAS_BY_LABEL   DT_ALIAS(alias_by_label)
#define NODE_PROPS_ALIAS_BY_PATH    DT_ALIAS(alias_by_path)
#define NODE_PROPS_ALIAS_BY_STRING  DT_ALIAS(alias_as_string)
```

The `DT_ALIAS` macro simply pastes `DT_N_ALIAS_` and the given node identifier and therefore resolves to the macros that we've already seen in the section about [`/aliases` and `/chosen`](#aliases-and-chosen). In turn, all alias macros resolve to the node identifier `DT_N_S_node_with_props`.

| API                         | Pasted macro                 | Node identifier          |
| :-------------------------- | :--------------------------- | :----------------------- |
| `DT_ALIAS(alias_by_label)`  | `DT_N_ALIAS_alias_by_label`  | `DT_N_S_node_with_props` |
| `DT_ALIAS(alias_by_path)`   | `DT_N_ALIAS_alias_by_path`   | `DT_N_S_node_with_props` |
| `DT_ALIAS(alias_as_string)` | `DT_N_ALIAS_alias_as_string` | `DT_N_S_node_with_props` |

You might have noticed that the properties in the DTS file use _dashes_, e.g., "`alias-by-label`", whereas in the code we need to replace the dashes with _underscores_ for the alias name, resulting in `alias_by_label`. We've learned this transformation in the section about [understanding Devicetree macro names](#understanding-devicetree-macro-names). The macros in the API, however, cannot change the format of their parameters and thus identifiers. Therefore, _you_ have to perform the **"lowercase-and-underscores"** transformation for all identifiers passed to Devicetree API macros:

- All letters are converted to lowercase,
- and non-alphanumeric characters are converted to underscores "`_`".

No other transformations are needed, e.g., you'll never need to provide a path with `/` replaced by `_S_` or prefix Devicetree macros yourself. The Devicetree API does that for you and provides macros for __all__ such use cases.

As mentioned before, the resulting _node identifier_ `DT_N_S_node_with_props` is only a _token_. No macro with the same name exists, the following search does not yield any results:

```bash
$ grep -E 'DT_N_S_node_with_props[ \t]' \
  ../build/zephyr/include/generated/devicetree_generated.h

```

Therefore, we cannot use a node identifier on its own anywhere in the code. Well, since it is a _token_, technically we could use it, e.g., as variable name, but that's not the point (and please don't do that). The point is, that the `C` preprocessor cannot further resolve the token, and wherever you'd use the node identifier `DT_N_S_node_with_props`, it would be placed as text (not as string literal) in code.

Moving on! Just like for `/aliases`, Zephyr provides the `DT_CHOSEN` macro to get a node's identifier via the `/chosen` node:

```c
// Node identifier by /chosen node.
// DT_CHOSEN(chosen) = DT_N_CHOSEN_ ## chosen
#define NODE_PROPS_CHOSEN_BY_LABEL  DT_CHOSEN(chosen_by_label)
#define NODE_PROPS_CHOSEN_BY_PATH   DT_CHOSEN(chosen_by_path)
#define NODE_PROPS_CHOSEN_AS_STRING DT_CHOSEN(chosen_as_string)
```

The `DT_CHOSEN` macro simply pastes `DT_N_CHOSEN_` and the given node identifier and again resolves to the macros that we've seen in the section about [`aliases` and `chosen`](#aliases-and-chosen). Just like the aliases, all chosen nodes resolve to the node identifier `DT_N_S_node_with_props`:

| API                           | Pasted macro                   | Node identifier          |
| :---------------------------- | :----------------------------- | :----------------------- |
| `DT_CHOSEN(chosen_by_label)`  | `DT_N_CHOSEN_chosen_by_label`  | `DT_N_S_node_with_props` |
| `DT_CHOSEN(chosen_by_path)`   | `DT_N_CHOSEN_chosen_by_path`   | `DT_N_S_node_with_props` |
| `DT_CHOSEN(chosen_as_string)` | `DT_N_CHOSEN_chosen_as_string` | `DT_N_S_node_with_props` |

This leaves us with node labels and retrieving a node's identifier by its path. Zephyr provides the two macros `DT_NODELABEL` and `DT_PATH` for this:

```c
// Node identifier by label.
// DT_NODELABEL(label) = DT_N_NODELABEL_ ## label
#define NODE_PROPS_BY_LABEL DT_NODELABEL(label_with_props)

// Node identifier by path.
// DT_PATH(...) = DT_N_ pasted with S_<node> for all nodes in the path.
#define NODE_PROPS_BY_PATH  DT_PATH(node_with_props)
```

The `DT_NODELABEL` is again a simple token pasting of `DT_N_NODELABEL_` and the provided _label_, resulting in the macro `DT_N_NODELABEL_label_with_props` that we've seen in the section about [labels and paths](#labels-and-paths), which again resolves to the node identifier `DT_N_S_node_with_props`.

The macro `DT_PATH` is a _variadic_ macro that allows retrieving a node's identifier using its full path. The path to a node is specified by the sequence of nodes, starting at the root node `/`. Each argument is thus a _node identifier_; the root node `/` is omitted. The Devicetree API simply pastes `DT_N` and `_S_<node>` for each node (in the "lowercase-and-underscores" form) in the path, resulting in the _nodde identifier_ `DT_N_S_node_with_props`.

> **Note:** The path `/soc/uart@40002000` is an example of a node that is two levels deep, obtained using `DT_PATH(soc, uart_40002000)`. Notice that it is **not** possible to use node labels in paths.
