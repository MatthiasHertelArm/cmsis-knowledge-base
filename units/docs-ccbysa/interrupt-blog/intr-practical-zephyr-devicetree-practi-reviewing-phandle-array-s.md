---
id: "intr-practical-zephyr-devicetree-practi-reviewing-phandle-array-s"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting the GPIO pin information type / Reviewing *phandle-array*s"
summary: "Part of: Dissecting the GPIO pin information type"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#reviewing-phandle-array-s"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting the GPIO pin information type_

Properties of type `phandle-array` are heavily used in Devicetrees. Since we now have one at hand with our *Blinky* example, let's use it to review what we've learned about `phandle-array`s - practice and repetition is the key to learning new concepts! The `/leds/led0` is defined in the board's DTS file as follows:

`(reduced) zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 {
      gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
    };
  };
};
```

The matching binding specifies that all child nodes of `led` have the required property `gpios` of type `phandle-array`:

`(reduced) zephyr/dts/bindings/led/gpio-leds.yaml`

```yaml
compatible: "gpio-leds"
child-binding:
  description: GPIO LED child node
  properties:
    gpios:
      type: phandle-array
      required: true
```

Nothing unexpected here: Since `gpios` is of type `phandle-array`, we can use it to refer to any of the board's GPIO instances. Looking at the above binding you might ask yourself: Except for the property's name, how do we know which nodes we can refer to in this `phandle-array`?

We don't.

Looking at the *Devicetree* in isolation, you can, in fact, use references to _any_ node, as long as the node has the matching `#gpio-cells` property. You could, e.g., create your own node and binding, where `#gpio-cells` doesn't use `pin` and `flags` as specifiers. E.g., we could define our own binding `custom-cells-a`:

`dts/bindings/custom-cells-a.yaml`

```yaml
description: Dummy for matching "cells"
compatible: "custom-cells-a"
gpio-cells:
  - name-of-cell-one
  - name-of-cell-two
  - name-of-cell-three
```

In our board overlay, we can create a dummy `node_a` with the above binding, and overwrite the property `gpio` of `led0` with a reference to this dummy node:

`boards/nrf52840dk_nrf52840.overlay`

```dts
/ {
    chosen {
        app-led = &led0;
    };
    node_a {
        compatible = "custom-cells-a";
        #gpio-cells = <3>;
    };
};
&led0 {
    gpios = <&{/node_a} 1 2 3>;
};
```

If we were to revert our `main.c` file to the original dummy application that doesn't use the `gpio` subsystem, the build passes without warnings and we'd find our `/leds/led_0` node with the following properties in the merged `zephyr.dts` file:

`build/zephyr/zephyr.dts`

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 {
      gpios = < &{/node_a} 0x1 0x2 0x3 >;
      label = "Green LED 0";
    };
  };
};
```

There is no mechanism in *Devicetree* that allows declaring a `phandle-array` which is _"generic over a type"_ or _"something GPIO compatible"_. E.g., there's no such thing as a _base class_, _interface_, or _trait_ that you might know from programming languages.

Even if there was an annotation `phandle-array<T>`, e.g., to specify the required `compatible` property, what would we provide for `T`? GPIO nodes use different models depending on the vendor, e.g., the following snippets show the `compatible` properties of the GPIO nodes of the nRF52840 and STM32:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    gpio0: gpio@50000000 { compatible = "nordic,nrf-gpio"; };
    gpio1: gpio@50000300 { compatible = "nordic,nrf-gpio"; };
  };
};
```

`zephyr/dts/arm/st/c0/stm32c0.dtsi`

```dts
/ {
  soc {
    pinctrl: pin-controller@50000000 {
      gpioa: gpio@50000000 { compatible = "st,stm32-gpio"; };
      gpiob: gpio@50000400 { compatible = "st,stm32-gpio"; };
      gpioc: gpio@50000800 { compatible = "st,stm32-gpio"; };
      gpiof: gpio@50001400 { compatible = "st,stm32-gpio"; };
    };
  };
};
```

Sure, both "nordic,nrf-gpio" and "st,stm32-gpio" could claim compatibility with some "base binding", but there'd always be the odd corner case that doesn't entirely match the model.

By discarding such a requirement, we gain flexibility - at the cost of "loose typing" _within the Devicetree_. If we were to try and use the Zephyr GPIO API with the above assignment to `gpios`, the application would fail to compile since the required _specifier cells_ do not have the names `pin` and `flags` read using the `DT_PHA_BY_IDX[_OR]` macros in the `GPIO_DT_SPEC_GET` macro. There's one more thing within `GPIO_DT_SPEC_GET` that is related to this discussion, can you see it?

```c
#define GPIO_DT_SPEC_GET(node_id, prop)                              \
  {                                                                  \
    .port = DEVICE_DT_GET(/* --snip-- */),                           \
    .pin = DT_PHA_BY_IDX(node_id, prop, /*idx*/0, pin),              \
    .dt_flags = DT_PHA_BY_IDX_OR(node_id, prop, /*idx*/0, flags, 0), \
  }
```

Looking at `dt_flags`, we see that `GPIO_DT_SPEC_GET` uses the `_OR` variant of the phandle macro `DT_PHA_BY_IDX` to read the `flags` from the Devicetree:

* For nodes with a _compatible binding_ that have both, `pin` and `flags` specifiers, the Devicetree compiler ensures that values are provided for both, `pin` and `flags` whenever the node is references in a `phandle-array`; providing a value for `flags` is **not** optional for such phandles.
* For nodes with a _compatible binding_ that do **not** have the `flags` specifier, the value _0_ is used in the specification. The compatible driver can also completely ignore the _flags_ field in any API call.

This adds another level of flexibility to the generic binding `gpio-leds` for LEDs, supporting any kind of GPIO node LEDs, regardless of whether or not they support using `flags`, e.g., as follows:

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 { gpios = <&gpio0 13>; };
  };
};
```
