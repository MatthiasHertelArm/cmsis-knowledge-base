---
id: "zep-device-power-management-device-power-management-x-system-power-m"
type: "concept"
domain: "optimization"
title: "Device Power Management: Device Power Management X System Power Management"
summary: "When managing power in embedded systems, it's crucial to understand the interplay between device power state and the overall system power state. Some devices may have dependencies on the system power state."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

When managing power in embedded systems, it's crucial to understand
the interplay between device power state and the overall system power
state. Some devices may have dependencies on the system power
state. For example, certain low-power states of the SoC might not
supply power to peripheral devices, leading to problems if the device
is in the middle of an operation. Proper coordination is essential to
maintain system stability and data integrity.

To avoid this sort of problem, devices must get and release lock
power states that cause power loss during an operation.

Zephyr provides a mechanism for devices to declare which power states cause power
loss and an API that automatically get and put lock on them. This feature is
enabled setting `CONFIG_PM_POLICY_DEVICE_CONSTRAINTS` to `y`.

Once this feature is enabled, devices must declare in devicetree which
states cause power loss. In the following example, device `test_dev`
says that power states `state1` and `state2` cause power loss.

```devicetree

power-states {
        state0: state0 {
                compatible = "zephyr,power-state";
                power-state-name = "suspend-to-idle";
                min-residency-us = <10000>;
                exit-latency-us = <100>;
        };

        state1: state1 {
                compatible = "zephyr,power-state";
                power-state-name = "standby";
                min-residency-us = <20000>;
                exit-latency-us = <200>;
        };

        state2: state2 {
                compatible = "zephyr,power-state";
                power-state-name = "suspend-to-ram";
                min-residency-us = <50000>;
                exit-latency-us = <500>;
        };

        state3: state3 {
                compatible = "zephyr,power-state";
                power-state-name = "suspend-to-ram";
                status = "disabled";
        };
};

test_dev: test_dev {
        compatible = "test-device-pm";
        status = "okay";
        zephyr,disabling-power-states = <&state1 &state2>;
};
```
After that devices can lock these state calling
`pm_policy_device_power_lock_get` and release with
`pm_policy_device_power_lock_put`. For example:

```C

static void timer_expire_cb(struct k_timer *timer)
{
       struct test_driver_data *data = k_timer_user_data_get(timer);

       data->ongoing = false;
       k_timer_stop(timer);
       pm_policy_device_power_lock_put(data->self);
}

void test_driver_async_operation(const struct device *dev)
{
       struct test_driver_data *data = dev->data;

       data->ongoing = true;
       pm_policy_device_power_lock_get(dev);

       /** Lets set a timer big enough to ensure that any deep
        *  sleep state would be suitable but constraints will
        *  make only state0 (suspend-to-idle) will be used.
        */
       k_timer_start(&data->timer, K_MSEC(500), K_NO_WAIT);
}
```
The same pattern applies to device paths that can produce
zero-latency interrupts. A zero-latency ISR must not call PM APIs
or other kernel APIs. If the ISR depends on resources that are unavailable in
some system power states, the normal driver path that arms the interrupt source
can hold the device power policy lock while that path is active. The driver
should mask or disable the interrupt source before releasing the lock when the
path is no longer active.
