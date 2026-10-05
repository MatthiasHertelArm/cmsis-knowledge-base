---
id: "intr-practical-zephyr-devicetree-practi-node-approach-with-the-stm32"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting UART peripheral pin multiplexing / Node approach with the STM32"
summary: "Part of: Dissecting UART peripheral pin multiplexing"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#node-approach-with-the-stm32"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting UART peripheral pin multiplexing_

Having seen the _grouped approach_, let's see how the _node approach_ is applied for the STM32 by looking at the
[STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html)'s DTS file:

`zephyr/boards/st/nucleo_c031c6/nucleo_c031c6.dts`

```dts
&usart2 {
  pinctrl-0 = <&usart2_tx_pa2 &usart2_rx_pa3>;
  pinctrl-names = "default";
  current-speed = <115200>;
  status = "okay";
};
```

Since the `pinctrl-<x>` properties are predefined by Zephyr, the format of the above snippet looks very familiar: The `pinctrl-names` only contains the operational mode `"default"` - it thus seems like the `"sleep"` mode is not supported (yet) by the STM32 drivers. Therefore, only `pinctrl-0` is provided, which now contains _two_ references instead of one.

Aside from the fact that we're using **two** _phandles_, the node names already indicate that this is a node-based approach with fixed pin multiplexing. This is especially clear when comparing the node names to the _alternate function mapping_ table in the datasheet:

- Pin _PA2_ has the alternative function `AF1=USART2_TX`, matching `usart2_tx_pa2`
- Pin _PA3_ has the alternative function `AF1=USART2_RX`, matching `usart2_rx_pa3`

The content in the matching DTS file in the [STM32 HAL](https://github.com/zephyrproject-rtos/hal_stm32) specifies just that:

`hal_stm32/dts/st/c0/stm32c031c(4-6)tx-pinctrl.dtsi`

```dts
/ {
  soc {
    pinctrl: pin-controller@50000000 {
      /omit-if-no-ref/ usart2_tx_pa2: usart2_tx_pa2 {
        pinmux = <STM32_PINMUX('A', 2, AF1)>;
        bias-pull-up;
      };
      /omit-if-no-ref/ usart2_rx_pa3: usart2_rx_pa3 {
        pinmux = <STM32_PINMUX('A', 3, AF1)>;
      };
    };
  };
};
```

> **Note:** If you're also using the Nordic toolchain installer to install Zephyr, you won't find the `stm32c031c(4-6)tx-pinctrl.dtsi` locally, since `hal_stm32` is not included in the installation. Check the [STM32 HAL on GitHub](https://github.com/zephyrproject-rtos/hal_stm32) until we solve this problem in the next article.

> **Note:** `/omit-if-no-ref/` is used to tell the Devicetree generator that no code should be generated for the node in case it is not referenced in the Devicetree. This avoids adding unnecessary content to the Devicetree since `pinctrl` nodes are only used when referenced.

On the STM32, the RX and TX functionality for `USART2` can only be selected via a pin's alternative function and is therefore not available on all pins. Instead of providing macros for all combinations, in the node approach, you'll find predefined _nodes_ for all pins and functions, e.g., for `USART2_TX` the following nodes exist in `stm32c031c(4-6)tx-pinctrl.dtsi`.

- `usart2_tx_pa2`
- `usart2_tx_pa4`
- `usart2_tx_pa8`
- `usart2_tx_pa14`

The `USART2_TX` functionality is therefore only available on the pins _PA2_, _PA4_, _PA8_ and _PA14_, as specified in the datasheet. The order in which the pins are assigned to `pinctrl-<n>` is again irrelevant since the pin's configuration determines its function. E.g., selecting `AF1` for the pin _PA2_ means that this pin is used for UART-TX of the USART2 peripheral.

As stated in [Zephyr's official documentation about pin control](https://docs.zephyrproject.org/latest/hardware/pinctrl/index.html), the _node approach_ method is discouraged if autogeneration is not an option. Therefore, you should really only encounter this pattern for MCUs where predefined nodes exist for all possible pin/function combinations.

This also means, that for MCUs using the _node approach_ you should **never** attempt to change the properties of the `pinctrl` nodes, e.g., in your overlay files. When mapping a peripheral to a different set of pins, you should instead _change_ the node **references** in the `pinctrl-<n>` property.
