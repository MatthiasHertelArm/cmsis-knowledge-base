---
id: "intr-practical-zephyr-devicetree-semant-understanding-devicetree-macro-names"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Towards bindings / Understanding Devicetree macro names"
summary: "Before we dig deeper, let's try to gain a better understanding of the macro names in devicetree_generated.h. Once we understand those, we should be able to know which macro (or macros) Zephyr should generate for our node's properties."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#understanding-devicetree-macro-names"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Towards bindings_

Before we dig deeper, let's try to gain a better understanding of the macro names in `devicetree_generated.h`. Once we understand those, we should be able to know which macro (or macros) Zephyr should generate for our node's properties.

In Zephyr's `doc` folder, you can find the _"RFC 7405 ABNF grammar for Devicetree macros"_ `zephyr/doc/build/dts/macros.bnf`. This RFC describes the macros that are directly generated out of the Devicetree sources. In simple words, the following rules apply (we've seen some of those already in the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt), but it really can't hurt to repeat them):

- `DT` is the common prefix for Devicetree macros,
- `S` is a forward slash `/`,
- `N` refers to a _node_,
- `P` is a _property_,
- all letters are converted to lowercase,
- and non-alphanumerics characters are converted to underscores "`_`"

Let's look at our favorite `/soc/uart@40002000` node, specified in the nRF52840's DTS file, and modified by the nRF52840 development kit's DTS file:

`zephyr/dts/arm/nordic/nrf52840.dtsi`
```dts
/ {
  soc {
    uart0: uart@40002000 {
      compatible = "nordic,nrf-uarte";
      reg = <0x40002000 0x1000>;
    };
  };
};
```

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`
```dts
&uart0 {
  compatible = "nordic,nrf-uarte";
  status = "okay";
  current-speed = <115200>;
  /* other properties */
};
```

Following the previous rules, we can transform the paths and property names into tokens:
- The node path `/soc/uart@40002000` is transformed to `_S_soc_S_uart_40002000`.
- The property name `current-speed` is transformed to `current_speed`.
- The property name `status` stays the same.

Since node paths are unique, by combining the node's path with its property names we can create a unique macro for each property - and that's exactly what Zephyr's Devicetree generator does. The leading `_N_` is used to indicate that it is followed by a node's path, `_P_` separates the node's path from its property. For `uart@40002000`, we get the following:

- `/soc/uart@40002000`, property `current-speed`
  becomes `N_S_soc_S_uart_40002000_P_current_speed`
- `/soc/uart@40002000`, property `status`
  becomes `N_S_soc_S_uart_40002000_P_status`

Adding the `DT_` prefix, we can indeed find those macros in `devicetree_generated`:

```bash
$ grep -sw DT_N_S_soc_S_uart_40002000_P_current_speed \
  ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_soc_S_uart_40002000_P_current_speed 115200

$ grep -sw DT_N_S_soc_S_uart_40002000_P_status \
  ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_soc_S_uart_40002000_P_status "okay"
```

For our little demo overlay we can do the same:

`dts/playground/props-basics.overlay`
```dts
/ {
  node_with_props {
    int = <1>;
    string = "foo";
  };
};
```

For `/node_with_props`' properties, the generator should create the following macros:
- `DT_N_S_node_with_props_P_int` for the property `int`,
- `DT_N_S_node_with_props_P_string` for the property `string`.

Thus, in our `devicetree_generated.h` we should be able to find the above macros - but we don't:

```bash
$ grep -sw DT_N_S_node_with_props_P_int \
  ../build/zephyr/include/generated/devicetree_generated.h

$ grep -sw DT_N_S_node_with_props_P_string \
  ../build/zephyr/include/generated/devicetree_generated.h
```

Something's still missing.
