---
id: "spec-package-components-element-component-files"
type: "concept"
domain: "pack"
title: "/package/components element: Component Files"
summary: "The files of a Software Component will be used in development tool-chains to build an application. Depending on the attributes, the files are handled differently: - Libraries, source, and header files without an attribute cannot be modified."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The files of a Software Component will be used in development tool-chains to build an application. Depending on the
attributes, the files are handled differently:
  - Libraries, source, and header files without an attribute cannot be modified. These files are stored in the folders of
    the Software Component and get directly included  from this location into the project.
  - Source and header files that have the attribute `"config"` are copied to the project so that they can be edited by the
    user and tailored to the needs of the application. If a Software Component allows multiple instances of files, they
    can be copied multiple times to a project and will get a suffix __\%Instance%_ (see Component_Instances). Please
    note that header files that are used with the attribute `"config"` need to be stored separately from other header files
    (for example in an extra directory) to avoid that due to the include path search order of the compiler, the unmodified
    header file in the pack repository is found first and used by the compiler (creating unexpected results).
  - Source and header files that have the attribute `"template"` can be added to a project manually by the user.

The following image shows the dependency between the attribute and the display in a development environment:

  "Display of files of a Software Component in development tools"
