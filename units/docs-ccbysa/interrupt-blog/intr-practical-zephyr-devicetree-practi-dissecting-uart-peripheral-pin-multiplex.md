---
id: "intr-practical-zephyr-devicetree-practi-dissecting-uart-peripheral-pin-multiplex"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting UART peripheral pin multiplexing"
summary: "With &led0 we've seen that it's quite straightforward to use GPIOs in Zephyr. Changing the GPIO pin, e.g., of an LED node, can be as easy as changing the corresponding phandle's pin specifier."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#dissecting-uart-peripheral-pin-multiplexing"
license: "CC-BY-SA-4.0"
mode: "V"
---

With `&led0` we've seen that it's quite straightforward to use GPIOs in Zephyr. Changing the GPIO pin, e.g., of an LED node, can be as easy as changing the corresponding phandle's pin specifier. We'll now look at how pin assignments work for _peripherals_. For that, we'll use our old friend _UART_.

We've learned that UART is used for the console output and thus for `printk`, so let's use some `printk` calls to make use of it. We'll output `"tick"` each time the LED is turned on, and `"tock"` each time it is turned off:

```c
int main(void)
{
    int err   = 0;
    bool tick = true;

    if (!gpio_is_ready_dt(&led))
    {
        printk("Error: LED pin is not available.\n");
        return -EIO;
    }

    err = gpio_pin_configure_dt(&led, GPIO_OUTPUT_ACTIVE);
    if (err != 0)
    {
        printk("Error %d: failed to configure LED pin.\n", err);
        return -EIO;
    }

    while (1)
    {
        (void) gpio_pin_toggle_dt(&led);
        k_msleep(SLEEP_TIME_MS);

        if (tick != false) { printk("Tick\n"); }
        else { printk("Tock\n"); }
        tick = !tick;
    }
}
```

> **Note:** If you've been following along, make sure to set the UART node's status back to `"okay"` in case you've disabled it in the last section.
