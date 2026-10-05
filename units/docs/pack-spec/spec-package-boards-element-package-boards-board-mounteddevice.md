---
id: "spec-package-boards-element-package-boards-board-mounteddevice"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/mountedDevice"
summary: "The element specifies the devices mounted on the board. Exactly one device must be specified per deviceIndex."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element specifies the devices mounted on the board. Exactly one device must be specified per deviceIndex. In case no device is mounted on the board, like in the case of the daughter boards (called also expansion or extension boards), the `Dvendor` and `Dname` attributes shall be set respectively to "NO_VENDOR:0" and "NO_MCU".

**Example**
```
<mountedDevice deviceIndex="0" Dvendor="STMicroelectronics:13" Dname="STM32F429ZITx"/>
```

 		



  | 
    Parent | 
    Chain | 
  

  | 
    board | 
    element_board | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    deviceIndex | 
    Index number of the device (in case more than one device is present on the board). | 
    xs:string | 
    optional | 
  

  | 
    Dvendor | 
    Is the name of vendor of the device specified by `Dname`. Use predefined values as listed in the table Device Vendor. If no device is mounted on the board, use predefined value "NO_VENDOR:0". | 
    DeviceVendorEnum | 
    required | 
  

  | 
    Dname | 
	Is the name of the target device used on the board. If the device is specified by a variant this string needs to be assigned to the Dname attribute. If no device is mounted on the board, use value "NO_MCU". | 
	xs:string | 
	required |
