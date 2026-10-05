---
id: "spec-system-description-file-sdf-format"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format"
summary: "An SDF file enables the silicon provider to describe more complex debug topologies than with a debugdescription in a tool agnostic way. Multiple debug and access ports and the setup of the different debug/trace components can be described consistently."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

An SDF file enables the silicon provider to describe more complex debug topologies than with a debug_description in a
tool agnostic way. Multiple debug and access ports and the setup of the different debug/trace components can be described
consistently. Also, mandatory settings for a debugger can be described, such as trace signal delay settings,
availability/usability of certain reset methods or timings, etc. This information is used by the debugger to access the right
components that are requested by the user or application. The SDF format provides the XML elements for defining the debug
system view of a device. These are "expert" settings that cannot be specified in a PDSC file.

**Note:** SDF files are referenced in a PDSC file via the `\<debugconfig\>` element.

**Example CMSIS System Description File (*.SDF)**
```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
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
            
            <!-- ARM Cortex-M4 -->
            <dap name="ARMCS-DP_CM4" type="ARMCS-DP" irLength="4" protocol="SWD:JTAG">
                <!-- CoreSight DAP Info -->
                <device_info_items>
                    <device_info_item name="JTAG_IDCODE">0x4BA00477</device_info_item>
                </device_info_items>
                
                <!-- Access Ports -->
                <device name="CM4_AHB-AP" type="CSMEMAP"> <!-- Cortex-M4 AHB-AP -->
                    <config_items>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                    <device_info_items>
                        <device_info_item name="AP_TYPE">AHB-AP</device_info_item>
                        <device_info_item name="ROM_TABLE_BASE_ADDRESS">0xE00FF000</device_info_item>
                    </device_info_items>
                </device>
                
                <!-- Cortex-M4 AHB-AP Components -->
                <device name="CM4_CPU" type="Cortex-M4">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE000E000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM4_DWT" type="CSDWT">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0001000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM4_FPB" type="CSFPB">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0002000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM4_ITM" type="CSITM">
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0000000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
                <device name="CM4_TPIU" type="CSTPIU">
                    <device_info_items>
                      <device_info_item name="ARCHITECTURE"             >V7-M</device_info_item>
                      <device_info_item name="SUPPORTED_FORMATTER_MODES">CONTINUOUS</device_info_item>
                      <device_info_item name="SUPPORTED_PORT_SIZES"     >1;2;4</device_info_item>
                    </device_info_items>
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0040000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
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
                <device name="CM4_ETB" type="CSETB">
                    <device_info_items>
                        <device_info_item name="MEM_WIDTH"     >32</device_info_item>
                        <device_info_item name="RAM_SIZE_BYTES">0x4000</device_info_item>
                    </device_info_items>
                    <config_items>
                        <config_item name="CORESIGHT_BASE_ADDRESS">0xE0042000</config_item>
                        <config_item name="CORESIGHT_AP_INDEX">0</config_item>
                    </config_items>
                </device>
            </dap>
            
        </scanchain>
    
        <topology>
            <!-- Trace Links -->
            <!-- Core Trace - Cortex-M4 -->
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_DWT"/>
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_ITM"/>
            <topology_link type="CoreTrace" master="CM4_CPU" slave="CM4_ETM"/>
            <topology_link type="ATB" master="CM4_ETM"       slave="CM4_TPIU" slave_interface="0"/>
            <topology_link type="ATB" master="CM4_ITM"       slave="CM4_TPIU" slave_interface="1"/>
            <!-- Trace - Cortex-M4 ETB (Direct Connection ETM -> ETB) -->
            <topology_link type="ATB" master="CM4_ETM"       slave="CM4_ETB"/>
        </topology>
    </platform>
</system_description>
```
