---
id: "zep-device-power-management-shell-commands"
type: "concept"
domain: "optimization"
title: "Device Power Management: Shell Commands"
summary: "Power management actions can be triggered from shell commands for testing purposes. To do that, enable the CONFIG_PM_DEVICE_SHELL option and issue a pm command on a device from the shell, for example:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

Power management actions can be triggered from shell commands for testing
purposes. To do that, enable the `CONFIG_PM_DEVICE_SHELL`
option and issue a `pm` command on a device from the shell, for example:

```console

uart:~$ device list
- buttons (active)
uart:~$ pm suspend buttons
uart:~$ device list
devices:
- buttons (suspended)
```
To print the power management state of a device, enable
`CONFIG_DEVICE_SHELL` and use the `device list` command, for
example:

```console

uart:~$ device list
devices:
- i2c@40003000 (active)
- buttons (active, usage=1)
- leds (READY)
```
In this case, `leds` does not support PM, `i2c` supports PM with manual
suspend and resume actions and it's currently active, `buttons` supports
runtime PM and it's currently active with one user.
