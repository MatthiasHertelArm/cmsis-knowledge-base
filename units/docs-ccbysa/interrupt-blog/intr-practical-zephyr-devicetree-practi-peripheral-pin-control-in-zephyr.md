---
id: "intr-practical-zephyr-devicetree-practi-peripheral-pin-control-in-zephyr"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting UART peripheral pin multiplexing / Peripheral pin control in Zephyr"
summary: "Part of: Dissecting UART peripheral pin multiplexing"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#peripheral-pin-control-in-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting UART peripheral pin multiplexing_

To see how pins are assigned to our UART peripheral, we need to look into our board's DTS file. There, we find `pinctrl-<x>` properties for the `&uart0` node:

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

Before we look at how `pinctrl` works, you might ask yourself why we need another mechanism when we have `gpios`, and what the difference between the two is. Couldn't we just use `gpios` and, e.g., pass _phandles_ for all the pins we need for our UART interface?

For some MCUs, like Nordic's nRF series, this might work since pin multiplexing for such MCUs is not restricted: On Nordic's MCUs it is possible to assign any functionality to any pin. Other MCUs (e.g., STM32) typically restrict this and clearly define possible alternate pin functions for all pins.

MCU manufacturers can be quite creative when it comes to pin multiplexing, and before Zephyr 3.0, pin multiplexing was entirely vendor-specific. Zephyr 3.0 adopted the [Linux `pinctl`](https://www.kernel.org/doc/html/v4.13/driver-api/pinctl.html) concept as a _standardized_ way of assigning peripheral functions to pins in Devicetree - and called it `pinctrl`.

There is, of course, still an overlap between `gpios` and `pinctrl` since both associate nodes with pins and their parameters (e.g., pull resistors). As a rule of thumb, `pinctrl` is generally used if the pin goes to a **peripheral** in the `/soc` node, whereas `gpios` are used if the pin is used directly by the application.

#### Pin control concepts

[Zephyr's official documentation](https://docs.zephyrproject.org/latest/hardware/pinctrl/index.html) distinguishes between two general concepts: _Distributed_ and _centralized_ pin control. The difference between the two concepts is essentially defined by which device decides about possible pin assignments, as we've seen before:

**Distributed pin control**

Some MCUs, such as the nRF series from Nordic, do not restrict pin assignments, and the pin assignment is defined by each _peripheral_. E.g., the UART node selects whichever pins it uses for RXD, TXD, CTS, and RTS. The pin control is thus _distributed_ across all peripherals; there is no centralized pin multiplexer.

**Centralized pin control**

Other MCUs, such as the STM32, do not allow an arbitrary pin assignment. Instead, pins support alternative functions, managed by a centralized pin multiplexer which assigns the pin to a certain _peripheral_.

**Devicetree approach**

Whether an MCU uses centralized or distributed pin control does not necessarily have an impact on how the pin control is reflected in the Devicetree. Zephyr supports two approaches in _Devicetree_ for pin multiplexing: **Grouped** and **node** approach.

- In the **node approach** the vendor provides a DTS file containing dedicated nodes for **all** pins and the supported alternative functions. The provided nodes are referenced **unmodified** by the `pinctrl` properties of the peripheral. This is mostly used for MCUs with centralized pin control and fixed alternative functions and we'll see a practical example when browsing the [STM32 Devicetree source files](#node-approach-with-the-stm32).

- In the **grouped approach** the vendor's Devicetree sources do not provide nodes for all possible combinations. Instead, nodes containing the pin configuration are created either for the board or by the application, and pins are grouped by their configuration (e.g., pull resistors), thus the name "grouped". The pin multiplexing may or may not be restricted and thus this approach is for both, distributed and centralized pin multiplexing. We'll see this when we browse the [Nordic Devicetree source files in the next section](#node-approach-with-the-stm32).

Neither concept or approach is "better or worse", it is just what's implemented by hardware. As mentioned, MCU manufacturers can be very, very creative, and thus pin control will probably always remain vendor-specific.
