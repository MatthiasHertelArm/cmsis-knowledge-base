---
id: "intr-practical-zephyr-devicetree-basics-phandle"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): References and `phandle` types / `phandle`"
summary: "Part of: References and phandle types"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#phandle"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: References and `phandle` types_

So what is a `phandle`? The easy answer is: Devicetree source files need some way to refer to nodes, something like pointers in `C`, and that's what `phandle`s are. If we're being picky about the terminology - it's complicated. Why?

- In the [DTSpec](https://www.devicetree.org/specifications/), we've seen that a `phandle` is a base **type**.
- In addition, the [DTSpec](https://www.devicetree.org/specifications/) also defines a standard **property** named `phandle` - ironically of type _32-bit integer_, and not _phandle_. We'll see this property in just a second.
- In Zephyr, the term `phandle` is used pretty much only for node **references** in any format and never even mentions the same named _property_.

Why this ambiguity? Because in the end, any reference to a node is replaced by a unique, 32-bit value that identifies the node - the value stored in the node's `phandle` property. The fact that `phandle` _property_ is not intended to be set manually, but is instead created by the Devicetree compiler for each referenced node, makes mentioning the `phandle` property as such unnecessary. Thus, the approach chosen in Zephyr's documentation - referring to any reference as `phandle` - makes a lot of sense.

But enough nit-picking. Let's see how this looks in a real Devicetree source file. Let's create two nodes `node_a` and `node_refs` in our overlay file, and have `node_refs` reference the `node_a` once by its path and once by a label `label_a` that we create for `node_a`. How do we do this? The syntax is specified in the [DTSpec](https://www.devicetree.org/specifications/) as follows:

> "Labels are created by appending a colon ('`:`') to the label name. References are created by prefixing the label name with an ampersand ('`&`'), or they may be followed by a node's full path in braces." [[DTSpec]](https://www.devicetree.org/specifications/)

Thus, in our Devicetree overlay file, we can create the properties as shown below. Notice how we're missing the DTS version `/dts-v1/;`: The version is only defined Devicetree *source* files, but **not** in *overlay* files.

```dts
/ {
  label_a: node_a { /* Empty. */ };
  node_refs {
    phandle-by-path = <&{/node_a}>;
    phandle-by-label = <&label_a>;
  };
};
```

Let's run a build to ensure that our overlay is sent through the preprocessor so that we can have a look at the generated `zephyr.dts`:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE=dts/playground/props-phandles.overlay
```

`build/zephyr/zephyr.dts`

```dts
/dts-v1/;

/ {
  /* Possibly lots of other nodes ... */
  label_a: node_a {
    phandle = < 0x1c >;
  };
  node_refs {
    phandle-by-path = < &{/node_a} >;
    phandle-by-label = < &label_a >;
  };
};
```

We can now see that the generator has created a `phandle` property for our referenced `node_a`. Your mileage may vary on the exact value for the property since it depends on the number of referenced nodes in the set of DTS files that are merged. What is this `phandle` property? The [DTSpec](https://www.devicetree.org/specifications/) defines `phandle` as follows:

> Property name `phandle`, value type _32-bit integer_.
>
> The `phandle` property specifies a numerical identifier for a node that is unique within the Devicetree. The `phandle` property value is used by other nodes that need to refer to the node associated with the property.
>
> **Note:** Most devicetrees [...] will not contain explicit phandle properties. The DTC tool automatically inserts the phandle properties when the DTS is compiled [...].

This is also what we see in the generated `zephyr.dts`: Since `node_a` is referenced by `node_ref`, Zephyr's DTS generator has inserted the property `phandle` for `node_a` in our Devicetree. To see what happens to the reference within this `phandle` property, we need to jump back to the syntax section in the [DTSpec](https://www.devicetree.org/specifications/), where we find the following:

> "In a cell array, a reference to another node will be expanded to that node's phandle."

This means that the references `&{/node_a}` and `&label_a` in our properties `phandle-by-path` and `phandle-by-label` are essentially expanded to `node_a`'s `phandle` _0x1c_. Thus, **the reference is equivalent to its phandle**. Zephyr's documentation is right to refer to `&{/node_a}` and `&label_a` as "`phandle`s". Could we also define `node_a`'s `phandle` property by ourselves? Let's find out:

```dts
/ {
  label_a: node_a {
    phandle = <0xC0FFEE>;
  };
  node_refs {
    phandle-by-path = <&{/node_a}>;
    phandle-by-label = <&label_a>;
  };
};
```

After executing `west build` with the previous parameters again, we indeed end up with the value `0xc0ffee` for `node_a`'s `phandle` property:

`build/zephyr/zephyr.dts`

```dts
/dts-v1/;

/ {
  /* Possibly lots of other nodes ... */
  label_a: node_a {
    phandle = < 0xc0ffee >;
  };
  node_refs {
    phandle-by-path = < &{/node_a} >;
    phandle-by-label = < &label_a >;
  };
};
```

What's the use of a `phandle`? A single `phandle` can be useful where a 1:1 relation between nodes in the Devicetree is required. E.g., the following is a snippet from the nRF52840 DTS include file, which contains a software PWM node with a configurable generator, which by default refers to `timer2`:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  /* ... */
  sw_pwm: sw-pwm {
    compatible = "nordic,nrf-sw-pwm";
    status = "disabled";
    generator = <&timer2>;
    clock-prescaler = <0>;
    #pwm-cells = <3>;
  };
};
```

We've seen the type of the _phandle_ property, but what about the types of the properties `phandle-by-path` and `phandle-by-label`? Knowing that a `phandle` is expanded to a *cell* we might guess that `phandle-by-path` and `phandle-by-label` are of type `int` or `array`: Assuming that `node_a`'s _phandle_ has the value 0xc0ffee, both `<&{/node_a}>` and `<&label_a>` essentially expand to `<0xc0ffee>`, which could either be a single `int` or an `array` of size `1` containing a 32-bit value.

In Zephyr, however, an array containing a **single** node reference has its own type **`phandle`**.
