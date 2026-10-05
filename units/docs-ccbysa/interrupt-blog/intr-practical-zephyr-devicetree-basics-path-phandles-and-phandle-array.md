---
id: "intr-practical-zephyr-devicetree-basics-path-phandles-and-phandle-array"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): References and `phandle` types / `path`, `phandles` and `phandle-array`"
summary: "Part of: References and phandle types"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#path-phandles-and-phandle-array"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: References and `phandle` types_

In addition to the `phandle` type, three more types are available in Zephyr when dealing with `phandle`s and references:


| Zephyr type     | DTSpec equivalent      | Example                                |
| :-------------- | :--------------------- | :------------------------------------- |
| `path`          | `32-bit integer cells` | `zephyr,console = &uart0;`             |
| `phandle`       | `phandle`              | `pinctrl-0 = <&uart0_default>;`        |
| `phandles`      | `32-bit integer cells` | `cpu-power-states = <&idle &suspend>;` |
| `phandle-array` | `32-bit integer cells` | `gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;` |

Let's go through the remaining types one by one, starting with `path`s: In our previous example, we've enclosed the references in `<` and `>` and ended up with our `phandle` type. If we don't place the reference within `<` and `>`, the [DTSpec](https://www.devicetree.org/specifications/) defines the following behavior:

> "Outside a cell array, a reference to another node will be expanded to that node's full path."

So let's try this out: Let's first get rid of the properties `phandle-by-path` and `phandle-by-label`, and create two new properties `path-by-path` and `path-by-label` as follows:

```dts
/ {
  label_a: node_a { /* Empty. */ };
  node_refs {
    path-by-path = &{/node_a};
    path-by-label = &label_a;
  };
};
```

If we now execute `west build`, we can see something interesting in our generated `zephyr.dts`:

`build/zephyr/zephyr.dts`

```dts
/dts-v1/;

/ {
  /* Lots of other nodes ... */
  label_a: node_a {
  };
  node_refs {
    path-by-path = &{/node_a};
    path-by-label = &label_a;
  };
};
```

The `phandle` property for `node_a` is gone! The reason for this is simple - and also matches exactly what is stated in the [DTSpec](https://www.devicetree.org/specifications/): The references used for the values of the properties `path-by-path` and `path-by-label` are really just a different notation for the path `/node_a`. They are **not** `phandle`s, and therefore do not require a property _phandle_ in the referenced node.

In Zephyr, you'll encounter `path`s exclusively for properties of the standard nodes `/aliases` and `/chosen`, both of which we'll see in a [later section in this article](#about-aliases-and-chosen). Meaning: You can't actually use `path`s for your own nodes.

Next, `phandles`. This is not a typo: The plural form `phandles` of `phandle` is really a separate type in Zephyr, and it's as simple as it sounds: Instead of supporting only a single _reference_ - or _phandle_ - in its value, it is an **array** of _phandles_. Let's create another `node_b` and change `node_refs` to contain only a new property `phandles` and recompile:


```dts
/ {
  label_a: node_a { };
  label_b: node_b { };
  node_refs {
    phandles = <&{/node_a} &label_b>;
  };
};
```
`build/zephyr/zephyr.dts`

```dts
/dts-v1/;

/ {
  /* Lots of other nodes ... */
  label_a: node_a {
    phandle = < 0x1c >;
  };
  label_b: node_b {
    phandle = < 0x1d >;
  };
  node_refs {
    phandles = < &{/node_a} &label_b >;
  };
};
```

The output is not surprising: Both nodes are now referenced by `node_ref`'s `phandles` and therefore get their own `phandle` property. The `phandles` type is especially useful when we need to reference nodes of the same type, like the `cpu-power-states` example in the previous table.

This leaves us with the last type `phandle-array`, a type that is used quite a lot in Devicetree. Let's go by example:

```dts
/ {
  label_a: node_a {
    #phandle-array-of-ref-cells = <2>;
  };
  label_b: node_b {
    #phandle-array-of-ref-cells = <1>;
  };
  node_refs {
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 3>;
  };
};
```
`build/zephyr/zephyr.dts`

```dts
/dts-v1/;

/ {
  /* Lots of other nodes ... */
  label_a: node_a {
    #phandle-array-of-ref-cells = < 0x2 >;
    phandle = < 0x1c >;
  };
  label_b: node_b {
    #phandle-array-of-ref-cells = < 0x1 >;
    phandle = < 0x1d >;
  };
  node_refs {
    phandle-array-of-refs = < &{/node_a} 0x1 0x2 &label_b 0x3 >;
  };
};
```

So what's this `phandle-array` type? It is a list of phandles _with metadata_ for each phandle. This is how it works:

- By convention, a `phandle-array` property is plural and its name should thus end with "_s_".
- The value of a `phandle-array` property is an array of phandles, but each phandle can be followed by cells (32-bit values), sometimes also called a phandle's "metadata". In the example above, the two values `1 2` are `&{/node_a}`'s _metadata_, whereas `3` is `&label_b`'s metadata.
- The new properties `#phandle-array-of-ref-cells` tell the compiler how many metadata _cells_ are supported by the corresponding node. Such properties are called [specifier cells](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-cell-names-cells): In our example, `node_a` specifies that the node supports _two_ cells, `node_b`'s specifier cell only allows _one_ cell after its phandle.

_Specifier cells_ like `#phandle-array-of-ref-cells` have a defined naming convention: The name is formed by removing the plural '_s_' and attaching '_-cells_' to the name of the `phandle-array` property. For our property _phandle-array-of-refs_, we thus end up with _phandle-array-of-ref~~s~~**-cells**_.

If you've been browsing Zephyr's Devicetree files, you may have noticed that the property `#gpio-cells` doesn't follow the specifier cell naming convention: Every rule has its exceptions, and in case you're interested in details, I'll leave you with a reference to [Zephyr's documentation on specifier cells](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-cell-names-cells).

Before we look at a real-world example of a `phandle-array`, let's sum up `phandle` types. You'll find this exact list also in [Zephyr's documentation on `phandle` types](https://docs.zephyrproject.org/latest/build/dts/phandles.html), but since it is a short one, I hope it's OK to borrow it:

- To reference exactly one node, use the `phandle` type.
- To reference _zero_ or more nodes, we use the `phandles` type.
- To reference _zero_ or more nodes **with** metadata, we use a `phandle-array`.

In case you're still confused, we'll look at a real-world example for a `phandle-array` just now.


#### Syntax and semantics for `phandle-array`s

In case you've been experimenting with the above overlay, you may have noticed that I've been cheating a little: The project still _compiles_ just fine even if you delete the `#phandle-array-of-ref-cells` properties, or give `phandle-array-of-refs` a different name that does _not_ end in an _s_.

Why? Our Devicetree is still _syntactically_ correct even if we do not follow the given convention. In the end, `phandle-array-of-refs` is simply an array of cells since every reference is expanded to the node's `phandle` property's value - even without the expansion, its syntax would still fit an array of 32-bit integer cells. A _syntactically_ sound Devicetree, however, is only half the job: Eventually, we'll have to define some _schema_ and add _meaning_ to all the properties and their values; we'll have to define the Devicetree's **semantics**.

Without semantics, the DTS generator can't make sense of the provided Devicetree and therefore also won't generate anything that you'd be able to use in your application. Once you add semantics to your nodes, you'll have to strictly follow the previous convention, which is also why I've already included the notation in this article. The details, however, we'll explore in the next article about Devicetree _bindings_.


#### `phandle-array` in practice

How are `phandle-array`s used in practice? Let's look at the nRF52840's _General Purpose input and outputs (GPIOs)_. In the datasheet, we can find the following table on the GPIO instances:

| Base address | Peripheral | Instance | Description  | Configuration  |
| :----------: | :--------: | :------: | :----------- | :------------- |
|  0x50000000  |    GPIO    |    P0    | GPIO, port 0 | P0.00 to P0.31 |
|  0x50000300  |    GPIO    |    P1    | GPIO, port 1 | P1.00 to P1.15 |

Thus, the nRF52840 uses two instances `P0` and `P1` of the GPIO peripheral to expose control over its GPIOs. In the nRF52840 DTS include file, we find the matching nodes `gpio0` for port _0_ and `gpio1` for port _1_:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    gpio0: gpio@50000000 {
      compatible = "nordic,nrf-gpio";
      gpio-controller;
      reg = <0x50000000 0x200 0x50000500 0x300>;
      #gpio-cells = <2>;
      status = "disabled";
      port = <0>;
    };

    gpio1: gpio@50000300 {
      compatible = "nordic,nrf-gpio";
      gpio-controller;
      reg = <0x50000300 0x200 0x50000800 0x300>;
      #gpio-cells = <2>;
      ngpios = <16>;
      status = "disabled";
      port = <1>;
    };
  };
};
```

With this structure it is clear that we cannot just reference the entire `gpio` instance in case we want to control only one pin: We always have to choose either `gpio0` or `gpio1` _and_ specify at least which exact _pin_ of the _port_ we need. Let's see how this is solved in the nRF52840 development kit's Devicetree source file.

The nRF52840 development kit connects LEDs to the nRF52840 MCU, which are described using the node `leds` in the board's DTS file. Within this Devicetree, we now see how the `led` instances reference to the nRF52840's GPIOs: E.g., `gpio0` is used in `led0`'s property `gpios` using a `phandle-array`:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 {
      gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
      label = "Green LED 0";
    };
  };
};
```

There are no individual nodes for each pin in the nRF52840's Devicetree. Therefore, when referencing the `gpio0` node, we need to be able to tell exactly which pin we're using for our LED. In addition, we also typically need to provide some configuration for our pin, e.g., set the pin to _active low_.

The nodes `gpio0` and `gpio1` both contain the _specifier cells_ `#gpio-cells` which indicate that we need to pass exactly two _cells_ to use the node in a `phandle-array`. In the `led0`'s property `gpios` of type `phandle-array` we can see that we do exactly that: We use the two cells to specify the _pin_ and _flags_ that we're using for the LED. Now, how would we know that `13` is the pin number and `GPIO_ACTIVE_LOW` is a flag?

As we've seen before, without additional information all the DTS compiler can do is make sure the _syntax_ of your file is correct. It doesn't know anything about the **semantics** and therefore can't really associate the values in the `phandle-array` to `gpio0`. It therefore also doesn't care about any semantic requirements.

In the next article, we'll see how to use the standard property `compatible` and so-called **bindings** to provide the semantics - and thus the information that we need to associate the first cell with the _pin_ number and the second cell with the _flags_.
