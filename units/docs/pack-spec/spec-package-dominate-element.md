---
id: "spec-package-dominate-element"
type: "concept"
domain: "pack"
title: "/package/dominate element"
summary: "The element_dominate specifies that the Pack contains one or more device, API, or component that overrules other packs that contain identical named device, API, or component."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_dominate.html"
license: "Apache-2.0"
mode: "V"
---

The element_dominate specifies that the Pack contains one or more device, API, or component that overrules
other packs that contain identical named device, API, or component.

This attribute is useful for framing packs that:
  - Contain **certified** software components which should overrule software components with identical name of other packs.
  - Contain new device definitions of devices that were previously defined in different packs.



**Example:**
```
<package>
  ...
  <dominate info="CMSIS-Core, RTOS2, RTX5, Event Recorder, C Library certified for Cortex-M3"/>
  ...
</package>
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| package | element_package |  |  |
| Attributes | Description | Type | Use |
| info | Descriptive text that explains the reason for the overwrite using dominate. | xs:string | required |
