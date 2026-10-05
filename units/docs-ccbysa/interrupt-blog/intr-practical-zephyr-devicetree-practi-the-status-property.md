---
id: "intr-practical-zephyr-devicetree-practi-the-status-property"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): The `status` property"
summary: "One important property that we've touched already is the status property. While our LED node has no such property, the referenced GPIO node in its gpios property does."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#the-status-property"
license: "CC-BY-SA-4.0"
mode: "V"
---

One important property that we've touched already is the `status` property. While our LED node has no such property, the referenced GPIO node in its `gpios` property does. The nodes are first defined in the MCU's DTS file with the `status` property set to `"disabled"`:

`zephyr/dts/arm/nordic/nrf52840.dtsi`

```dts
/ {
  soc {
    gpio0: gpio@50000000 { /* --snip-- */ status = "disabled"; port = <0>; };
    gpio1: gpio@50000300 { /* --snip-- */ status = "disabled"; port = <1>; };
  };
};
```

In the nRF52840 development kit's DTS file, the `status` property is overwritten with `"okay"`:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
&gpio0 { status = "okay"; };
&gpio1 { status = "okay"; };
```

Zephyr's introduction to Devicetree explains the `status` property in a dedicated section for [important Devicetree properties](https://docs.zephyrproject.org/2.7.5/guides/dts/intro.html#important-properties) as follows:

> "A node is considered enabled if its `status` property is either `"okay"` or not defined (i.e., does not exist in the Devicetree source). Nodes with `status` `"disabled"` are explicitly disabled. [...] Devicetree nodes which correspond to physical devices must be enabled for the corresponding `struct` device in the Zephyr driver model to be allocated and initialized."

This matches with what we've seen for the `DT_INST_FOREACH_STATUS_OKAY` macro in `gpio_nrfx.c`: Instances are only created for each node with the `status` set to `"okay"`. We can disable the node by setting the `status` to `"disabled"` in our application's board overlay file:

```dts
&gpio0 {
    status = "disabled";
};
```

Trying to recompile the project leads to the linker error that we've seen in the documentation of `DEVICE_NAME_GET`:

```
/opt/nordic/ncs/v3.2.1/zephyr/include/zephyr/device.h:84:41: error:
'__device_dts_ord_11' undeclared here (not in a function);
did you mean '__device_dts_ord_15'?
   84 | #define DEVICE_NAME_GET(dev_id) _CONCAT(__device_, dev_id)
      |                                         ^~~~~~~~~
```

The matching device object has not been allocated in `gpio_nrfx.c` and thus the linker can't resolve the symbol `__device_dts_ord_11`. For demonstration purposes (this is not typically done in an application) we _could_ transform this into a compiler error by using the `devicetree.h` API as follows:

```c#
#if DT_NODE_HAS_STATUS(DT_PHANDLE(LED_NODE, gpios), okay)
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);
#else
#error "The status of the GPIO referenced by the LED node is not 'okay'"
#endif
```

Discard the changes to the board's overlay and remove the conditional compilation in the sources. The documentation also mentions, that the `status` property is implicitly added with the value `"okay"` for nodes that do not define the property in the Devicetree. As we can see in the merged `zephyr.dts` file in the build folder, our `/leds/led_0` node doesn't have the `status` property:

`build/zephyr/zephyr.dts`

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 {
      gpios = < &gpio0 0xd 0x1 >;
      label = "Green LED 0";
    };
  };
};
```

Instead of looking into `devicetree_generated.h`, we can also check that the node is indeed implicitly assigned the `status` with the value `"okay"` using the following compile time switch and macros from `devicetree.h`:

```c
#if !DT_NODE_HAS_STATUS(LED_NODE, okay)
#error "LED node status is not okay." /* `status` is added implicitly. */
#endif
```

Rebuilding the application works without any warnings or errors and the LED continues blinking happily. You'll find such conditional compilation switches in many of Zephyr's source files. _How_ the `status` property is used varies between the corresponding subsystems.

What's the use of the `status`, then? You can and should use `status` to _disable_ all nodes that you don't need. This typically leads to a (slight) reduction of code size but is especially important for low-power applications to reduce power consumption by disabling unused peripherals.

> **Note:** In case you're wondering what the difference between the `status` property and the `is_ready_dt` function call is - you're not alone, so let's clarify this briefly. The `status` property is used to _remove_ instances altogether, whereas the `is_ready_dt` ensures that the driver is ready to be used. You can't call `is_ready_dt` with a specification for a disabled node - as we've seen, the compilation or linking fails entirely for disabled nodes.

> **Note:** The dreaded `'__device_dts_ord_<n>' undeclared` linker error can now also be investigated using [Zephyr's devicetree doctor](https://docs.zephyrproject.org/latest/develop/sca/dtdoctor.html). This devicetree doctor is a static analysis tool and can be run using `west build <your arguments> -- -DZEPHYR_SCA_VARIANT=dtdoctor`.


### Intermezzo: Power profiling

Let's apply what we've just learned and observe the MCU's current consumption with and without disabling unused nodes. To do that, I'll be using Nordic's [Power Profiler Kit](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2). You can, of course, use any clamp meter or other measurement hardware to verify the current consumption.





Without disabling unused nodes, I'm observing a current consumption in the application's sleep cycles of around *550 uA*. The screenshot below shows the measurement for an interval of 3 seconds, where the y-axis measures the current consumption truncated to a range of *0 .. 5 mA*. You should still be able to make out the three peaks in the current consumption where the MCU wakes up to toggle the LED.



How can we find out which nodes to disable?

Zephyr's board DTS files typically enable plenty of nodes, mostly for you to be able to run the samples without having to use an overlay to enable the required nodes. For a custom board, this might not be the case, meaning nodes could be _disabled_ by default and you might have to enable nodes before using them. In the end, you should be well aware of the peripherals and thus nodes that you need, and should thus _simply know_ which nodes can be disabled.

In case of doubt another good location to look for a node's `status` is the `zephyr.dts` in the build directory. I've picked the following nodes from there and disabled them in the board's overlay:

`boards/nrf52840dk_nrf52840.overlay`

```dts
&adc {status = "disabled"; };
&i2c0 {status = "disabled"; };
&i2c1 {status = "disabled"; };
&pwm0 {status = "disabled"; };
&spi0 {status = "disabled"; };
&spi1 {status = "disabled"; };
&spi3 {status = "disabled"; };
&usbd {status = "disabled"; };
&nfct {status = "disabled"; };
&temp {status = "disabled"; };
&radio {status = "disabled"; };
&uart0 {status = "disabled"; };
&uart1 {status = "disabled"; };
```

> **Note:** We're also disabling `uart0` and therefore the `/chosen` node for our console output - the boot banner `*** Booting Zephyr OS build v3.3.99-ncs1 ***` will no longer be output.

After rebuilding and flashing the application, I can perform the same measurement again and I indeed got a very different result, as you can see in the below screenshot:



Notice that the scale of the y-axis changed from *0 .. 5 mA* to  *0 .. 20 uA*, that's a factor 250 smaller! This is also visible in the MCU's current consumption in the sleep phase, which dropped from *550 uA* to an average of *7 uA*.

It is quite convenient and easy enough to disable unused peripherals. If you think that power management is Zephyr is as simple as that, however, I'll have to disappoint you: This is really just a way to disable peripherals that are _not used at all_. If we'd, e.g., need the UART while the device is not in sleep mode, we're looking at an entirely different mechanism. We'll only scratch the surface of power management in Zephyr when we have a look at [pin control](#peripheral-pin-control-in-zephyr), but for details, you'll need to dive into the [official documentation](https://docs.zephyrproject.org/latest/services/pm/index.html).

Comparing the memory usage of the build with and without optimized node status, we can also see a slight gain in the flash memory consumption:

```
# west build with all nodes "okay"
Memory region     Used Size  Region Size  %age Used
       FLASH:       27808 B         1 MB      2.65%
         RAM:        7552 B       256 KB      2.88%
    IDT_LIST:          0 GB         2 KB      0.00%
```

```
# west build with optimized node status
Memory region     Used Size  Region Size  %age Used
       FLASH:       25352 B         1 MB      2.42%
         RAM:        7552 B       256 KB      2.88%
    IDT_LIST:          0 GB         2 KB      0.00%
```
