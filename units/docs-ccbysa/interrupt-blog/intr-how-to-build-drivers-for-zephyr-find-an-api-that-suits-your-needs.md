---
id: "intr-how-to-build-drivers-for-zephyr-find-an-api-that-suits-your-needs"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Find an API that suits your needs"
summary: "Initialization is great, but how the heck do we use the driver. This is where a driver API comes into play."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#find-an-api-that-suits-your-needs"
license: "CC-BY-SA-4.0"
mode: "V"
---

Initialization is great, but how the heck do we *use* the driver. This is where a driver API comes into play.

In the `zephyr/include/drivers` directory, you can find all the API level code for every conceivable driver in Zephyr. In some cases, the API for your device may be there. In other cases, it may not be. The `counter_driver_api` seemed to be the best fit for the PCF85063A. Unfortunately, this API doesn't have any hooks for the clock functionality.

When you use a higher-level API, you write static functions that match the API you're working with. You pass the functions into an API struct and then on to the `DEVICE_AND_API_INIT` macro.

That was a mouthful. Let's see what it actually looks like:

```c
static const struct counter_driver_api pcf85063a_driver_api = {
    .start = pcf85063a_start,
    .stop = pcf85063a_stop,
    .get_value = pcf85063a_get_value,
    .set_alarm = pcf85063a_set_alarm,
    .cancel_alarm = pcf85063a_cancel_alarm,
    .set_top_value = pcf85063a_set_top_value,
    .get_pending_int = pcf85063a_get_pending_int,
    .get_top_value = pcf85063a_get_top_value,
    .get_max_relative_alarm = pcf85063a_get_max_relative_alarm,
};
```

Implementing a function looked something like this:

```c
static int pcf85063a_start(struct device *dev)
{

    // Get the data pointer
    struct pcf85063a_data *data = pcf85063a_dev->driver_data;

    // Turn it back on (active low)
    uint8_t reg = 0;
    uint8_t mask = PCF85063A_CTRL1_STOP;

    // Write back the updated register value
    int ret = i2c_reg_update_byte(data->i2c, DT_REG_ADDR(DT_DRV_INST(0)),
                                  PCF85063A_CTRL1, mask, reg);
    if (ret)
    {
        LOG_ERR("Unable to stop RTC. (err %i)", ret);
        return ret;
    }

    return 0;
}
```

If you check out `counter.h` you can see how you can implement your static functions:

```c
typedef int (*counter_api_start)(struct device *dev);
typedef int (*counter_api_stop)(struct device *dev);
typedef int (*counter_api_get_value)(struct device *dev, u32_t *ticks);
typedef int (*counter_api_set_alarm)(struct device *dev, u8_t chan_id,
        const struct counter_alarm_cfg *alarm_cfg);
typedef int (*counter_api_cancel_alarm)(struct device *dev, u8_t chan_id);
typedef int (*counter_api_set_top_value)(struct device *dev,
        const struct counter_top_cfg *cfg);
typedef u32_t (*counter_api_get_pending_int)(struct device *dev);
typedef u32_t (*counter_api_get_top_value)(struct device *dev);
typedef u32_t (*counter_api_get_max_relative_alarm)(struct device *dev);
typedef u32_t (*counter_api_get_guard_period)(struct device *dev, u32_t flags);
typedef int (*counter_api_set_guard_period)(struct device *dev, u32_t ticks,
        u32_t flags);

__subsystem struct counter_driver_api {
    counter_api_start start;
    counter_api_stop stop;
    counter_api_get_value get_value;
    counter_api_set_alarm set_alarm;
    counter_api_cancel_alarm cancel_alarm;
    counter_api_set_top_value set_top_value;
    counter_api_get_pending_int get_pending_int;
    counter_api_get_top_value get_top_value;
    counter_api_get_max_relative_alarm get_max_relative_alarm;
    counter_api_get_guard_period get_guard_period;
    counter_api_set_guard_period set_guard_period;
};
```

Repeat the process for all the API related functions from your `__subsystem struct` and you'll be good to go!
