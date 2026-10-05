---
id: "spec-package-components-element-3"
type: "concept"
domain: "pack"
title: "/package/components element: "
summary: "The build environment shall generate a C/C++ header file with the name Pre_Include\\<Cclass>\\<component>.h from the selected component and add this file to the command line as a pre-include file for the build of all modules of this component."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The build environment shall generate a C/C++ header file with the name **Pre_Include_\`<Cclass>`_\`<component>`.h**
from the selected component and add this file to the command line as a pre-include file for the build of all modules of this component.
The same is done for each component containing a "Pre_Include_Local_Component_h" element.
Note: files shall be generated into the RTE/\`<target>` subdirectory.

```
<component Cclass="Other" Cgroup="Alpha" ...>
  <Pre_Include_Local_Component_h>
    // enabling local pre include
    #define Local_Component_Alpha 1
  </Pre_Include_Local_Component_h>
</component>

```

results in .../RTE/target_1/Pre_Include_Other_Alpha.h:
```
    // enabling local pre include
    #define Local_Component_Alpha 1
```

No need to explicitly include this file as it is automatically added as pre-include into the build for all modules of component Other:Alpha.
