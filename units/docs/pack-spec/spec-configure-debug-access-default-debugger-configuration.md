---
id: "spec-configure-debug-access-default-debugger-configuration"
type: "concept"
domain: "pack"
title: "Configure debug access: Default debugger configuration"
summary: "To simplify the debugger configuration in an IDE the <debugconfig> element can be used to specify the default working debugger configuration that should be used as a starting point until the user explicitely makes project-specific changes."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_setup_access.html"
license: "Apache-2.0"
mode: "V"
---

To simplify the debugger configuration in an IDE the `<debugconfig>` element can be used to specify the default working debugger configuration that should be used as a starting point until the user explicitely makes project-specific changes.

For example the code below specifies SWD interface as default one with debug clock 5MHz. The debug port supports switching between SWD and JTAG debug protocols.

```
<devices>
  <family Dfamily="LPC54000 Series" Dvendor="NXP:11">
    <debugconfig default="swd" clock="5000000" swj="true"/>
    ...
  </family>
</devices>
```

Using `<debug>` it is also possible to specify the default reset type to be used. See dbg_debug for details.
