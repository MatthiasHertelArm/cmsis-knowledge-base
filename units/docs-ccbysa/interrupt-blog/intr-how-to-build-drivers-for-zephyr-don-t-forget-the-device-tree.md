---
id: "intr-how-to-build-drivers-for-zephyr-don-t-forget-the-device-tree"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Don't forget the Device Tree"
summary: "In Zephyr, the Device Tree dictates hardware access. Gone are the days of initializing the driver in main. Instead, you must use references to the Device Tree to access peripherals."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#don-t-forget-the-device-tree"
license: "CC-BY-SA-4.0"
mode: "V"
---

In Zephyr, the Device Tree dictates hardware access. Gone are the days of initializing the driver in `main`. Instead, you must use references to the Device Tree to access peripherals.

In my case, I needed to use I2C to get the PCF85063A working. Here's what the nRF9160 Feather's Device Tree looks like before I added the PCF85063A:

```
&i2c1 {
    compatible = "nordic,nrf-twim";
    status = "okay";
    sda-pin = <26>;
    scl-pin = <27>;
};
```

Here's what it looked like after:

```
&i2c1 {
    compatible = "nordic,nrf-twim";
    status = "okay";
    sda-pin = <26>;
    scl-pin = <27>;

    pcf85063a@51 {
        compatible = "nxp,pcf85063a";
        label = "PCF85063A";
        reg = <0x51>;
    };

};
```

I got my inspiration from the drivers for the `bh1749` driver in the nRF Connect SDK. You can see how Nordic implemented it in `thingy91_nrf910_common.dts`. ([Github link](https://github.com/nrfconnect/sdk-nrf/blob/master/boards/arm/thingy91_nrf9160/thingy91_nrf9160_common.dts))

You can see that the address of the PCF85063A address of `0x51` is in two places. As the `reg` value is what the driver uses whereas the `@51` is a naming convention. This allows you to have two or more of the same device without interference. (Granted they're operating at different hardware addresses!)

The `compatible` entry references the code in `pcf85063a.c`. This value must be unique. We'll discuss this a bit more in a second.

The `label` allows us to use the device tree macros to reference the hardware.

As with any device, your driver may look different. The Zephyr project is full of example driver implementations. You can check out more in the `nrf/drivers/` folder and also the `zephyr/drivers` folder.
