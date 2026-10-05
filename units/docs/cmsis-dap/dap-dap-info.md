---
id: "dap-dap-info"
type: "concept"
domain: "debug"
title: "DAP_Info"
summary: "Get Information about CMSIS-DAP Debug Unit."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Info.html"
license: "Apache-2.0"
mode: "V"
---

Get Information about CMSIS-DAP Debug Unit.

The **DAP_Info Command** provides configuration information about the Debug Unit itself and the capabilities.

**DAP_Info Command:**
```
| BYTE | BYTE |
> 0x00 | ID   |
|******|******|
```

- **ID:** Request Identifier to obtain information in the Response:
  - **0x01** = Get the **Vendor Name** (string).
  - **0x02** = Get the **Product Name** (string).
  - **0x03** = Get the **Serial Number** (string).
  - **0x04** = Get the **CMSIS-DAP Protocol Version** (string).
  - **0x05** = Get the **Target Device Vendor** (string).
  - **0x06** = Get the **Target Device Name** (string).
  - **0x07** = Get the **Target Board Vendor** (string).
  - **0x08** = Get the **Target Board Name** (string).
  - **0x09** = Get the **Product Firmware Version** (string, vendor-specific format).
  - **0xF0** = Get information about the **Capabilities** (BYTE) of the Debug Unit (see below for details).
  - **0xF1** = Get the **Test Domain Timer** parameter information (see below for details).
  - **0xFB** = Get the **UART Receive Buffer Size** (WORD).
  - **0xFC** = Get the **UART Transmit Buffer Size** (WORD).
  - **0xFD** = Get the **SWO Trace Buffer Size** (WORD).
  - **0xFE** = Get the maximum **Packet Count** (BYTE).
  - **0xFF** = Get the maximum **Packet Size** (SHORT).

**DAP_Info Response:**
```
| BYTE | BYTE | BYTE |
< 0x00 | Len  | Info |
|******|******|++++++|
```

- **Len:**  Info length in bytes.
- **Info:**
  - a **string** encoded as UTF-8. Len is the string length including the \\x00 terminator. Len = 0 indicates no information, and is distinct from an empty string indicated by Len = 1.
  - a **BYTE** value (indicated with Len = 1).
  - a **SHORT** value (indicated with Len = 2).
  - a **WORD** value (indicated with Len = 4).

**Note:**
An unrecognized ID returns no value (indicated by Len = 0).

**Note:**
The ID for **Vendor Name**, **Product Name**, and **Serial Number** may return no string (indicated by Len = 0).
In this case the USB Device Information is used to obtain Vendor Name, Product Name, and Serial Number.

**Note:**
The value of **CMSIS-DAP Protocol Version** must be one of the versions from the CMSIS-DAP revision history, such as "2.1.0".

**Note:**
**Target Device Vendor**, **Target Device Name**, **Target Board Vendor** and **Target Board Name**
are only available on On-Board Debug Units with known Target. Refer to TARGET_FIXED for more information.
Strings should match the listed attribute values from the corresponding CMSIS Board Support Pack.
If the Target is not known no string is returned (indicated by Len = 0).

**Note:**
**Target Device Vendor** should match the Dvendor
attribute value (excluding the colon and vendor code suffix when present) of the `mountedDevice`.

**Note:**
**Target Device Name** should match the Dname
attribute value of the `mountedDevice`.

**Note:**
**Target Board Vendor** should match the vendor
attribute value (excluding the colon and vendor code suffix when present).

**Note:**
**Target Board Name** should match the name
attribute value.

**Note:**
**Product Firmware Version** may return no string (indicated by Len = 0).



**DAP_Info Response (for ID=0xF0):**

The ID=0xF0 **Capabilities** obtains information about the available interface to the Device.
The reply consists of one or two **Info** bytes with bits that indicate the features of the **Debug Unit**.
The features indicate the command scope of the CMSIS-DAP firmware. If certain features are not available, the debugger should not call the related commands as the may not be implemented. Commands that are not implemented reply with 0xFF instead of repeating the command byte.


```
| BYTE | BYTE | BYTE *| BYTE  |
< 0x00 | Len  | Info0 | Info1 |
|******|******|*******|*******|
```

- **Len:**  **1 = Info0** present, **2 = Info0, Info1** present.

Available transfer protocols to target:
 - Info0 - Bit 0: **1 = SWD** Serial Wire Debug communication is implemented (0 = DAP_swd_gr not implemented).
 - Info0 - Bit 1: **1 = JTAG** communication is implemented (0 = DAP_jtag_gr not implemented).

Serial Wire Trace (SWO) support:
 - Info0 - Bit 2: **1 = SWO UART** - UART Serial Wire Output is implemented (0 = not implemented).
 - Info0 - Bit 3: **1 = SWO Manchester** - Manchester Serial Wire Output is implemented (0 = not implemented).

Command extensions for transfer protocol:
 - Info0 - Bit 4: **1 = Atomic Commands** - DAP_atomic_gr support is implemented (0 = DAP_atomic_gr not implemented).

Time synchronisation via Test Domain Timer:
 - Info0 - Bit 5: **1 = Test Domain Timer** - debug unit support for Test Domain Timer is implemented (0 = not implemented).

SWO Streaming Trace support:
 - Info0 - Bit 6: **1 = SWO Streaming Trace** is implemented (0 = not implemented).

UART Communication Port support:
 - Info0 - Bit 7: **1 = UART Communication Port** is implemented (0 = not implemented).

UART Communication via USB COM Port support:
 - Info1 - Bit 0: **1 = USB COM Port** is implemented (0 = not implemented).



**DAP_Info Response (for ID=0xF1):**

The ID=0xF1 **Test Domain Timer** obtains the parameter information about an optional 32-bit Test Domain Timer that may be used for various time measurements.

```
| BYTE | BYTE | WORD *****|
< 0x00 | 0x08 | Frequency |
|******|******|***********|
```

- **Frequency:**  Input frequency of the Test Domain Timer which indicates the resolution of the 32-bit TD_TimeStamp values.
