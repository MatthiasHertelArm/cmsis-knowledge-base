---
id: "view-elemhead-component-viewer-objects-9"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/out/.../list}"
summary: "\\elemhead{component_viewer/objects/object/out/.../list}"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Walk through \elem{readlist} arrays.

**Note:**
This element is different from elem_list.

 


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<out>` | elem_out |  |  |
| `<item>` | elem_item |  |  |
| \refelem{elem_listout,list} | elem_listout |  |  |
| Attributes | Description | Type | Use |
| name | Name of the list. Can be used in scvd_expression. Must be of type `int`. | xs:string | required |
| start | Starting value. | xs:string | required |
| limit | The end value is `limit-1`. If `limit=<0`, then the list is skipped. Cannot be used with \attr{while} in the same \elem{list} element. | xs:string | optional |
| while | Specifies the next value for iterations. When using \attr{while}, iteration does not start if `start==0`. Cannot be used with \attr{limit} in the same \elem{list} element. | xs:string | optional |
| cond | Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| `<item>` | Output a line. | ItemType | 0..* |
| \refelem{elem_listout,list} | Read complex variables, arrays, or linked lists. Walk through `<readlist>` arrays. | ListType | 0..* |


 
**Example:**
```
<object>
  <out>
    <list name="ListX" start="Threads:TCB[i].OS_MUCB" while="Threads:MCB(m).p_mlnk">  // walk through pointer lists
  </out>
</object>
```
