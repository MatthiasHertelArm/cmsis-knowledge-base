---
id: "intr-practical-zephyr-devicetree-practi-basics-and-grouped-pin-control-with-the"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting UART peripheral pin multiplexing / Basics and grouped pin control with the nRF52840"
summary: "Part of: Dissecting UART peripheral pin multiplexing"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#basics-and-grouped-pin-control-with-the-nrf52840"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting UART peripheral pin multiplexing_

Let's bring up the `&uart0` node in the nRF52840 development kit's DTS file to save you some scrolling:

#### Pin control basics

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
&uart0 {
  compatible = "nordic,nrf-uarte";
  status = "okay";
  current-speed = <115200>;
  pinctrl-0 = <&uart0_default>;
  pinctrl-1 = <&uart0_sleep>;
  pinctrl-names = "default", "sleep";
};
```

The first thing we notice are the two properties `pinctrl-0` and `pinctrl-1`. The property names don't really give a hint about their semantics. You could, of course, look at the matching binding `zephyr/dts/bindings/pinctrl/pinctrl-device.yaml`, but in this case, the meaning of these properties is better described in [Zephyr's official documentation about pin control](https://docs.zephyrproject.org/latest/hardware/pinctrl/index.html):

Each device can have multiple _pin controller_ **states**. The names of the supported states are listed in the `pinctrl-names` property, in this case `"default"` and `"sleep"`. Both states are standard states defined by Zephyr for when the device is operational and in its sleep mode (if supported).

Whichever states are supported by a device is defined by its _driver_. Therefore, you can't, e.g., simply add another `pinctrl-2` and add a new name to `pinctrl-names` in an overlay and expect your application to compile or work. The _device driver_ must support multiple states for you to be able to use them.

> **Note:** We won't go into detail about how a device driver switches modes or _dynamic pin control_ in this article. Also, the `"sleep"` mode is described in more detail in Zephyr's official documentation about the [power management OS service](https://docs.zephyrproject.org/latest/services/pm/index.html). E.g., the `"sleep"` mode can be disabled using the _Kconfig_ symbol [`PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE). For now, it is enough to know that such states exist and how we can configure them.

As the names of the _phandles_ in the `pinctrl-<n>` suggest, `pinctrl-<n>` is the pin control configuration for device state with index `n` in the property `pinctrl-names`: `pinctrl-0` is used for the operational state `"default"`, and `pinctrl-1` is used for the sleep state `"sleep"`.

Except for a list of pre-defined properties that we'll see in just a bit, this is it for the standardized part of pin control! The structure of the referenced nodes is entirely vendor-specific, though vendors typically at least either follow the _grouping_ or _node approaches_ that we've mentioned before.

#### Grouped pin control

We can find the referenced nodes `&uart0_default` and `&uart0_sleep` in the matching `-pinctrl.dtsi` DTS include file of the board:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840-pinctrl.dtsi`

```dts
&pinctrl {
  uart0_default: uart0_default {
    group1 {
      psels = <NRF_PSEL(UART_TX, 0, 6)>, <NRF_PSEL(UART_RTS, 0, 5)>;
    };
    group2 {
      psels = <NRF_PSEL(UART_RX, 0, 8)>, <NRF_PSEL(UART_CTS, 0, 7)>;
      bias-pull-up;
    };
  };
  uart0_sleep: uart0_sleep {
    group1 {
      psels =
        <NRF_PSEL(UART_TX, 0, 6)>,  <NRF_PSEL(UART_RX, 0, 8)>,
        <NRF_PSEL(UART_RTS, 0, 5)>, <NRF_PSEL(UART_CTS, 0, 7)>;
      low-power-enable;
    };
  };
};
```

The above is an example of the _grouping approach_ for pin control:

Pins with common _properties_ are _grouped_ into child nodes with the name `group<m>`. E.g., the pins configured in `/pinctrl/uart0_default/group2` all use the `bias-pull-up` property to indicate that pull-up resistors are enabled for all pins in `psels`. Notice that the index `m` has nothing to do with the corresponding `pinctrl-<n>` properties of the peripheral node; it is simply used as _group_ index. All groups _combined_ contain the complete pin configuration for the state where they're referenced, e.g., _"default"_ or _"sleep"_.

> **Note:** Naming child nodes of `pinctrl` using the format `group<m>` is only a convention for the _grouped approach_. In fact, for most drivers that follow this _grouped approach_ the actual node names within the `pinctrl` node is irrelevant: The drivers simply iterate over all child nodes regardless of their names.

Within each group, Nordic uses a vendor-specific format and thus also vendor-specific binding. We can find the referenced node `&pinctrl` in the included `nrf_common.dtsi` file, where the compatible binding is defined:

`zephyr/dts/arm/nordic/nrf_common.dtsi`

```dts
/ {
  pinctrl: pin-controller {
    compatible = "nordic,nrf-pinctrl";
  };
};
```

Within the `nordic,nrf-pinctrl.yaml` binding, we find a `child-binding` property to define the child nodes of `nordic,nrf-pinctrl`:

`zephyr/dts/bindings/pinctrl/nordic,nrf-pinctrl.yaml`

```yaml
compatible: "nordic,nrf-pinctrl"
include: base.yaml

child-binding:
  child-binding:
    include:
      - name: pincfg-node.yaml
        property-allowlist:
          - bias-disable
          - bias-pull-down
          - bias-pull-up
          - low-power-enable

    properties:
      psels:
        required: true
        type: array
        description: |
          An array of pins sharing the same group properties. The pins should
          be defined using the NRF_PSEL utility macro that encodes the port,
          pin and function. NRF_PSEL_DISCONNECTED is also available to explicitly
          disconnect a pin.

      # --snip-- more nordic-specific properties
```

The property `psels` is specific to Nordic MCUs and - as documented - you're supposed to use the `NRF_PSEL` macro to create an entry in the `psels` array for all pins that you're using. This macro (defined in `zephyr/include/zephyr/dt-bindings/pinctrl/nrf-pinctrl.h`) takes the pin _function_, _port_, and _pin_ as a parameter.

Other vendors use an entirely different set of properties and macros for their Devicetree nodes and values. E.g., _Espressif_ uses the property `pinmux` instead of `psels` for the ESP32, as specified by `espressif,esp32-pinctrl.yaml`:

`zephyr/boards/espressif/esp_wrover_kit/esp_wrover_kit-pinctrl.dtsi`

```dts
&pinctrl {
  uart0_default: uart0_default {
    group1 {
      pinmux = <UART0_TX_GPIO1>;
    };
    group2 {
      pinmux = <UART0_RX_GPIO3>;
      bias-pull-up;
    };
  };
};
```

ESP32 provides a fixed [set of macros for their bindings](https://github.com/zephyrproject-rtos/hal_espressif/blob/zephyr/include/dt-bindings/pinctrl) as thoroughly documented in their [`pinctrl` index page](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/espressif%2Cesp32-pinctrl.html#dtbinding-espressif-esp32-pinctrl): On the ESP32 a particular I/O pin does not necessarily have a certain pin function. Instead of providing a parameterized macro, the fixed macros `UART0_TX_GPIO1` and `UART0_RX_GPIO3` are used to configure the GPIO and function for the corresponding pins.

But let's get back to our `&uart0` node on the nRF52840 development kit. We've now seen `psels`, but what is this `pincfg-node.yaml` include?

#### Standard pin control properties

The binding `pincfg-node.yaml` contains **standardized** pin properties that _should_, in turn, be used by a vendor's `pinctrl`. E.g., properties for the pull resistor configuration, low-power modes, slew rates, etc.

`zephyr/dts/bindings/pinctrl/pincfg-node.yaml`

```yaml
properties:
  bias-disable:
    type: boolean
    description: disable any pin bias
  # --snip--
  bias-pull-up:
    type: boolean
    description: enable pull-up resistor
  bias-pull-down:
    type: boolean
    description: enable pull-down resistor
  # --snip--
  low-power-enable:
    type: boolean
    description: enable - mode
  # --snip--
```

Each vendor can, in turn, restrict which properties are supported by MCU pins using the `property-allowlist`. The following is the matching snippet from the nRF52840 DTS file that we've seen before:

```yaml
child-binding:
  child-binding:
    include:
      - name: pincfg-node.yaml
        property-allowlist:
          - bias-disable
          - bias-pull-down
          - bias-pull-up
          - low-power-enable
```
