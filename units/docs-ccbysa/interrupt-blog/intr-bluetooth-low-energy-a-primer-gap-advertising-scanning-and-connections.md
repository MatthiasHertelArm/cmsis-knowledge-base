---
id: "intr-bluetooth-low-energy-a-primer-gap-advertising-scanning-and-connections"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: GAP, Advertising, Scanning, and Connections"
summary: "GAP stands for Generic Access Profile. It provides a framework that defines how BLE devices interact with each other. This includes:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#gap-advertising-scanning-and-connections"
license: "CC-BY-SA-4.0"
mode: "V"
---

GAP stands for Generic Access Profile. It provides a framework that defines how BLE devices interact with each other. This includes:

- Roles of BLE devices
- Advertisements (Broadcasting, Discovery, Advertisement parameters, Advertisement data)
- Connection establishment (initiating connections, accepting connections, Connection parameters)
- Security

The different roles of a BLE device are:

- **Broadcaster**: a device that sends out Advertisements and does not receive packets or allow Connections from others.
- **Observer**: a device that listens to others sending out Advertising Packets, but does not initiate a Connection with the Advertising device.
- **Central**: a device that discovers and listens to other devices that are Advertising. A Central also has the capability of connecting to an Advertising device.
- **Peripheral**: a device that Advertises and accepts Connections from Central devices.

Keep in mind that a single device may operate in multiple Roles at the same time. For example, your smartphone can operate in the Central role when communicating with your smartwatch, and also act in the Peripheral role while communicating with a PC.

### Advertising & Scanning
In the Advertising state a device sends out packets containing useful data for others to receive and process. The packets are sent at a fixed interval defined as the Advertising Interval. There are 40 RF channels in BLE, each separated by 2 MHz (center-to-center), as shown in the following figure. Three of these channels are called the Primary Advertising Channels, while the remaining 37 channels are used for Secondary Advertisements and for Data Packet transfer during a Connection.



Advertisements always start with Advertisement Packets sent on the 3 Primary Advertising Channels (or a subset of these Channels). This allows Centrals to find the Advertising device (Peripheral or Broadcaster) and parse its Advertising packets. The Central can then Initiate a Connection if the Advertiser allows it (Peripheral devices).

### Scanning
Centrals tune into the three Primary Advertising Channels one at a time. So, in order for a Central to discover a Peripheral, the Central has to be tuned into the same channel that the Peripheral is Advertising on at that given point. To increase the possibility of this happening, and in order to make it happen quickly, the different advertising and scanning parameters can be adjusted.

### Connections
In order for two BLE devices to connect to each other, the following needs to happen:

- The Peripheral needs to start Advertising and send out Connectable Advertisement packets.
- The Central device needs to be Scanning for Advertisements while the Peripheral is Advertising.
- If the Central happens to be listening on an Advertising Channel that the Peripheral is Advertising on, then the Central device discovers the Peripheral and is able to read the Advertisement packet and all the necessary information in order to establish a Connection.
- The Central then sends a Connection Request packet.
- The peripheral always listens for a short interval on the same Advertising Channel after it sends out the Advertising packet. This allows it to receive the Connection Request packet from the Central device — which triggers the forming of the Connection between the two devices.

After that, the Connection is considered “created” but not yet “established”. A Connection is considered “established ” once the device receives a packet from its peer device. After a Connection becomes established, the Central becomes known as the Master, and the Peripheral becomes known as the Slave. The Master is responsible for managing the Connection, controlling the Connection Parameters and the timing of the different events within a Connection.

#### Connection Events
During a Connection Event, the Master and Slave alternate sending data packets to each other until neither side has data to send. Here are a few aspects of Connections that are very important to know:

- A Connection Event contains at least one packet sent by the Master.
The Slave always sends a packet back if it received a packet from the Master.
- If the Master does not receive a packet back from the Slave, the Master will close the Connection Event — it resumes sending packets at the next Connection Event.
- The Connection Event can be closed by either side.
- The starting points of consecutive Connection Events are spaced by a period of time called the Connection Interval.

#### Connection Parameters
The most important parameters that define a Connection include:

- **Connection Interval**: the interval at which two connected BLE devices wake up the radio and exchange data (at each Connection Event).
- **Slave Latency**: this value allows the Peripheral to skip a number of consecutive Connection Events and not listen to the Central at these Connection Events without compromising the Connection. For example, a Slave Latency of 3 allows a Slave to skip 3 Connection Events and a value of 0 means that the Slave has to send data to the Master at every Connection Event.
- **Supervision Timeout**: the maximum time between two received data packets before the Connection is considered lost.
