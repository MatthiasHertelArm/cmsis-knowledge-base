---
id: "intr-practical-zephyr-devicetree-basics-devicetree-includes-and-sources-in-zephy"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Devicetree and Zephyr / Devicetree includes and sources in Zephyr"
summary: "If you're familiar with the Devicetree specification, you might have wondered why the Devicetree snippet that we've seen before uses C/C++ style #include directives:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#devicetree-includes-and-sources-in-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Devicetree and Zephyr_

If you're familiar with the [Devicetree specification](https://www.devicetree.org/specifications/), you might have wondered why the Devicetree snippet that we've seen before uses `C/C++` style `#include` directives:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```c
#include <arm/armv7-m.dtsi>
#include "nrf_common.dtsi"
```

The [Devicetree specification](https://www.devicetree.org/specifications/) introduces a dedicated `/include/` compiler directive to include other sources in a DTS file. E.g., our include for `nrf_common.dtsi` should have the following format:

```dts
/include/ "nrf_common.dtsi"
```

The reason for this discrepancy is that Zephyr uses the `C/C++` preprocessor to resolve includes - and for resolving actual `C` macros that are used within DTS files. This happens in the call to the CMake function `zephyr_dt_preprocess` in the mentioned Devicetree CMake module.

Let's have a look at the "include" tree of the Devicetree source file of the nRF52840 development kit used in my build:

```
nrf52840dk_nrf52840.dts
├── nordic/nrf52840_qiaa.dtsi
│   ├── mem.h
│   └── nordic/nrf52840.dtsi
│       ├── arm/armv7-m.dtsi
│       │   └── skeleton.dtsi
│       └── nrf_common.dtsi
│           ├── zephyr/dt-bindings/adc/adc.h
│           ├── zephyr/dt-bindings/adc/nrf-adc.h
│           │   └── zephyr/dt-bindings/dt-util.h
│           │       └── zephyr/sys/util_macro.h
│           │           └── zephyr/sys/util_internal.h
│           │               └── util_loops.h
│           ├── zephyr/dt-bindings/gpio/gpio.h
│           ├── zephyr/dt-bindings/i2c/i2c.h
│           ├── zephyr/dt-bindings/pinctrl/nrf-pinctrl.h
│           ├── zephyr/dt-bindings/pwm/pwm.h
│           ├── freq.h
│           └── arm/nordic/override.dtsi
└── nrf52840dk_nrf52840-pinctrl.dtsi
```

> **Note:** You might have noticed the file extensions `.dts` and `.dtsi`. Both file extensions are Devicetree source files, but by convention the `.dtsi` extension is used for DTS files that are intended to be _included_ by other files.

That "include" tree makes a lot of sense, doesn't it?
- Since we didn't specify anything external in an overlay file, our outermost Devicetree source file is our _board_ `nrf52840dk_nrf52840.dts`.
- Our board uses the nRF52840 QIAA microcontroller from Nordic, which is described in its own Devicetree include source file `nrf52840_qiaa.dtsi`.
- That MCU is, in turn, a variant of the nRF52840, and therefore includes `nrf52840.dtsi`.
- The nRF52840 is an ARMv7 core, which is described in `armv7-m.dtsi`.
- In addition, the nRF52840 uses Nordic's peripherals, specified in `nrf_common.dtsi`.

The included `C/C++` header files `.h` are just a "bonus" since Zephyr uses the preprocessor and we're therefore allowed to use `C/C++` macros within Devicetree source files: All the macros will be replaced by their values before the actual compilation process. E.g., the macro `NRF_DEFAULT_IRQ_PRIORITY` in `interrupts = <2 NRF_DEFAULT_IRQ_PRIORITY>;` that we've seen before is expanded and thus replaced by its actual value before the Devicetree is compiled.

This type of include graph is very common for Devicetrees in Zephyr: You start with your _board_, which uses a specific _MCU_, which has a certain _architecture_ and vendor-specific peripherals.

Each Devicetree source file can _reference_ nodes to add, remove, or modify properties for each included file. E.g., for our console output we can find the following parts (the below snippets are incomplete!) in the Devicetree source file of the development kit:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  chosen {
    zephyr,console = &uart0;
  };
};

&uart0 {
  compatible = "nordic,nrf-uarte";
  status = "okay";
  current-speed = <115200>;
  /* other properties */
};
```

With `zephyr,console` we seem to be able to tell Zephyr that we want it to use the node `uart0` for the console output and therefore `printk` statements. We're also modifying the `&uart0` reference's properties, e.g., we set the baud rate to `115200` and enable it by setting its status to "okay".

The `uart0` node is originally defined in the included Devicetree source file of the SoC `nrf52840.dtsi`, and seems to be disabled by default:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    uart0: uart@40002000 {
      compatible = "nordic,nrf-uarte";
      reg = <0x40002000 0x1000>;
      interrupts = <2 NRF_DEFAULT_IRQ_PRIORITY>;
      status = "disabled";
    };
  };
};
```

But that's enough Devicetree syntax for now. After this step, we end up with a single `zephyr.dts.pre` Devicetree (DTS) source file in the `build/zephyr` output directory. In there, we can also find our `uart@40002000` node (with the value of the expanded `NRF_DEFAULT_IRQ_PRIORITY` macro):

`build/zephyr/zephyr.dts.pre`

```dts
/ {
  soc {
    uart0: uart@40002000 {
      compatible = "nordic,nrf-uarte";
      reg = < 0x40002000 0x1000 >;
      interrupts = < 0x2 0x1 >;
      status = "okay";
      current-speed = < 0x1c200 >;
      pinctrl-0 = < &uart0_default >;
      pinctrl-1 = < &uart0_sleep >;
      pinctrl-names = "default", "sleep";
    };
  };
};
```
