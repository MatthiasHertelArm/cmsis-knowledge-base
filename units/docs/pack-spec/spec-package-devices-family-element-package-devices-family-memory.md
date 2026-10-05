---
id: "spec-package-devices-family-element-package-devices-family-memory"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../memory"
summary: "This element specifies memory regions that devices can have. Memory types are predefined and can be selected. This element can be defined on various levels. Inner memory elements supersede outer elements."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies memory regions that devices can have. Memory types are predefined and can be selected.
This element can be defined on various levels. Inner memory elements supersede outer elements.

**Example**
```
</package>
  ...
  <devices>
    <family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
      <memory name="SRAM" access="rwx" start="0x20000000" size="0x20000" default="1"/>

      <subFamily DsubFamily="STM32F407">
        <debug  __dp="0" __ap="0" svd="SVD/STM32F40x.svd"/>
        <memory name="SRAM1" access="rwx" start="0x20020000" size="0x20000" default="1"/>
        <memory name="SRAM2" access="rwx" start="0x10000000" size="0x10000" default="1"/>
        
        <device Dname="STM32F407IE">
          <memory name="Flash" access="rx" start="0x08000000" size="0x80000" startup="1" default="1"/>
        </device>
        
      </subFamily>
    </family>
  </devices>
  ...
</package>
```

\n



  | 
    Parents | 
    Element Chain | 
  

  | 
    family | 
    element_family | 
  

  | 
    subFamily | 
    element_subFamily | 
  

  | 
    device | 
    element_device | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor identifier. This attribute **is mandatory for devices that embed multiple processors**. 
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.  | 
    RestrictedString | 
    optional | 
  

  | 
    id (deprecated since version 1.4.0) | 
    Identifier of the memory region consisting of a type indicator and an index (for example, `IRAM1`). | 
    Predefined values can be selected as defined in MemoryIDTypeEnum. | 
    MemoryIDTypeEnum | 
    optional | 
  

  | 
    name (new since version 1.4.0) | 
    
      
Unique name of the memory to be used in conjunction with _access_.
      
If a memory with the same name is already defined in a parent scope, the parent one is extended/overwritten.
      
Backward compatibility: If no 'name' attribute is given but 'id' attribute
      is still present, the given 'id' attribute is used as the 'name'.
     | 
    xs:string | 
    optional | 
  

  | 
    access (new since version 1.4.0) | 
    Access permission of the memory. See MemoryAccessTypeString for details. | 
    MemoryAccessTypeString | 
    optional | 
  

  | 
    start | 
    Base address of the memory using a hexadecimal value. | 
    NonNegativeInteger | 
    required | 
  

  | 
    size | 
    Size of the memory in bytes using a hexadecimal value. | 
    NonNegativeInteger | 
    required | 
  

  | 
    default | 
    
      
Indicates a general purpose memory region, that does not require any special considerations (access speed, remapping, protection, etc.).
      
If `true`, then an IRAM memory region will be used by the linker for locating any data and an IROM memory region will for locating 
      any code. Every device needs at least one default IRAM region.
      
If an algorithm element is specified (without `RAMstart` and
      `RAMsize` attributes), the first listed IRAM region with default="1" will also be used for executing the flash programming algorithm.
      
Default value is `false`.
     | 
    xs:boolean | 
    optional | 
  

  | 
    startup | 
    If `true`, the startup code of the application will be placed into this memory region. Default value is `false`. | 
    xs:boolean | 
    optional | 
  

  | 
    init (deprecated since version 1.6.3) | 
    
      
If `true`, the memory region shall not be zero initialized.
      
Default value is `false`.
     | 
    xs:boolean | 
    optional | 
  

  | 
    uninit (new since version 1.6.3) | 
    
      
If `true`, the memory region shall be kept uninitialized (i.e. keep the memory state as is).
      
Default value is `false`.
     | 
    xs:boolean | 
    optional | 
  

  | 
    alias (new since Version 1.4.0) | 
    
      Reference to another memory (by it's 'name' attribute) which shares the same physical memory. Some physical
      memory is made accessible via different addresses, for example, cached vs. non-cached accesses. This
      avoids the impression that the device has twice as much memory available.
     | 
    xs:string | 
    optional | 
  



\n

 **Table: Memory ID Types**

The table lists identifiers for memory types.


  | 
    id= | 
    Description | 
  

  | 
    RAM_x_ | 
    External RAM. _x_ can have a value between 1..8  | 
  

  | 
    ROM_x_ | 
    External ROM. _x_ can have a value between 1..8  | 
  

  | 
    IRAM_x_ | 
    Internal RAM. _x_ can have a value between 1..8  | 
  

  | 
    IROM_x_ | 
    Internal ROM. _x_ can have a value between 1..8  | 
  



\delim

 **Table: Memory Access Attribute String**

The table lists the letters and their meaning for use in the access attribute string. The values can be used in:
 - element_memory, element_board_memory



  | 
    access= | 
    Description | 
  

  | 
    r | 
    _R_eadable | 
  

  | 
    w | 
    _W_ritable | 
  

  | 
    x | 
    e_X_ecutable | 
  

    | 
    p | 
    _P_eripheral area. Details described in SVD. | 
  

  | 
    s | 
    _S_ecure attribute | 
  

  | 
    n | 
    _N_on-secure attribute | 
  

  | 
    c | 
    non-secure _C_allable attribute | 
  



\delim
