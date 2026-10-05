---
id: "txmw-chapter-2-installation-and-use-of-tcp-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / TCP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / TCP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#tcp-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option | Description |
|---|---|
|NX_DISABLE_RESET_DISCONNECT | Defined, disables the reset processing during disconnect when the timeout value supplied is specified as ***NX_NO_WAIT***.|
|NX_DISABLE_TCP_INFO | Defined, disables TCP information gathering.|
|NX_DISABLE_TCP_RX_CHECKSUM | Defined, disables checksum logic on received TCP packets. This is only useful in situations in which the link-layer has reliable checksum or  CRC processing, or the interface driver is able to verify the TCP checksum in hardware, and the application does not use IPsec.|
|NX_DISABLE_TCP_TX_CHECKSUM | Defined, disables checksum logic for sending TCP packets. This is only useful in situations in which the receiving network node has received TCP checksum logic disabled or the underlying network driver is capable of generating the TCP checksum, and the application does not use IPsec.|
|NX_ENABLE_TCP_KEEPALIVE | Defined, enables the optional TCP keepalive timer. The default settings is not enabled.|
|NX_ENABLE_TCP_MSS_CHECK | Defined, enables the verification of minimum peer MSS before accepting a TCP connection. To use this feature, the symbol ***NX_ENABLE_TCP_MSS_MINIMUM*** must be defined. By default, this option is not enabled.|
|NX_ENABLE_TCP_QUEUE_DEPTH_UPDATE_NOTIFY| Defined, allows the application to install a callback function that is invoked when the TCP transmit queue depth is no longer at maximum value. This callback serves as an indication that the TCP socket is ready to transmit more data. By default this option is not enabled.|
|NX_ENABLE_TCP_WINDOW_SCALING | Enables the window scaling option for TCP applications. If defined, window scaling option is negotiated during TCP connection phase, and the application is able to specify a window size larger than 64K. The default setting is not enabled (not defined).|
|NX_MAX_LISTEN_REQUESTS | Specifies the maximum number of server listen requests. The default value is 10 and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_ACK_EVERY_N_PACKETS | Specifies the number of TCP packets to receive before sending an ACK. Note if ***NX_TCP_IMMEDIATE_ACK*** is enabled but ***NX_TCP_ACK_EVERY_N_PACKETS*** is not, this value is automatically set to 1 for backward compatibility.|
|NX_TCP_ACK_TIMER_RATE | Specifies how the number of system ticks (NX_IP_PERIODIC_RATE) is divided to calculate the timer rate for the TCP delayed ACK processing. The default value is 5, which represents 200ms, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_ENABLE_KEEPALIVE | Renamed to ***NX_ENABLE_TCP_KEEPALIVE***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_TCP_KEEPALIVE***.|
|NX_TCP_ENABLE_MSS_CHECK | Renamed to ***NX_ENABLE_TCP_MSS_CHECK***.Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_TCP_MSS_CHECK.***|
|NX_TCP_ENABLE_WINDOW_SCALING | Renamed to ***NX_ENABLE_TCP_WINDOW_SCALING***.Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_TCP_WINDOW_SCALING***.|
|NX_TCP_FAST_TIMER_RATE | Specifies how the number of NetX Duo internal ticks (NX_IP_PERIODIC_RATE) is divided to calculate the fast TCP timer rate. The fast TCP timer is used to drive the various TCP timers, including the delayed ACK timer. The default value is 10, which represents 100ms assuming the ThreadX timer is running at 10ms. This value is defined in ***nx_tcp.h***. The  application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_IMMEDIATE_ACK| Defined, enables the optional TCP immediate ACK response processing. Defining this symbol is equivalent to defining  ***NX_TCP_ACK_EVERY_N_PACKETS*** to be 1.|
|NX_TCP_KEEPALIVE_INITIAL | Specifies the number of seconds of inactivity before the keepalive timer activates. The default value is 7200, which represents 2 hours, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_KEEPALIVE_RETRIES | Specifies how many keepalive retries are allowed before the connection is deemed broken. The default value is 10, which represents 10 retries, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_KEEPALIVE_RETRY | Specifies the number of seconds between retries of the keepalive timer assuming the other side of the connection is not responding. The default value is 75, which represents 75 seconds between retries, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_MAX_OUT_OF_ORDER_PACKETS | Symbol that defines the maximum number of out-of-order TCP packets can be kept in the TCP socket receive queue. This symbol can be used to limit the number of packets queued in the TCP receive socket, preventing the packet pool from being starved. By default this symbol is not defined, thus there is no limit on the number of out of order packets being queued in the TCP socket.|
|NX_TCP_MAXIMUM_RETRIES | Specifies how many data transmit retries are allowed before the connection is deemed broken. The default value is 10, which represents 10 retries, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_MAXIMUM_RX_QUEUE | Symbol that defines the maximum receive queue for TCP sockets. This feature is enabled by ***NX_ENABLE_LOW_WATERMARK***.|
|NX_TCP_MAXIMUM_TX_QUEUE | Specifies the maximum depth of the TCP transmit queue before TCP send requests are suspended or rejected. The default value is 20, which means that a maximum of 20 packets can be in the transmit queue at any given time. Note packets stay in the transmit queue until an ACK that covers some or all of the packet data is received from the other side of the connection. This constant is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_MSS_MINIMUM | Symbol that defines the minimal MSS value NetX Duo TCP module accepts. This feature is enabled by ***NX_ENABLE_TCP_MSS_CHECK***.|
|NX_TCP_QUEUE_DEPTH_UPDATE_NOTIFY_ENABLE | Renamed to ***NX_ENABLE_TCP_QUEUE_DEPTH_UPDATE_NOTIFY***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_TCP_QUEUE_DEPTH_UPDATE_NOTIFY***.|
|NX_TCP_RETRY_SHIFT | Specifies how the retransmit timeout period changes between retries. If this value is 0, the initial retransmit timeout is the same as subsequent retransmit timeouts. If this value is 1, each successive retransmit is twice as long. If this value is 2, each subsequent retransmit timeout is four times as long. The default value is 0 and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_TCP_TRANSMIT_TIMER_RATE | Specifies how the number of system ticks (***NX_IP_PERIODIC_RATE***) is divided to calculate the timer rate for the TCP transmit retry processing. The default value is 1, which represents 1 second, and is defined in ***nx_tcp.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
