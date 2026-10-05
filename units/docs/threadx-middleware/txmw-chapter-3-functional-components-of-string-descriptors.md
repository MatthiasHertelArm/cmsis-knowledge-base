---
id: "txmw-chapter-3-functional-components-of-string-descriptors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: USB Device Framework / String descriptors"
summary: "String descriptors are optional. If a device does not support string descriptors, all references to string descriptors within device, configuration, and interface descriptors must be reset to zero."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#string-descriptors"
license: "MIT"
mode: "V"
---

_Part of: USB Device Framework_

String descriptors are optional. If a device does not support string descriptors, all references to string descriptors within device, configuration, and interface descriptors must be reset to zero.

String descriptors use UNICODE encoding, thus allowing the support for several character sets. The strings in a USB device may support multiple languages. When requesting a string descriptor, the requester specifies the desired language using a language ID defined by the USB-IF. The list of currently defined USB LANGIDs can be found in the USBX appendix ??.
String index zero for all languages returns a string descriptor that contains an array of two-byte LANGID codes supported by the device. It should be noted that the UNICODE string is not 0 terminated. Instead, the size of the string array is computed by subtracting two from the size of the array contained in the first byte of the descriptor.

The USB string descriptor 0 is encoded as follows.

| Offset | Field           | Size | Value    | Description                      |
| ------ | --------------- | ---- | -------- | -------------------------------- |
| 0      | bLength         | 1    | N+2      | Size of this descriptor in bytes |
| 1      | bDescriptorType | 1    | Constant | STRING Descriptor Type           |
| 2      | wLANGID[0]      | 2    | Number   | LANGID code 0                    |
| ...    | ...]            | ...  | ...      | ...                              |
| N      | wLANGID[n]      | 2    | Number   | LANGID code n                    |

Other USB string descriptors are encoded as follows.

| Offset | Field           | Size | Value    | Description                      |
| ------ | --------------- | ---- | -------- | -------------------------------- |
| 0      | bLength         | 1    | Number   | Size of this descriptor in bytes |
| 1      | bDescriptorType | 1    | Constant | STRING Descriptor Type           |
| 2      | bString         | n    | Number   | UNICODE encoded string           |

USBX defines a non-zero length USB string descriptor as follows:

```c
typedef struct UX_STRING_DESCRIPTOR_STRUCT
{
    UINT bLength;
    UINT bDescriptorType;
    USHORT bString[1];
} UX_STRING_DESCRIPTOR;
```
