---
id: "svd-device-cpu-element"
type: "concept"
domain: "pack"
title: "/device/cpu element"
summary: "The CPU section describes the processor included in the microcontroller device. This section is mandatory if the SVD file is used to generate the device header file."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_cpu.html"
license: "Apache-2.0"
mode: "V"
---

The CPU section describes the processor included in the microcontroller device.
This section is mandatory if the SVD file is used to generate the device header file.

**Example**
```
<device>
  ...
  <cpu>
    <name>CM7</name>
    <revision>r0p0</revision>
    <endian>little</endian>
    <mpuPresent>true</mpuPresent>
    <!-- has double precision FPU -->
    <fpuPresent>true</fpuPresent>
    <fpuDP>true</fpuDP>
    <!-- has instruction and data cache -->
    <icachePresent>true</icachePresent>
    <dcachePresent>true</dcachePresent>
    <!-- has no instruction nor data tighly coupled memory -->
    <itcmPresent>false</itcmPresent>
    <dtcmPresent>false</dtcmPresent>
    <nvicPrioBits>4</nvicPrioBits>
    <vendorSystickConfig>false</vendorSystickConfig>
  </cpu>
  ...
<device>
```

This example describes a device based on a `Cortex-M7` core of HW revision `r0p0`,
with fixed `little` endian memory scheme, including `Memory Protection Unit` and
`double precision hardware Floating Point Unit`. It has a `data cache` and no `instruction` nor
a tightly coupled memory. The Nested Vectored Interrupt Controller uses `4` bits
to configure the priority of an interrupt. It is equipped with the standard System Tick Timer as defined by Arm.


**/device/cpu**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| device | /device |  |  |
| Child Elements | Description | Type | Occurrence |
| name | The predefined tokens are: - `CM0`: Arm Cortex-M0 - `CM0PLUS`: Arm Cortex-M0+ - `CM0+`: Arm Cortex-M0+ - `CM1`: Arm Cortex-M1 - `CM3`: Arm Cortex-M3 - `CM4`: Arm Cortex-M4 - `CM7`: Arm Cortex-M7 - `CM23`: Arm Cortex-M23 - `CM33`: Arm Cortex-M33 - `CM35P`: Arm Cortex-M35P - `CM52`: Arm Cortex-M52 - `CM55`: Arm Cortex-M55 - `CM85`: Arm Cortex-M85 - `SC000`: Arm Secure Core SC000 - `SC300`: Arm Secure Core SC300 - `CA5`: Arm Cortex-A5 - `CA7`: Arm Cortex-A7 - `CA8`: Arm Cortex-A8 - `CA9`: Arm Cortex-A9 - `CA15`: Arm Cortex-A15 - `CA17`: Arm Cortex-A17 - `CA53`: Arm Cortex-A53 - `CA57`: Arm Cortex-A57 - `CA72`: Arm Cortex-A72 - `SMC1`: Arm China STAR-MC1 - `other`: other processor architectures | cpuNameType | 1..1 |
| revision | Define the HW revision of the processor. The version format is `r N p M ` (N,M = [0 - 99]). | revisionType | 1..1 |
| endian | Define the endianness of the processor being one of: - `little`: little endian memory (least significant byte gets allocated at the lowest address). - `big`: byte invariant big endian data organization (most significant byte gets allocated at the lowest address). - `selectable`: little and big endian are configurable for the device and become active after the next reset. - `other`: the endianness is neither little nor big endian. | endianType | 1..1 |
| mpuPresent | Indicate whether the processor is equipped with a memory protection unit (MPU). This tag is either set to `true` or `false`, `1` or `0`. | boolean | 0..1 |
| fpuPresent | Indicate whether the processor is equipped with a hardware floating point unit (FPU). Cortex-M4, Cortex-M7, Cortex-M33 and Cortex-M35P are the only available Cortex-M processor with an optional FPU. This tag is either set to `true` or `false`, `1` or `0`. | boolean | 0..1 |
| fpuDP | Indicate whether the processor is equipped with a double precision floating point unit. This element is valid only when \tagem{fpuPresent} is set to `true`. Cortex-M7 processors and above can have a double precision floating point unit. | boolean | 0..1 |
| dspPresent | Indicates whether the processor implements the optional SIMD DSP extensions (DSP). Cortex-M33 and Cortex-M35P are the only available Cortex-M processor with an optional DSP extension. For ARMv7M SIMD DSP extensions are a mandatory part of Cortex-M4 and Cortex-M7. This tag is either set to `true` or `false`, `1` or `0`. This element is mandatory for Cortex-M33 processors and higher with optional SIMD DSP instruction set. | boolean | 0..1 |
| icachePresent | Indicate whether the processor has an instruction cache. Note: only relevant for Arm Cortex-M7 and above. | boolean | 0..1 |
| dcachePresent | Indicate whether the processor has a data cache. Note: only relevant for Arm Cortex-M7 and above. | boolean | 0..1 |
| itcmPresent | Indicate whether the processor has an instruction tightly coupled memory. Note: Note: only relevant for Arm Cortex-M7 and above. | boolean | 0..1 |
| dtcmPresent | Indicate whether the processor has a data tightly coupled memory. Note: only for Arm Cortex-M7 and above. | boolean | 0..1 |
| vtorPresent | Indicate whether the Vector Table Offset Register (VTOR) is implemented in Cortex-M0+ based devices. This tag is either set to `true` or `false`, `1` or `0`. If not specified, then VTOR is assumed to be present. | boolean | 0..1 |
| nvicPrioBits | Define the number of bits available in the Nested Vectored Interrupt Controller (NVIC) for configuring priority. | scaledNonNegativeInteger | 1..1 |
| vendorSystickConfig | Indicate whether the processor implements a vendor-specific System Tick Timer. If `false`, then the Arm-defined System Tick Timer is available. If `true`, then a vendor-specific System Tick Timer must be implemented. This tag is either set to `true` or `false`, `1` or `0`. | boolean | 1..1 |
| deviceNumInterrupts | Add `1` to the highest interrupt number and specify this number in here. You can start to enumerate interrupts from `0`. Gaps might exist between interrupts. For example, you have defined interrupts with the numbers `1`, `2`, and `8`. Add `9 :(8+1)` into this field. | scaledNonNegativeInteger | 0..1 |
| sauNumRegions | Indicate the amount of regions in the Security Attribution Unit (SAU). If the value is greater than zero, then the device has a SAU and the number indicates the maximum amount of available address regions. | scaledNonNegativeInteger | 0..1 |
| `<sauRegionsConfig>` | If the Secure Attribution Unit is preconfigured by HW or Firmware, then the settings are described here. | SauRegionsConfigType | 0..1 |



\delim_sec
