---
id: "intr-practical-zephyr-devicetree-basics-complete-examples-and-alternative-array"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Complete examples and alternative array syntax"
summary: "Along with the complete list of Zephyr's property types, we can now create two overlay files as complete examples for basic types, phandles, /aliases, and /chosen nodes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#complete-examples-and-alternative-array-syntax"
license: "CC-BY-SA-4.0"
mode: "V"
---

Along with [the complete list of Zephyr's property types](#a-complete-list-of-zephyrs-property-types), we can now create two overlay files as complete examples for basic types, `phandle`s, `/aliases`, and `/chosen` nodes.

> **Note:** The full example application including all the Devicetree files that we've seen throughout this article is available in the [`02_devicetree_basics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/02_devicetree_basics).

The first example covers all the basic types that we've seen:

`dts/playground/props-basics.overlay`

```dts
/ {
  aliases {
    // Aliases cannot be used as a references in the Devicetree itself, but are
    // used within the application as an alternative name for a node.
    alias-by-label = &label_equivalent;
    alias-by-path = &{/node_with_equivalent_arrays};
    alias-as-string = "/node_with_equivalent_arrays";
  };

  chosen {
    // `chosen` describes parameters "chosen" or specified by the application. In Zephyr,
    // all `chosen` parameters are paths to nodes.
    chosen-by-label = &label_equivalent;
    chosen-by-path = &{/node_with_equivalent_arrays};
    chosen-as-string = "/node_with_equivalent_arrays";
    // Technically, `chosen` properties can have any valid type.
    chosen-foo = "bar";
    chosen-bar = <0xF00>;
  };

  node_with_props {
    existent-boolean;
    int = <1>;
    array = <1 2 3>;
    uint8-array = [ 12 34 ];
    string = "foo";
    string-array = "foo", "bar", "baz";
  };
  label_equivalent: node_with_equivalent_arrays {
    // No spaces needed for uint8-array values.
    uint8-array = [ 1234 ];
    // Alternative syntax for arrays.
    array = <1>, <2>, <3>;
    int = <1>;
  };
};

// It is not possible to refer to a node via its alias - aliases are just properties!
// &alias-by-label {... };

// It is possible to "extend" and overwrite (non-const) properties of a node using
// its full path or its label.
&{/node_with_equivalent_arrays} {
  int = <2>;
};
&label_equivalent {
  string = "bar";
```

There are two things that we have already seen but haven't explicitly described throughout this article: We can use node references outside the root node to define _additional_ properties for a node or change a node's existing properties, and we can use a different syntax for specifying array values:

In the above example, the property `int` of the node `/node_with_equivalent_arrays` is overwritten with the value _2_, and a value `"bar"` is added to the node's property `string` using its label `label_equivalent`.

We also see that we don't have to provide all values of an `array` within a single set of `<..>`, but can instead place each value into its own pair of `<..>` and separate the values via commas. We also see the alternative syntax for `uint8-arrays`. In the semantics article, we'll see that the output is indeed the same, for now, you have to trust me on this.

The following is the generated output for the two nodes `/node_with_props` and `/node_with_equivalent_arrays`:

`/build/zephyr/zephyr.dts`

```dts
/ {
  node_with_props {
    existent-boolean;
    int = < 0x1 >;
    array = < 0x1 0x2 0x3 >;
    uint8-array = [ 12 34 ];
    string = "foo";
    string-array = "foo", "bar", "baz";
  };
  label_equivalent: node_with_equivalent_arrays {
    uint8-array = [ 12 34 ];
    array = < 0x1 >, < 0x2 >, < 0x3 >;
    int = < 0x2 >;
    string = "bar";
  };
};
```

The second overlay file shows the use of `path`s, `phandle`, `phandle`s, and `phandle-array`, including the alternative array syntax that we've just seen. Here, for the property `phandle-array-of-refs`, you can see how this syntax can sometimes result in a more readable Devicetree source file.

`dts/playground/props-phandles.overlay`

```dts
/ {
  label_a: node_a {
    // The value assignment for the cells is redundant in Zephyr, since
    // the binding already specifies all names and thus the size.
    #phandle-array-of-ref-cells = <2>;
  };
  label_b: node_b {
    #phandle-array-of-ref-cells = <1>;
  };
  node_refs {
    // Properties of type `path`
    path-by-path = &{/node_a};
    path-by-label = &label_a;

    // Properties of type `phandle`
    phandle-by-path = <&{/node_a}>;
    phandle-by-label = <&label_a>;

    // Array of phandle, type `phandles`
    phandles = <&{/node_a} &label_b>;
    // Array of phandles _with metadata_, type `phandle-array`
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;
  };

  node_refs_equivalents {
    phandles = <&{/node_a}>, <&label_b>;
    phandle-array-of-refs = <&{/node_a} 1 2>, <&label_b 3>;
  };

  node_with_phandle {
    // It is allowed to explicitly provide the phandle's value, but the
    // DTS generator does this for us.
    phandle = <0xC0FFEE>;
  };
};
```

You can add those files to your own sources and provide both files using the `EXTRA_DTC_OVERLAY_FILE` option by separating the paths using a semicolon:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE="dts/playground/props-basics.overlay;dts/playground/props-phandles.overlay"
```
