---
id: "intr-how-to-build-drivers-for-zephyr-driver-smarts"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Driver Smarts"
summary: "Now that you're configured and your Device Tree is set, it's time to write some code! In this section, we'll review the important macros and nuances of driver development."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#driver-smarts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that you're configured and your Device Tree is set, it's time to write some code! In this section, we'll review the important macros and nuances of driver development.

### Helpers

Who doesn't like a handy macro that makes life easier? I found that the macros like `BIT` and `BIT_MASK` were extra useful. They're located in `zephyr/include/sys/util.h`  Here's what it looks like for the CTRL1 register of the PCF85063A

```c
#ifndef ZEPHYR_DRIVERS_RTC_PCF85063A_PCF85063A_H_
#define ZEPHYR_DRIVERS_RTC_PCF85063A_PCF85063A_H_

#define PCF85063A_CTRL1 0x00
#define PCF85063A_CTRL1_EXT_TEST BIT(7)
#define PCF85063A_CTRL1_STOP BIT(5)
#define PCF85063A_CTRL1_SR BIT(4)
#define PCF85063A_CTRL1_CIE BIT(2)
#define PCF85063A_CTRL1_12_24 BIT(1)
#define PCF85063A_CTRL1_CAP_SEL BIT(0)
```

Though these macros don't do too much, they keep your code clean and easy to read.

### `DEVICE_AND_API_INIT`

The `DEVICE_AND_API_INIT` macro adds the initialization of your driver before any user code. Here's what the setup looks like for the PCF85063A:

```c
DEVICE_AND_API_INIT(pcf85063a, DT_INST_LABEL(0), pcf85063a_init, &pcf85063a_data,
  &pcf85063_cfg_info, POST_KERNEL, CONFIG_I2C_INIT_PRIORITY,
  &pcf85063a_driver_api);
```

If we look closer at the definition, we can see what each entry does:

```c
#define DEVICE_AND_API_INIT(dev_name, drv_name, init_fn, data, cfg_info, \
level, prio, api) \
```

This allows the bulk of this private code to remain private. It's only accessible through a shared API struct. In my case, it was the `pcf85063a_driver_api`. We'll talk more about device APIs more shortly.

You can also change *when* the driver gets initialized by changing the **level** argument. Here are the levels as shown in `linker-defs.h`:

```c
#define	INIT_SECTIONS()                  \
    __init_start = .;                    \
    CREATE_OBJ_LEVEL(init, PRE_KERNEL_1) \
    CREATE_OBJ_LEVEL(init, PRE_KERNEL_2) \
    CREATE_OBJ_LEVEL(init, POST_KERNEL)  \
    CREATE_OBJ_LEVEL(init, APPLICATION)  \
    CREATE_OBJ_LEVEL(init, SMP)          \
    __init_end = .;                      \
```

In most cases, `POST_KERNEL` is good enough. If you need immediate initialization, then one of the `PRE_KERNEL` options is better.

### `DT_DRV_COMPAT`

This is a particularly important macro. It ties the **compatible** line in your Device Tree to the driver itself. Without this, we wouldn't be able to use macros like `DT_INST_LABEL(0)` to get the **label** of the device.

In my case, I defined `DT_DRV_COMPAT` as

```c
#define DT_DRV_COMPAT nxp_pcf85063a
```

This aligns with the `compatible = "nxp,pcf85063a";` set in the Device Tree. (Replacing a `,` with `_`)
