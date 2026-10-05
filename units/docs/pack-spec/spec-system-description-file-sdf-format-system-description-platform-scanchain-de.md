---
id: "spec-system-description-file-sdf-format-system-description-platform-scanchain-de"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/scanchain/device"
summary: "Depending on the context, a device type can be one of the following types:"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

| 
    Parents | 
    Element Chain | 
  

  | 
    scanchain | 
    /system_description/platform/scanchain | 
  

  | 
    dap | 
    /system_description/platform/scanchain/dap | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    sdf_element_device | 
    Describes a single nested device associated with this device. | 
    complexType | 
    0..* |   
  

  | 
    sdf_element_device_info_items | 
    Describes a sequence of device information items. | 
    complexType | 
    0..* |   
  

  | 
    sdf_element_config_items | 
    Configuration items specific to this device. | 
    complexType | 
    0..* |   
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Unique name of the device. | 
    xs:string | 
    required | 
  
  
  | 
    type | 
    Specifies the device type (see below). | 
    xs:string | 
    required | 
  
  
  | 
    irLength | 
    Specifies the IR length of the device (default value: 4). | 
    xs:string | 
    optional | 
  
  


Depending on the context, a device type can be one of the following types:

-# A core device, where the type is usually specified as "Cortex-xx" (such as Cortex-A72,Cortex-M0+, Cortex-R5). It can also
   be a vendor-specific core type, or an older JTAG ARM core. Current cores are: \n
   "Cortex-A5", "Cortex-A7", "Cortex-A8", "Cortex-A9", "Cortex-A12", "Cortex-A15", "Cortex-A17", "Cortex-A32", "Cortex-A35",
   "Cortex-A53", "Cortex-A57", "Cortex-A72", "Cortex-A73", "Cortex-M0", "Cortex-M0+", "Cortex-M0+_JTAG-AP", "Cortex-M1",
   "Cortex-M3", "Cortex-M3_JTAG-AP", "Cortex-M4", "Cortex-M7", "Cortex-M23", "Cortex-M33", "Cortex-M35P", "Cortex-M55",
   "Cortex-R4", "Cortex-R5", "Cortex-R7", "Cortex-R8", "Cortex-R52", "SC000", "SC100D", "SC200D", "SC300",
   "ThunderX", "ThunderX-r2", "ARMV8MBL", "ARMV8MML", "ARMV81MML", "88FR101", "88FR111", "88FR331", "88SV581x-v7_PJ4",
   "88SV581x-v7_PJ4_TZ", "ARM1136JF-S", "ARM1136JF-S_JTAG-AP", "ARM1156T2F-S", "ARM1156T2F-S_JTAG-AP", "ARM1176JZF-S",
   "ARM1176JZF-S_JTAG-AP", "ARM11MPCore", "ARM11MPCore_JTAG-AP", "ARM710T", "ARM720T", "ARM720T_r4", "ARM740T", "ARM7EJ-S",
   "ARM7EJ-S_JTAG-AP", "ARM7TDMI", "ARM7TDMI_JTAG-AP", "ARM7TDMI_r4", "ARM7TDMI_r4_JTAG-AP", "ARM920T", "ARM922T", "ARM925T",
   "ARM926EJ-S", "ARM926EJ-S_JTAG-AP", "ARM940T", "ARM946E-S", "ARM946E-S_JTAG-AP", "ARM966E-S", "ARM966E-S_JTAG-AP", "ARM968E-S",
   "ARM968E-S_JTAG-AP", "ARM968E-Srd", "ARM996HS", "ARM9E-S", "ARM9EJ-S", "ARM9EJ-S_JTAG-AP", "ARM9TDMI", "V7A-Generic",
   "V8-Generic", "V8M-Generic", "V8R-Generic", "V8_1-Generic", "V8_2-Generic".
-# An Access Port (AP) type such as "CSAUTHAP", "CSJTAGAP" or "CSMEMAP".
-# A CoreSight device type that can be one of "CSCTI", "CSETM", "CSITM", "CSMTB", "CSPMU", "CSPTM", "CSTFunnel", "CSTMC",
   "CSTPIU","CSSTM", "CSSWO", "CSELA", "CSATBReplicator", "CSGPR", "CSETB", "CSDWT", "CSETB", "CSTSGEN", "CSHTM", "CSFPB"
-# A JTAG device, which is directly on the scanchain (e.g. ARM11).

**Example:**

```
<system_description version="2.0">
    <debug_and_trace_config>
      <!-- Not filled at the moment -->
      <!-- Means using defaults in this area -->
    </debug_and_trace_config>
    <platform>
        <!-- Description of the scanchain -->
        <scanchain>
            <device name="My Custom TAP" type="Other" irLength="5">
                <!-- JTAG-TAP Info -->
                <device_info_items>
                    <device_info_item name="JTAG_IDCODE">0x04560014</device_info_item>
                </device_info_items>
            </device>
	...
</system_description>
```

\delim
