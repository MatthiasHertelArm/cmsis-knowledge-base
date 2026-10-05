---
id: "intr-practical-zephyr-devicetree-semant-bindings-in-zephyr"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Towards bindings / Bindings in Zephyr"
summary: "Zephyr's official documentation provides a comprehensive explanation of the syntax used for bindings. Unless you're adding your own devices and drivers, you'll hardly ever need to create bindings yourself."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#bindings-in-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Towards bindings_

[Zephyr's official documentation](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html) provides a comprehensive explanation of the syntax used for bindings. Unless you're adding your own devices and drivers, you'll hardly ever need to create bindings yourself. Therefore, in this section, we'll walk through some existing bindings in Zephyr to gain a general understanding, and then create [our own example bindings](#bindings-by-example) in the next section.

Let's have a look at what we can find out about `/soc/uart@40002000`'s `current-speed` and `status` properties in Zephyr: Via its `compatible` property, the node `/soc/uart@40002000` claims compatibility with a binding `nordic,nrf-uarte`. The comma is used to specify a _vendor prefix_ (we'll see cover this when looking at [binding names](#naming)), so we're looking for `nordic`'s model (binding) for `nrf-uarte` devices:

`zephyr/dts/arm/nordic/nrf52840.dtsi`
```dts
/ {
  soc {
    uart0: uart@40002000 {
      compatible = "nordic,nrf-uarte";
      /* ... */
    };
  };
};
```

Zephyr recursively looks for Devicetree bindings (`.yaml` files) in `zephyr/dts/bindings`. Bindings are matched against the strings provided in the `compatible` property of a node. Thus, for our UART node, Zephyr looks for a binding that matches `nordic,nrf-uarte`. Conveniently, binding files in Zephyr use the same basename as the `compatible` string, and thus we can find the correct binding by searching for a file called `nordic,nrf-uarte.yaml`, which can be found in the `serial` bindings subfolder:

`zephyr/dts/bindings/serial/nordic,nrf-uarte.yaml`
```yaml
description: Nordic nRF family UARTE (UART with EasyDMA)
compatible: "nordic,nrf-uarte"
include: ["nordic,nrf-uart-common.yaml", "memory-region.yaml"]
```

Checking the _compatible_ key, we see that it indeed matches the node's _compatible_ property. This _compatible_ key is what Zephyr really matches the Node's _compatible_ property against: In theory, the file could have a different name, but _by convention_, the filename matches what's in its _compatible_ key. Zephyr doesn't care about the convention.

Apart from _compatible_, the binding also has a textual _description_ and some *include*s. As the name suggests, the _include_ key allows to include the content of other bindings. Files are included by filename without specifying any paths or directories - Zephyr determines the search paths, one of which includes all subfolders of `zephyr/dts/bindings`. For the exact syntax, have a look at the [official documentation](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#include).

The contents of included files are essentially merged using a recursive dictionary merge. In short: Everything that's declared in included bindings is available in the including file.

> **Note:** In case you're wondering what happens with duplicated keys and/or values, try it out based on what we'll learn in the next section, where we'll create our own bindings.

Since `nordic,nrf-uarte.yaml` doesn't seem to define anything related to our properties - just like in the [article about Kconfig](https://interrupt.memfault.com/blog/practical_zephyr_kconfig) - we once again have to follow the include tree. Let's try `nordic,nrf-uart-common.yaml`:

`zephyr/dts/bindings/serial/nordic,nrf-uart-common.yaml`
```yaml
include: [uart-controller.yaml, pinctrl-device.yaml]
properties:
  # --snip--
  current-speed:
    description: |
      Initial baud rate setting for UART. Only a fixed set of baud
      rates are selectable on these devices.
    enum:
      - 1200
      - 2400
      # --snip--
      - 921600
      - 1000000
```

This must be it! There's now a key _properties_, with a child element that matches our `current-speed` property. And sure enough, the _properties_ key is used to define all [properties for nodes with the matching binding may or must contain](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#properties).

Here, Nordic seems to restrict the allowed baud rates using an *enum*eration: We can only specify values from the given list. But how does the Devicetree compiler know the type of the property? Couldn't we also use an *enum*eration to pre-define `string`s? Yes, we could, and there's indeed something missing: A key for the property's _type_.

To find out the property's type, we need to step further down the include tree, into `uart-controller.yaml`. This is Zephyr's base model for UART controllers, which is used regardless of the actual vendor:

`zephyr/dts/bindings/serial/uart-controller.yaml`
```yaml
include: base.yaml

bus: uart

properties:
  # --snip--
  current-speed:
    type: int
    description: Initial baud rate setting for UART
  # --snip--
```

Now, we finally know that `current-speed` is of type `int` and is used to configure the initial baud rate setting for UART (though the description fails to mention that the baud rate is specified in _bits per second_).

Combining this with the information in `nordic,nrf-uart-common.yaml`, we know that we can only select from a pre-defined list of baud rates and cannot specify our own custom baud rate - at least not in the Devicetree. Given this _binding_, the Devicetree compiler now rejects any but the allowed values, and it is therefore not possible to specify a _syntactically_ correct value that is not an _integer_ of the given list.

> **Note:** `bus: uart` is a special key/value pair that allows you to associate devices with a bus system, e.g., I2C, SPI or UART. This feature is especially useful if a device supports multiple bus types, e.g., a sensor that can be connected either via SPI or I2C. This is out of the scope of this article, though, but is explained nicely in the [official documentation](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#bus).

We now know about `current-speed`, but what about `status`? As you might have guessed, we need to take yet another step down the include tree and have a look at the `base.yml` binding. This binding contains common fields used by _all_ devices in Zephyr. Here, we do not only encounter the `status` property but also `compatible`:

`zephyr/dts/bindings/base/base.yaml`
```yaml
include: [pm.yaml]

properties:
  status:
    type: string
    description: indicates the operational status of a device
    enum:
      - "ok" # Deprecated form
      - "okay"
      - "disabled"
      - "reserved"
      - "fail"
      - "fail-sss"

  compatible:
    type: string-array
    required: true
    description: compatible strings
  # --snip--
```

`status` therefore is simply a property of type `string` with pre-defined values that can be assigned in the Devicetree. It indicates the operational status of a device, which we'll see in action the practical example in the next article. You can, however, imagine that a device with the status "disabled" won't be functioning.

While going through binding files may seem tedious, the include tree depth for bindings is usually quite limited, and once you know about the base bindings such as `base.yaml`, it typically comes down to a handful of files. There is, however, no conveniently "flattened" output file like `build/zephyr/zephyr.dts`, and therefore it is always necessary to walk through the bindings. We'll have a quick look at [Nordic's](https://www.nordicsemi.com/) plugin for _Visual Studio Code_ in the next article, but thus far you'll always need to look at the source files. The following shows the include tree of `nordic,nrf-uarte.yaml` at the time of writing:

```
nordic,nrf-uarte.yaml
├── nordic,nrf-uart-common.yaml
│   ├── uart-controller.yaml
│   │   └── base.yaml
│   │       └── pm.yaml
│   └── pinctrl-device.yaml
└── memory-region.yaml
```

There's one more important thing about `compatible` and matching bindings: If a node has more than one string in its `compatible` property, the build system looks for compatible bindings in the listed order and uses the **first** match.
