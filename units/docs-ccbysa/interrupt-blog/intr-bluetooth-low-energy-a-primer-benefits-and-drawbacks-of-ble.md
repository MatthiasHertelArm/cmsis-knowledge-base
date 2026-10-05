---
id: "intr-bluetooth-low-energy-a-primer-benefits-and-drawbacks-of-ble"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Benefits and Drawbacks of BLE"
summary: "Every technology has its own benefits and limitations, and BLE is no exception. It’s important to know these pros and cons to be able to determine whether BLE is suitable for your specific application and use case or not."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#benefits-and-drawbacks-of-ble"
license: "CC-BY-SA-4.0"
mode: "V"
---

Every technology has its own benefits and limitations, and BLE is no exception. It’s important to know these pros and cons to be able to determine whether BLE is suitable for your specific application and use case or not.

### Benefits
- Lower power consumption even when compared to other low power technologies.
  This is achieved by keeping the radio off as much as possible and sending small amounts of data at low transfer speeds.
- No cost to access the official specification documents. With most other wireless protocols and technologies, you would have to be a member of the official group or consortium for that technology in order to access the specification.
- Lower cost of modules and chipsets, even when compared to other similar technologies.
- Most importantly, its existence in most smartphones in the market.
### Drawbacks and limitations
- **Data Throughput**: the data throughput of BLE is limited by the physical radio layer (PHY) data rate, which is the rate at which the radio transmits data. This rate depends on the Bluetooth version used. For Bluetooth 4.2 and earlier, the rate is fixed at 1 Mbps. For Bluetooth 5 and later, however, the rate varies depending on the mode and PHY used. The rate can be 1 Mbps like earlier versions, or 2 Mbps when utilizing the high-speed feature.
- **Range**: Bluetooth Low Energy (and Bluetooth in general) was designed for short-range applications and hence its range of operation is limited. There are a few factors that affect the range of BLE:
	- BLE operates in the 2.4 GHz ISM spectrum which is greatly affected by obstacles that exist all around us such as metal objects, walls, and water (especially human bodies).
	- Performance and design of the antenna of the BLE device.
	- Physical enclosure and orientation of the device.

- **Gateway Requirement for Internet Connectivity**: In order to transfer data from a BLE-only device to the Internet, another BLE device that has an IP connection is needed to receive this data and then, in turn, relay it to another IP device (or to the Internet).
