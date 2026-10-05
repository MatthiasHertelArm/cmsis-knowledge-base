---
id: "spec-package-components-element-2"
type: "concept"
domain: "pack"
title: "/package/components element: "
summary: "The build environment shall generate a C/C++ header file with the name Pre_Include_Global.h from all selected components and add this file to the command line as a pre-include file for the build of all modules in the project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The build environment shall generate a C/C++ header file with the name **Pre_Include_Global.h** from all selected components and add this file
to the command line as a pre-include file for the build of all modules in the project.
Note: the file shall be generated into the RTE/\`<target>` subdirectory.

```
<component Cclass="Other" Cgroup="Alpha" ...>
  <Pre_Include_Global_h>
    // enabling global pre include
    #define GLOBAL_Component_Alpha 0x4
  </Pre_Include_Global_h>
</component>

<component Cclass="Other" Cgroup="Beta" ...>
  <Pre_Include_Global_h>
    // enabling global pre include
    #define GLOBAL_Component_Beta 0x8
  </Pre_Include_Global_h>
</component>
```

results in .../RTE/target_1/Pre_Include_Global.h:
```
    // enabling global pre include
    #define GLOBAL_Component_Alpha 0x4
    // enabling global pre include
    #define GLOBAL_Component_Beta 0x8
```

No need to explicitly include this file as it is automatically added as pre-include into the build for all modules.
