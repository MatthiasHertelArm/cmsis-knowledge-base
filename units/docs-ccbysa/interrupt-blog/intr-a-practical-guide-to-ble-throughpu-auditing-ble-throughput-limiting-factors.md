---
id: "intr-a-practical-guide-to-ble-throughpu-auditing-ble-throughput-limiting-factors"
type: "concept"
domain: "debug"
title: "A Practical Guide to BLE Throughput: Auditing BLE Throughput Limiting Factors"
summary: "A full discussion of how to use protocol analyzers is outside the scope of this article but they can be an invaluable resource when trying to understand performance issues on your Bluetooth link."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-24-ble-throughput-primer.md"
doc_source: "https://interrupt.memfault.com/blog/ble-throughput-primer#auditing-ble-throughput-limiting-factors"
license: "CC-BY-SA-4.0"
mode: "V"
---

### LE Protocol Analyzers

A full discussion of how to use protocol analyzers is outside the scope of this article but they can be an invaluable resource when trying to understand performance issues on your Bluetooth link. They give you detailed views of the raw packets being sent over the air and very useful visualizations of the data being sent at the different protocol layers.

My two favorite analyzers on the market today are the

- Frontline Sodera LE [^5]
- Ellysis Bluetooth Explorer [^6]

Both of these are built on top of a _Software Defined Radio_ (_SDR_) meaning as the BLE spec
evolves, the vendors should be able to ship a software update adding the support rather than
requiring you purchase new hardware. Both these analyzers already support new features that have
been added as part of BLE Specification revisions (Data Packet Length Extension, Channel Selection
Algorithm #2, LE 2M & Coded PHY) which are becoming must have features when analyzing
communications between the latest BLE chips. The Ellysis analyzer will also let you feed external
GPIO lines into the analyzer that you can see synchronized with your transmissions sent over the
air, which can be super helpful for debugging classes of bugs related to RF transmit windows.

> Note: /u/introiboad on Reddit[^8] also pointed out that the Nordic BLE Sniffer[^9] can be a great
> tool for tracing connections and is a fraction of the cost because all you need to use it is a
> nRF52 development board.

### Throughput Optimization Checklist

Ultimately, there are a number of variables that influence the throughput achieved during a BLE
connection. Furthermore, there's several parameters that can vary widely depending on the software
stack of the bluetooth chip in use and have a significant impact on throughput. In the sections
below, I'll discuss the common settings to check when trying to analyze and optimize the throughput
of a connection.

> NOTE: If you are evaluating a Bluetooth chip for a new design, it's very important you are using
> a capable chip to test the new one against. If you are testing the new chip against one with the
> limitations described below, you may miss some of the limitations of the new chip being analyzed.

{:.no_toc}

#### Supported Packets Per Connection Event

The number of packets which can be transmitted in one _connection event_ is limited by the Bluetooth software stack in use. Some older devices only support one packet per connection interval. Assuming the fastest connection interval, _7.5ms_, this would mean the max raw data throughput which could be realized is only:

`27 bytes / 7.5ms = 3.6kBytes / second = 0.029 Mbps`

The end of a connection event is controlled by the _More Data_ (_MD_) bit in the header of the link layer packet discussed [above](#ll-packet). The LL packet header looks like this:



A good description of how the MD bit works can be found in the Bluetooth Core Specification [^4]



If you have a protocol analyzer, you can analyze how the MD is being set to figure out what side of the connection is responsible for limiting the throughput.

{:.no_toc}

#### Supported Connection Intervals

Many devices only support a subset of the valid connection parameter range (7.5ms - 4s). For example, Apple documents this information quite well in Section "25.6 Connection Parameters" of the "Accessory Design Guidelines For Apple Devices" [^7]:

> 

A longer connection event in itself isn't necessarily a problem for throughput. Some devices will send and receive data for an entire connection event so if you are streaming data continuously the same throughput can be realized even if you are using a 30ms interval instead of a 15ms interval.

What the connection interval _does_ impact is latency. Many higher layer protocols have messages which need to be acknowledged by higher level software components. The longer the connection interval, the longer it will take for these round trips to complete

{:.no_toc}

#### Maximum Supported ATT MTU Size

As we discussed [above](#max-throughput-gatt), the ATT MTU size has an impact on the max throughput
which can be realized when using GATT due to protocol overhead. Some chips only support the default
size (especially older Android Phones). When first testing a chip it's important to check and make
sure larger packets can be sent! It's also a good idea to see how many ATT packets you can queue up
and receive. Some stacks will only let you queue up or receive a single MTU worth of data so it's not
possible to keep the link saturated.

{:.no_toc}

#### Coexistence

A lot of devices share the 2.4GHz antenna for several different RF protocols. For example, on a phone this would typically be Bluetooth Classic (used for things like audio streaming to speakers), Bluetooth LE & WiFi. Additionally, sometimes for Bluetooth there will be multiple simultaneous connections that need to be managed.

When multiple devices are sharing the same radio, the software stack on the device will assign some prioritization between the different protocols. For example, the scheduler in a phones may prioritize traffic based on whether the app using the connection is in the foreground or background or streaming audio.

{:.no_toc}

#### Reliability

Counterintuitively, even though the Link Layer of BLE is _reliable_, packet loss is still something
to be concerned about for BLE. This is because many many stacks drop data within the software
stack. For example, BLE messages get queued up in the stack and when the heap holding the packets
runs out of memory, some stacks will silently drop data. This means if you are sending large
amounts of data over BLE you will usually want to add some sort of reliability layer that can
detect & retransmit messages when data is dropped. The way this is implemented can have sizeable
impacts on throughput. For example, if you have designed your own protocol on top of L2CAP or GATT
and every message sent requires an acknowledgement before another message is sent, you'll typically
wind up adding a connection interval worth of latency getting the data sent out, effectively
halving the max throughput which can be achieved.

> NOTE: If you are using GATT and trying to optimize throughput you will want to check the GATT
> operation types being used.[^10] From a _Server_ to a _Client_, it is favorable to send
> **Notifications** instead of **Indications** because **Indications** require a round trip
> **Confirmation** to be sent before another message can be sent. From a _Client_ to a _Server_ you
> will want to use **Write Commands** instead of **Write Requests** because **Requests** require a
> **Response** from the _Server_. In general, I'd advise not relying on **Indications** or
> **Requests** if you need reliability because data can _still_ be dropped on many stacks before
> making it to your application (especially on mobile).

#### Maximum Supported Link Layer Data Packet Size

As mentioned [above](#ll-data-packet-length-extension), as of Bluetooth 4.2, the size of a Link
Layer data payload can be up to 251 bytes. However, not all devices support this maximal
size. Ideally, you'll want to test the chip you are using and make sure it supports the entire
range. For optimal throughput you'll want to make sure the connection interval is an integer
multiple of the packet transmission time. We will walk through an example of this
[below](#optimal-connection-interval-example)
