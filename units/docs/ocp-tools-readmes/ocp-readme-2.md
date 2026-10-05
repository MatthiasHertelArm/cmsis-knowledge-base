---
id: "ocp-readme-2"
type: "concept"
domain: "project"
title: "README"
summary: "Board: ARM AVH_MPS3_Corstone-310 ----------------------------------------------"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Board/AVH_MPS3_Corstone-310/IoT/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/AVH_MPS3_Corstone-310/IoT/README.md"
license: "Apache-2.0"
mode: "V"
---

Board: ARM AVH_MPS3_Corstone-310
----------------------------------------------

MPS3 platform for Corstone-310 simulated by Arm Virtual Hardware Targets (VHT).

The following models are available:
 - VHT_Corstone_SSE-310: Corstone-310 for MPS3
 - VHT_Corstone_SSE-310_Ethos-U65: Corstone-310 with Ethos-U65 for MPS3

Running the VHT in uVision requires the following settings:
 - open "Options for Target"
 - select "Debug" tab
 - under "Use" select "Models ARMv8-M Debugger" and click "Settings" end enter the following:
   - Command: `$KARM\VHT\VHT_Corstone_SSE-310.exe`
   - Target: `cpu0`
   - Configuration File: `<board_path>\fvp_config.txt`

Running the VHT via command line (from project root directory and VHT executable in path):
`VHT_Corstone_SSE-310 -f <board_path>/AVH_MPS3_Corstone-310/fvp_config.txt -a <image>`

> Note: running on fast computers can lead to simulation running too quickly resulting in dropping incoming data packets from the network. 
  This will be seen as error messages in the terminal window.  
  Reduce the number of ticks to simulate for each quantum by specifying the following command line option `-Q <n>`, 
  where `<n>` is the number of ticks (default value = 10000).  
  Example: `-Q 10`


### System Configuration

| System Component        | Setting
|:------------------------|:----------------------------------------
| Device                  | SSE-310-MPS3
| Clock                   | 32 MHz
| Heap                    | 64 kB (configured in regions_V2M_MPS3_SSE_310.h file)
| Stack (MSP)             | 1 kB (configured in regions_V2M_MPS3_SSE_310.h file)

**STDIO** is routed to USART0

### CMSIS-Driver mapping

| CMSIS-Driver | Peripheral
|:-------------|:----------
| ETH_MAC0     | Ethernet LAN91C111
| ETH_PHY0     | Ethernet LAN91C111
| USART0       | USART0
