---
id: "txmw-chapter-3-functional-components-of-endpoint-descriptors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: USB Device Framework / Endpoint Descriptors"
summary: "Each endpoint associated with an interface has its own endpoint descriptor."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#endpoint-descriptors"
license: "MIT"
mode: "V"
---

_Part of: USB Device Framework_

Each endpoint associated with an interface has its own endpoint descriptor. This descriptor contains the information required by the host stack to determine the bandwidth requirements of each endpoint, the maximum payload associated with the endpoint, its periodicity, and its direction. An endpoint descriptor is always returned by a GET_DESCRIPTOR command for the configuration.

The default control endpoint associated with the device descriptor is not counted as part of the endpoint(s) associated with the interface and therefore not returned in this descriptor.

When the host software requests a change of the alternate setting for an interface, all the associated endpoints and their USB resources are modified according to the new alternate setting.

Except for the default control endpoints, endpoints cannot be share between interfaces.

| Offset | Field            | Size | Value    | Description                       |
| ------ | ---------------- | ---- | -------- | --------------------------------- |
| 0      | bLength          | 1    | Number   | Size of this descriptor in bytes. |
| 1      | bDescriptorType  | 1    | Constant | ENDPOINT Descriptor Type. |
| 2      | bEndpointAddress | 1    | Endpoint | The address of the endpoint on the USB device described by this descriptor. The address is encoded as follows:
Bit 3...0: The endpoint number
Bit 6...4: Reserved, reset to zero
Bit 7: Direction, ignored for control endpoints
0 = OUT endpoint
1 = IN endpoint |
| 3      | bmAttributes     | 1    | Bitmap   | This field describes the endpoint's attributes when it is configured using the **bConfigurationValue** field. Bits 1..0: Transfer Type
00 = Control
01 = Isochronous
10 = Bulk
11 = Interrupt
If not an isochronous endpoint, bits 5..2 are reserved and must be set to zero. If isochronous, they are defined as follows:
Bits 3..2: Synchronization Type
00 = No Synchronization
01 = Asynchronous
10 = Adaptive
11 = Synchronous
Bits 5..4: Usage Type
00 = Data endpoint
01 = Feedback endpoint
10 = Implicit feedback data endpoint
11 = Reserved |
| 4      | wMaxPacketSize   | 2    | Number   | Maximum packet size this endpoint is capable of sending or receiving when this configuration is selected.
For isochronous endpoints, this value is used to reserve the bus time in the schedule, required for the per-(micro)frame data payloads. The pipe may, on an ongoing basis, actually use less bandwidth than that reserved. The device reports, if necessary, the actual bandwidth used via its normal, non-USB defined mechanisms.
For all endpoints, bits 10..0 specify the maximum packet size (in bytes).
For high-speed isochronous and interrupt endpoints:
Bits 12..11 specify the number of additional transaction opportunities per microframe: 00 = None (1 transaction per microframe)
01 = 1 additional (2 per microframe)
10 = 2 additional (3 per microframe)
11 = Reserved
Bits 15..13 are reserved and must be set to zero. |
| 6      | bInterval        | 1     | Number   | Number interval for polling endpoint for data transfers.
Expressed in frames or microframes depending on the device operating speed (i.e., either 1 millisecond or 125 µs units).
For full-/high-speed isochronous endpoints, this value must be in the range from 1 to 16. The **bInterval** is used as the exponent for a 2bInterval-1 value; e.g., a **bInterval** 4 means a period of 8 (24-1).
For full-/low-speed interrupt endpoints, the value of this field may be from 1 to 255.
For high-speed interrupt endpoints, the **bInterval** is used as the exponent for a 2bInterval-1 value; e.g., a **bInterval** 4 means a period of 8 (24-1). This value must be from 1 to 16.
For high-speed bulk/control OUT endpoints, the **bInterval** specify the maximum NAK rate of the endpoint. A value of 0 indicates the endpoint never NAKs. Other values indicate at most one NAK each **bInterval** of microframes.
This value must be in the range from 0 to 255. |

USBX defines a USB endpoint descriptor as follows:

```c
typedef struct UX_ENDPOINT_DESCRIPTOR_STRUCT
{
    UINT bLength;
    UINT bDescriptorType;
    UINT bEndpointAddress;
    UINT bmAttributes;
    USHORT wMaxPacketSize;
    UINT bInterval;
} UX_ENDPOINT_DESCRIPTOR;
```

The USB endpoint descriptor is part of an endpoint container, which is described as follows.

```c
typedef struct UX_ENDPOINT_STRUCT {
    ULONG    ux_endpoint_handle;
    ULONG    ux_endpoint_state;
    VOID    *ux_endpoint_ed;
    struct UX_ENDPOINT_DESCRIPTOR_STRUCT    ux_endpoint_descriptor;
    struct UX_ENDPOINT_STRUCT    *ux_endpoint_next_endpoint;
    struct UX_INTERFACE_STRUCT    *ux_endpoint_interface;
    struct UX_DEVICE_STRUCT    *ux_endpoint_device;
    struct UX_TRANSFER REQUEST_STRUCT    ux_endpoint_transfer request;
} UX_ENDPOINT;

```

- **ux_endpoint_handle**: Handle of the endpoint. This is typically the address of the instance of this structure for the endpoint.
- **ux_endpoint_state**: State of the endpoint.
- **ux_endpoint_ed**: Pointer to the physical endpoint at the host controller layer.
- **ux_endpoint_descriptor**: USB endpoint descriptor.
- **ux_endpoint_next_endpoint**: Pointer to the next endpoint that belongs to the same interface.
- **ux_endpoint_interface**: Pointer to the interface that owns this endpoint interface.
- **ux_endpoint_device**: Pointer to the parent device container.
- **ux_endpoint_transfer request**: USB transfer request used to send/receive data from to/from the device.
