---
id: "txmw-chapter-5-netx-duo-network-drivers-example-ram-ethernet-network-driver"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Example RAM Ethernet Network Driver"
summary: "The NetX Duo demonstration system is delivered with a small RAM-based network driver, defined in the file nx_ram_network_driver.c."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#example-ram-ethernet-network-driver"
license: "MIT"
mode: "V"
---

The NetX Duo demonstration system is delivered with a small RAM-based network driver, defined in the file ***nx_ram_network_driver.c.*** This driver assumes the IP instances are all on the same network and simply assigns virtual hardware addresses (MAC addresses) to each device instance as they are created. This file provides a good example of the basic structure of NetX Duo physical network drivers. Users may develop their own network drivers using the driver framework presented in this example.

The entry function of the network driver is ***_nx_ram_network_driver(),*** which is passed to the IP instance create call. Entry functions for additional network interfaces can be passed into the *nx_ip_interface_attach()* service. After the IP instance starts to run, the driver entry function is invoked to initialize and enable the device (refer to the case **NX_LINK_INITIALIZE** and **NX_LINK_ENABLE**). After the **NX_LINK_ENABLE** command is issued, the device should be ready to transmit and receive packets. 

The IP instance transmits network packets via one of these commands:

| Command                         |  Description                                                   |
| ------------------------------- | -------------------------------------------------------------- |
| ***NX_LINK_PACKET_SEND***    | An IPv4 or IPv6 packet is being transmitted,                   |
| ***NX_LINK_ARP_SEND***       | An ARP request or ARP response packet is being transmitted,    |
| ***NX_LINK_ARP_RARP_SEND*** | A Reverse ARP request or response packet is being transmitted, |

On processing these commands, the network driver needs to prepend the appropriate Ethernet frame header, and then send it to the underlying hardware for transmission. During the transmission process, the network driver has the exclusive ownership of the packet buffer area. Therefore once the data is being transmitted (or once the data has been copied into the driver internal transfer buffer), the network driver is responsible for releasing the packet buffer by first moving the prepend pointer past the Ethernet header to the IP header (and adjust packet length accordingly), and then by calling the ***nx_packet_transmit_release()*** service to release the packet. Not releasing the packet after data transmission will cause packets to leak.

The network device driver is also responsible for handling incoming data packets. In the RAM driver example, the received packet is processed by the function ***_nx_ram_network_driver_receive()***. Once the device receives an Ethernet frame, the driver is responsible for storing the data in  NX_PACKET structure. Note that NetX Duo assumes the IP header starts from 4-byte aligned address. Since the length of Ethernet header is 14byte, the driver needs to store the starting of the Ethernet header at 2-byte aligned address to guarantee that the IP header starts at 4-byte aligned address.
