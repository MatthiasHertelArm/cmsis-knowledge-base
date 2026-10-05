---
id: "intr-a-practical-guide-to-ble-throughpu"
type: "concept"
domain: "debug"
title: "A Practical Guide to BLE Throughput"
summary: "Bluetooth Low Energy (BLE) was first added to smartphones in 2011 as part of the iPhone 4S. Since then it has become the de-facto way for smartphones to communicate with external devices."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-24-ble-throughput-primer.md"
doc_source: "https://interrupt.memfault.com/blog/ble-throughput-primer"
license: "CC-BY-SA-4.0"
mode: "V"
---

Bluetooth Low Energy (BLE) was first added to smartphones in 2011 as part of the iPhone 4S. Since then it has become the de-facto way for smartphones to communicate with external devices. While BLE was initially intended to send small amounts of information back and forth, today many applications stream large amounts of data, such as sensor data for tracking steps, binaries for firmware updates, and even audio. For these types of applications, the speed of transfer is very important.



In this article, we dive into the factors which influence BLE throughput. We will walk through the BLE protocol stack from version 4.0 to 5.1. We will discuss how to audit what is limiting throughput in a BLE connection and parameters which can be tuned to improve it. Finally, we will walk through a couple practical examples where we evaluate and optimize the throughput of a connection.



I recommend starting with our [Primer on Bluetooth Low Energy](https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer) if this is your first time working with BLE.
