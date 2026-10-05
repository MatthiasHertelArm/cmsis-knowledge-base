---
id: "spec-package-devices-family-element-package-devices-family-debug-datapatch"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debug/datapatch"
summary: "Describes a patch a debugger shall apply when reading data from the device."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a patch a debugger shall apply when reading data from the device.

**Example**
```
<family Dfamily="M0 Series" Dvendor="Generic:5">
  ...
  <debug>
    <!-- Patched ROM Table for a Cortex-M0+ -->
    <datapatch  type=”AP”__dp="0" __ap="0" address="0xF8" value="0xE00FF003" info="AP BASE Register, ROM Table at 0xE00FF000"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FF000" value="0xFFF0F003" info="ROM Table pointer to SCS at 0xE000E000"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FF004" value="0xFFF02003" info="ROM Table pointer to DWT at 0xE0001000"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FF008" value="0xFFF03003" info="ROM Table pointer to BPU at 0xE0002000"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FF00C" value="0x00000000" info="ROM Table End Marker"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFCC" value="0x00000001" info="ROM Table MEMTYPE"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFD0" value="0x00000004" info="ROM Table Peripheral ID4"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFD4" value="0x00000000" info="ROM Table Peripheral ID5"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFD8" value="0x00000000" info="ROM Table Peripheral ID6"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFDC" value="0x00000000" info="ROM Table Peripheral ID7"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFE0" value="0x000000C0" info="ROM Table Peripheral ID0"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFE4" value="0x000000B4" info="ROM Table Peripheral ID1"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFE8" value="0x0000000B" info="ROM Table Peripheral ID2"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFEC" value="0x00000000" info="ROM Table Peripheral ID3"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFF0" value="0x0000000D" info="ROM Table Component  ID0"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFF4" value="0x00000010" info="ROM Table Component  ID1"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFF8" value="0x00000005" info="ROM Table Component  ID2"/>
    <datapatch  __dp="0" __ap="0" address="0xE00FFFFC" value="0x000000B1" info="ROM Table Component  ID3"/>
  </debug>
  ...
</family>
```


 		



  | 
    Parents | 
    Element Chain | 
  

  | 
    debug | 
    element_debug | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    type | 
    
      The type of data access to patch. Predefined tokens must be used as defined in Table: Data Patch Access Type.
      This attribute defaults to `Mem` if not set.
     | 
    DataPatchAccessTypeEnum | 
    optional | 
  

  | 
    address | 
    The address for which to apply the patch.

    For an `AP` data patch for an APv2 as referenced by **__apid**, the address is the APv2 register offset added to the APv2's base address
    defined in the corresponding accessportV2 element. It must within the 4-KByte address range of the APv2 block. | 
    NonNegativeInteger | 
    required | 
  

  | 
    __dp | 
    
      The debug port ID to apply the patch for. The allowed values are defined by the **__dp** attribute of **debugport**
      elements for this device. If no debugport element exists, the only allowed value is 0. If this attribute is not set, the debug port
      ID for the data patch is set to the default **__dp** of this **debug** section.

      If accessportV1 or accessportV2 elements are specified then this attribute is only
      allowed for `DP` and `ACCESS_AP` accesses. Use **__apid** for all others.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    __ap | 
    
      The CoreSight access port index to apply the patch for. If this attribute is not set, the access port index
      for the data patch is set to the default **__ap** of this **debug** section.

      Must not be used if accessportV1 or accessportV2 elements are specified. Use **__apid** instead.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    __apid | 
    
      The unique ID of a CoreSight access port to apply the patch for. Requires accessportV1 and/or
      accessportV2 elements to be specified. If this attribute is not set, the access port ID
      for the data patch is set to the default **__apid** of this **debug** section.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    value | 
    The value with which the debugger patches the data access. **value** is specified in little-endian format. | 
    NonNegativeInteger | 
    required | 
  

  | 
    mask | 
    The bits of the data access to patch. The mask value is specified in little-endian format. | 
    NonNegativeInteger | 
    optional | 
  

  | 
    info | 
    Descriptive text to display for example for error diagnostics. | 
    xs:string | 
    optional | 
  




 		

 **Table: Data Patch Access Type**

The table lists the allowed values for data patch access types.


  | 
    type= | 
    Description | 
  

  | 
    AP | 
    CoreSight Access Port register access.  | 
  

  | 
    Mem | 
    Memory access.  | 
  

  | 
    DP | 
    **Removed from specification starting version 1.7.49**: CoreSight Debug Port register access.

    **Note:** This type refers to accesses via the **DPACC** instruction for **CoreSight JTAG-DPs**. Please refer to the
    corresponding documentation for differences in the register interface between JTAG and Serial Wire debug ports.
     | 
  

  | 
    ACCESS_AP | 
    **Removed from specification starting version 1.7.49**: Top-level Access Port access for a CoreSight ADIv6 DAP.  |
