---
id: "view-elemhead-component-viewer-objects-2"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/.../calc}"
summary: "Execute calculations using scvd_expression."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Execute calculations using scvd_expression.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<object>` | elem_object |  |  |
| \refelem{elem_list,list} | elem_list |  |  |
| Attributes | Description | Type | Use |
| cond | Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | xs:string | optional |
| Body | Description | Type | Use |
| text | scvd_expression that are calculated. No XML-comments are allowed in this section. | xs:string | optional |



**Example:**
```
    <object name="MyCalculations">
       <var  name="y"  type="int32_t" value="0"  />
       <var  name="z"  type="int32_t" value="0"  />
 
       <calc>
         y = 1;
         z = 1;
       </calc>
 
       <calc cond="z != 0" >
         z = (z == 1) ? 100 : 200;
         y = z / 4;
       </calc>
   
    <object>
```
