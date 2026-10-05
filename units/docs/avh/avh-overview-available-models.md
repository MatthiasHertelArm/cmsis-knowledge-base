---
id: "avh-overview-available-models"
type: "concept"
domain: "test"
title: "Overview: Available Models"
summary: "The Arm FVP simulation models build a subset of Arm Fast Models Fixed Virtual Platforms with extensions for armcmvp."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/main.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/main.md#available-models"
license: "Apache-2.0"
mode: "V"
---

The Arm FVP simulation models build a subset of
[Arm Fast Models Fixed Virtual Platforms](https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms)
with extensions for arm_cmvp.

The table below lists the available models:



| 
FVP Simulation Model Name         | Processor Cores    | Overview Description     | 

| 
FVP_Corstone_SSE-320      | Cortex-M85,
Ethos-U85,
Mali-C55    | [FVP for Arm Corstone SSE-320 Reference Guide](https://developer.arm.com/documentation/109760)   | 

| 
FVP_Corstone_SSE-315      | Cortex-M85,
Ethos-U65,
Mali-C55    | [FVP for Arm Corstone SSE-315 Reference Guide](https://developer.arm.com/documentation/109395)   | 

| 
FVP_Corstone_SSE-310_Ethos-U65    | Cortex-M85,
Ethos-U65    | [Arm Corstone SSE-310 FVP](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-310-FVP)   | 

| 
FVP_Corstone_SSE-310      | Cortex-M85
Ethos-U55    | [Arm Corstone SSE-310 FVP](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-310-FVP)     | 

| 
FVP_Corstone_SSE-300_Ethos-U65   | Cortex-M55,
Ethos-U65    | [Arm Corstone SSE-300 FVP](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-300-FVP)     | 

| 
FVP_Corstone_SSE-300_Ethos-U55   | Cortex-M55,
Ethos-U55    | [Arm Corstone SSE-300 FVP](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-300-FVP)     | 

| 
FVP_Corstone_SSE-300 | Cortex-M55        | [Arm Corstone SSE-300 FVP](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-300-FVP)     | 

| 
FVP_MPS2_Cortex-M85       | Cortex-M85 (2x)   | [FVP_MPS2_Cortex-M85 in FVP Reference Guide](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M85).

It is recommended to use Corstone-320/315/310 FVP models for Cortex-M85.     | 

| 
FVP_MPS2_Cortex-M55       | Cortex-M55 (2x)   | [FVP_MPS2_Cortex-M55 in FVP Reference Guide](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M55).

It is recommended to use Corstone-300 FVP models for Cortex-M55.     | 

| 
FVP_MPS2_Cortex-M52       | Cortex-M52 (2x)   | [FVP_MPS2_Cortex-M52 in FVP Reference Guide](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M52)   | 

| 
FVP_MPS2_Cortex-M35P      | Cortex-M35P (2x)  | [FVP_MPS2_Cortex-M35P in FVP Reference Guide](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M35P)  | 

| 
FVP_MPS2_Cortex-M33       | Cortex-M33 (2x)   | [ARM Cortex-M33 IoT Subsystem for V2M-MPS2+ (AppNote AN505)](https://developer.arm.com/documentation/dai0505)     | 

| 
FVP_MPS2_Cortex-M23       | Cortex-M23 (2x)   | [ARM Cortex-M23 IoT Subsystem for V2M-MPS2+ (AppNote AN519)](https://developer.arm.com/documentation/dai0519)     | 

| 
FVP_MPS2_Cortex-M7        | Cortex-M7         | [ARM Cortex-M7 SMM on V2M-MPS2 (AppNote AN399)](https://developer.arm.com/documentation/dai0386)     | 

| 
FVP_MPS2_Cortex-M4        | Cortex-M4         | [ARM Cortex-M4 SMM on V2M-MPS2 (AppNote AN386)](https://developer.arm.com/documentation/dai0386)     | 

| 
FVP_MPS2_Cortex-M3        | Cortex-M3         | [ARM Cortex-M3 SMM on V2M-MPS2 (AppNote AN385)](https://developer.arm.com/documentation/dai0385)     | 

| 
FVP_MPS2_Cortex-M0plus    | Cortex-M0+        | [ARM Cortex-M0+ SMM on V2M-MPS2 (AppNote AN383)](https://developer.arm.com/documentation/dai0383)    | 

| 
FVP_MPS2_Cortex-M0        | Cortex-M0         | [ARM Cortex-M0 SMM on V2M-MPS2 (AppNote AN382)](https://developer.arm.com/documentation/dai0382)     | 



> **Note**
> Arm FVPs are only available for Windows and Linux hosts. If you use macOS, a Docker-based approach helps you
> to run Arm FVPs on your machine. Refer to [FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac) to get started.
