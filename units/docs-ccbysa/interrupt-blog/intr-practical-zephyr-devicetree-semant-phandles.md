---
id: "intr-practical-zephyr-devicetree-semant-phandles"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example / Phandles"
summary: "Having seen labels and the /chosen and /aliases nodes, we can guess what Zephyr's output for the types phandle and phandles is - maybe even path and phandle-array is."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#phandles"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Bindings by example_

Having seen labels and the `/chosen` and `/aliases` nodes, we can guess what Zephyr's output for the types `phandle` and `phandles` is - maybe even `path` and `phandle-array` is. Nevertheless, we'll walk through the types using a similar example to the one we've used in the previous article.

#### `path`, `phandle`, and `phandles`

Let's get started by creating two new files `custom-props-phandles.yaml` and `props-phandles.overlay`:

```bash
$ tree --charset=utf-8 --dirsfirst.
├── dts
│   ├── bindings
│   │   ├── custom-props-basics.yaml
│   │   └── custom-props-phandles.yaml
│   └── playground
│       ├── props-basics.overlay
│       └── props-phandles.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

Our Devicetree overlay is pretty much identical to what we've used in the previous article, but for now, we're skipping `phandle-array` properties. Thus, we're creating properties of type `path`, `phandle`, and `phandles`:

```dts
/ {
  label_a: node_a { /* Empty. */ };
  label_b: node_b { /* Empty. */ };

  node_refs {
    compatible = "custom-props-phandles";

    path-by-path = &{/node_a};
    path-by-label = &label_a;

    phandle-by-path = <&{/node_a}>;
    phandle-by-label = <&label_a>;

    // Simple array of phandles
    phandles = <&{/node_a} &label_b>;
  };
};
```

The _compatible_ binding has the following contents:

```yaml
description: Custom properties
compatible: "custom-props-phandles"

properties:
  path-by-path:
    type: path
  path-by-label:
    type: path
  phandle-by-path:
    type: phandle
  phandle-by-label:
    type: phandle
  phandles:
    type: phandles
```

In the build, we could just switch out our overlay and ignore `props-basics.overlay`, but let's include both of them instead, remembering that we need to separate the paths by semicolon (or a space):

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DDTC_OVERLAY_FILE="dts/playground/props-basics.overlay;dts/playground/props-phandles.overlay"
```

The build succeeds without any problems and both overlays are detected. In the `devicetree_generated.h` we now find all of our new nodes, but we're especially interested in `node_refs` which is using our new binding `custom-props-phandles.yaml`:

```c
/*
 * Devicetree node: /node_refs
 *
 * Node identifier: DT_N_S_node_refs
 *
 * Binding (compatible = custom-props-phandles):
 *   /path/to/dts/bindings/custom-props-phandles.yaml
 */
// --snip--
/* Generic property macros: */
// --snip--
```

The properties `path-by-path` and `path-by-label` both have the type `path`. We might therefore expect a similar output that we got when specifying paths in the `/chosen` node, namely node identifiers. However, the only output we get for those nodes is the following:

```c
#define DT_N_S_node_refs_P_path_by_path_EXISTS 1
#define DT_N_S_node_refs_P_path_by_label_EXISTS 1
```

So basically, the `type: path` exists in Zephyr, but at the time of writing does not produce any output - except for the `_EXISTS` macros, which are useless without any additional macros. This may seem surprising but makes a lot of sense recalling that Zephyr's Devicetree is not compiled into a Devicetree blob `dtb`, but is instead used or resolved at _compile time_. Paths are of no use since nodes exist only as _node identifiers_ and are therefore nothing but _tokens_ that are used to access a node's properties. At the time of writing, there is in fact not a single binding in Zephyr that uses a `path`.

Let's move on to the generated output for the properties `phandle-by-path` and `phandle-by-label`:

```c
#define DT_N_S_node_refs_P_phandle_by_path DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_path_IDX_0 DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_path_IDX_0_PH DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_path_IDX_0_EXISTS 1
#define DT_N_S_node_refs_P_phandle_by_path_LEN 1
#define DT_N_S_node_refs_P_phandle_by_path_EXISTS 1

#define DT_N_S_node_refs_P_phandle_by_label DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_label_IDX_0 DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_label_IDX_0_PH DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_by_label_IDX_0_EXISTS 1
#define DT_N_S_node_refs_P_phandle_by_label_LEN 1
#define DT_N_S_node_refs_P_phandle_by_label_EXISTS 1
```

Zephyr's generator translated both property values into the node's identifier, just like we've seen for the `/aliases` and `/chosen` nodes. The format in which the property's value is provided in the Devicetree does not matter for the generated output - which is of the same type `phandle`.

It is a bit surprising, though, that Zephyr also generated macros containing `_IDX_0` and the macro with the suffix `_LEN`: After all, `phandle`-typed properties only support a single value (try adding more!). The reason for this becomes clear when looking at the output for our property `phandles` of the same-named type:

```c
#define DT_N_S_node_refs_P_phandles_IDX_0 DT_N_S_node_a
#define DT_N_S_node_refs_P_phandles_IDX_0_PH DT_N_S_node_a
#define DT_N_S_node_refs_P_phandles_IDX_0_EXISTS 1
#define DT_N_S_node_refs_P_phandles_IDX_1 DT_N_S_node_b
#define DT_N_S_node_refs_P_phandles_IDX_1_PH DT_N_S_node_b
#define DT_N_S_node_refs_P_phandles_IDX_1_EXISTS 1
/* --snip-- phandles_FOREACH */
#define DT_N_S_node_refs_P_phandles_LEN 2
#define DT_N_S_node_refs_P_phandles_EXISTS 1
```

Thus, the generated output for `phandle` and `phandles` is essentially handled in the same way. The only difference is, that for `phandles` _only_ the `_IDX_n` macros are generated, and thus the _node identifiers_ can only be accessed by index, whereas for the `phandle` type it is possible to retrieve the node's identifier using the node identifier and property name. We'll see this when we'll access _phandles_ via [the Devicetree API in a later section](#zephyrs-devicetree-api).

In contrast to `array`, `uint8-array`, and `string-array`, no _initializer expression_ is generated. Makes sense: _phandles_ are not _values_ but only _tokens_ and thus cannot be used as such by an application.

In summary: `path`s practically don't exist in Zephyr, `phandle` and `phandles` essentially produce the same output, and all Devicetree references and paths translate to node _identifiers_ - which are just _tokens_.

#### `phandle-array`

Let's briefly recall why we need a `phandle-array`: In the previous article, we've seen how `gpios` are represented by the nRF52840's Devicetree (for a detailed explanation, please read the corresponding section in the previous article):

##### `phandle-array` in Zephyr

`zephyr/dts/arm/nordic/nrf52840.dtsi`
```dts
/ {
  soc {
    gpio0: gpio@50000000 {
      compatible = "nordic,nrf-gpio";
      #gpio-cells = <2>;
      port = <0>;
    };

    gpio1: gpio@50000300 {
      compatible = "nordic,nrf-gpio";
      #gpio-cells = <2>;
      port = <1>;
    };
  };
};
```

Each instance handles _all_ pins in the corresponding port. However, some other Devicetree node, e.g., an LED, needs a way to control and configure a single pin of a given port. We can't do this using a normal _phandle_, e.g., `<&gpio0>`, we need a mechanism to pass some _parameters_ or _metadata_ along with the _phandle_. `phandle-array`s implement this exact use case, allowing to pass a predefined number of cells with the _phandle_, e.g., as we can see in the nRF52840's development kit DTS file for `/leds/led_0`:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`
```dts
/ {
  leds {
    led0: led_0 {
      gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
    };
  };
};
```

What we haven't seen yet, is how we can know that the first cell _13_ is the _pin_ within `gpio0`, and the second cell _GPIO_ACTIVE_LOW_ is a configuration _flag_. This is part of the _semantics_ defined by the _binding_ of the _gpio_ nodes that are compatible with `nordic,nrf-gpio`:

`zephyr/dts/bindings/gpio/nordic,nrf-gpio.yaml`
```yaml
description: NRF5 GPIO node
compatible: "nordic,nrf-gpio"
# --snip--

gpio-cells:
  - pin
  - flags
```

Here we see that `gpio-cells` consists of two items `pin` and `flags`, which are matched exactly against the provided metadata in the given order. Thus, _13_ refers to the `pin` and `GPIO_ACTIVE_LOW` to its `flags`.

You may have noticed that the `gpio` nodes do not conform to the naming convention that we've seen in the last article. This makes it a bit awkward to explain what needs to be provided for a `phandle-array` and the referenced nodes. Therefore, we'll build our own from scratch.

> **Note:** Have a look at [Zephyr's documentation about specifier cells](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-cell-names-cells) in case you want to know how `gpios` opts out of the mentioned naming convention.

##### A `phandle-array` from scratch

Let's briefly review the rules for using `phandle-array`s that we've seen in the previous article. Notice that there's no need to understand them out of context, we'll see all of them in action in our example:

- By convention, a `phandle-array` property is plural and its name must thus end in _s_.
- The value of a `phandle-array` property is an array of phandles, but each phandle is followed by the pre-defined number of cells for each referenced node.
- The number of cells that can follow a node's reference is specified by the node's _specifier cells_ property
- The _specifier cells_ property has a defined naming convention: The name is formed by removing the plural '_s_' and attaching '_-cells_' to the name of the `phandle-array` property: `#<name-without-s>-cells`

Let's extend our `props-phandles.overlay` with a new property `phandle-array-of-refs`. Within this property, we'll reference `/node_a` and pass along two cells, and `/node_b` with just one cell as metadata:

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_a: node_a { /* Empty. */ };
  label_b: node_b { /* Empty. */ };
  node_refs {
    compatible = "custom-props-phandles";
    /* --snip-- */
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;
  };
};
```

Within our binding for `custom-props-phandles`, we can now add the property `phandle-array-of-refs` of type `phandle-array`:

`dts/bindings/custom-props-phandles.yaml`
```yaml
description: Custom properties
compatible: "custom-props-phandles"

properties:
  # --snip--
  phandle-array-of-refs:
    type: phandle-array
```

With that, we fulfill our first rule, namely that our property name ends with an 's'. If we violate this rule, e.g., by using `phandle-array-of-ref` as the property name, the Devicetree compiler would reject the binding with the following error:

```
-- Found devicetree overlay: dts/playground/props-phandles.overlay
devicetree error: 'phandle-array-of-ref' in 'properties:'
in /path/to/dts/bindings/custom-props-phandles.yaml has type 'phandle-array'
and its name does not end in 's', but no 'specifier-space' was provided.
```

The mentioned _specifier-space_ is a way to work around the plural 's' rule and is used for properties that would otherwise result in weird names. We won't explain the workings of _specifier-space_ in this article, so I'll leave you with a reference to [Zephyr's documentation on specifier-space](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-space) in case you want to know how this works in detail.

For now, let's revert the name change and use `phandle-array-of-refs` as the property name and try to compile the project (the command didn't change). Now the Devicetree compiler complains that our _specifier-cells_ are missing:

```
-- Found devicetree overlay: dts/playground/props-phandles.overlay
devicetree error: <Node /node_a in '/opt/nordic/ncs/v3.2.1/zephyr/misc/empty_file.c'>
lacks #phandle-array-of-ref-cells
```

Looking at our value assignment `phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;` this error makes perfect sense since the compiler has no way of knowing how many _cells_ are supposed to follow each node's reference. We need to update our overlay with the required _specifier cells_ property for each referenced node:

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_a: node_a { #phandle-array-of-ref-cells = <2>; };
  label_b: node_b { #phandle-array-of-ref-cells = <1>; };
  node_refs {
    /* --snip-- */
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;
  };
};
```

Now the Devicetree compiler knows, that any reference to `/node_a` in a property of type `phandle-array` must be followed by exactly _2_ cells, whereas a reference to `/node_b` only expects one cell. Does this do the trick? Let's try to recompile the example:

```
-- Found devicetree overlay: dts/playground/props-phandles.overlay
devicetree error: phandle-array-of-ref controller
<Node /node_a in '/opt/nordic/ncs/v3.2.1/zephyr/misc/empty_file.c'>
for <Node /node_refs in '/opt/nordic/ncs/v3.2.1/zephyr/misc/empty_file.c'>
lacks binding
```

For any node referenced in a `phandle-array`, Zephyr requires a binding since it otherwise isn't able to generate the required macros. Without the bindings for our referenced nodes, Zephyr _could_ have been able to generate a partial set of macros, but thankfully it was decided that such incomplete bindings are rejected entirely.

Since the number of required cells in our nodes is different, we need _two separate_ bindings. We'll again use the binding name as a filename and create two files `dts/bindings/custom-cells-a.yaml` and `dts/bindings/custom-cells-b.yaml`:

```bash
$ tree --charset=utf-8 --dirsfirst.
├── dts
│   ├── bindings
│   │   ├── custom-cells-a.yaml
│   │   ├── custom-cells-b.yaml
│   │   ├── custom-props-basics.yaml
│   │   └── custom-props-phandles.yaml
│   └── playground
│       ├── props-basics.overlay
│       └── props-phandles.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

Within the binding files, as usual, we declare compatibility using `compatible` key. We might expect that `#phandle-array-of-ref-cells` are placed under the _properties_ key in the binding. They are, however, [top-level keys](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#top-level-keys) and give a [_name_](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#specifier-cell-names-cells) to each cell that follows the reference:

`dts/bindings/custom-cells-a.yaml`
```yaml
description: Dummy for matching "cells"
compatible: "custom-cells-a"

phandle-array-of-ref-cells:
  - name-of-cell-one
  - name-of-cell-two
```

`dts/bindings/custom-cells-a.yaml`
```yaml
description: Dummy for matching "cells"
compatible: "custom-cells-b"

phandle-array-of-ref-cells:
  - name-of-cell-one
```

The above binding thus defines a _name_ and **semantics** for each value that follows the corresponding _phandle_ when used in a `phandle-array`, just like we've seen for the `gpios` example and the cells `pin` and `flags`. E.g., for `phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;`, we now know that:
- For `/node_a`, the value _1_ is assigned to a cell named `name-of-cell-one` and the value _2_ to a cell named `name-of-cell-two`;
- for `/node_a`, the cell `name-of-cell-one` is assigned the value _1_.

We're therefore providing the means for the [Devicetree API](#zephyrs-devicetree-api) to access the _metadata_ passed with the _phandle_ using a descriptive name.

> **Note:** One thing that is not immediately clear is, that number of elements in the `-cells` key of the _binding_ **must** match the number of `-cells = <n>` specified in the _Devicetree_. It is, e.g., **not** possible to provide _more_ elements in a binding's list and restrict the exact number of cells using the matching Devicetree property. Thus, for any node that has a binding, the property `-cells` in the Devicetree is actually redundant.

We can now go ahead and assign the bindings to our nodes with the `compatible` property, and recompile the project.

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_a: node_a {
    compatible = "custom-cells-a";
    #phandle-array-of-ref-cells = <2>;
  };
  label_b: node_b {
    compatible = "custom-cells-b";
    #phandle-array-of-ref-cells = <1>;
  };
  node_refs {
    compatible = "custom-props-phandles";
    /* --snip-- */
    phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;
  };
};
```

For our node `/node_refs`, Zephyr's generator now produces the following macros:

```c
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_EXISTS 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_PH DT_N_S_node_a
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_VAL_name_of_cell_one 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_VAL_name_of_cell_one_EXISTS 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_VAL_name_of_cell_two 2
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_0_VAL_name_of_cell_two_EXISTS 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_1_EXISTS 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_1_PH DT_N_S_node_b
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_1_VAL_name_of_cell_one 1
#define DT_N_S_node_refs_P_phandle_array_of_refs_IDX_1_VAL_name_of_cell_one_EXISTS 1
/* --snip-- phandle_array_of_refs_FOREACH */
#define DT_N_S_node_refs_P_phandle_array_of_refs_LEN 2
#define DT_N_S_node_refs_P_phandle_array_of_refs_EXISTS 1
```

Unsurprisingly, the output looks a lot like what we get for `phandles`: We get a set of macros for each index _n_ `_IDX_n`, but now the length _n_ `_LEN` is not the total number of _cells_ within the array but matches the number of "tuples" of _phandles and metadata_.

Along the macro with the suffix `_PH` containing the _phandle_ and thus node's identifier, `_VAL_x` macros are generated for each cell that follows the _phandle_; the specifier name _x_ matches the name provided for each specifier in the binding.

Due to the fact that the index within a `phandle-array` does not refer to a cell's value, values for `phandle-array` properties are sometimes assigned using the alternative syntax that we've already seen in the previous article:
- `phandle-array-of-refs = <&{/node_a} 1 2>, <&label_b 1>;` is used instead of
- `phandle-array-of-refs = <&{/node_a} 1 2 &label_b 1>;`.

The generated output is identical.

Admittedly, the chosen names `name_of_cell_x` are not very descriptive, and the fact that `one` is assigned the value _1_ and `two` the value _2_ doesn't help, so let's have a quick lock at what's generated for the `gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;` property of the `/leds/led0`:

```c
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_EXISTS 1
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_PH DT_N_S_soc_S_gpio_50000000
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_pin 13
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_pin_EXISTS 1
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_flags 1
#define DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_flags_EXISTS 1
/* --snip-- gpios_FOREACH */
#define DT_N_S_leds_S_led_0_P_gpios_LEN 1
#define DT_N_S_leds_S_led_0_P_gpios_EXISTS 1
```

Here, we clearly see that we'll be using the _pin_ with the number _13_ from the selected node `/soc/gpio@50000000`, and we'll use the value `1` for its _flags_ - which is what `GPIO_ACTIVE_LOW` expands to.
