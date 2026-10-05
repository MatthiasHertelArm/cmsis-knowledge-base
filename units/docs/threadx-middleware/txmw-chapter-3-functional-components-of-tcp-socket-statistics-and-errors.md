---
id: "txmw-chapter-3-functional-components-of-tcp-socket-statistics-and-errors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Socket Statistics and Errors"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-socket-statistics-and-errors"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

If enabled, the NetX Duo TCP socket software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP/TCP instance:   

- Total TCP Packets Sent  
- Total TCP Bytes Sent  
- Total TCP Packets Received   
- Total TCP Bytes Received   
- Total TCP Invalid Packets   
- Total TCP Receive Packets Dropped    
- Total TCP Receive Checksum Errors   
- Total TCP Connections   
- Total TCP Disconnections   
- Total TCP Connections Dropped    
- Total TCP Packet Retransmits   
- TCP Socket Packets Sent   
- TCP Socket Bytes Sent   
- TCP Socket Packets Received   
- TCP Socket Bytes Received   
- TCP Socket Packet Retransmits    
- TCP Socket Packets Queued    
- TCP Socket Checksum Errors    
- TCP Socket State    
- TCP Socket Transmit Queue Depth    
- TCP Socket Transmit Window Size    
- TCP Socket Receive Window Size    

All these statistics and error reports are available to the application with the ***nx_tcp_info_get*** service for total TCP statistics and the ***nx_tcp_socket_info_get*** service for TCP statistics per socket.
