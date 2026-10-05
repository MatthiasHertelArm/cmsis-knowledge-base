---
id: "intr-bluetooth-low-energy-a-primer-bluetooth-classic-vs-bluetooth-low-energ"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Bluetooth Classic vs. Bluetooth Low Energy"
summary: "Itʼs important to note that thereʼs a big difference between Bluetooth Classic and Bluetooth Low Energy in terms of technical specification, implementation, and the types of applications to which theyʼre each suited."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#bluetooth-classic-vs-bluetooth-low-energy"
license: "CC-BY-SA-4.0"
mode: "V"
---

Itʼs important to note that thereʼs a big difference between Bluetooth Classic and Bluetooth Low Energy in terms of technical specification, implementation, and the types of applications to which theyʼre each suited. This is in addition to the fact that they are **incompatible** with each other.

Some of the notable differences are summarized in the following table:

| Bluetooth Classic                                                                                  | BLE                                                                                                 |
| :--------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------: |
| Used for streaming applications such as audio streaming, file transfers, and headsets              |              Used for sensor data, control of devices, and low-bandwidth applications               |
| Not optimized for low power, but has a higher data rate (3Mbps maximum compared to 2Mbps for BLE) |                              Meant for low power, low duty data cycles                              |
| Operates over 79 RF (radio frequency) channels                                                                       |                           Operates over 40 RF channels.                           |
| Discovery occurs on 32 channels                                                                    | Discovery occurs on 3 channels, leading to quicker discovery and connections than Bluetooth Classic |




BLE has gone through some major revisions and changes in the short time since its official release in 2010, with the most recent major updates being Bluetooth 5 released in December 2016 and Bluetooth 5.1 released in January 2019.

Bluetooth 5 introduced many important upgrades to the Bluetooth specification, most of which were focused on BLE. Some of the most important enhancements include twice the speed, four times the range, and eight times the advertising data capacity.

On the other hand, Bluetooth 5.1 focused on *direction finding* by utilizing Angle of Arrival (AoA) and Angle of Departure (AoD) techniques.
