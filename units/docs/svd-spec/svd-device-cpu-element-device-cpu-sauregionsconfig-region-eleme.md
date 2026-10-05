---
id: "svd-device-cpu-element-device-cpu-sauregionsconfig-region-eleme"
type: "concept"
domain: "pack"
title: "/device/cpu element: /device/cpu/sauRegionsConfig/region element"
summary: "Define the regions of the Secure Attribution Unit (SAU). The protection level is inherited from the attribute \\tagem{protectionWhenDisabled} of the enclosing element <sauRegionsConfig>."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_cpu.html"
license: "Apache-2.0"
mode: "V"
---

Define the regions of the Secure Attribution Unit (SAU). The protection level is inherited from the attribute
\tagem{protectionWhenDisabled} of the enclosing element `<sauRegionsConfig>`.

**Example:**
```
<sauRegionsConfig>
  <region name="SAU1">
    <base>0x10001000</base>
    <limit>0x10005000</limit>
    <access>n</access>
  </region>
  <region enabled="false" name="SAU2">
    <base>0x10006000</base>
    <limit>0x10008000</limit>
    <access>c</access>
  </region>
</sauRegionsConfig>
```

The example defines two secure regions with the names **SAU1** and **SAU2.**
SAU1 has the address boundries `0x10001000` and `0x10005000`. The region has non-secure access rights.
SAU2 has the address boundries `0x10006000` and `0x10008000`. The region has secure callable access rights.


**/device/cpu/sauRegionsConfig/region**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| sauRegionsConfig | elem_sauRegionsConfig |  |  |
| Attributes | Description | Type | Use |
| enabled | Specify whether the Secure Attribution Units are enabled. The following values can be used: `true` and `false`, or `1` and `0`. Default value is `true`. | xs:boolean | optional |
| name | Identifiy the region with a name. | xs:string | optional |
| Child Elements | Description | Type | Occurrence |
| base | Base address of the region. | scaledNonNegativeInteger | 1..1 |
| limit | Limit address of the region. | scaledNonNegativeInteger | 1..1 |
| access | Use one of the following predefined values to define the acces type of a region: \n - `n` : non-secure \n - `c` : secure callable | xs:string | 1..1 |
