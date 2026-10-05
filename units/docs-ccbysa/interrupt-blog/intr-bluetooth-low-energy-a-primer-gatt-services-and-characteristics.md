---
id: "intr-bluetooth-low-energy-a-primer-gatt-services-and-characteristics"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: GATT, Services, and Characteristics"
summary: "The main reason to connect two BLE devices to each other is to transfer data between them. Without a Connection, it is not possible to have a bidirectional data transfer between two BLE devices."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#gatt-services-and-characteristics"
license: "CC-BY-SA-4.0"
mode: "V"
---

The main reason to connect two BLE devices to each other is to transfer data between them. Without a Connection, it is not possible to have a bidirectional data transfer between two BLE devices.

Which brings us to the concept of GATT...

The Generic Attribute Profile (GATT) defines the format of the data exposed by a BLE device. It also defines the procedures needed to access the data exposed by a device.

There are two Roles within GATT: Server and Client. The Server is the device that exposes the data it controls or contains, and possibly some other aspects of its behavior that other devices may be able to control. A Client, on the other hand, is the device that interfaces with the Server with the purpose of reading the Server’s exposed data and/or controlling the Server’s behavior.

Keep in mind that a BLE device can act as both a Server and a Client at the same time. Simply put, it acts as the Server for the sake of exposing its own data, and as a Client when accessing another device’s data.

### Services and Characteristics
Services and Characteristics are probably the two most used terms in BLE! That’s why understanding them is crucial, especially for BLE devices that establish a connection with each other.

To better understand GATT, we need to cover a few important concepts (including Services and Characteristics):

- **Attributes**: a generic term for any type of data exposed by the Server and defines the structure of this data. For example, Services and Characteristics (both defined below) are types of Attributes.
- Services: a grouping of one or more Attributes (some of which are Characteristics). It’s meant to group together related Attributes that satisfy a specific functionality on the Server. For example, the SIG-adopted Battery Service contains one Characteristic called the Battery Level.
- **Characteristics**: a Characteristic is always part of a Service and it represents a piece of information/data that a Server wants to expose to a client. For example, the Battery Level Characteristic represents the remaining power level of a battery in a device which can be read by a Client.
- **Profiles**: Profiles are much broader in definition from Services. They are concerned with defining the behavior of both the Client and Server when it comes to Services, Characteristics and even Connections and security requirements. Services and their specifications, on the other hand, deal with the implementation of these Services and Characteristics on the Server side only.

A simplified representation of a Service:

```
Service——|
    |—Characteristic 1
    |—Characteristic 2
     ...
    |—Characteristic N
```

In BLE, there are six types of operations on Characteristics:

1. **Commands**: sent by the Client to the Server and do not require a Response (defined below). One example of a Command is a Write Command, which does not require a Response from the Server.
2. **Requests**: sent by the Client to the Server and require a Response. Some examples of Requests include: Read Requests and Write Requests.
3. **Responses**: sent by the Server in response to a Request.
4. **Notifications**: sent by the Server to the Client to let the Client know that a specific Characteristic Value has changed. In order for this to be triggered and sent by the Server, the Client has to enable Notifications for the Characteristic of interest. Note that a Notification does not require a Response from the Client to acknowledge its receipt.
5. **Indications**: sent by the Server to the Client. They are very similar to Notifications but require an acknowledgment to be sent back from the Client to let the Server know that the Indication was successfully received.

	**Note:** Notifications and Indications are exposed via the Client Characteristic Configuration Descriptor (CCCD) Attribute. Writing a “1” to this Attribute value enables Notifications, whereas writing a “2” enables Indications. Writing a “0” disables both Notifications and Indications.

- **Confirmations**: sent by the Client to the Server. These are the acknowledgment packets sent back to the Server to let it know that the Client received an Indication successfully.

Now that we've gone through the basics of BLE, we can take that knowledge and apply it to practice. In the next section, we will implement a simple BLE Peripheral running on the nRF52840 development kit.
