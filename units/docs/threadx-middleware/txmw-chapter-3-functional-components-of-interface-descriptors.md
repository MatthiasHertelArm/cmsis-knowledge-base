---
id: "txmw-chapter-3-functional-components-of-interface-descriptors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: USB Device Framework / Interface Descriptors"
summary: "The interface descriptor describes a specific interface within a configuration. An interface is a logical function within a USB device."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#interface-descriptors"
license: "MIT"
mode: "V"
---

_Part of: USB Device Framework_

The interface descriptor describes a specific interface within a configuration. An interface is a logical function within a USB device. A configuration provides one or more interfaces, each with zero or more endpoint descriptors describing a unique set of endpoints within the configuration. When a configuration supports more than one interface, the endpoint descriptors for a particular interface follow the interface descriptor in the data returned by the **GET_DESCRIPTOR** request for the specified configuration.

An interface descriptor is always returned as part of a configuration descriptor. An interface descriptor cannot be directly access by a GET_DESCRIPTOR request.

An interface may include alternate settings that allow the endpoints and/or their characteristics to be varied after the device has been configured. The default setting for an interface is always alternate setting zero. A class can select to change the current alternate setting to change the interface behavior and the characteristics of the associated endpoints. The SET_INTERFACE request is used to select an alternate setting or to return to the default setting.

Alternate settings allow a portion of the device configuration to be varied while other interfaces remain in operation. If a configuration has alternate settings for one or more of its interfaces, a separate interface descriptor and its associated endpoints are included for each setting.

If a device configuration contains a single interface with two alternate settings, the GET_DESCRIPTOR request for the configuration would return the configuration descriptor, then the interface descriptor with the **bInterfaceNumber** and **bAlternateSetting** fields set to zero and then the endpoint descriptors for that setting, followed by another interface descriptor and its associated endpoint descriptors. The second interface descriptor's **bInterfaceNumber** field would also be set to zero, but the **bAlternateSetting** field of the second interface descriptor would be set to 1 indicating that this alternate setting belongs to the first interface.

An interface may not have any endpoints associated with it, in which case only the default control endpoint is valid for that interface.

Alternate settings are used mainly to change the requested bandwidth for periodic endpoints associated with the interface. For example, a USB speaker streaming interface should have the first alternate setting with a 0 bandwidth demand on its isochronous endpoint. Other alternate settings may select different bandwidth requirements depending on the audio streaming frequency.

The USB descriptor for the interface is as follows:

| Offset | Field              | Size | Value     | Descriptor                              |
| ------ | ------------------ | ---- | --------- | --------------------------------------- |
| 0      | bLength            | 1    | Number    | Size of this descriptor in bytes.       |
| 1      | bDescriptorType    | 1    | Constant  | INTERFACE Descriptor Type               |
| 2      | bInterfaceNumber   | 1    | Number    | Number of interface. Zero-based value identifying the index in the array of concurrent interfaces supported by this configuration. |
| 3      | bAlternateSetting   | 1    | Number    | Value used to select alternate setting for the interface identified in the prior field. |
| 4      | bNumEndpoints      | 1    | Number    | Number of endpoints used by this interface (excluding endpoint zero). If this value is 0, this interface only uses endpoint zero. |
| 5      | bInterfaceClass    | 1    | Class     | Class code (assigned by USB)
If this field is reset to 0, the interface does not belong to any USB specified device class.
If this field is set to 0xFF, the interface class is vendor specific.
All other values are reserved for assignment by USB. |
| 6      | bInterfaceSubClass | 1    | SubClass  | Subclass code (assigned by USB).
These codes are qualified by the value of the bInterfaceClass field. If the bInterfaceClass field is reset to 0, this field must also be reset to 0. If the bInterfaceClass field is not set to 0xFF, all values are reserved for assignment by USB. |
| 7      | bInterfaceProtocol | 1    | Protocol  | Protocol code (assigned by USB). These codes are qualified by the value of the bInterfaceClass and the bInterfaceSubClass fields. If an interface supports class-specific requests, this code identifies the protocols that the device uses as defined by the specification of the device class.
If this field is reset to 0, the device does not use a class specific protocol on this interface. If this field is set to 0xFF, the device uses a vendor specific protocol for this interface. |
| 8      | iInterface         | 1    | Index     | Index of string descriptor describing this interface. |

USBX defines a USB interface descriptor as follows.

```c
typedef struct UX_INTERFACE_DESCRIPTOR_STRUCT
{
    UINT bLength;
    UINT bDescriptorType;
    UINT bInterfaceNumber;
    UINT bAlternateSetting;
    UINT bNumEndpoints;
    UINT bInterfaceClass
    UINT bInterfaceSubClass;
    UINT bInterfaceProtocol;
    UINT iInterface;
} UX_INTERFACE_DESCRIPTOR;
```

The USB interface descriptor is part of an interface container described as follows.

```c
typedef struct UX_INTERFACE_STRUCT
{
    ULONG ux_interface_handle;
    ULONG ux_interface_state;
    ULONG ux_interface_current_alternate_setting;
    struct UX_INTERFACE_DESCRIPTOR_STRUCT ux_interface_descriptor;
    struct UX_HOST_CLASS_STRUCT    *ux_interface_class;
    VOID    *ux_interface_class_instance;
    struct UX_ENDPOINT_STRUCT    *ux_interface_first_endpoint;
    struct UX_INTERFACE_STRUCT    *ux_interface_next_interface;
    struct UX_CONFIGURATION_STRUCT    *ux_interface_configuration;
} UX_INTERFACE;
```

- **ux_interface_handle**: Handle of the interface. This is typically the address of the instance of this structure for the interface.
- **ux_interface_state**: State of the interface.
- **ux_interface_descriptor**: USB interface descriptor.
- **ux_interface_class**: Pointer to the class type that owns this interface.
- **ux_interface_class_instance**: Pointer to the instance of the class that owns this interface.
- **ux_interface_first_endpoint**: Pointer to the first endpoint registered with this interface.
- **ux_interface_next_interface**: Pointer to the next interface associated with the configuration.
- **ux_interface_configuration**: Pointer to the configuration owner of this interface.
