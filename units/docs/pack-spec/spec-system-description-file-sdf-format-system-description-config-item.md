---
id: "spec-system-description-file-sdf-format-system-description-config-item"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/.../config_item"
summary: "A configitem can appear in various SDF elements. This group contains individual configuration items."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

A **config_item** can appear in various SDF elements. This group contains individual configuration items.



  | 
    Parents | 
    Element Chain | 
  

  | 
    debug | 
    /system_description/debug_and_trace_config/debug | 
  

  | 
    trace_capture | 
    /system_description/debug_and_trace_config/trace/trace_capture | 
  

  | 
    config_items | 
    /system_description/platform/scanchain/../config_items | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of the configuration item. | 
    xs:string | 
    required | 
  
  


Debug element
-------------

The **config_items** applicable to the debug element are the following:

| Item                   | Description | 
|------------------------|-------------|
| TRSTOnConnect          | Debugger should perform TAP reset on connect (True/False) - Default Value:True |
| SRSTOnConnect          | Debugger should perform a System reset on connect (True/False) - Default Value:False |
| AllowTRST              | Allow the Debugger to perform TAP reset (True/False) - Default Value:True |
| DoSoftTRST             | Debugger should perform a Soft Reset (True/False) - Default Value:True |
| TRSTHoldTime           | TAP reset hold time in milliseconds - Default Value:10 |
| TRSTPostResetTime      | Delay after TAP reset before next operation - Default Value:10 |
| ResetHoldTime          | Time in milliseconds that the target is held in a hardware reset state - Default Value:100 |
| PostResetDelay         | Time in milliseconds that the target will wait after reset is released before attempting any other debugging operations - Default Value:10 |
| Linked_SRST_TRST       | Target hardware has System Reset and TAP reset physically linked (True/False) - Default Value:False|

Device element
--------------

The **config_items** applicable to the device element are the following (only applicable for devices
that are child elements of another device or DAP):

| Item                   | Description | Use |
|------------------------|-------------|-----|
| CORESIGHT_BASE_ADDRESS | the 4K aligned base address of a CoreSight device | Required |
| CORESIGHT_AP_INDEX     | the access port index of the device | Required |
| CORESIGHT_AP_ADDRESS   | the memory-mapped access port address of the device | Required for ADIv6 APv2 devices, otherwise ignored |
| PARENT_AP_INDEX        | the parent access port index of this access port | Required for ADIv6 APv2 devices if accessed via a parent access port, otherwise ignored |

Trace element
-----------

The **config_items** applicable to the trace element are the following:
-# Parallel trace capture device configuration items ("type" = "parallel"). These "config_items" enable you to configure
   delays on the trace lines by a specified amount of time relative to the trace capture device defaults. These delays are
   used to allow for variations in target hardware. These configuration items have default values if not present.
   | Item                   | Description | Default |
   |------------------------|-------------|----------|
   | CLOCK_EDGE             | Set to 0 or 1 to specify the clock edge on which to capture data | 1 |
   | DELAY_TRACE_CLOCK      | Adjust the sampling point for the trace clock by the specified number of picoseconds | 0 |
   | DELAY_TRACE_SIGNAL_1 to DELAY_TRACE_SIGNAL_n | Adjust the sampling point for parallel trace signal 'n' by the specified number of picoseconds | 0 |
   
-# High-speed serial trace configuration items ("type"="HSSTP"). These configuration items do not have any default values. If
   they are not present in the SDF file then HSSTP trace is not supported by the target.
   | Item                   | Description | 
   |------------------------|-------------|
   | HSSTP_LANES            | The number of lanes (1-6) |
   | HSSTP_SPEED            | The HSSTP link speed (HSSTP_2_5Gbps, , HSSTP_3_0Gbps, HSSTP_3_125Gbps, HSSTP_4_25Gbps, HSSTP_5_0Gbps, HSSTP_6_0Gbps, HSSTP_6_25Gbps, HSSTP_8_0Gbps, HSSTP_10_0Gbps, HSSTP_10_3125Gbps, HSSTP_12_0Gbps, HSSTP_12_5Gbps, HSSTP_SETM_1_5Gbps, HSSTP_SETM_3_0Gbps, HSSTP_SETM_6_0Gbps)
   | HSSTP_PROTOCOL         | The HSSTP protocol (HSSTP_PROTOCOL_ARM_HSSTP, HSSTP_PROTOCOL_8_BIT_SETM, HSSTP_PROTOCOL_16_BIT_SETM, HSSTP_PROTOCOL_32_BIT_SETM)
   | HSSTP_NDALT            | Reverse byte bit-ordering (HSSTP_NDALT_Disabled/HSSTP_NDALT_Enabled) |
   | HSSTP_CONNECTOR        | The physical connector type (HSSTP_CONNECTOR_HSSTP/HSSTP_CONNECTOR_SMA) |
   | HSSTP_RX_EQUALIZATION  | The RX equalization type (RX_EQUALIZATION_DFE/RX_EQUALIZATION_LPM) |
   | HSSTP_CRC              | The type of CRC to use (HSSTP_CRC_Enabled, HSSTP_CRC_Disabled, HSSTP_CRC_Reversed, HSSTP_CRC_Ignored) |

**Example**

```
...
<device name="CM4_ETM" type="CSETM">
    <device_info_items>
        <device_info_item name="VERSION">3.5</device_info_item>
        <device_info_item name="SUPPORTS_CYCLE_ACCURATE">true</device_info_item>
    </device_info_items>
    <config_items>
        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0041000</config_item>
        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
    </config_items>
</device>
...
```
\delim
