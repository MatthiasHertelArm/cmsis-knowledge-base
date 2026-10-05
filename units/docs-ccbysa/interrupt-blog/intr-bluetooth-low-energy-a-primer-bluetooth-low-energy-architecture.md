---
id: "intr-bluetooth-low-energy-a-primer-bluetooth-low-energy-architecture"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Bluetooth Low Energy Architecture"
summary: "Here’s a diagram showing the different levels of the architecture of BLE:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#bluetooth-low-energy-architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

Here’s a diagram showing the different levels of the architecture of BLE:



The good thing is that, as a developer looking to develop BLE applications, you won’t have to worry much about the layers below the Security Manager and Attribute Protocol. But lets at least cover the definitions of these layers:

- The **Physical Layer (PHY)** refers to the physical radio used for communication and for modulating/demodulating the data. It operates in the ISM band (2.4 GHz spectrum).

- The **Link Layer** is the layer that interfaces with the Physical Layer (Radio) and provides the higher levels an abstraction and a way to interact with the radio (through an intermediary level called the HCI layer which we’ll discuss shortly). It is responsible for managing the state of the radio as well as the timing requirements for adhering to the Bluetooth Low Energy specification.

- **Direct Test Mode**: the purpose of this mode is to test the operation of the radio at the physical level (such as transmission power, receiver sensitivity, etc.).

- The **Host Controller Interface (HCI)** layer is a standard protocol defined by the Bluetooth specification that allows the Host layer to communicate with the Controller layer. These layers could exist on separate chips, or they could exist on the same chip.

- The **Logical Link Control and Adaptation Protocol (L2CAP)** layer acts as a protocol multiplexing layer. It takes multiple protocols from the upper layers and places them in standard BLE packets that are passed down to the lower layers beneath it.

- The **Security Manager** defines the protocols and algorithms for generating and exchanging keys between two devices. It involves five security features: pairing, bonding, authentication, encryption, and message integrity.

- The **Attribute Protocol (ATT)** defines how a server exposes its data to a client and how this data is structured. There are two roles within the ATT:
	
	- **Server**: the device that exposes the data it controls or contains, and possibly some other aspects of server behavior that other devices may be able to control.
	- **Client**: the device that interfaces with the server with the purpose of reading the server’s exposed data and/or controlling the server’s behavior.
