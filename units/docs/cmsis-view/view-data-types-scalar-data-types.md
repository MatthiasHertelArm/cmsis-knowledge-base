---
id: "view-data-types-scalar-data-types"
type: "concept"
domain: "trace"
title: "Data types: Scalar Data Types"
summary: "The following scalar data types are supported and can be used in <read>, <typedef>, and <var> elements. <read> and <var> also support arrays based on scalar data types."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The following scalar data types are supported and can be used in `<read>`, `<typedef>`, and `<var>` elements.
`<read>` and `<var>` also support arrays based on scalar data types.

Table with supported scalar types:

 Data Type  | Description
------------|----------------------------------------------------------------------
 uint8_t    | unsigned char (8-bit)
 int8_t     | signed char (8-bit)
 uint16_t   | unsigned short (16-bit)
 int16_t    | signed short (16-bit)
 uint32_t   | unsigned int (32-bit)
 int32_t    | signed int (32-bit)
 uint64_t   | unsigned long long (64-bit)
 int64_t    | signed long long (64-bit)
 float      | single precision floating number (32-bit)
 double     | double precision floating number (64-bit)

**Code** **Example**
```
<read name="main"        type="uint8_t"     symbol="main"    size="64"    const="1"  />
<var  name="ObjSum"      type="uint32_t"                                  value="0"  />
<var  name="i"           type="int32_t"                                   value="0"  />       <!-- helper -->
  
<!-- sum up object code bytes starting from main() with the given size in <read main>: -->
<list name="i" start="0" limit="main._count" >
   <calc>
      ObjSum += main[i];
   </calc>
</list>
```
