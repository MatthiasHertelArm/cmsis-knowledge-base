---
id: "view-elemhead-component-viewer-objects-4"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/.../read}"
summary: "Read values of scalar variables or arrays from application program that runs in the target system. A redefinition of a \\elem{read} element is not permitted and creates an error."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Read values of scalar variables or arrays from application program that runs in the target system. A redefinition of a \elem{read} element is not permitted and creates an error.

\elem{read} manages a \elem{member} variable with the following name:
  - **_name_._count**  &mdash;         number of element in an array `(0 .. n-1)`.

Refer to predefined_variable.



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    `<object>` | 
    elem_object | 
  

  | 
    \refelem{elem_list,list} | 
    elem_list | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of variable. Can be used in scvd_expression. | 
    xs:string | 
    required | 
  

  | 
    type | 
    Data type read from memory, following types are possible:
          - scalar_data_type, no pointers allowed
          - complex_data_type defined with `<typedef>` | 
    xs:string | 
    required | 
  

  | 
    size | 
    Is an scvd_expression representing the array size or the number of values to read from target. 
        The maximum array size is limited to `512`. Default value is `1`.  | 
    xs:string | 
    optional | 
  

  | 
    symbol | 
    Symbol name to access memory in the target system which is used to calculate a memory address.
    xs:string | 
    optional | 
  

  | 
    offset | 
    Offset to the \attr{symbol} address. If no \attr{symbol} is not specified, then it is the memory address. Default value is `0`.
    xs:string | 
    optional | 
  

  | 
    const | 
    Variables with \attr{const} set to `"1"` are constants that are read only once after debugger start. Default value is `0`.
    xs:int | 
    optional | 
  

  | 
    info | 
    Descriptive text with additional information (comment). | 
    xs:string | 
    optional | 
  

  | 
    cond | 
    Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | 
    xs:string | 
    optional | 
  

  | 
    endian | 
    Endianness for scalar data types. `endian="L"` &mdash; little endian. `endian="B"` &mdash; big endian. Default is **automatic.**
    xs:string | 
    optional | 
  



**Example:**
```
<objects>
  <object name="MyObject">
    <read name="MySymbol" type="MyType" symbol="mysymbol" const="0"/>
  </object>
  
  <object name="Threads">
    <read name="main"           type="uint8_t"     symbol="main"          size="64"    const="1" /> 
    <read name="szText"         type="uint8_t"     symbol="szText"        size="64"    const="1"   cond="0"   info="ignored because of condition" />
    <read name="My_TCB"         type="Thread_CB"      offset="adr_os_idle_TCB + 4"   info="indirect address via offset-expression" />
  
    <list name="Tsk_List">
      <read name="cur_tsk"     type="uint32_t"    symbol="os_tsk"        offset="0"      info="index current running task"    />
      <read name="next_tsk"    type="uint32_t"    symbol="os_tsk"        offset="4"      info="index task that will run next" />
    </list>
  <object>
<objects>
```
 add example with _count.
