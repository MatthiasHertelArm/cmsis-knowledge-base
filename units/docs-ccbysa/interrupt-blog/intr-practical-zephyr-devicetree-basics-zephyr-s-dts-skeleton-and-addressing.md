---
id: "intr-practical-zephyr-devicetree-basics-zephyr-s-dts-skeleton-and-addressing"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Zephyr's DTS skeleton and addressing"
summary: "Ok - we've seen nodes, labels, properties, and value types including phandles, we know how Zephyr compiles the Devicetree and we've even seen the standard nodes /aliases and /chosen. Are we done yet? Almost."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#zephyr-s-dts-skeleton-and-addressing"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ok - we've seen nodes, labels, properties, and value types _including_ `phandles`, we know how Zephyr compiles the Devicetree and we've even seen the standard nodes `/aliases` and `/chosen`. Are we done yet? Almost. There's the famous _one last thing_ that is worth looking into before wrapping up on the Devicetree _basics_. Yes, these are the basics, there's more coming in the next article!

> **Note:** Technically, we're again describing **semantics** even though I've promised that we'll wait with that until the next article about _bindings_, but one of our goals was being able to read Zephyr Devicetree files. Without understanding the standard properties `#address-cells`, `#size-cells`, and `reg`, we'd hardly be able to claim that.

When [exploring Zephyr's build](#devicetree-includes-and-sources-in-zephyr), we've seen that our DTS file "include" tree ends up including a skeleton file `zephyr/dts/common/skeleton.dtsi`. The following is a stripped-down version of the full "include" tree that we've seen in the [introduction](#devicetree-includes-and-sources-in-zephyr) when building our empty application for the nRF52840 development kit:

```
nrf52840dk_nrf52840.dts
└── nordic/nrf52840_qiaa.dtsi
    └── nordic/nrf52840.dtsi
        └── arm/armv7-m.dtsi
            └── skeleton.dtsi
```

This `skeleton.dtsi` contains the minimal set of nodes and properties in a Zephyr Devicetree:

```dts
/ {
  #address-cells = <1>;
  #size-cells = <1>;
  chosen { };
  aliases { };
};
```

We've already seen the `/chosen` and `/aliases` nodes. The `#address-cells` and `#size-cells` properties look a lot like the [specifier cells](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-cell-names-cells) we've seen when looking at [the `phandle-array` type](#path-phandles-and-phandle-array), right?

Even though they match the naming convention, their purpose, however, is a different one: They provide the necessary _addressing_ information for nodes that use a _unit-addresses_. Too many new terms in one article? Let's quickly repeat what we've already seen in the section about [node names](#node-names-unit-addresses-reg-and-labels):

- Nodes can have addressing information in their node name. Such nodes use the name format `node-name@unit-address` and **must** have the property `reg`.
- Nodes _without_ a _unit-address_ in the node name do _not_ have the property `reg`.

Let's first have a look at what we can find out about `reg` in the [DTSpec](https://www.devicetree.org/specifications/):

> Property name `reg`, value type _32-bit integer cells_ encoded as an arbitrary number of _(address, length)_ pairs.
>
> The `reg` property describes the address of the device’s resources within the address space defined by its parent [...]. Most commonly this means the offsets and lengths of memory-mapped IO register blocks [...].
>
> The value consists of _32-bit integer cells_, composed of an arbitrary number of pairs of _address and length_, `<address length>`. The number of 32-bit cells required to specify the address and length are [...] specified by the `#address-cells` and `#size-cells` properties in the parent of the device node. If the parent node specifies a value of _0_ for `#size-cells`, the length field in the value of `reg` shall be omitted.

Bit much? Let's bring up our good old `uart@40002000` node from the nRF52840's DTS include file:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
#include <arm/armv7-m.dtsi>
#include "nrf_common.dtsi"

/ {
  soc {
    uart0: uart@40002000 { reg = <0x40002000 0x1000>; };
    uart1: uart@40028000 { reg = <0x40028000 0x1000>; };
  };
};
```

Using the information from the [DTSpec](https://www.devicetree.org/specifications/), we should now be able to tell for sure that `0x40002000` is the _address_ and `_0x1000` the _length_, right? Yes, but no: We've also learned that a 64-bit integer value is represented using two cells, thus `<0x40002000 0x1000>` could technically be a single 64-bit integer, and _length_ could be omitted. To be _really_ sure how `uart@40002000` is addressed, we need to look at the parent node's `#address-cells` and `#size-cells` properties. So what are those properties? Let's look them up in the [DTSpec](https://www.devicetree.org/specifications/):

> Property names `#address-cells`, `#size-cells`, value type _32-bit integer_.
>
> The `#address-cells` and `#size-cells` properties [...] describe how child device nodes should be addressed.
> - The `#address-cells` property defines the number of _32-bit integers_ used to encode the **address** field in a child node’s `reg` property.
> - The `#size-cells` property defines the number of _32-bit integers_ used to encode the **size** field in a child node’s `reg` property.
>
> The `#address-cells` and `#size-cells` properties are not inherited from ancestors in the Devicetree. [...] A DTSpec-compliant boot program shall supply `#address-cells` and `#size-cells` on **all** nodes that have children. If missing, a client program should assume a default value of _2_ for `#address-cells`, and a value of _1_ for `#size-cells`.

Ok, now we're getting somewhere: We need to look at the parent's properties to know how many cells in the `reg` property's value are used to encode the _address_ and the _length_. In the DTS file `zephyr/dts/arm/nordic/nrf52840.dtsi`, however, there are no such properties for `soc`.

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    /* Just nodes, no properties ... */
  };
};
```

So, do we need to assume the defaults defined in the [DTSpec](https://www.devicetree.org/specifications/)? We might have to, but we've learned that node properties don't all need to be provided in one place, and therefore the `#address-cells` and `#size-cells` of the `soc` might be provided by some includes.

Instead of going through all includes, we've seen that in Zephyr all includes are resolved by the preprocessor, and therefore a single Devicetree file is available in the build directory. You can therefore find the combined `soc`'s properties in `build/zephyr/zephyr.dts`. Since our include graph is rather easy to traverse, though, we'll also find the missing information in the CPU architecture's DTS file:

`zephyr/dts/arm/armv7-m.dtsi`

```dts
#include "skeleton.dtsi"

/ {
  soc {
    #address-cells = <1>;
    #size-cells = <1>;
    /* ... */
  };
};
```

Now we really can tell for sure that for our `uart@40002000` node, the `reg`'s value `<0x40002000 0x1000>` indeed refers to the _address_ `0x40002000` and the _length/size_ `0x1000`. This is also not surprising since the nRF52840 uses **32-bit architecture**.

We can also find an example of a **64-bit architecture** in Zephyr's DTS files:

`zephyr/dts/riscv/sifive/riscv64-fu740.dtsi`

```dts
/ {
  soc {
    #address-cells = <2>;
    #size-cells = <2>;

    uart0: serial@10010000 {
      reg = <0x0 0x10010000 0x0 0x1000>;
    };
  };
};
```

Here, `uart0`'s _address_ is formed by the 64-bit integer value `<0x0 0x10010000>` and the _length_ by the 64-bit integer value `<0x0 0x1000>`.

Addressing is not only used for register mapped devices but, e.g., also for _bus_ addresses. For this, let's have a look at [Nordic's Thingy:53](https://www.nordicsemi.com/Products/Development-hardware/Nordic-Thingy-53), a more complex board with several I2C peripherals connected to the nRF5340 MCU. The I2C bus of the nRF5340 uses the `#address-cells` and `#size-cells` properties to indicate that I2C nodes are uniquely identified via their address, no size is needed:

`zephyr/dts/arm/nordic/nrf5340_cpuapp_peripherals.dtsi`

```dts
i2c1: i2c@9000 {
  #address-cells = <1>;
  #size-cells = <0>;
};
```

In the _board_ DTS file, we find which I2C peripherals are actually hooked up to the I2C interface:
- The `BMM150` geomagnetic sensor uses the I2C address `0x10`,
- the `BH1749` ambient light sensor uses the I2C address `0x38`,
- and the `BME688` gas sensor the address `0x76`.

`zephyr/boards/nordic/thingy53/thingy53_nrf5340_common.dtsi`

```dts
&i2c1 {
  bmm150: bmm150@10 { reg = <0x10>; };
  bh1749: bh1749@38 { reg = <0x38>; };
  bme688: bme688@76 { reg = <0x76>; };
};
```

With this, we're really done with our Devicetree introduction.
