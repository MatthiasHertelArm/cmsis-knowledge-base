---
id: "drv-usbh-packet-information"
type: "concept"
domain: "drivers"
title: "USBH Packet Information"
summary: "Specify USB packet information used by the function ARMUSBHPipeTransfer"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

Specify USB packet information used by the function ARM_USBH_PipeTransfer
 
This section provides the packet information values (parameter **packet)** for the ARM_USBH_PipeTransfer function.

The following values are defined:

### ARM_USBH_PACKET_SETUP

```c
ARM_USBH_PACKET_SETUP
```

Generate SETUP transaction.

### ARM_USBH_PACKET_OUT

```c
ARM_USBH_PACKET_OUT
```

Generate OUT transaction.

### ARM_USBH_PACKET_IN

```c
ARM_USBH_PACKET_IN
```

Generate IN transaction.

### ARM_USBH_PACKET_PING

```c
ARM_USBH_PACKET_PING
```

Generate PING transaction (no data packet).

### ARM_USBH_PACKET_DATA0

```c
ARM_USBH_PACKET_DATA0
```

Force DATA0 PID (Packet Identifier) for the initial data packet. When not specified than the driver provides the initial value according to the current state.

### ARM_USBH_PACKET_DATA1

```c
ARM_USBH_PACKET_DATA1
```

Force DATA1 PID (Packet Identifier) for the initial data packet. When not specified than the driver provides the initial value according to the current state.

### ARM_USBH_PACKET_SSPLIT

```c
ARM_USBH_PACKET_SSPLIT
```

Used when driver does not support automatic handling of SPLIT packets and indicates Start-Split packet.
For isochronous OUT it indicates that the High-speed data is in the middle of the Full-speed data payload.

### ARM_USBH_PACKET_SSPLIT_S

```c
ARM_USBH_PACKET_SSPLIT_S
```

Used when driver does not support automatic handling of SPLIT packets and indicates Start-Split packet.
Valid only for isochronous OUT and indicates that the High-speed data is the start of the Full-speed data payload.

### ARM_USBH_PACKET_SSPLIT_E

```c
ARM_USBH_PACKET_SSPLIT_E
```

Used when driver does not support automatic handling of SPLIT packets and indicates Start-Split packet.
Valid only for isochronous OUT and indicates that the High-speed data is the end of the Full-speed data payload.

### ARM_USBH_PACKET_SSPLIT_S_E

```c
ARM_USBH_PACKET_SSPLIT_S_E
```

Used when driver does not support automatic handling of SPLIT packets and indicates Start-Split packet.
Valid only for isochronous OUT and indicates that the High-speed data is all of the Full-speed data payload.

### ARM_USBH_PACKET_CSPLIT

```c
ARM_USBH_PACKET_CSPLIT
```

Used when driver does not support automatic handling of SPLIT packets and indicates Complete-Split packet.

### ARM_USBH_PACKET_PRE

```c
ARM_USBH_PACKET_PRE
```

Generate PRE (Preamble) for low-speed devices within a full/low-speed signaling environment.
