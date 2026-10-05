---
id: "intr-how-to-build-drivers-for-zephyr-using-your-driver-in-code"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Using your driver in code"
summary: "You've created a Device Tree entry and you've picked an API. You've sprinkled CMakeLists.txt and Kconfig throughout your code. It's time to use your driver!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#using-your-driver-in-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've created a Device Tree entry and you've picked an API. You've sprinkled `CMakeLists.txt` and `Kconfig` throughout your code. It's time to use your driver!

First, you'll likely want to include the high-level API to your app. Here was my include to the counter API:

```c
#include <drivers/counter.h>
```

During the early stages of your app, you can fetch your device. Using the **label** defined in your Device Tree, use the `device_get_binding` function call.

```c
// Get the device
rtc = device_get_binding("PCF85063A");
if (rtc == NULL)
{
    LOG_ERR("Failed to get RTC device binding\n");
    return;
}

LOG_INF("device is %p, name is %s", rtc, log_strdup(rtc->name));
```

This allows you to fetch the context and API access to do all the things! Instead of accessing the PCF85063A functions, you'll use the public API calls.

In my case, my code uses the `counter_get_pending_int` and `counter_cancel_channel_alarm` functions.

```c
if (!timer_flag)
{
    int ret = counter_get_pending_int(rtc);
    LOG_INF("Interrupt? %d", ret);

    if (ret == 1)
    {
        timer_flag = true;

        int ret = counter_cancel_channel_alarm(rtc, 0);
        if (ret)
        {
            LOG_ERR("Unable to cancel channel alarm!");
        }
    }
}
```

This abstracts your hardware. That way you can use this code with any other `counter_api` capable device. If you want to switch it up, change the name passed to `device_get_binding` and you'll be golden.
