---
id: "zep-shields-gpio-nexus-nodes"
type: "concept"
domain: "bring-up"
title: "Shields: GPIO nexus nodes"
summary: "GPIOs accessed by the shield peripherals must be identified using the shield GPIO abstraction, for example from the arduino-header-r3 compatible. Boards that provide the header must map the header pins to SOC-specific pins."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

GPIOs accessed by the shield peripherals must be identified using the
shield GPIO abstraction, for example from the `arduino-header-r3`
compatible.  Boards that provide the header must map the header pins
to SOC-specific pins.  This is accomplished by including a `nexus
node`_ that looks like the following into the board devicetree file:

```devicetree

arduino_header: connector {
        compatible = "arduino-header-r3";
        #gpio-cells = <2>;
        gpio-map-mask = <0xffffffff 0xffffffc0>;
        gpio-map-pass-thru = <0 0x3f>;
        gpio-map = <0 0 &gpioa 0 0>,    /* A0 */
                   <1 0 &gpioa 1 0>,    /* A1 */
                   <2 0 &gpioa 4 0>,    /* A2 */
                   <3 0 &gpiob 0 0>,    /* A3 */
                   <4 0 &gpioc 1 0>,    /* A4 */
                   <5 0 &gpioc 0 0>,    /* A5 */
                   <6 0 &gpioa 3 0>,    /* D0 */
                   <7 0 &gpioa 2 0>,    /* D1 */
                   <8 0 &gpioa 10 0>,   /* D2 */
                   <9 0 &gpiob 3 0>,    /* D3 */
                   <10 0 &gpiob 5 0>,   /* D4 */
                   <11 0 &gpiob 4 0>,   /* D5 */
                   <12 0 &gpiob 10 0>,  /* D6 */
                   <13 0 &gpioa 8 0>,   /* D7 */
                   <14 0 &gpioa 9 0>,   /* D8 */
                   <15 0 &gpioc 7 0>,   /* D9 */
                   <16 0 &gpiob 6 0>,   /* D10 */
                   <17 0 &gpioa 7 0>,   /* D11 */
                   <18 0 &gpioa 6 0>,   /* D12 */
                   <19 0 &gpioa 5 0>,   /* D13 */
                   <20 0 &gpiob 9 0>,   /* D14 */
                   <21 0 &gpiob 8 0>;   /* D15 */
};
```
This specifies how Arduino pin references like ``<&arduino_header 11
0>` are converted to SOC gpio pin references like `<&gpiob 4 0>``.

In Zephyr GPIO specifiers generally have two parameters (indicated by
`#gpio-cells = <2>`): the pin number and a set of flags.  The low 6
bits of the flags correspond to features that can be configured in
devicetree.  In some cases it's necessary to use a non-zero flag value
to tell the driver how a particular pin behaves, as with:

```devicetree

drdy-gpios = <&arduino_header 11 GPIO_ACTIVE_LOW>;
```
After preprocessing this becomes `<&arduino_header 11 1>`.  Normally
the presence of such a flag would cause the map lookup to fail,
because there is no map entry with a non-zero flags value.  The
`gpio-map-mask` property specifies that, for lookup, all bits of the
pin and all but the low 6 bits of the flags are used to identify the
specifier.  Then the `gpio-map-pass-thru` specifies that the low 6
bits of the flags are copied over, so the SOC GPIO reference becomes
`<&gpiob 4 1>` as intended.

See nexus node for more information about this capability.
