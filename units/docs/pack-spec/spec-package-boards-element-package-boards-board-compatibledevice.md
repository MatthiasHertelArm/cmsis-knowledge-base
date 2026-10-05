---
id: "spec-package-boards-element-package-boards-board-compatibledevice"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/compatibleDevice"
summary: "This element contains information about devices that are compatible to the device used on the board. Compatible means that the user is able to generate code for compatible devices and test it on the development board."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element contains information about devices that are compatible to the device used on the board. Compatible
means that the user is able to generate code for compatible devices and test it on the development board. At least one compatible device must be specified. In case no compatible device exists for the device mounted on the board or if no device is mounted on the board, like in the case of the daughter boards (called also expansion or extension boards), the `Dvendor` and `Dname` attributes shall be set respectively to "NO_VENDOR:0" and "NO_MCU".

**Example**
```
<compatibleDevice Dvendor="STMicroelectronics:13" Dfamily="STM32F4 Series" DsubFamily="STM32F429"/>
```

Since Dfamily and DsubFamily are volatile, it is recommended to use Dname attribute with wild-cards.

```
<compatibleDevice Dvendor="STMicroelectronics:13" Dname="STM32F429*"/>
```


 		



| Parent | Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| deviceIndex | Index number of the device (in case more than one device is present on the board). | xs:string | optional |
| Dvendor | Vendor name of the target device specified by **Dname.** Use predefined values as listed in the table Device Vendor. If no compatible device exists for the device mounted on the board or if no device is mounted on the board, use predefined value "NO_VENDOR:0". This element is required if at least one of the following attributs is defined: **Dname,** **DsubFamily,** **Dfamily. | DeviceVendorEnum | required |
| Dname***** | Name of the target device used on the board. Requires **Dvendor** to be specified. | xs:string | optional |
| Dfamily | Name of the target device family used on the board. Requires **Dvendor** to be specified. | xs:string | optional |
| DsubFamily | Name of the target device sub-family used on the board. Requires **Dvendor** to be specified. | xs:string | optional |



***)** Wild-cards can be used to match names with the following definitions:
       - '*'  matches any substring
       - '?'  matches any single character
       - [abc] matches any character in the set (a,b,c)
