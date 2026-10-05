---
id: "spec-package-devices-element-package-devices"
type: "concept"
domain: "pack"
title: "/package/devices element: /package/devices"
summary: "Group level containing device family descriptions. A package can contain only one element \\elem{devices}. The group is not mandatory."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_devices_pg.html"
license: "Apache-2.0"
mode: "V"
---

Group level containing device family descriptions. A package can contain only one element \elem{devices}.
The group is not mandatory.

**Example**
```
<package>
  ...
  <devices>
    ...
  </devices>
  ...
</package>

```

\n



| Parents | Element Chain |  |  |
|---|---|---|---|
| package | /package |  |  |
| Child Elements | Description | Type | Occurrence |
| family | Device family group. Define all properties that are in common to devices of a family. | complexType | 1..* |



\delim
