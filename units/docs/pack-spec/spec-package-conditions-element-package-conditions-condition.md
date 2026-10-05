---
id: "spec-package-conditions-element-package-conditions-condition"
type: "concept"
domain: "pack"
title: "/package/conditions element: /package/conditions/condition"
summary: "Conditions are dependency rules that can apply to elements such as a component or file. Other elements can refer to a rule using their attribute condition, which links to the attribute id of a condition."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/conditions_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html"
license: "Apache-2.0"
mode: "V"
---

Conditions are dependency rules that can apply to elements such as a component or file.
Other elements can refer to a rule using their attribute **condition,** which links to the attribute **id** of a condition.
If a condition resolves to `false`, then the component or file description is ignored.



| Parent | Chain |  |  |
|---|---|---|---|
| conditions | /package/conditions |  |  |
| Attributes | Description | Type | Use |
| id | Condition identifier which is unique within a software pack. The condition identifier is referenced by other elements with the attribute **condition. | xs:string | required |
| Child Elements | Description | Type | Occurrence |
| description | Descriptive (comment) text that explains the condition in an human readable way. | xs:string | 0..1 |
| accept 1 | At least one accept must be true to signal a true for the complete condition (**OR-Rule) | FilterType | 0..* |
| require 1 | All require must be true to signal a true for the complete condition (**AND-Rule). | FilterType | 0..* |
| deny 1 | If one deny is true the complete condition becomes false. This element overrules require and accept (**AND-NOT-Rule). | FilterType | 0..* |


**Note:**
**1:** At least one of these elements must be present in any condition.
