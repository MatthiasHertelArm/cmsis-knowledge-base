---
id: "intr-practical-zephyr-devicetree-basics-node-names-unit-addresses-reg-and-labels"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Basic source file syntax / Node names, unit-addresses, `reg`, and labels"
summary: "Let's start from scratch. We create an empty Devicetree source file .dts with the following empty tree:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#node-names-unit-addresses-reg-and-labels"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Basic source file syntax_

Let's start from scratch. We create an empty Devicetree source file `.dts` with the following empty tree:

```dts
/dts-v1/;
/ { /* Empty. */ };
```

The first line contains the _tag_ `/dts-v1/;` which identifies the file as a version _1_ Devicetree source file. Without this tag, the Devicetree compiler would treat the file as being of the obsolete version _0_ - which is incompatible with the current major Devicetree version _1_ used by Zephyr. The tag `/dts-v1/;` is therefore required when working with Zephyr. Following the version tag is an empty Devicetree: Its only _node_ is the _root node_, identified by convention by a forward slash `/`.

> **Note:** Devicetree source files use `C/C++` style comments. You can use both, multi-line `/* ... */` and single-line `//` comments.

Within this root node, we can now define our own nodes in the form of a tree, kind of like a `JSON` object or nested `C` structure:

```dts
/dts-v1/;

/ {
  node {
    subnode {
      /* name/value properties */
    };
  };
};
```

Nodes are identified via their _node name_. Each node can have _subnodes_ and _properties_. In the above example, we have a node with the name _node_, containing a subnode named, well, _subnode_. For now, all you need to know about _properties_ is that they are name/value pairs.

A node in the Devicetree can be uniquely identified by specifying the full _path_ from the root node, through all subnodes, to the desired node, separated by forward slashes. E.g., our full path to our _subnode_ is `/node/subnode`.

Node names can also have an optional, hexadecimal _unit-address_, specified using an `@` and thus resulting in the full node name format `node-name@unit-address`. E.g., we could give our `subnode` the _unit-address_ `0123ABC` as follows:

```dts
/dts-v1/;

/ {
  node {
    subnode@0123ABC {
      reg = <0x0123ABC>;
      /* properties */
    };
  };
};
```

The _unit-address_ can be used to distinguish between several subnodes of the same type. It can be a real register address, typically a base address, e.g., the base address of the register space of a specific UART interface, but also a plain instance number, e.g., when describing a multi-core MCU by using a `/cpus` node, with two instances `cpu@0` and `cpu@1` for each CPU core. Each node with a _unit-address_ **must** also have the property `reg` - and any node _without_ a _unit-address_ must _not_ have the property `reg`. It may seem redundant now, but we'll learn more about the `reg` property later in this article.

Let's finish up on the node name with a convention that ensures that each node in the Devicetree can be uniquely identified by specifying its full _path_. For any node name and property at the same level in the tree:
- in the case of _node-name_ without an _unit-address_ the `node-name` must be unique,
- or if a node has a _unit-address_, then the full `node-name@unit-address` must be unique.

Now we can address all of our nodes using their full path. As you might imagine, within a more complex Devicetree the paths become quite long, and if you'd ever need to reference a node (we'll see how that works in practice later) this is quite tedious, which is why any node can be assigned a unique _node label_:

```dts
/dts-v1/;

/ {
  node {
    subnode_label: subnode@0123ABC {
      reg = <0x0123ABC>;
      /* properties */
    };
  };
};
```

Now, instead of using `/node/subnode@0123ABC` to identify the node, we can simply use its label `subnode_label` - which must be **unique** throughout the entire Devicetree. This form of the label syntax is known as a _node label_. This term is not explicitly defined in the Devicetree specification but is used extensively in Zephyr.

That's it for the first theory lesson - let's see how nodes look like in a real Devicetree source (_include_) file in Zephyr. The following is a snippet of the Devicetree source file for the nRF52840 microcontroller:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    uart0: uart@40002000 {
      reg = <0x40002000 0x1000>;
    };
    uart1: uart@40028000 {
      reg = <0x40028000 0x1000>;
    };
  };
};
```

The System-On-Chip is described using the `soc` node. The `soc` node contains two _uart_ instances, which match the UARTE instances that we can find in the register map of the nRF52840 datasheet (the `E` in UARTE refers to _EasyDMA_ support):

|  ID   | Base address | Peripheral | Instance | Description               |
| :---: | :----------: | :--------: | :------: | :------------------------ |
|   0   |  0x40000000  |   CLOCK    |  CLOCK   | Clock control             |
|       |     ...      |            |          |                           |
|   2   |  0x40002000  |   UARTE    |  UARTE0  | UART with EasyDMA, unit 0 |
|   3   |  0x40003000  |    SPIM    |  SPIM0   | SPI master 0              |
|       |     ...      |            |          |                           |
|  40   |  0x40028000  |   UARTE    |  UARTE1  | UART with EasyDMA, unit 1 |
|  41   |  0x40029000  |    QSPI    |   QSPI   | External memory interface |
|       |     ...      |            |          |                           |

As we can see, the _unit-address_ of each `uart` node matches its base address. The `reg` property seems to be some kind of value list enclosed in angle brackets `<...>`. The first value of the property matches the node's _unit-address_ and thus the base address of the UARTE instance, but the property also has a second value and thus provides more information than the _unit-address_ itself: Looking at the register map we can see that the second value `0x1000` matches the length of the address space that is reserved for each UARTE instance:

- The base address of the `UARTE0` instance is `0x40002000`, followed by `SPIM0` at `0x40003000`.
- The base address of the `UARTE1` instance is `0x40028000`, followed by `QSPI` at `0x40029000`.

Finally, each UART instance also has a unique label:
- `uart0` is the label of the node `/soc/uart@40002000`,
- `uart1` is the label of the node `/soc/uart@40028000`.

> **Note:** Throughout this article, we sometimes refer to _node_ labels as just "labels". The [Devicetree specification](https://www.devicetree.org/specifications/) also allows creating labels to reference properties and their values but Zephyr's DTS generator ignores this feature. We therefore use the terms _label_ and _node label_ interchangeably.
