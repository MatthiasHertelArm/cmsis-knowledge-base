---
id: "intr-practical-zephyr-devicetree-semant-macrobatics"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API / Macrobatics"
summary: "Having seen the macros provided by Zephyr's generator script, it is now pretty obvious how nodes and property values are accessed by Zephyr's Devicetree API: The big \"mystery\" behind the Devicetree API is token pasting."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#macrobatics"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr's Devicetree API_

Having seen the macros provided by Zephyr's generator script, it is now pretty obvious how nodes and property values are accessed by Zephyr's Devicetree API: The big "mystery" behind the Devicetree API is _token pasting_. In its simplest form, tokens are pasted or concatenated using the token-pasting operator `##`:

```c
// Let's assume we use macros with the format <node identifier>_<property>,
// e.g., a "node" with property "string_value" set to "123-test"
#define node_string_value "123-test"

// Tokens in C macros are pasted using `##`.
#define TOKEN_CAT_3(a1, a2, a3)      a1##a2##a3
#define NODE_PROP(node_id, property) TOKEN_CAT_3(node, _, property)

// The following resolves to `node_string_value` and thus to "123-test"
static const char *str = NODE_PROP(node, string_value);
```

Zephyr takes token pasting to another level in its Devicetree API, using variadic macro arguments, macro repetitions, and other neat tricks. In his presentation ["Zephyr Devicetree Mysteries, Solved"](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe) from the _Zephyr Development Summit 2022_, Martí Bolívar fittingly describes those mechanisms as _"macrobatics"_.

> **Note:** I highly recommend watching [his presentation](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe) (maybe after reading through this article), and if you're curious, digging into `util_macro.h` and `util_loops.h` in `zephyr/include/zephyr/sys`. The files are very well documented, and the macros `MACRO_MAP_CAT` (used by the `DT_PATH`) and `IS_ENABLED` (resolving the `_EXISTS` macros) are especially interesting.
