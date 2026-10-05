---
id: "intr-practical-zephyr-devicetree-semant-specifier-cells-in-phandle-array-s"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API / Specifier cells in `phandle-array`s"
summary: "We've seen how phandle-arrays are specified in DTS files, and how to create the corresponding bindings. Now, we finally see how to access the entries in phandle-array-of-ref-cells in our props-phandles.overlay:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#specifier-cells-in-phandle-array-s"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr's Devicetree API_

We've seen how `phandle-array`s are specified in DTS files, and how to create the [corresponding bindings](#phandle-array). Now, we finally see how to _access_ the entries in `phandle-array-of-ref-cells` in our `props-phandles.overlay`:

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_a: node_a {
    compatible = "custom-cells-a";
    #phandle-array-of-ref-cells = <2>;
    // - name for cell 0: "name-of-cell-one"
    // - name for cell 1: "name-of-cell-two"
    dummy-value = <0xc0ffee>;
  };
  label_b: node_b {
    compatible = "custom-cells-b";
    #phandle-array-of-ref-cells = <1>;
    // - name for cell 0: "name-of-cell-one"
  };

  node_refs {
    compatible = "custom-props-phandles";
    // --snip--
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;
  };
};
```

In the above Devicetree source we see that `phandle-array-of-refs` has two entries:
- The _phandle_ for `/node_a` is followed by two specifier cells _1_ and _2_,
- the _phandle_ for `/node_b` is followed by the specifier cell _1_.

> **Note:** Remember that in order to know where one entry starts and the next entry ends, it is necessary to check the `#<name>-cells` property of the referenced node. Typically, a _phandle_ marks the start of a new entry. The alternative syntax `<&{/node_a} 1 2>, <&label_b 1>` can be used to make the separation more visible.

Looking into the binding, we can also retrieve the _names_ of the corresponding cells:
- In the metadata for `/node_a`:
  - _1_ is the value for the cell with the name _name-of-cell-one_
  - _2_ is the value for the cell with the name _name-of-cell-two_
- In the metadata for `/node_b`:
  - _1_ is the value for the cell with the name _name-of-cell-one_

The above example is a bit unfortunate since it is very uncommon for a `phandle-array` to contain specifiers for different node types: `/node_a` and `/node_b` in the above example have nothing in common, and the specifier cell with index _0_ wouldn't even need to have the same name.

Nevertheless, we'll now squash them into the same self-defined structure using the Devicetree macros `DT_PHA_BY_IDX` and `DT_PHA_BY_IDX_OR`:

```c
typedef struct
{
    uint32_t cell_one;
    uint32_t cell_two;
} node_spec_t;

#define NODE_DT_SPEC_GET_BY_IDX(node_id, prop, idx)                            \
    {                                                                          \
        .cell_one = DT_PHA_BY_IDX(node_id, prop, idx, name_of_cell_one),       \
        .cell_two = DT_PHA_BY_IDX_OR(node_id, prop, idx, name_of_cell_two, 0), \
    }

// node_a = {.cell_one = 1, .cell_two = 2};
node_spec_t node_a = NODE_DT_SPEC_GET_BY_IDX(NODE_REFS, phandle_array_of_refs, 0);
// node_b = {.cell_one = 1, .cell_two = 0};
node_spec_t node_b = NODE_DT_SPEC_GET_BY_IDX(NODE_REFS, phandle_array_of_refs, 1);

// configure_node(node_a);
// configure_node(node_b);
```

As we can see, the _names_ of the specifier cells must be known by the application; it is not possible to access the specifier cells by their index. The above example is again a simplified version of how Devicetree APIs are used by device drivers: The node's specification is retrieved using a Devicetree macro, and the specification is then passed along to the corresponding API function.

We'll see how this works in detail in the next article, where we'll retrieve the associated `gpio` using `GPIO_DT_SPEC_GET`, and pass the specification to the matching `gpio_pin_configure_dt` function. We could, e.g., imagine writing a driver for a board's LEDs:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`
```dts
/ {
  leds {
    led0: led_0 {
      // gpio0: compatible = "nordic,nrf-gpio";
      gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
      // gpio-cells:
      //   - pin
      //   - flags
    };
  };
};
```

The following is some pseudo code, showing how a driver could provide a macro to assemble the GPIO configuration for the LED pin:

```c
#define LED_GPIO_SPEC_GET_BY_IDX(node_id, idx)                 \
    {                                                          \
        .pin   = DT_PHA_BY_IDX(node_id, gpios, idx, pin),      \
        .flags = DT_PHA_BY_IDX_OR(node_id, gpios, idx, flags), \
    }

// The application can then assemble its GPIO device specification ...
const device_spec_t led_gpio = LED_GPIO_SPEC_GET_BY_IDX(DT_NODELABEL(led0), 0);
// ... and use it in the corresponding API function.
(void) led_gpio_configure_dt(&led_gpio);
```

What's also shown in our own example is an `_OR` type macro: Such macros exist for practically all "normal" Devicetree macros and allow providing a default value in case the property does not exist - meaning its `_EXISTS` macro is _not defined_. Since `/node_b` does not have a specifier cell named `name-of-cell-two`, the field `cell_two` in its `node_spec_t` is always set to zero.

Without using conditional compilation or the `_OR` macro, any access would not compile, e.g.:

```c
(void) DT_PHA_BY_IDX(NODE_REFS, phandle_array_of_refs, 1, name_of_cell_two);
```

With that said and done, let's wrap up this article.
