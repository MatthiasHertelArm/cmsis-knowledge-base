---
id: "view-value-output-d-x-t-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%d, \\%x, \\%T format specifier"
summary: "The following example shows how to output integer values using: - \\%d for decimal number format. - \\%x for hexadecimal number format. - \\%T for number format that depends on the data type."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example shows how to output integer values using:
 - **\%d** for decimal number format.
 - **\%x** for hexadecimal number format.
 - **\%T** for number format that depends on the data type.

**Example**

C source file:
```
  uint8_t   cval   = 1;
  uint16_t  sval   = 0x2;
  uint32_t  ival   = 0x46;
  uint64_t  llval  = 0xFF12001612LL;
  
  int8_t    scval  = 1;
  int16_t   ssval  = -2;
  int32_t   sival  = 46;
  int64_t   sllval = -6899123456;
  
  float     fval   = 3.14156;
  double    dval   = 15300.6711123;
```

SCVD file:
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>
 
  <objects>
    <object name="MyProgram">
      <read name="c_value"     type="uint8_t"  symbol="cval"               />
      <read name="s_value"     type="uint16_t" symbol="sval"               />
      <read name="i_value"     type="uint32_t" symbol="ival"               />
      <read name="ll_value"    type="uint64_t" symbol="llval"              />
 
      <read name="sc_value"    type="int8_t"   symbol="scval"               />
      <read name="ss_value"    type="int16_t"  symbol="ssval"               />
      <read name="si_value"    type="int32_t"  symbol="sival"               />
      <read name="sll_value"   type="int64_t"  symbol="sllval"              />
 
      <read name="f_value"     type="float"    symbol="fval"                />
      <read name="d_value"     type="double"   symbol="dval"                />
 
      <out name="MyProgram">
        <item property="Unsigned integer format %%d"
              value="cval=%d[c_value] | sval=%d[s_value] | ival=%d[i_value] | llval=%d[ll_value]" />
        <item property="Unsigned integer format %%x"
              value="cval=%x[c_value] | sval=%x[s_value] | ival=%x[i_value] | llval=%x[ll_value]" />
        <item property="Unsigned integer format  %%T"
              value="cval=%T[c_value] | sval=%T[s_value] | ival=%T[i_value] | llval=%T[ll_value] " />
  
        <item property="Signed integer format %%d"
              value="scval=%d[sc_value] | ssval=%d[ss_value] | sival=%d[si_value] | sllval=%d[sll_value]" />
        <item property="Signed integer format %%x"
              value="scval=%x[sc_value] | ssval=%x[ss_value] | sival=%x[si_value] | sllval=%x[sll_value]" />
        <item property="Signed integer format %%T"
              value="scval=%T[sc_value] | ssval=%T[ss_value] | sival=%T[si_value] | sllval=%T[sll_value] " />
  
        <item property="Floating point format %%d"
              value="fval=%d[f_value] | dval=%d[d_value]" />
        <item property="Floating point format %%x"
              value="fval=%x[f_value] | dval=%x[d_value]" />
        <item property="Floating point format %%T"
              value="fval=%T[f_value] | dval=%T[d_value]" />
      </out>
    <object>
  </objects>
 
</component_viewer>
```

Output:
" "Output of \%d, \%x, \%T format specifiers"
