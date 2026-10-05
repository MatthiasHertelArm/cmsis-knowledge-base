---
id: "spec-package-components-element-component-bundle"
type: "concept"
domain: "pack"
title: "/package/components element: Component Bundle"
summary: "In case multiple inter-dependent components that belong to the same Cclass form part of a solution, these can be grouped into a bundle."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

In case multiple inter-dependent components that belong to the same **Cclass** form part of a solution, these can be grouped
into a _bundle_. A component bundle is a named set of components that must share identical attributes for **Cvendor** and 
**Cclass** by introducing the attribute **Cbundle,** which becomes a mandatory part of the component ID. If the attribute **Cvendor**
is not specified in the **bundle** element, the value is inherited from the pack level **vendor** element.

The attributes **Cvendor,** **Cclass,** **Cbundle** as well as **Cversion** are inherited by all **component** elements within a **bundle** section.
Only the **Cversion** attribute can be redefined in the **component** elements.

Components of the same **Cclass** belonging to a different **Cbundle** shall not be selected concurrently. In this way bundles ensure
interoperability across multiple components and restrict the mix and match of components within a **Cclass.**
