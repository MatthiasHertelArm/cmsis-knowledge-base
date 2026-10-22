---
id: "zep-devicetree-howtos-use-devicetree-overlays"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Use devicetree overlays"
summary: "See set-devicetree-overlays for how to add an overlay to the build."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

See set-devicetree-overlays for how to add an overlay to the build.

Overlays can override node property values in multiple ways.
For example, if your BOARD.dts contains this node:

```devicetree

/ {
        soc {
                serial0: serial@40002000 {
                        status = "okay";
                        current-speed = <115200>;
                        /* ... */
                };
        };
};
```
These are equivalent ways to override the `current-speed` value in an
overlay:

.. Disable syntax highlighting as this construct does not seem supported by pygments
```none

/* Option 1 */
&serial0 {
    current-speed = <9600>;
};

/* Option 2 */
&{/soc/serial@40002000} {
    current-speed = <9600>;
};
```
We'll use the `&serial0` style for the rest of these examples.

You can add aliases to your devicetree using overlays: an alias is just a
property of the `/aliases` node. For example:

```devicetree

/ {
    aliases {
        my-serial = &serial0;
    };
};
```
Chosen nodes work the same way. For example:

```devicetree

/ {
    chosen {
        zephyr,console = &serial0;
    };
};
```
To delete a property (in addition to deleting properties in general, this is
how to set a boolean property to false if it's true in BOARD.dts):

```devicetree

&serial0 {
    /delete-property/ some-unwanted-property;
};
```
You can add subnodes using overlays. For example, to configure a SPI or I2C
child device on an existing bus node, do something like this:

```devicetree

/* SPI device example */
&spi1 {
 my_spi_device: temp-sensor@0 {
     compatible = "...";
     label = "TEMP_SENSOR_0";
     /* reg is the chip select number, if needed;
      * If present, it must match the node's unit address. */
     reg = <0>;

     /* Configure other SPI device properties as needed.
      * Find your device's DT binding for details. */
     spi-max-frequency = <DT_FREQ_M(4)>;
 };
};

/* I2C device example */
&i2c2 {
 my_i2c_device: touchscreen@76 {
     compatible = "...";
     label = "TOUCHSCREEN";
     /* reg is the I2C device address.
      * It must match the node's unit address. */
     reg = <76>;

     /* Configure other I2C device properties as needed.
      * Find your device's DT binding for details. */
 };
};
```
Other bus devices can be configured similarly:

- create the device as a subnode of the parent bus
- set its properties according to its binding

Assuming you have a suitable device driver associated with the
`my_spi_device` and `my_i2c_device` compatibles, you should now be able to
enable the driver via Kconfig and get the struct device
for your newly added bus node, then use it with that driver API.
