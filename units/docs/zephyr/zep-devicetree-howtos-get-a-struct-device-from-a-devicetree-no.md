---
id: "zep-devicetree-howtos-get-a-struct-device-from-a-devicetree-no"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Get a struct device from a devicetree node"
summary: "When writing Zephyr applications, you'll often want to get a driver-level struct device corresponding to a devicetree node."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

When writing Zephyr applications, you'll often want to get a driver-level
struct device corresponding to a devicetree node.

For example, with this devicetree fragment, you might want the struct device
for `serial@40002000`:

```devicetree

/ {
        soc {
                serial0: serial@40002000 {
                        status = "okay";
                        current-speed = <115200>;
                        /* ... */
                };
        };

        aliases {
                my-serial = &serial0;
        };

        chosen {
                zephyr,console = &serial0;
        };
};
```
Start by making a node identifier for the device
you are interested in. There are different ways to do this; pick whichever one
works best for your requirements. Here are some examples:

```c

/* Option 1: by node label */
#define MY_SERIAL DT_NODELABEL(serial0)

/* Option 2: by alias */
#define MY_SERIAL DT_ALIAS(my_serial)

/* Option 3: by chosen node */
#define MY_SERIAL DT_CHOSEN(zephyr_console)

/* Option 4: by path */
#define MY_SERIAL DT_PATH(soc, serial_40002000)
```
Once you have a node identifier there are two ways to proceed. One way to get a
device is to use `DEVICE_DT_GET`:

```c

const struct device *const uart_dev = DEVICE_DT_GET(MY_SERIAL);

if (!device_is_ready(uart_dev)) {
        /* Not ready, do not use */
        return -ENODEV;
}
```
There are variants of `DEVICE_DT_GET` such as
`DEVICE_DT_GET_OR_NULL`, `DEVICE_DT_GET_ONE` or
`DEVICE_DT_GET_ANY`. This idiom fetches the device pointer at
build-time, which means there is no runtime penalty. This method is useful if
you want to store the device pointer as configuration data. But because the
device may not be initialized, or may have failed to initialize, you must verify
that the device is ready to be used before passing it to any API functions.
(This check is done for you by `device_get_binding`.)

In some situations the device cannot be known at build-time, e.g., if it depends
on user input like in a shell application. In this case you can get the
`struct device` by combining `device_get_binding` with the device
name:

```c

const char *dev_name = /* TODO: insert device name from user */;
const struct device *uart_dev = device_get_binding(dev_name);
```
You can then use `uart_dev` with uart_api API functions like
`uart_configure`. Similar code will work for other device types; just
make sure you use the correct API for the device.

If you're having trouble, see dt-trouble. The first thing to check is
that the node has `status = "okay"`, like this:

```c

#define MY_SERIAL DT_NODELABEL(my_serial)

#if DT_NODE_HAS_STATUS(MY_SERIAL, okay)
const struct device *const uart_dev = DEVICE_DT_GET(MY_SERIAL);
#else
#error "Node is disabled"
#endif
```
If you see the `#error` output, make sure to enable the node in your
devicetree. In some situations your code will compile but it will fail to link
with a message similar to:

```none

...undefined reference to `__device_dts_ord_N'
collect2: error: ld returned 1 exit status
```
This likely means there's a Kconfig issue preventing the device driver from
being built, resulting in a reference that does not exist. If your code compiles
successfully, the last thing to check is if the device is ready, like this:

```c

if (!device_is_ready(uart_dev)) {
     printk("Device not ready\n");
}
```
If you find that the device is not ready, it likely means that the device's
initialization function failed. Enabling logging or debugging driver code may
help in such situations. Note that you can also use `device_get_binding`
to obtain a reference at runtime. If it returns `NULL` it can either mean that
device's driver failed to initialize or that it does not exist.
