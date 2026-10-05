---
id: "txmw-chapter-3-functional-components-of-tsn-components"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: TSN Components"
summary: "Time-Sensitive Networking (TSN) is a suite of standards crafted by the IEEE 802.1 working group aimed at augmenting the capabilities of Ethernet networks. These standards define mechanisms for transmitting time-sensitive data over deterministic Ethernet networks."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tsn-components"
license: "MIT"
mode: "V"
---

Time-Sensitive Networking (TSN) is a suite of standards crafted by the IEEE 802.1 working group aimed at augmenting the capabilities of Ethernet networks. These standards define mechanisms for transmitting time-sensitive data over deterministic Ethernet networks.

In this section, the TSN compents in below frame work in colour blue are described.

(figure: Diagram of TSN Framework)

**FIGURE 15. TSN Framework**

### Link layer
In NetxDuo, the Link Layer component offers a range of essential functionalities, These include:

VLAN Interface Creation: NetxDuo allows for the seamless creation of Virtual Local Area Network (VLAN) interfaces, enabling the segmentation of network traffic into distinct logical networks.

VLAN ID Modification: It provides the capability to modify VLAN IDs on specific VLAN interface, facilitating the customization and management of VLAN configurations to suit specific network requirements.

Raw Packet Transmission: NetxDuo provides a Raw Packet transmission interface for direct transmission of network packets at the Link Layer. This is particularly useful for specialized network communication needs, such as the direct sending of packets by MRP and ptp components using raw packet transmission.

Packet Distribution for Received Packets: The Link Layer in NetxDuo efficiently handles the reception of network packets, distributing them appropriately based on packet types. This includes the distribution of VLAN-tagged packets to the corresponding VLAN interfaces and the distribution of untagged packets to the default interface.

Above functionalities are used by TSN components to implement TSN features.

### Credit-based shaper (CBS) - IEEE 802.1Qav Forwarding and Queuing Enhancements for Time-Sensitive Stream
Credit-based shaper (CBS) is a traffic shaping mechanism that is in audio video bridge(AVB) network, to ensure/control the bandwidth of specific audio and video traffic streams. this mechanism can ensure that the data is transmitted at a constant rate and to avoid congestion in the network.

In CBS module of NetxDuo, following functionalities are provided:
- CBS shaper creation and deletion.
- The Mapping configuration of PCP on VLAN tag to related hardware queue.
- CBS parameters Setting, such as idle slope, send slope, and CBS credit limit.

By utilizing these functionalities, we can assign different SR class traffic to specific hardware queues and control the bandwidth of the traffic by setting the CBS parameters on related hardware queues.

### Time-Aware Shaper (TAS) - IEEE 802.1Qbv Enhancements to Traffic Scheduling
TAS (Time-Aware Scheduler) in TSN (Time-Sensitive Networking) is designed to ensures deterministic and prioritized communication by controlling the bandwidth allocation for high-priority streams through gate control and regulating cycles.

The IEEE 802.1Qbv time-aware scheduler orchestrates Ethernet network communication by dividing it into fixed-length, repeating time cycles. Within these cycles, customizable time slices are allocated to one or multiple of the eight Ethernet priorities. This approach enables exclusive utilization of the Ethernet transmission medium for time-sensitive traffic classes, ensuring uninterrupted transmission guarantees when needed. Operating on a time-division multiple access (TDMA) scheme, the scheduler establishes virtual communication channels for specific time periods, effectively segregating time-critical communication from non-critical background traffic.

In TAS module of NetxDuo, following functionalities are provided:
- TAS shaper creation and deletion. (Shared with CBS and FPE)
- The Mapping configuration of PCP on VLAN tag to related hardware queue.(Shared with CBS)
- TAS parameters setting. Include base time, cycle time, time slot and associated gate control settings.

By leveraging these functionalities, high-priority traffic can be directed to specific hardware queues with allocated time slots, enabling precise bandwidth control. Furthermore, through synchronized TAS settings across the entire TSN infrastructure and time synchronization facilitated by gPTP (generalized Precision Time Protocol), we can effectively manage end-to-end latency for traffic, ensuring timely and reliable communication.

### Frame preemption (FPE) - 802.1Qbu
Frame Preemption (FPE) is a TSN feature that allows high-priority frames to interrupt the transmission of lower-priority frames. This feature is particularly useful in time-sensitive applications, where the timely delivery of high-priority frames is critical. By preempting the transmission of lower-priority frames, high-priority frames can be transmitted without delay, ensuring that they are delivered within the required time frame.

In FPE module of NetxDuo, following functionalities are provided:
- FPE shaper creation and deletion. (Shared with CBS and TAS)
- FPE parameters setting. such as enable/disable the FPE verification, express queue bitmap setting, ha/ra time setting, express queue guard band enable/disable.

FPE (Frame Preemption Engine) is typically utilized in conjunction with TAS (Time-Aware Scheduler). By fragmenting preemptable frames, the guard band required for preemptable frame slots is reduced, thus increasing bandwidth utilization efficiency.

### Time synchronization(gPTP)
The gPTP (Generalized Precision Time Protocol), as described in the IEEE 1588 Precision Time Protocol standard, is utilized within Time-Sensitive Networks (TSN) to synchronize time across network devices.

In gPTP module of NetxDuo, following functionalities are provided:
- Creation and deletion of PTP client.
- Starting and stopping the PTP client.
- Retrieving and setting the PTP clock in the client.
- Acquiring master clock information and sync message details through the PTP client.
- Transmission of timestamp notifications for PTP packets.
- Implementation of a software-based PTP clock.
- Utility of computing the difference between two PTP times. 
- Utility of converting a PTP time to a UTC date and time. 

### Stream Registration Protocol (SRP)
SRP (Stream Reservation Protocol) is a protocol used in Time-Sensitive Networking (TSN). It allows devices to reserve resources for specific streams of data across the network. This ensures that these streams have the necessary bandwidth and can meet their time sensitivity requirements. 

In SRP module of NetxDuo, following functionalities are provided:
- Initialization of SRP service.
- Starting and stopping the SRP talker service.
- Starting and stopping the SRP listener service.

### Multiple Stream Reservation Protocol (MSRP)
MSRP (Multiple Stream Reservation Protocol) in Time-Sensitive Networking (TSN) is an extension of the Stream Reservation Protocol (SRP). By allowing multiple stream reservations, MSRP enhances the deterministic data delivery capabilities of TSN, ensuring that data can be delivered with a guaranteed level of performance across multiple streams.

In MSRP module of NetxDuo, following functionalities are provided:
- Initialization of an MSRP instance.
- Parsing and packing of MRP Data Units (MRPDUs).
- Management of the registration and deregistration processes for a stream.
- Management of the registration and deregistration processes for an attachment to a stream.
- Handling of indications for a stream's registration and deregistration events.
- Handling of indications for an attachment's registration and deregistration events.
- Management of the registration and deregistration processes for a domain, as well as handling the indications of these events.

### Multiple vlan registration protocol (MVRP)
The Multiple VLAN Registration Protocol (MVRP) is a protocol that provides dynamic VLAN registration service. It is an MRP (Multiple Registration Protocol) application that makes use of MRP Attribute Declaration (MAD) and MRP Attribute Propagation (MAP) to provide common state machine descriptions and attribute propagation mechanisms. 
MVRP provides a mechanism for dynamic maintenance of the contents of Dynamic VLAN Registration Entries for each VLAN and propagates the information they contain to other Bridges. This information allows MVRP-aware devices to dynamically establish and update their knowledge of the set of VLANs that currently have active members, and through which Ports those members can be reached. 
In MVRP module of NetxDuo, following functionalities are provided to SRP/MRP components:
- Initialization of an MVRP instance.
- Parsing and packing of MRP Data Units (MRPDUs).
- Process the join or leave a VLAN request command from SRP, and trigger the corresponding VLAN registration or deregistration process.
- Handling of indications for a stream's registration and deregistration events from MRP.

### Multiple registration protocol (MRP)
The Multiple Registration Protocol (MRP) is a protocol that provides dynamic registration and deregistration of attributes in a network. It is used to manage resources in a network, such as VLANs, multicast addresses, and streams. MRP operates uses a common state machine and attribute propagation mechanisms to provide a consistent view of the network resources. MRP is used by other protocols, such as MVRP (Multiple VLAN Registration Protocol) and MSRP (Multiple Stream Registration Protocol), to provide dynamic registration of VLANs and streams, respectively.

In MRP module of NetxDuo, following functionalities are provided to MRP applications:
- Provide the interface of MRP initialization.
- Maintaining state machine for MRP applications.
- Process the event triggered by receiving different MRP messages.
- Receiving the message from ethernet, and distribute the MRP messages to the corresponding MRP applications.
- Handle the timer event for MRP applications.
