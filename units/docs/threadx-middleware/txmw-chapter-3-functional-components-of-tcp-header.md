---
id: "txmw-chapter-3-functional-components-of-tcp-header"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Header"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-header"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

On transmission, TCP header is placed in front of the data from the user. On reception, TCP header is removed from the incoming packet, leaving only the user data available to the application. TCP utilizes the IP protocol to send and receive packets, which means there is an IP header in front of the TCP header when the packet is on the network. Figure 13 shows the format of the TCP header.

(figure: Diagram of the TCP header format.)

**FIGURE 13. TCP Header**

The following describes the TCP header format:

|Header Field |Purpose |
|------|------|
| **16-bit source port number** | This field contains the port the TCP packet is being sent out on. Valid TCP ports range from 1 through 0xFFFF. |
| **16-bit destination port** | This field contains the TCP port the packet is being sent to. Valid TCP ports range from 1 through 0xFFFF. |
| **32-bit sequence number** | This field contains the sequence number for data sent from this end of the connection. The original sequence is established during the initial connection sequence between two TCP nodes. Every data transfer from that point results in an increment of the sequence number by the amount bytes sent. |
| **32-bit acknowledgement number** | This field contains the sequence number corresponding to the last byte received by this side of the connection. This is used to determine whether or not data previously sent has successfully been received by the other end of the connection. |
| **4-bit header length** | This field contains the number of 32-bit words in the TCP header. If no options are present in the TCP header, this field is 5. |
| **6-bit code bits** |This field contains the six different code bits used to indicate various control information associated with the connection. The control bits are defined as follows:`<br \>` - URG (21): Urgent data present<br \> - ACK (20): Acknowledgement number is valid<br \> - PSH (19): Handle this data immediately<br \> - RST (18): Reset the connection<br \> - SYN (17): Synchronize sequence numbers (used to establish connection)`<br \>` - FIN (16): Sender is finished with transmit (used to close connection) |
|**16-bit window** |This field is used for flow control. It contains the amount of bytes the socket can currently receive. This basically is used for flow control. The sender is responsible for making sure the data to send will fit into the receiver's advertised window. |
|**16-bit TCP checksum** |This field contains the 16-bit checksum for the packet including the TCP header, the packet data area, and the pseudo IP header. |
|**16-bit urgent pointer** |This field contains the positive offset of the last byte of the urgent data. This field is only valid if the URG code bit is set in the header. |

> **Note:** *All headers in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address*.
