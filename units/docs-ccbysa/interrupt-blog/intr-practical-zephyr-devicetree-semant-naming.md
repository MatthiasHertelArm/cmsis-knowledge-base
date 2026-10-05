---
id: "intr-practical-zephyr-devicetree-semant-naming"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example / Naming"
summary: "Before we start, we need to solve one of the hardest problems in engineering: Finding a good name for our bindings."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#naming"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Bindings by example_

Before we start, we need to solve one of the hardest problems in engineering: Finding a good _name_ for our bindings. The [Devicetree specification](https://www.devicetree.org/specifications/) contains a guideline on the value for the `compatible` property of a node - and therefore the name of the binding:

> "The `compatible` string should consist only of lowercase letters, digits, and dashes, and should start with a letter. A single comma is typically only used following a vendor prefix. Underscores should not be used." [DTSpec](https://www.devicetree.org/specifications/)

Let's try this with the binding name _custom,props-basic_, and thus vendor prefix _custom_. We'll follow the convention and use the binding's name as filename and create a new file `custom,props-basics.yaml` in the application's `dts/bindings` directory:

```bash
$ tree --charset=utf-8 --dirsfirst.
├── dts
│   ├── bindings
│   │   └── custom,props-basics.yaml
│   └── playground
│       └── props-basics.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

In our binding, we set the `compatible` key as `"custom,props-basics"`, and add the two properties `int` and `string` of the matching type, without providing any description:

`dts/bindings/custom,props-basics.yaml`
```yaml
description: Custom properties
compatible: "custom,props-basics"

properties:
  int:
    type: int
  string:
    type: string
```

As we've seen before, bindings define a node's properties under the key _properties_. The template given below is the simplest form for a property in a binding:

```yaml
properties:
  <property-name>:
    type: <property-type>
    # required: false -> omitted by convention if false
```

Properties have a _name_ and are therefore unique within the node, and each property is assigned a _type_ using the corresponding key. Other keys such as _required_ are optional.

There are several other keys and "features", e.g., it is possible to define the properties for _children_ of a node with the matching `compatible` property, but we'll only have a look at the very basics. Definitely dive into [Zephyr's official documentation](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html) once you're through with this article!

Finally, we create a new property `compatible = "custom,props-basic"` for our existing `node_with_props` ...

`dts/playground/props-basics.overlay`
```dts
/ {
  node_with_props {
    compatible = "custom,props-basic"
    int = <1>;
    string = "foo bar baz";
  };
};
```

... and recompile:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE="dts/playground/props-basics.overlay"
```
```
-- Found devicetree overlay: dts/playground/props-basics.overlay
node '/node_with_props' compatible 'custom,props-basics' has unknown vendor prefix 'custom'
-- Generated zephyr.dts: /path/to/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: /path/to/build/zephyr/include/generated/devicetree_generated.h
```

> **Note:** As mentioned, at the time of writing and in contrast to overlay files, bindings are not listed in the build output, not even for bindings in the application's `dts/bindings` directory.

Even though the build passes, it seems that the Devicetree compiler is not too happy about our _"custom"_ vendor prefix. Zephyr warns us here since it maintains a _"Devicetree binding vendor prefix registry"_ `zephyr/dts/bindings/vendor-prefixes.txt` to avoid name-space collisions for properties and bindings. If you're a vendor, you can of course add your name upstream, but for this article, we'll simply skip the vendor prefix and use the binding name _custom-props-basics_ instead.

```bash
$ mv dts/bindings/custom,props-basics.yaml dts/bindings/custom-props-basics.yaml
$ sed -i .bak 's/custom,/custom-/g' dts/bindings/custom-props-basics.yaml
$ sed -i .bak 's/custom,/custom-/g' dts/playground/props-basics.overlay
$ rm dts/**/*.bak

$ tree --charset=utf-8 --dirsfirst.
├── dts
│   ├── bindings
│   │   └── custom-props-basics.yaml
│   └── playground
│       └── props-basics.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

After recompiling, we can check whether the generator script has added our properties to `devicetree_generated.h`. The value _foo_ is unique enough for a quick `grep`; for our property _int_ we'll use what we've learned and expect to find some macro containing `node_with_props_P_int`. And indeed, we **finally** have our generated output!

```bash
$ grep foo ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_node_with_props_P_string "foo bar baz"
#define DT_N_S_node_with_props_P_string_STRING_UNQUOTED foo bar baz
#define DT_N_S_node_with_props_P_string_STRING_TOKEN foo_bar_baz
$ grep node_with_props_P_int ../build/zephyr/include/generated/devicetree_generated.h
#define DT_N_S_node_with_props_P_int 1
#define DT_N_S_node_with_props_P_int_EXISTS 1
```

We'll learn how to use those macros in the section about [Zephyr's Devicetree API](#zephyrs-devicetree-api). In this section, we just make sure that our bindings lead to some generated output for all supported types. In case you can't wait and want to have a more detailed look instead, I suggest you have a look at [Zephyr's great introduction to Devicetree bindings](https://docs.zephyrproject.org/latest/build/dts/bindings-intro.html).

> **Note:** If you're experimenting and don't see any output, make sure that the `compatible` property is set correctly. The Devicetree compiler does **not** complain in case it doesn't find a matching binding. E.g., in case you have a typo in your `compatible` property, the application builds without warnings, but `devicetree_generated.h` won't have any content for the desired properties.
