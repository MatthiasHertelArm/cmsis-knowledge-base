---
id: "svd-device-cpu-element-device-cpu-sauregionsconfig-element"
type: "concept"
domain: "pack"
title: "/device/cpu element: /device/cpu/sauRegionsConfig element"
summary: "Set the configuration for the Secure Attribution Unit (SAU) when they are preconfigured by HW or Firmware."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_cpu.html"
license: "Apache-2.0"
mode: "V"
---

Set the configuration for the Secure Attribution Unit (SAU) when they are preconfigured by HW or Firmware.

**Example**
```
<device>
  ...
  <sauRegionsConfig protectionWhenDisabled="n">
    <region>
      ...
    </region>
    ...
    <region>
      ...
    </region>
  </sauRegionsConfig>
  ...
</device>
```

The example defines two Secure Attribution Units, which are enabled by default. When
the SAU regions are disabled, the protection level is non-secure (`n`).


**/device/cpu/sauRegionsConfig**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<cpu>` | elem_cpu |  |  |
| Attributes | Description | Type | Use |
| enabled | Specify whether the Secure Attribution Units are enabled. The following values can be used: `true`,`false`,`1`, and `0`. | xs:boolean | optional |
| protectionWhenDisabled | Set the protection mode for disabled regions. When the complete SAU is disabled, the whole memory is treated either `"s"`=secure or `"n"`=non-secure. This value is inherited by the \tagem{region} element. Refer to element ` ` for details and predefined values. | xs:string | optional |
| Child Elements | Description | Type | Occurrence |
| `<region>` | Group to configure SAU regions. | xs:string | 0..* |



\delim_sec
