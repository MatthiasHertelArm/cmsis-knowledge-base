---
id: "txmw-chapter-3-functional-components-of-configuration-descriptors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: USB Device Framework / Configuration Descriptors"
summary: "The configuration descriptor describes information about a specific device configuration. A USB device may contain one or more configuration descriptors. The bNumConfigurations field in the device descriptor indicates the number of configuration descriptors."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#configuration-descriptors"
license: "MIT"
mode: "V"
---

_Part of: USB Device Framework_

The configuration descriptor describes information about a specific device configuration. A USB device may contain one or more configuration descriptors. The **bNumConfigurations** field in the device descriptor indicates the number of configuration descriptors. The descriptor contains a **bConfigurationValue** field with a value that, when used as a parameter to the Set Configuration request, causes the device to assume the described configuration.

The descriptor describes the number of interfaces provided by the configuration. Each interface represents a logical function within the device and may operate independently. For instance a USB audio speaker may have three interfaces, one for audio streaming, one for audio control, and one HID interface to manage the speaker's buttons.

When the host issues a GET_DESCRIPTOR request for the configuration descriptor, all related interface and endpoint descriptors are returned.

| Offset | Field               | Size | Value    | Description                       |
| ------ | ------------------- | ---- | -------- | --------------------------------- |
| 0      | bLength             | 1    | Number   | Size of this descriptor in bytes. |
| 1      | bDescriptorType     | 1    | Constant | CONFIGURATION                     |
| 2      | wTotalLength        | 2    | Number   | Total length of data returned for this configuration. Includes the combined length of all descriptors (configuration, interface, endpoint, and class or vendor specific) returned for this configuration. |
| 4      | bNumInterfaces      | 1    | Number   | Number of interfaces supported by this configuration. |
| 5      | bConfigurationValue | 1    | Number   | Value to use as an argument to Set
Configuration to select this configuration. |
| 6      | iConfiguration      | 1    | Index    | Index of string descriptor describing this configuration. |
| 7      | bMAttributes        | 1    | Bitmap   | Configuration characteristics D7 Bus Powered
D6 Self Powered
D5 Remote Wakeup
D4..0 Reserved (reset to 0)
A device configuration that uses power from the bus and a local source sets both D7 and D6. The actual power source at runtime may be determined using the Get Status device request.
If a device configuration supports remote wakeup, D5 is set to 1. |
| 8      | MaxPower            | 1    | mA       | Maximum power consumption of USB device from the bus in this specific configuration when the device is fully operational.
Expressed in 2 mA units (e.g., 50 = 100 mA).
Note: A device configuration reports whether the configuration is bus-powered or self-powered.
Device status reports whether the device is currently self-powered. If a device is disconnected from its external power source, it updates device status to indicate that it is no longer self-powered. |

USBX defines a USB configuration descriptor as follows.

```c
typedef struct UX_CONFIGURATION_DESCRIPTOR_STRUCT
{
    UINT bLength;
    UINT bDescriptorType;
    USHORT wTotalLength;
    UINT bNumInterfaces;
    UINT bConfigurationValue;
    UINT iConfiguration;
    UINT bmAttributes;
    UINT MaxPower;
} UX_CONFIGURATION_DESCRIPTOR;
```

The USB configuration descriptor is part of a configuration container described as shown below.

```c
typedef struct UX_CONFIGURATION_STRUCT
{
    ULONG ux_configuration_handle;
    ULONG ux_configuration_state;
    struct UX_CONFIGURATION_DESCRIPTOR_STRUCT ux_configuration_descriptor;
    struct UX_INTERFACE_STRUCT *ux_configuration_first_interface;
    struct UX_CONFIGURATION_STRUCT *ux_configuration_next_configuration;
    struct UX_DEVICE_STRUCT *ux_configuration_device;
} UX_CONFIGURATION;
```

- **ux_configuration_handle**: Handle of the configuration. This is typically the address of the instance of this structure for the configuration.
- **ux_configuration_state**: State of the configuration.
- **ux_configuration_descriptor**: USB device descriptor.
- **ux_configuration_first_interface**: Pointer to the first interface for this configuration.
- **ux_configuration_next_configuration**: Pointer to the next configuration for the same device.
- **ux_configuration_device**: Pointer to the device owner of this configuration.
