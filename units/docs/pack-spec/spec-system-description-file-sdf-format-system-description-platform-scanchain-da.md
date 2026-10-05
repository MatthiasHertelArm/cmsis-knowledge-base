---
id: "spec-system-description-file-sdf-format-system-description-platform-scanchain-da"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/scanchain/dap"
summary: "Describes a DAP and a list of devices associated with that DAP."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a DAP and a list of devices associated with that DAP.



  | 
    Parents | 
    Element Chain | 
  

  | 
    scanchain | 
    /system_description/platform/scanchain | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    sdf_element_device | 
    List of devices associated with this DAP. | 
    complexType | 
    0..* |   
  

  | 
    sdf_element_device_info_items | 
    Contains implementation details for the DAP. Applicable items for a DAP are "JTAG_IDCODE" (the JTAG ID code for the
	    DAP) or "DPIDR" (the Debug Port Identification Register contents). | 
    complexType | 
    0..* |   
  

  | 
    sdf_element_config_items | 
    Configuration items specific to a DAP type. | 
    complexType | 
    0..* |   
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Unique name of the DAP. | 
    xs:string | 
    required | 
  
  
  | 
    type | 
    Specifies the type of the DAP (e.g. ARMCS-DP). | 
    xs:string | 
    required | 
  
  
  | 
    irLength | 
    Specifies the IR length of the DAP (default value: 4). | 
    xs:string | 
    optional | 
  
  
  | 
    protocol | 
    Colon delimited list of protocols via which the DAP can be use. Possible values are SWD, JTAG, and cJTAG. | 
    xs:string | 
    optional | 
  
  
  | 
    targetsel | 
    Specifies the SW-DPv2 TARGETSEL register value that selects this DAP in a serial-wire debug multi-drop system. | 
    xs:string | 
    optional | 
  
  


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
        
            <!-- ARM Cortex-M0APP -->
            <dap name="ARMCS-DP_CM0APP" type="ARMCS-DP" irLength="4" protocol="JTAG">
                <!-- CoreSight DAP Info -->
                <device_info_items>
                    <device_info_item name="JTAG_IDCODE">0x0BA01477</device_info_item>
                </device_info_items>
                
                <!-- Access Ports -->
                <device name="CM0APP_AHB-AP" type="CSMEMAP"> <!-- Cortex-M0APP AHB-AP -->
                    <config_items>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                    <device_info_items>
                        <device_info_item name="AP_TYPE">AHB-AP</device_info_item>
                        <device_info_item name="ROM_TABLE_BASE_ADDRESS">0xE00FF000</device_info_item>
                    </device_info_items>
                </device>
                
                <!-- Cortex-M0APP AHB-AP Components -->
                <device name="CM0APP_CPU" type="Cortex-M0">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE000E000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM0APP_DWT" type="CSDWT">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0001000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM0APP_FPB" type="CSFPB">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0002000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
            </dap>
    ...
</system_description>
```

\delim
