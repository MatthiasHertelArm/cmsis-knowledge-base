---
id: "zep-device-runtime-power-management-implementation-guidelines"
type: "concept"
domain: "optimization"
title: "Device Runtime Power Management: Implementation guidelines"
summary: "In a first place, a device driver needs to implement the PM action callback used by the PM subsystem to suspend or resume devices."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/device_runtime.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/device_runtime.rst"
license: "Apache-2.0"
mode: "V"
---

In a first place, a device driver needs to implement the PM action callback used
by the PM subsystem to suspend or resume devices.

```c

static int mydev_pm_action(const struct device *dev,
                           enum pm_device_action action)
{
    switch (action) {
    case PM_DEVICE_ACTION_SUSPEND:
        /* suspend the device */
        ...
        break;
    case PM_DEVICE_ACTION_RESUME:
        /* resume the device */
        ...
        break;
    default:
        return -ENOTSUP;
    }

    return 0;
}
```
The PM action callback calls are serialized by the PM subsystem, therefore, no
special synchronization is required.

To enable device runtime power management on a device, the driver needs to call
`pm_device_runtime_enable` at initialization time. Note that this
function will suspend the device if its state is
`PM_DEVICE_STATE_ACTIVE`. In case the device is physically
suspended, the init function should call
`pm_device_init_suspended` before calling
`pm_device_runtime_enable`.

```c

/* device driver initialization function */
static int mydev_init(const struct device *dev)
{
    int ret;
    ...

    /* OPTIONAL: mark device as suspended if it is physically suspended */
    pm_device_init_suspended(dev);

    /* enable device runtime power management */
    ret = pm_device_runtime_enable(dev);
    if (ret < 0) {
        return ret;
    }
}
```
Device runtime power management can also be automatically enabled on a device
instance by adding the `zephyr,pm-device-runtime-auto` flag onto the corresponding
devicetree node. If enabled, `pm_device_runtime_enable` is called immediately
after the `init` function of the device runs and returns successfully.

```dts

foo {
    /* ... */
    zephyr,pm-device-runtime-auto;
};
```
Assuming an example device driver that implements an `operation` API call, the
*get* and *put* operations could be carried out as follows:

```c

static int mydev_operation(const struct device *dev)
{
    int ret;

    /* "get" device (increases usage count, resumes device if suspended) */
    ret = pm_device_runtime_get(dev);
    if (ret < 0) {
        return ret;
    }

    /* do something with the device */
    ...

    /* "put" device (decreases usage count, suspends device if no more users) */
    return pm_device_runtime_put(dev);
}
```
In case the suspend operation is *slow*, the device driver can use the
asynchronous API:

```c

static int mydev_operation(const struct device *dev)
{
    int ret;

    /* "get" device (increases usage count, resumes device if suspended) */
    ret = pm_device_runtime_get(dev);
    if (ret < 0) {
        return ret;
    }

    /* do something with the device */
    ...

    /* "put" device (decreases usage count, schedule suspend if no more users) */
    return pm_device_runtime_put_async(dev, K_NO_WAIT);
}
```
