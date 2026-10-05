---
id: "spec-technical-background-references"
type: "concept"
domain: "pack"
title: "Technical background: References"
summary: "Software components can reference other software components (either within the same pack or in other packs) using conditions:"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

Software components can reference other software components (either within the same pack or in other packs) using conditions:



A condition describes dependencies on:
- a specific device
- a certain processor
- tool attributes
- the presence of other components (pcak internal or external)

Conditions can be used to ensure that specific software components are either present in the system or can prevent that
illegal combinations of software components are chosen by the user.

Conditions are used to define **AND/OR** rules that make components conditional and therefore only available under
certain circumstances, for example for specific devices or processors. Conditions are also used to express dependencies
between software components.

Each condition has an **id** that is unique within the scope of a the PDSC file. An id can be referenced in the
`condition` attribute of components, APIs, examples, files and other conditions.
All attributes set in a **accept**, **require**, or **deny** element must resolve to true for the element to become
true. A condition becomes true when:
- At least one **accept** element is true, _AND_
- all **require** elements are true, _AND_
- no **deny** element is true.

If a condition resolves to false during processing, the respective element will be ignored.
