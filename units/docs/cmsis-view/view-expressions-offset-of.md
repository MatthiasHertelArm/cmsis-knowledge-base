---
id: "view-expressions-offset-of"
type: "concept"
domain: "trace"
title: "Expressions: __Offset_of"
summary: "Get offset of type member - typedef_mem_name: Is the member name of a specified type and has the form typedef_name:typedef_member_name. Returns: The offset value of the specified typedef member."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

```
uint32_t __Offset_of (typedef_mem_name)
```
    Get offset of type member
- `typedef_mem_name`: Is the member name of a specified type and has the form _typedef_name:typedef_member_name_.
Returns:  The offset value of the specified typedef member.
 
The function returns the offset value of the specified typedef member. When using a `<typedef>` element with the _import_ attribute, __Offset_of 
returns for members that are defined in the SCVD file but not present in the compiled image the value -1.  The value -1 indicates that a member does not exist in the image.

**Example:** 
```
__Offset_of (Thread_CB:Task_ID)
```
