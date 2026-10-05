---
id: "txmw-chapter-3-functional-components-of-device-descriptors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: USB Device Framework / Device Descriptors"
summary: "Each USB device has one single device descriptor. This descriptor contains the device identification, the number of configurations supported, and the characteristics of the default control endpoint used for configuring the device."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#device-descriptors"
license: "MIT"
mode: "V"
---

_Part of: USB Device Framework_

Each USB device has one single device descriptor. This descriptor contains the device identification, the number of configurations supported, and the characteristics of the default control endpoint used for configuring the device.

| Offset | Field              | Size | Value    | Description                             |
| ------ | ------------------ | ---- | -------- | --------------------------------------- |
| 0      | BLength            | 1    | Number   | Size of this descriptor in bytes |
| 1      | bDescriptorType    | 1    | Constant | DEVICE Descriptor Type |
| 2      | bcdUSB             | 2    | BCD      | USB Specification Release Number in BinaryCoded Dec
Example: 2.10 is equivalent to 0x210. This field identifies the release of the USB Specification that the device and its descriptors are compliant with. |
| 4      | bDeviceClass       | 1    | Class    | Class code (assigned by USB-IF).
If this field is reset to 0, each interface within a configuration specifies its own class information and the various interfaces operate independently.
If this field is set to a value between 1 and 0xFE, the device supports different class specifications on different interfaces and the interfaces may not operate independently. This value identifies the class definition used for the aggregate interfaces.
If this field is set to 0xFF, the device class is vendor specific. |
| 5      | bDeviceSubClass    | 1    | SubClass | Subclass code (assigned by USB-IF).
These codes are qualified by the value of the bDeviceClass field. If the bDeviceClass field is reset to 0, this field must also be reset to 0. If the bDeviceClass field is not set to 0xFF, all values are reserved for assignment by USB. |
| 6      | bDeviceProtocol    | 1    | Protocol | Protocol code (assigned by USB-IF).
These codes are qualified by the value of the bDeviceClass and the bDeviceSubClass fields. If a device supports class-specific protocols on a device basis as opposed to an interface basis, this code identifies the protocols that the device uses as defined by the specification of the device class. If this field is reset to 0, the device does not use class specific protocols on a device basis.
However, it may use class specific protocols on an interface basis.
If this field is set to 0xFF, the device uses a vendor specific protocol on a device basis. |
| 7      | bMaxPacketSize0    | 1    | Number   | Maximum packet size for endpoint zero (only byte sizes of 8, 16, 32, or 64 are valid) |
| 8      | idVendor           | 2    | ID       | Vendor ID (assigned by USB-IF) |
| 10     | idProduct          | 2    | ID       | Product ID (assigned by the Manufacturer) |
| 12     | bcdDevice          | 2    | BCD      | Device release number in binary-coded decimal |
| 14     | iManufacturer      | 1    | Index    | Index of string descriptor describing manufacturer |
| 15     | iProduct           | 1    | Index    | Index of string descriptor describing product |
| 16     | iSerialNumber       | 1    | Index    | Index of string descriptor describing the device's serial number |
| 17     | bNumConfigurations | 1    | Number   | Number of possible configurations |

USBX defines a USB device descriptor as follows:

```c
typedef struct UX_DEVICE_DESCRIPTOR_STRUCT
{
    UINT      bLength;
    UINT      bDescriptorType;
    USHORT    bcdUSB;
    UINT      bDeviceClass;
    UINT      bDeviceSubClass;
    UINT      bDeviceProtocol;
    UINT      bMaxPacketSize0;
    USHORT    idVendor;
    USHORT    idProduct;
    USHORT    bcdDevice;
    UINT      iManufacturer;
    UINT      iProduct;
    UINT      iSerialNumber;
    UINT      bNumConfigurations;
} UX_DEVICE_DESCRIPTOR;
```

The USB device descriptor is part of a device container described as:

```c
typedef struct UX_DEVICE_STRUCT
{
    ULONG ux_device_handle;
    ULONG ux_device_type;
    ULONG ux_device_state;
    ULONG ux_device_address;
    ULONG ux_device_speed;
    ULONG ux_device_port_location;
    ULONG ux_device_max_power;
    ULONG ux_device_power_source;
    UINT ux_device_current_configuration;

    TX_SEMAPHORE ux_device_protection_semaphore;
    struct UX_DEVICE_STRUCT *ux_device_parent; 
    struct UX_HOST_CLASS_STRUCT *ux_device_class; 
    VOID *ux_device_class_instance;
    struct UX_HCD_STRUCT *ux_device_hcd;
    struct UX_CONFIGURATION_STRUCT *ux_device_first_configuration; 
    struct UX_DEVICE_STRUCT *ux_device_next_device;
    struct UX_DEVICE_DESCRIPTOR_STRUCT ux_device_descriptor;
    struct UX_ENDPOINT_STRUCT ux_device_control_endpoint;
    struct UX_HUB_TT_STRUCT ux_device_hub_tt[UX_MAX_TT];
} UX_DEVICE;
```

- **ux_device_handle**: Handle of the device. This is typically the address of the instance of this structure for the device.
- **ux_device_type**: Obsolete value. Unused.
- **ux_device_state**: Device State, which can have one of the following values:
    - **UX_DEVICE_RESET**                0
    - **UX_DEVICE_ATTACHED**             1
    - **UX_DEVICE_ADDRESSED**            2
    - **UX_DEVICE_CONFIGURED**           3
    - **UX_DEVICE_SUSPENDED**            4
    - **UX_DEVICE_RESUMED**              5
    - **UX_DEVICE_SELF_POWERED_STATE**   6
    - **UX_DEVICE_SELF_POWERED_STATE**   7
    - **UX_DEVICE_REMOTE_WAKEUP**        8
    - **UX_DEVICE_BUS_RESET_COMPLETED**  9
    - **UX_DEVICE_REMOVED**              10
    - **UX_DEVICE_FORCE_DISCONNECT**     11
- **ux_device_address**: Address of the device after the **SET_ADDRESS** command has been accepted (from 1 to 127).
- **ux_device_speed**: Speed of the device:
    - **UX_LOW_SPEED_DEVICE**      0
    - **UX_FULL_SPEED_DEVICE**     1
    - **UX_HIGH_SPEED_DEVICE**     2
- **ux_device_port_location**: Index of the port of the parent device (root hub or hub).
- **ux_device_max_power**: Maximum power in mA that the device may take in the selected configuration.
- **ux_device_power_source**: Can be one of the two following values:
    - **UX_DEVICE_BUS_POWERED**     1
    - **UX_DEVICE_SELF_POWERED**    2
- **ux_device_current_configuration**: Index of the current configuration being used by this device.
- **ux_device_parent**: Device container pointer of the parent of this device. If the pointer is null, the parent is the root hub of the controller.
- **ux_device_class**: Pointer to the class type that owns this device.
- **ux_device_class_instance**: Pointer to the instance of the class that owns this device.
- **ux_device_hcd**: USB Host Controller Instance where this device is attached.
- **ux_device_first_configuration**: Pointer to the first configuration container for this device.
- **ux_device_next_device**: Pointer to the next device in the list of device on any of the buses detected by USBX.
- **ux_device_descriptor**: USB device descriptor.
- **ux_device_control_endpoint**: Descriptor of the default control endpoint used by this device.
- **ux_device_hub_tt**: Array of Hub TTs for the device
