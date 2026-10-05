---
id: "spec-package-devices-family-element-package-devices-family-debug"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debug"
summary: "Describes configuration settings, default values, and patches for data accesses for a debug connection. Multiple debug elements can be defined which are either specific to a processor identified by attribute Pname, or which apply to all connections."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes configuration settings, default values, and patches for data accesses for a debug connection. Multiple **debug**
elements can be defined which are either specific to a processor identified by attribute **Pname**, or which apply
to all connections.

**Example** **1**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <debug Pname="Cortex-M4" __dp="0" __ap="0" svd="SVD/LPC43xx.svd">
    ...
  </debug>
  ...
  <debug Pname="Cortex-M0" __dp="1" __ap="0" svd="SVD/LPC43xx.svd">
    ...
  </debug>
  ...
</family>
```

**Example** **2**
```
<device name="MCIMX7D">
  ...
  <processor Dcore="Cortex-A7" DcoreVersion="r0p5" Pname="Cortex-A7" Punits="2" />
  <processor Dcore="Cortex-M4" DcoreVersion="r0p1" Pname="Cortex-M4"/>
  ...
  <debug   Pname="Cortex-A7" Punit="0" svd="SVD/iMX7D_A7.svd" __dp="0" __ap="1" address="0x80070000"/> 
  <debug   Pname="Cortex-A7" Punit="1" svd="SVD/iMX7D_A7.svd" __dp="0" __ap="1" address="0x80072000"/>
  <debug   Pname="Cortex-M4"           svd="SVD/iMX7D_M4.svd" __dp="0" __ap="4"/>
  ...
</device>
```


 		



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
    __dp | 
    
      Default debug port ID to use for target accesses in this debug connection. The allowed values are
      defined in **debugport** elements for this device. If no **debugport** element exists, the only
      allowed value is `0`.

      The debug access variable **__dp** is initialized to this value when entering a pre-defined debug access
      sequence because of a debug event.

      This attribute defaults to `0` if not set.

      Must not be used if accessportV1 or accessportV2 elements are specified. Use **__apid** instead.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    __ap | 
    
      Default access port index to use for target accesses in this debug connection.

      The debug access variable **__ap** is initialized to this value when entering a pre-defined debug access
      sequence because of a debug event.

      This attribute defaults to `0` if not set.

      Must not be used if accessportV1 or accessportV2 elements are specified. Use **__apid** instead.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    __apid | 
    
      Default access port ID to use for target accesses in this debug connection.

      The debug access variable **__apid** is initialized to this value when entering a pre-defined debug access sequence because of a debug event. Requires accessportV1 and/or accessportV2 elements to be specified.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
    address | 
    
      Base "address" of the CPU debug block referenced by "Pname" (and "Punit" in an MPCore system). Use in combination
      with attributes "__dp" and "__ap", or "__apid" respectively. Mandatory if multiple CPU debug blocks are accessible via a single AP. Optional
      if an AP hosts a single CPU debug block. Then a debugger can determine its base address by analyzing the ROM
      table behind the selected AP.
     | 
    NonNegativeInteger | 
    optional | 
  

  | 
    svd | 
    The system viewer description (*.SVD) file to load for this debug connection. The file path is relative
    to the package base folder. | 
    xs:string | 
    optional | 
  

  | 
    Pname | 
    
      Reference to a processor identifier as specified for a **processor** element. If **Pname** is set
      this **debug** element's settings and data patches only apply for target connections to the referenced
      processor. Otherwise, they apply for all processors.
      **This attribute must be set if defining multiple **debug** elements within the same section.**
      Only alphabetical characters, decimal digits, '-' and '_' are allowed.
     | 
    RestrictedString | 
    optional | 
  

  | 
    Punit | 
    
      Use "Punit" in addition to "Pname" to select a specific processor unit of a symmetric MPCore that the `<debug>`
      configuration applies to. "Punit" is a '0'-based index and must be less than "Punits" of `
`. If
      "Punit" is not specified, the `<debug>` configuration applies to all processor units of the MPCore.
     | 
    xs:unsignedInt | 
    optional | 
  

  | 
     defaultResetSequence | 
    
      Specifies the debug sequence that shall be used by default for the reset operation. It can be set to one of the predefined reset sequences such as resetSystem, resetHardware and resetProcessor or also to any user-defined debug sequence. If not specified then resetSystem sequence will be set as default.
     | 
    xs:string | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    datapatch | 
    Define a patch to apply for data reads in this debug connection. | 
    DataPatchType | 
    0..* | 
  



\delim
