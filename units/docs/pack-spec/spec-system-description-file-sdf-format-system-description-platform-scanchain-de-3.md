---
id: "spec-system-description-file-sdf-format-system-description-platform-scanchain-de-3"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform/scanchain/../../device_info_items/device_info_item"
summary: "Describes implementation specific details of the specified device or DAP."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes implementation specific details of the specified device or DAP.



  | 
    Parents | 
    Element Chain | 
  

  | 
    device_info_items | 
    /system_description/platform/../../device_info_items | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Unique name for the device information item. | 
    xs:string | 
    required | 
  
  


The following device information items are applicable for each type of "device":

| Device     | Device Information Item           | Description |
|------------|-----------------------------------|-------------|
| **CSMEMAP** | AP_TYPE                           | Access port type is one of AHB-AP, APB-AP-M, APB-AP, APB4-AP and AXI-AP |
|            | ROM_TABLE_BASE_ADDRESS            | The ROM table base address (in hex) |
|            | AP_VERSION                        | AP architecture version is one of APv1 and APv2 (Default Value: APv1) |
| **CSETM**   | VERSION                           | The ETM Version (e.g. 4.0 - required) |
|            | SUPPORTS_CONTEXT_IDS              | Supports Context ID Tracing (True/False - Default Value:False) |
|            | SUPPORTS_VIRTUAL_CONTEXT_IDS      | Supports Virtual Context ID Tracing (True/False - Default Value:False) |
|            | SUPPORTS_CYCLE_ACCURATE           | Supports Cycle Accurate Trace (True/False - Default Value:False) |
|            | SUPPORTS_DATA_VALUE_TRACE         | Supports Data Value Trace (True/False - Default Value:False) |
|            | SUPPORTS_DATA_ADDRESS_TRACE       | Supports Data Address Trace (True/False - Default Value:False) |
|            | SUPPORTS_DATA_ONLY_MODE           | Supports Data Only Trace Mode (True/False - Default Value:False) |
|            | SUPPORTS_TIMESTAMPS               | Supports Timestamps(True/False - Default Value:False) |
|            | SUPPORTS_TRACE_RANGES             | Supports Trace Ranges (True/False - Default Value:False) |
|            | SUPPORTS_BRANCH_BROADCAST         | Supports Branch Broadcasting (True/False - Default Value:False) |
|            | SUPPORTS_CONDITIONAL_INSTRUCTIONS | Supports tracing conditional non-branch instruction (True/False - Default Value:False) |
|            | SUPPORTS_Q_ELEMENTS               | Supports Q Elements (True/False - Default Value:False) |
| **CSMTB**   | RAM_SIZE_BYTES                    | MTB SRAM buffer size in bytes |
|            | SUPPORTS_USER_PRIV                | User/Privileged support present |
| **CSTPM**   | VERSION                           | The PTM Version (eg 1.1) - Required |
|            | SUPPORTS_VMID                     | VMID Tracing support (True/False - Default Value:False) |
|            | SUPPORTS_CONTEXT_IDS              | Context ID Tracing support (True/False - Default Value:False) |
|            | SUPPORTS_RETURN_STACK             | Return stack support (True/False - Default Value:False) |
|            | SUPPORTS_CYCLE_ACCURATE           | Cycle Accurate trace support (True/False - Default Value:False) |
|            | SUPPORTS_BRANCH_BROADCAST         | Supports Branch Broadcasting (True/False - Default Value:False) |
|            | SUPPORTS_TIMESTAMPS               | Supports Timestamping (True/False - Default Value:False) |
|            | SUPPORTS_FIFOFULL                 | Supports FIFOFULL (True/False - Default Value:False) |
| **CSTMC**   | CONFIG_TYPE                       | The TMC device configuration can be one of (ETR, ETF or ETB) - required |
|            | RAM_SIZE_BYTES                    | The SRAM memory size used in ETF and ETR configurations (512 Bytes to 4 GiB) - Default: 512 Bytes |
| **CSTPIU**  | SUPPORTED_PORT_SIZES              | Semicolon separated list of supported port sizes (in bits) - required |
|            | ARCHITECTURE                      | The TPIU variant is one of (Coresight, TPIU-Lite, V7-M or V8-M) - Required |

**Example:**

```
<system_description version="2.0">
  ...
  <platform>
    <!-- Description of the scanchain -->
    <scanchain>
        <!-- ARM Cortex-M0APP -->
        <dap name="ARMCS-DP_CM0APP" type="ARMCS-DP" irLength="4" protocol="JTAG">
            <!-- CoreSight DAP Info -->
            <device_info_items>
                <device_info_item name="JTAG_IDCODE">0x00000000</device_info_item>
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
  ...
```

\delim
