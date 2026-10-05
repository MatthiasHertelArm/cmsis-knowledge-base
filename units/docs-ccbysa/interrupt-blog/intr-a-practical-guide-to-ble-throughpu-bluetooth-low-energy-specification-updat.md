---
id: "intr-a-practical-guide-to-ble-throughpu-bluetooth-low-energy-specification-updat"
type: "concept"
domain: "debug"
title: "A Practical Guide to BLE Throughput: Bluetooth Low Energy Specification Updates Impacting Throughput"
summary: "Over the years, the Bluetooth SIG has added a number of additions to the Low Energy Specification to help improve the throughput that can be achieved. In this section we explore these settings."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-24-ble-throughput-primer.md"
doc_source: "https://interrupt.memfault.com/blog/ble-throughput-primer#bluetooth-low-energy-specification-updates-impacting-throughput"
license: "CC-BY-SA-4.0"
mode: "V"
---

Over the years, the Bluetooth SIG has added a number of additions to the Low Energy Specification to help improve the throughput that can be achieved. In this section we explore these settings.

> CAUTION: Even though some of these features have been around for a while, support within the ecosystem still varies. If you are planning to leverage these features, I'd strongly recommend having away to dynamically enable/disable them in your software stack. While the Bluetooth Specification has a robust set of hardware level BLE "Direct Test"s a device must pass to be certified, there really is no thorough test of the software stack itself. This in part has contributed to very buggy BLE software stacks getting shipped and numerous interoperability issues when different Bluetooth Chips try to talk to one another.

{: #ll-data-packet-length-extension}

### LE Data Packet Length Extension (BT v4.2)

As part of the 4.2 Bluetooth Core Specification revision, a new feature known as _LE Data Packet Length Extension_ was added [^1]. This _optional_ feature allows for a device to extend the length of the Data Payload in a [Link Layer packet](#ll-packet) from 27 up to 251 bytes! This means that instead of sending 27 bytes of data in a 41 byte payload, 251 bytes of data can now be sent in a 265 byte payload. Furthermore, we can send a lot more data with fewer `T_IFS` gaps. Let's take a look at what exchanging a maximally sized packet looks like:



We can calculate the raw data throughput and see that this modification yields greater than a _2x_ improvement on the maximum raw data throughput which can be achieved!

`251 bytes / 2500μs = 100.4 kBytes/sec = ~0.803 Mbps`

### LE 2M PHY (BT v5.0)

As part of the 5.0 Bluetooth Core Specification revision, a new feature known as "LE 2M PHY"[^4] was added. As you may recall in the section [above](#ble-radio), we discussed how the BLE Radio is capable of transmitting 1 symbol per μs for a bitrate of 1Mbps. This revision to the Bluetooth Low Energy Physical Layer (PHY), allows for a symbol rate of 2Mbps. This means we can transmit each individual bit in half the time. However, the 150μs IFS is still needed between transmissions. Let's take a look on how this impacts the throughput when sending packets that are using the data packet length extension feature:



We can calculate this throughput and see the modification yields almost a _4x_ improvement over the original maximal raw data speed that could be achieved with BLE 4.0:

`251 bytes / 1400μs = 179.3 kBytes/sec = ~1.434 Mbps`

### LE Coded PHY (BT v5.0)

The "LE Coded PHY" feature, also introduced in the 5.0 Spec [^4] provides a way to extend the range of BLE at the cost of speed. The feature works by encoding a bit across multiple symbols on the radio. This makes the bits being transmitted more resilient to noise. There are two operation modes where either two symbols or eight symbols can be used to encode a single bit. This effectively reduces the radio bitrate to
500 kbps or 125kbps, respectively.
