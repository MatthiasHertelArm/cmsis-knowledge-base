---
id: "zep-devicetree-howtos-device-drivers-that-depend-on-other-devi"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Device drivers that depend on other devices"
summary: "At times, one struct device depends on another struct device and requires a pointer to it. For example, a sensor device might need a pointer to its SPI bus controller device. Some advice:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

At times, one `struct device` depends on another `struct device` and
requires a pointer to it. For example, a sensor device might need a pointer to
its SPI bus controller device. Some advice:

- Write your devicetree binding in a way that permits use of
  devicetree-hw-api from devicetree.h if possible.
- In particular, for bus devices, your driver's binding should include a
  file like `dts/bindings/spi/spi-device.yaml` which provides
  common definitions for devices addressable via a specific bus. This enables
  use of APIs like `DT_BUS` to obtain a node identifier for the bus
  node. You can then dt-get-device for the bus in the usual way.

Search existing bindings and device drivers for examples.
