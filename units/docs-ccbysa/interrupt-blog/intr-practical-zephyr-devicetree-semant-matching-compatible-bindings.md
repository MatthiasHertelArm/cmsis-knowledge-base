---
id: "intr-practical-zephyr-devicetree-semant-matching-compatible-bindings"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Towards bindings / Matching `compatible` bindings"
summary: "What's the difference between /soc/uart@40002000 and our /node_with_props? Admittedly, there are lots of differences, but the significant difference is that /soc/uart@40002000 has a compatible property. compatible is a standard property defined in the DTSpec, so let's look it up:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#matching-compatible-bindings"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Towards bindings_

What's the difference between `/soc/uart@40002000` and our `/node_with_props`? Admittedly, there are _lots_ of differences, but the significant difference is that `/soc/uart@40002000` has a **compatible** property. `compatible` is a standard property defined in the [DTSpec](https://www.devicetree.org/specifications/), so let's look it up:

> Property name `compatible`, value type `<stringlist>`.
>
> The `compatible` property value consists of one or more strings that define the specific programming model for the device. This list of strings should be used by a client program for device driver selection. The property value consists of a concatenated list of null-terminated strings, from most specific to most general. They allow a device to express its compatibility with a family of similar devices [...].
>
> The recommended format is `"manufacturer,model"`. [...] The compatible string should consist only of lowercase letters, digits and dashes, and should start with a letter. [...]

Let's rephrase this: `compatible` is a list of strings, where each string is essentially a reference to some _model_. The [DTSpec](https://www.devicetree.org/specifications/) uses a specific term for such models: They are called **bindings**.

The [DTSpec](https://www.devicetree.org/specifications/) defines _bindings_ as _"requirements [...] for how specific types and classes of devices are represented in the Devicetree."_ In very simple words, a binding defines the properties that a node (or its children) can or even must have, their exact type, and their **meaning**.

How is this any different from what we've been doing until now in our Devicetree source files? Well, without a _binding_, we can give a node any number of properties and can assign any property any value of any type, as long as all nodes, properties, and values are _syntactically_ sound. Also, any property name must be considered random. Let's take our own `node_with_props`:

`dts/playground/props-basics.overlay`
```dts
/ {
  node_with_props {
    int = <1>;
    string = "foo";
  };
};
```

The Devicetree compiler won't complain if we assign a `string` value to the property `int`. In fact, it doesn't even know whether or not `node_with_props` should have the `int` property at all. We could delete it and the compiler won't complain. We also don't know what the purpose of `int` or `string` is, what they mean, or what they're used for.

While the property names `int` or `string` are not very revealing as such, the same is also true for the `current-speed` property of the `/soc/uart@40002000` node in the nRF52840 Devicetree: Without any additional information, we can only _assume_ that this is the baud rate in bits/s, but we can't know for sure.

By providing _compatible bindings_, we're telling the Devicetree compiler to check whether the given node really matches the properties and types defined in a _binding_, and we're telling it what to do with the information provided in the Devicetree. Bindings also add **semantics to a Devicetree** by giving properties a _meaning_.

The [DTSpec](https://www.devicetree.org/specifications/) includes some standard bindings, e.g., bindings for serial devices such as our UART device. It thus defines how serial devices need to look like in a Devicetree. This binding includes the `current-speed` property:

| Field       | Details                                                                                                                                             |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property    | `current-speed`                                                                                                                                     |
| Value type  | `<u32>`                                                                                                                                             |
| Description | Specifies the current speed of a serial device in bits per second. A boot program should set this property if it has initialized the serial device. |
| Example     | 115,200 Baud: `current-speed = <115200>;`                                                                                                           |

> **Note:** In case you're wondering why `current-speed` is not listed in the _"Standard Properties"_ section in the [DTSpec](https://www.devicetree.org/specifications/), but all of a sudden appears in the section about "Serial devices" in the "Device Bindings", there's a very short answer for that: `current-speed` is only relevant for certain node types. It isn't a property that is globally defined and can be applied to any kind of node.

Finally, we're getting somewhere! We now know what the `current-speed` property is all about: We know its type, its physical unit, and its _meaning_. But this is just some table in the [DTSpec](https://www.devicetree.org/specifications/), how is this information represented in Zephyr?

_Bindings_ live outside the Devicetree. The [DTSpec](https://www.devicetree.org/specifications/) doesn't specify any file format or syntax that is used for bindings. Zephyr, like [Linux](https://docs.kernel.org/devicetree/bindings/writing-schema.html), uses `.yaml` files for its bindings. I'm assuming you're familiar with `YAML` - in case you're not, have a quick look at its [online documentation](https://yaml.org/).
