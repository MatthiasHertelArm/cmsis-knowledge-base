---
id: "intr-a-practical-guide-to-ble-throughpu-bluetooth-low-energy-packet-structure"
type: "concept"
domain: "debug"
title: "A Practical Guide to BLE Throughput: Bluetooth Low Energy Packet Structure"
summary: "To best understand how to optimize for BLE, it's first important to have a basic understanding of how the lower layers of the stack work together."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-24-ble-throughput-primer.md"
doc_source: "https://interrupt.memfault.com/blog/ble-throughput-primer#bluetooth-low-energy-packet-structure"
license: "CC-BY-SA-4.0"
mode: "V"
---

To best understand how to optimize for BLE, it's first important to have a basic understanding of how the lower layers of the stack work together.

{:.no_toc}

### Terminology

Before we get started, there are a couple pieces of terminology that we will use extensively below:

- **Connection Event** - For BLE, _exactly_ two devices are talking with each other in one
  _connection_. Even if data is not being exchanged, the devices must exchange a packet
  periodically to ensure the _connection_ is still alive. The start of every period in which two
  devices can exchange information with one another is known as a _Connection Event_. A connection
  itself is thus a sequence of Connection Events.

- **Connection Interval** - The time between each _Connection Event_. The _Connection Interval_ can be negotiated once the two devices are connected. Longer connection intervals save power at the cost of latency. _Connection Intervals_ can range from _7.5ms_ to _4s_.

{: #ble-radio}

### Bluetooth Baseband / Radio

For Bluetooth 4.0, the BLE Radio is capable of transmitting 1 symbol per microsecond and one bit of data can be encoded in each symbol. This gives a raw radio bitrate of 1 Megabit per second (**Mbps**). This is **not** the throughput which will be observed for several reasons:

1. There is a mandatory _150μs_ delay that must be between each packet sent. This is known as the _Inter Frame Space_ (_T_IFS_).
2. The BLE Link Layer protocol is _reliable_ meaning every packet of data sent from one side must be acknowledged (ACK'd) by the other. The size of an _ACK_ packet is _80bits_ and thus takes _80μs_ to transmit.
3. The BLE protocol has overhead for every data payload which is sent so some time is spent sending headers, etc for data payloads

> Fun Fact: As an antenna is used it heats up. As it heats up, the frequency it transmits or
> receives at can start to drift. The IFS allows for simpler antenna design & stabilization
> circuitry for BLE by giving the antenna a chance to cool down before it needs to transmit or
> receive again, which helps to keep chip costs down.

{: #ll-packet}

### The Link Layer (LL) Packet

All data during a BLE connection is sent via _Link Layer_ (**LL**) packets. All higher level messages are packed within _Data Payloads_ of _LL Packets_. Below is what a LL Packet sending data looks like (each tick mark represents 1 byte):



> NOTE: The astute reader may note that Data Payload can be up to 251 bytes. This however is an optional feature known as "LE Data Packet Length Extension" which we will explore in more detail [below](#ll-data-packet-length-extension)

{:.no_toc}

#### Maximum Link Layer Data Payload Throughput

With the three rules we mentioned about transmissions on the Bluetooth Radio in mind, let's take a look at the procedure to transmit a maximally sized LL packet.

- Side A sends a maximum size LL data packet (**27** bytes of data in a **41** byte payload) which takes **328μs** (`41 bytes * 8 bits / byte * 1Mbps`) to transmit
- Side B receives the packet and waits `T_IFS` (**150μs**)
- Side B ACKs the LL packet it received in **80μs** (**0** bytes of data)
- Side A waits `T_IFS` before sending any more data

Here's an example exchange of two packets of data in one _Connection Event_:


The time it takes to transmit one packet can be computed as:

`328μs data packet + 150μs T_IFS + 80μs ACK + 150μs T_IFS = 708μs`

During this time period, **27** bytes of actual data can be transmitted which takes **216μs**.

This yields a raw data throughput of:

`(216μs / 708μs) * 1Mbps = 305,084 bits/second = ~0.381 Mbps`

### L2CAP Channels & Payloads

L2CAP is the next layer above the Link Layer and is packed inside the **Data Payloads** of the Link Layer packets. L2CAP allows:

- unrelated data flows to be multiplexed across different _logical channels_
- fragmenting and de-fragmenting data across multiple LL Packets (since an L2CAP payload can span multiple LL Packets)

There are only a few different L2CAP channels used for Bluetooth Low Energy:

1. **Security Manager protocol** (**SMP**) - for BLE security setup
2. **Attribute protocol** (**ATT**) - Android & iOS both offer APIs that allow 3rd party apps to control transfers over this channel.
3. **LE L2CAP Connection Oriented Channels** (**CoC**) - Custom channels which are advantageous for streaming applications. Apple exposed APIs for L2CAP Channels in iOS 11[^2]. Android also exposed APIs as part of Android 10[^3]. Since both of the mobile APIs are still fairly "new" and many phones aren't running OS updates which support these features, most devices which need to talk to a mobile device still need to use ATT. If your application does not need to send data to a mobile device, it's definitely worth trying to use CoCs!

{:.no_toc}

#### The L2CAP Packet

Below is a diagram of the layout of an L2CAP packet. As you can see there are 4 bytes of overhead (Length + Channel ID) per packet sent.



### Attribute Protocol (ATT) Packet

In the _L2CAP Information Payload_ we have the ATT packet. This is the packet structure the _GATT_
protocol uses.

> NOTE: For an excellent article about GATT itself, check out Mohammad Afaneh's thorough [BLE Primer post](https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer) on the topic!

ATT packets can span multiple LL packets. The size of the data unit within an ATT packet is known
as the _Maximum Transmission Unit_ (**MTU**). The default size is 23 bytes (which allows the packet
to fit in one LL packet) but the size can be negotiated via the _Exchange MTU Request & Response_.

Per the Bluetooth Core Specification, the maximum allowed length of an attribute value (the ATT payload) is 512
bytes[^11]. While this technically means the MTU size can be slightly larger than 512 bytes (to
accommodate for the ATT protocol overhead), most bluetooth stacks support a maximum MTU value of 512 bytes.

The packet looks like this:



{:.no_toc}

#### Maximum throughput over GATT

The Attribute Protocol _Handle Value Notification_ is the best way for a server to stream data to a client when using GATT. The _Opcode Overhead_ for this operation is 2 bytes. That means there are 3 bytes of ATT packet overhead and 4 bytes of L2CAP overhead for each ATT payload. We can determine the max ATT throughput by taking the maximum raw Link Layer throughput and multiplying it by the efficiency of the ATT packet:

`ATT Throughput = LL throughput * ((MTU Size - ATT Overhead) / (L2CAP overhead + MTU Size))`

Tabulating this information for a couple common MTU sizes we get:

{: #max-throughput-gatt}

| MTU size (bytes) | Throughput (Mbps) |
| ---------------- | ----------------- |
| 23 (default)     | 0.226             |
| 185 (iOS 10 max) | 0.294             |
| 512              | 0.301             |
