---
id: "zep-debugging-debugging-i2c-communication"
type: "concept"
domain: "debug"
title: "Debugging: Debugging I2C communication"
summary: "There is a possibility to log all or some of the I2C transactions done by the application."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/debug/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/debug/index.rst"
license: "Apache-2.0"
mode: "V"
---

There is a possibility to log all or some of the I2C transactions done by the application.
This feature is enabled by the Kconfig option `CONFIG_I2C_DUMP_MESSAGES`, but it
uses the `LOG_DBG` function to print the contents so the
`CONFIG_I2C_LOG_LEVEL_DBG` option must also be enabled.

The sample output of the dump looks like this::
```
D: I2C msg: io_i2c_ctrl7_port0, addr=50
D:    W      len=01: 00
D:    R Sr P len=08:
D: contents:
D: 43 42 41 00 00 00 00 00 |CBA.....
```
The first line indicates the I2C controller and the target address of the transaction.
In above example, the I2C controller is named `io_i2c_ctrl7_port0` and the target device address
is `0x50`


**Note:** the address, length and contents values are in hexadecimal, but lack the `0x` prefix

Next lines contain messages, both sent and received. The contents of write messages is
always shown, while the content of read messages is controlled by a parameter to the
function `i2c_dump_msgs_rw`. This function is available for use by user, but is also
called internally by `i2c_transfer` API function with read content dump enabled.
Before the length parameter, the header of the message is printed using abbreviations:

  - W - write message
  - R - read message
  - Sr - restart bit
  - P - stop bit

The above example shows one write message with byte `0x00` representing the address of register to
read from the I2C target. After that the log shows the length of received message and following
that, the bytes read from the target `43 42 41 00 00 00 00 00`.
The content dump consist of both the hex and ASCII representation.


### Filtering the I2C communication dump


By default, all I2C communication is logged between all I2C controllers and I2C targets.
It may litter the log with unrelated devices and make it difficult to effectively debug the
communication with a device of interest.

Enable the Kconfig option `CONFIG_I2C_DUMP_MESSAGES_ALLOWLIST` to create an
allowlist of I2C targets to log.
The allowlist of devices is configured using the devicetree, for example::
```
/ {
    i2c {
        display0: some-display@a {
            ...
        };
        sensor3: some-sensor@b {
            ...
        };
    };

    i2c-dump-allowlist {
        compatible = "zephyr,i2c-dump-allowlist";
        devices = <&display0>, <&sensor3>;
    };
};
```
The filters nodes are identified by the compatible string with `zephyr,i2c-dump-allowlist` value.
The devices are selected using the `devices` property with phandles to the devices on the I2C bus.

In the above example, the communication with device `display0` and `sensor3` will be displayed
in the log.



.. _Eclipse IDE for C/C++ Developers: https://www.eclipse.org/downloads/packages/eclipse-ide-cc-developers/oxygen2
.. _pyOCD v0.11.0: https://github.com/pyocd/pyOCD/releases/tag/v0.11.0
