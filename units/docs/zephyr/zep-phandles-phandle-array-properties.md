---
id: "zep-phandles-phandle-array-properties"
type: "concept"
domain: "project"
title: "Phandles: phandle-array properties"
summary: "These properties are commonly used to specify a resource that is owned by another node along with additional metadata about the resource."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

These properties are commonly used to specify a resource that is owned by
another node along with additional metadata about the resource.


### High level description


Usually, properties with this type are written like `phandle-array-prop` in
this example:

```dts

node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>, <&baz 4 5>;
};
```
That is, the property's value is written as a comma-separated sequence of
"groups", where each "group" is written inside of angle brackets (`< ... >`).
Each "group" starts with a phandle (`&foo`, `&bar`, `&baz`). The values
that follow the phandle in each "group" are called *specifiers*. There are
three specifiers in the above example:

#. `1 2`
#. `3`
#. `4 5`

The phandle in each "group" is used to "point" to the hardware that controls
the resource you are interested in. The specifier describes the resource
itself, along with any additional necessary metadata.

The rest of this section describes a common example. Subsequent sections
document more rules about how to use phandle-array properties in practice.


### Example phandle-arrays: GPIOs


Perhaps the most common use case for phandle-array properties is specifying one
or more GPIOs on your SoC that another chip on your board connects to. For that
reason, we'll focus on that use case here. However, there are **many other use
cases** that are handled in devicetree with phandle-array properties.

For example, consider an external chip with an interrupt pin that is connected
to a GPIO on your SoC. You will typically need to provide that GPIO's
information (GPIO controller and pin number) to the :ref:`device driver
<device_model_api>` for that chip. You usually also need to provide other
metadata about the GPIO, like whether it is active low or high, what kind of
internal pull resistor within the SoC should be enabled in order to communicate
with the device, etc., to the driver.

In the devicetree, there will be a node that represents the GPIO controller
that controls a group of pins. This reflects the way GPIO IP blocks are usually
developed in hardware. Therefore, there is no single node in the devicetree
that represents a GPIO pin, and you can't use a single phandle to represent it.

Instead, you would use a phandle-array property, like this:

```

my-external-ic {
        irq-gpios = <&gpioX pin flags>;
};
```
In this example, `irq-gpios` is a phandle-array property with just one
"group" in its value. `&gpioX` is the phandle for the GPIO controller node
that controls the pin. `pin` is the pin number (0, 1, 2, ...). `flags` is a
bit mask describing pin metadata (for example ``(GPIO_ACTIVE_LOW |
GPIO_PULL_UP)``); see `include/zephyr/dt-bindings/gpio/gpio.h` for
more details.

The device driver handling the `my-external-ic` node can then use the
`irq-gpios` property's value to set up interrupt handling for the chip as it
is used on your board. This lets you configure the device driver in devicetree,
without changing the driver's source code.

Such properties can contain multiple values as well:

```

my-other-external-ic {
        handshake-gpios = <&gpioX pinX flagsX>, <&gpioY pinY flagsY>;
};
```
The above example specifies two pins:

- `pinX` on the GPIO controller with phandle `&gpioX`, flags `flagsX`
- `pinY` on `&gpioY`, flags `flagsY`

You may be wondering how the "pin and flags" convention is established and
enforced. To answer this question, we'll need to introduce a concept called
specifier spaces before moving on to some information about devicetree
bindings.
