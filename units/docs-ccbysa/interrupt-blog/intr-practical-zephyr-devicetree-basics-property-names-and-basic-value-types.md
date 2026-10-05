---
id: "intr-practical-zephyr-devicetree-basics-property-names-and-basic-value-types"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Basic source file syntax / Property names and basic value types"
summary: "Let's now have a look at properties. As we've already seen for the property reg, properties consist of a name and a value and are used to describe the characteristics of the node. Property names can contain:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#property-names-and-basic-value-types"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Basic source file syntax_

Let's now have a look at properties. As we've already seen for the property `reg`, properties consist of a _name_ and a _value_ and are used to describe the characteristics of the node. Property names can contain:

- digits `0-9`,
- lower and uppercase letters `a-z` and `A-Z`,
- and any of the special characters `.,_+?#-`.

Most of the properties you'll encounter in Zephyr simply use `kebab-case` names, though you'll also encounter properties starting with a `#`, e.g., the standard properties `#address-cells` and `#size-cells` (also described in the [Devicetree specification](https://www.devicetree.org/specifications/)). The special character `#` is really just part of the property name, there's no magic behind it.



Zephyr uses the type names summarized below. For details, refer to the [_"type"_ section in Zephyr's documentation on Devicetree bindings](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#type) or [Zephyr's Devicetree introduction on property values](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#writing-property-values).

> **Note:** If you're planning on reading the Devicetree specification, skip ahead to the section _"Devicetree Source (DTS) Format"_, specifically the subsection _"Node and property definitions"_. In case something is unclear, try to find the information in the initial chapters. Reading the specification top to bottom can be quite confusing.

The syntax used for property _values_ is a bit peculiar. Except for `phandles`, which we'll cover separately, the following table contains all property types supported by Zephyr and their DTSpec equivalent.

| Zephyr type      | DTSpec equivalent              | Example                                            |
| :--------------- | :----------------------------- | :------------------------------------------------- |
| `boolean`        | `property with no value`       | `interrupt-controller;`                            |
| `string`         | `string`                       | `status = "disabled";`                             |
| `array`          | `32-bit integer cells`         | `reg = <0x40002000 0x1000>;`                       |
| `int`            | `A single 32-bit integer cell` | `current-speed = <115200>;`                        |
| `64-bit integer` | `32-bit integer cells`         | `value = <0xBAADF00D 0xDEADBEEF>;`                 |
| `uint8-array`    | `bytestring`                   | `mac-address = [ DE AD BE EF 12 34 ];`             |
| `string-array`   | `stringlist`                   | `compatible = "nordic,nrf-egu", "nordic,nrf-swi";` |
| `compound`       | "comma-separated components"   | `foo = <1 2>, [3, 4], "five"`                      |

The table deserves some observations and explanations, but we'll repeat all the types just for the sake of completeness:

**`boolean`**

A `boolean` property is `true` if the property exists, otherwise `false`.

**`string`**

A `string` property is just like a `C` string literal: double-quoted, null-terminated text.

**`array`**

An `array` is a lists of values enclosed in `<` and `>`, separated by spaces. `arrays` could in theory contain mixed elements of any supported type but most commonly uses 32-bit integers. Just like in `C/C++`, the prefix `0x` is used for hexadecimal numbers, and numbers _without_ a prefix are decimals.

**`int`**

An `int`eger is represented as an `array` containing a single 32-bit value ("cell"): It's a single 32-bit value enclosed in `<` and `>`.

> **Note:** The term **"cell"** is typically used to refer to the individual data elements within properties and can thus be thought of as a single unit of data in a property. The [Devicetree specification](https://www.devicetree.org/specifications/) v0.4 defines a **"cell"** as _"a unit of information consisting of 32 bits"_ and thus explicitly defines its size as 32 bits. Meaning it is just another confusing name for a 32-bit integer.

64-bit integers do not have their own type but are instead represented by an array of two `int`egers.

**`uint8-array`**

A `uint-array` consists of 8-bit hexadecimal values enclosed in `[` and `]`, _optionally_ separated by spaces.

In contrast to an `array`, a `uint8-array` _always_ uses **hexadecimal** literals _without_ the prefix `0x` - which can be confusing at first. E.g., `<11 12>` represents the two _32-bit_ integers with the decimal values `11` and `12`, whereas `[11, 12]` represents the two _8-bit_ integers with the decimal values `17` and `18`.

The spaces between each byte in a `uint8-array` are optional. E.g., `mac-address = [ DEADBEEF1234 ];` is equivalent to `mac-address = [ DE AD BE EF 12 34 ];`. It practice, you'll rarely see `uint8-array`s without spaces between each byte.

**`string-array`**

A `string-array` is just a comma-separated list of strings. The only thing worth mentioning is, that the value of a `string-array` property may also be a single `string`. E.g., `compatible = "something"` is still a valid value assignment for a `string-array` property.

**`compound`**

The `compound` type is essentially a "catch-all" for custom types. Zephyr does **not** generate any code for `compound` properties. Also, notice how compound value definitions are syntactically ambiguous, e.g., for `foo = <1 2>, "three", "four"`: Is `"three", "four"` a single value of type `string-array`, or two separate `string` values?

When reading Zephyr DTS files, keep in mind that [in Zephyr all DTS files are fed into the preprocessor](#devicetree-includes-and-sources-in-zephyr) and therefore Zephyr allows the use of macros in DTS files. E.g., you might encounter properties like `max-frequency = <DT_FREQ_M(8)>;`, which do not match the Devicetree syntax at all. There, the preprocessor replaces the macro `DT_FREQ_M` with the corresponding literal before the source file is parsed.

The following is a snippet of a test file of Zephyr's Python Devicetree generator. It contains the node `props` that nicely demonstrate the different property types supported by Zephyr.

`zephyr/scripts/dts/python-devicetree/tests/test.dts`

```dts
/dts-v1/;

/ {
  props {
    existent-boolean;
    int = <1>;
    array = <1 2 3>;
    uint8-array = [ 12 34 ];
    string = "foo";
    string-array = "foo", "bar", "baz";
  };
};
```

There's one more thing that is worth mentioning: Parentheses, arithmetic operators, and bitwise operators are allowed in property values, though the entire expression must be parenthesized. [Zephyr's introduction on property values](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#writing-property-values) provides the following example for a property `bar`:

```dts
/ {
  foo {
    bar = <(2 * (1 << 5))>;
  };
};
```

The property `bar` contains a single 32-bit value ("cell") with the value _64_. Notice that operators are not just allowed in Zephr, but also according to the [Devicetree specification](https://www.devicetree.org/specifications/): You therefore don't _need_ to use macros for simple arithmetic or bit operations.
