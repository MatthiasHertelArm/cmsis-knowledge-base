---
id: "view-elemhead-component-viewer-objects-elemhead-component-viewer-objects-object"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects}: \\elemhead{component_viewer/objects/object}"
summary: "Define variables, calculations, and the viewer output for a software component."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define variables, calculations, and the viewer output for a software component.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<objects>` | elem_objects |  |  |
| Attributes | Description | Type | Use |
| name | Name of the object (this name is used to open the view) | xs:string | required |
| Child Element | Description | Type | Occurrence |
| \refelem{elem_var,var} | Define temporary variables. | VarType | 0..* |
| \spref{elem_calc,calc} | Calculate temporary variables. | CalcType | 0..* |
| \spref{elem_list,list} | Iterate a loop (for or while construct). | ListTypeO | 0..* |
| \spref{elem_read,read} | Read scalar variables or arrays from application program. | ReadType | 0..* |
| \spref{elem_readlist,readlist} | Read a list of structured variables (arrays or linked list) from application program. | ReadlistType | 0..* |
| \spref{elem_out,out} | Generate output for this object. | OutType | 0..* |
