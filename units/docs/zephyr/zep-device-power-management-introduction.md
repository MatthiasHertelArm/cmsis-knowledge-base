---
id: "zep-device-power-management-introduction"
type: "concept"
domain: "optimization"
title: "Device Power Management: Introduction"
summary: "Device Power Management in Zephyr is a feature which presents mechanisms to coherently affect the control of power management actions to be taken by device drivers."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

Device Power Management in Zephyr is a feature which presents mechanisms
to coherently affect the control of power management actions to be taken
by device drivers. This control is based on unambiguous expectations
which could be set by any component of the system, and on power-related
dependencies that devices may have on each other.

Zephyr supports two methods of device power management:

 - Device Runtime Power Management
 - System-Managed Device Power Management


### Device Runtime Power Management


Device runtime power management involves coordinated interaction between
device drivers, subsystems, and applications. While device drivers
play a crucial role in directly controlling the power state of
devices, the decision to suspend or resume a device can also be
influenced by higher layers of the software stack.

Each layer—device drivers, subsystems, and applications—can operate
independently without needing to know about the specifics of the other
layers because the subsystem uses reference count to check when it needs
to suspend or resume a device.

- **Device drivers** are responsible for managing the
  power state of devices. They interact directly with the hardware to
  put devices into low-power states (suspend) when they are not in
  use, and bring them back (resume) when needed. Drivers should use the
  device runtime power management APIs provided
  by Zephyr to control the power state of devices.

- **Subsystems**, such as sensors, file systems,
  and network, can also influence device power management.
  Subsystems may have better knowledge about the overall system
  state and workload, allowing them to make informed decisions about
  when to suspend or resume devices. For example, a networking
  subsystem may decide to keep a network interface powered on if it
  expects network activity in the near future.

- **Applications** running on Zephyr can impact device
  power management as well. An application may have specific
  requirements regarding device usage and power consumption. For
  example, an application that streams data over a network may need
  to keep the network interface powered on continuously.

Coordination between device drivers, subsystems, and applications is
key to efficient device power management. For example, a device driver
may not know that a subsystem will perform a series of sequential
operations that require a device to remain powered on. In such cases,
the subsystem can use device runtime power management to ensure that
the device remains in an active state until the operations are
complete.

When using this Device Runtime Power Management, the System Power
Management subsystem is able to change power states quickly because it
does not need to spend time suspending and resuming devices that are
runtime enabled.

For more information, see pm-device-runtime.


### System-Managed Device Power Management


The system managed device power management (PM) framework is a method where
devices are suspended along with the system entering a CPU (or SoC) power state.
It can be enabled by setting `CONFIG_PM_DEVICE_SYSTEM_MANAGED`.
When using this method, device power management is mostly done inside
`pm_system_suspend()`.

If a decision to enter a CPU lower power state is made, the power management
subsystem will check if the selected low power state triggers device power
management and then suspend devices before changing state. The subsystem takes
care of suspending devices following their initialization order, ensuring that
possible dependencies between them are satisfied. As soon as the CPU wakes up
from a sleep state, devices are resumed in the opposite order that they were
suspended.

The decision about suspending devices when entering a low power state is done based on the
state and if it has set the property `zephyr,pm-device-disabled`. Here is
an example of a target with two low power states with only one triggering device power
management:

```devicetree

/* Node in a DTS file */
cpus {
     power-states {
             state0: state0 {
                     compatible = "zephyr,power-state";
                     power-state-name = "standby";
                     min-residency-us = <5000>;
                     exit-latency-us = <240>;
                     zephyr,pm-device-disabled;
             };
             state1: state1 {
                     compatible = "zephyr,power-state";
                     power-state-name = "suspend-to-ram";
                     min-residency-us = <8000>;
                     exit-latency-us = <360>;
             };
     };
};
```

**Note:** When using pm-system, device transitions can be run from the idle thread. As functions in this context cannot block, transitions that intend to use blocking APIs **must** check whether they can do so with `k_can_yield`.

This method of device power management can be useful in the following scenarios:

- Systems with no device requiring any blocking operations when suspending and
  resuming. This implementation is reasonably simpler than device runtime
  power management.
- For devices that can not make any power management decision and have to be
  always active. For example a firmware using Zephyr that is controlled by an
  external entity (e.g Host CPU). In this scenario, some devices have to be
  always active and should be suspended together with the SoC when requested by
  this external entity.

It is important to emphasize that this method has drawbacks (see above) and
Device Runtime Power Management is the
**preferred** method for implementing device power management.


**Note:** When using this method of device power management, the CPU will not enter a low-power state if a device cannot be suspended. For example, if a device returns an error such as `-EBUSY` in response to the `PM_DEVICE_ACTION_SUSPEND` action, indicating it is in the middle of a transaction that cannot be interrupted. Another condition that prevents the CPU from entering a low-power state is if the option is marked as busy.


**Note:** Devices are suspended only when the last active core is entering a low power state and devices are resumed by the first core that becomes active.
