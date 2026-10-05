---
id: "dv-socket-testing"
type: "concept"
domain: "drivers"
title: "Socket testing"
summary: "Due to limitations of WiFi modules and their Software Development Kits (SDK), often it is not possible to comply with CMSIS-Driver BSD rules regarding function behavior or function return codes."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_WiFi.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/wifi_sock_testing.html"
license: "Apache-2.0"
mode: "V"
---

Due to limitations of WiFi modules and their Software Development Kits (SDK), often it is not possible to comply with
CMSIS-Driver BSD rules regarding function behavior or function return codes. Hence, the WiFi Driver tests accept alternative
error codes and report them as Warnings and considers certain error codes as acceptable for certain functions.
Exceptions to BSD-strict error codes and functionality are written below: 

WiFi socket deviations from the BSD-strict specification
========================================================

-# **SocketBind**
 - bind socket to same address again

   **BSD-strict** expected return code **ARM_SOCKET_EINVAL
non** BSD-strict accepted return codes: `0` or `ARM_SOCKET_ERROR`

 - bind another socket to used address

   **BSD-strict** expected return code **ARM_SOCKET_EADDRINUSE
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - bind on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketListen**
 - listen on already listening socket

   **BSD-strict** expected return code **ARM_SOCKET_EINVAL
non** BSD-strict accepted return codes: `0` or `ARM_SOCKET_ERROR`

 - listen on unbound socket

   **BSD-strict** expected return code **ARM_SOCKET_EINVAL
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - listen on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - listen on datagram socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTSUP
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketAccept**
 - receive on disconnected socket

   **BSD-strict** expected return code **ARM_SOCKET_ECONNRESET
non** BSD-strict accepted return codes: `ARM_SOCKET_EAGAIN` or `ARM_SOCKET_ERROR`

 - accept on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - listen on datagram socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTSUP
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - accept on datagram socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTSUP
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketConnect**
 - connect socket to same address again

   **BSD-strict** expected return code **ARM_SOCKET_EISCONN
non** BSD-strict accepted return codes: `0` or `ARM_SOCKET_ERROR`

 - bind on connected socket

   **BSD-strict** expected return code **ARM_SOCKET_EISCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - connect on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - connect to non-existent port

   **BSD-strict** expected return code **ARM_SOCKET_ECONNREFUSED
non** BSD-strict accepted return codes: `ARM_SOCKET_ETIMEDOUT` or `ARM_SOCKET_ERROR`

 - connect to non-existent stream server

   **BSD-strict** expected return code **ARM_SOCKET_ETIMEDOUT
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - connect on listening socket

   **BSD-strict** expected return code **ARM_SOCKET_EINVAL
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - connect datagram socket to unspecified address (0.0.0.0)

   **BSD-strict** expected return code **0
non** BSD-strict accepted return codes: `ARM_SOCKET_EINVAL` or `ARM_SOCKET_ERROR`
   (special case that deletes the socket destination & filtering address)

-# **SocketRecv**
 - recv on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - recv on created socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - recv on bound socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - recv on listening socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketRecvFrom**
 - recvfrom on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketSend**
 - send on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - send on disconnected socket

   **BSD-strict** expected return code **ARM_SOCKET_ECONNRESET
non** BSD-strict accepted return codes: >`0` or `ARM_SOCKET_EAGAIN` or `ARM_SOCKET_ERROR`

 - send on created socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - send on bound socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - send on listening socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - send on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketSendTo**
 - sendto on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketGetSockName**
 - getsockname on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - getsockname on unbound socket

   **BSD-strict** expected return code **ARM_SOCKET_EINVAL
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketGetPeerName**
 - getpeername on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - getpeername on created socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - getpeername on bound socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

 - getpeername on listening socket

   **BSD-strict** expected return code **ARM_SOCKET_ENOTCONN
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketGetOpt**
 - getsockopt on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketSetOpt**
 - setsockopt on closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`

-# **SocketClose**
 - close already closed socket

   **BSD-strict** expected return code **ARM_SOCKET_ESOCK
non** BSD-strict accepted return code `0`

-# **SocketGetHostByName**
 - gethostbyname for non-existing host

   **BSD-strict** expected return code **ARM_SOCKET_EHOSTNOTFOUND
non** BSD-strict accepted return code `ARM_SOCKET_ERROR`
