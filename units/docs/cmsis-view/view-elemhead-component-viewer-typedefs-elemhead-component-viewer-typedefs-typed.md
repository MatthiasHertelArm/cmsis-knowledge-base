---
id: "view-elemhead-component-viewer-typedefs-elemhead-component-viewer-typedefs-typed"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/typedefs}: \\elemhead{component_viewer/typedefs/typedef}"
summary: "does not accept complex data types. Is this a bug in UV or intentional?"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

does not accept complex data types.  Is this a bug in UV or intentional?

Define complex data types that may be used in `<read>` and `<readlist>` elements.  This data type definition is used
to read information from the target memory of the application. Optionally it may include also \spref{elem_var,var} elements that
create temporary helper variables for calculations at the debugger level.


explain that complex_data_type referenced via a  `<typedef>` pointer using  `type=\"*&lt;name of typedef>\"`.  | 




  | 
    Parent Element | 
    Element Chain | 
  

  | 
    typedefs | 
    elem_typedefs | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Define the name of a data type. This name is used in `<read>` and `<readlist>` elements. | 
    xs:anySimpleType | 
    required | 
  

  | 
    size | 
    Expression that specifies the size (in `[Bytes]`) to read from target memory. | 
    xs:anySimpleType | 
    optional | 
  

  | 
    info | 
    Descriptive text with additional information (comment). | 
    xs:anySimpleType | 
    optional | 
  

  | 
    import | 
    Name of a symbol in the user application which is loaded into the debugger. The underlaying data type of this symbol is used to:
 - recalculate the value of the \attr{size} of this `<typedef>` element.
 - for \refelem{elem_member,member} elements with no explicit \attr{offset}, the offset value of matching \refelem{elem_member,member} is set. If the \refelem{elem_member,member} is not part of the symbol in the user application the \attr{offset} value is set to `-1`. __Offset_of can be used to check this value.

**Example:** Use the data type information of symbol **tcb** in source module **main.c**
```
<typedef name="tcb_type" size="12"  import="main.c/tcb">  // size is recalculated from symbol tcb
  <member name="type"  type="uint8_t"  offset="0"/>       // offset not updated, because specified
  <member name="name"  type="uint8_t"  size="16" />       // offset updated, because not specified
</typedef>
```
     | 
    xs:string | 
    optional | 
  

  | 
    Child Element | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    \spref{elem_member,member} | 
    Name of a member variable in target memory. | 
    MemberType | 
    0..* | 
  

  | 
    \spref{elem_var,var} | 
    Temporary variables for local calculations in component viewer. | 
    VarType | 
    0..* | 
  


 

** Example: Using **var****

```
  <typedefs>
    
    <!-- Structure reflecting an array -->
    <typedef name="TypeArray1" size="8">
      <member name="type_ref"      type="uint32_t"   offset="0"  info="Pointer to array"/>
      <member name="id1"           type="uint8_t"    offset="4"  info="Type ID"/>
      <member name="attr"          type="uint8_t"    offset="5"  info="Type Attribute"/>
      <var    name="idx"           type="uint32_t"               info="Index in array"/>
    </typedef>
    
    <!-- Helper variables for Stack-usage calculation -->
    <typedef name="TypeArray2" size="8">
       <var   name="XcurSP"        type="uint32_t"   value="0"/>
       <var   name="bSimpleStk"    type="int32_t"/>
     </typedef>
    
  </typedefs>
```

**Example: Using **read****

**main.c file**
```
struct MyComp_info_t {
  int version;             // component version
  int channels;            // number of communication channels available
  int buffersize;          // size of the communication buffer
};
 
struct MyComp_info_t MyComp_info;
 
void MyComp_initialize (void) {
  MyComp_info.version = 3;                         // Set information
  MyComp_info.channels = 1;
  MyComp_info.buffersize = sizeof(MyComp_data.buf);
}
```

***.SCVD file**
```
<objects>
  <object name="MyComponent">
    <read name="MyComp_info" type="MyComp_info" symbol="MyComp_info"/>
    <out name="MyComponent Overview">
      <item property="Generic">
        <item property="Version"            value="%d[MyComp_info.version]"/>
        <item property="Channels"           value="%d[MyComp_info.channels]"/>
        <item property="Max. Transmit Size" value="%d[MyComp_info.buffersize] Bytes"/>
      </item>
    </out>
  </object>
</objects>
```


**Example: Using **import****

**main.c File**
```
// Configuration defines 
#define CONDITION_0             (0)
#define CONFIG_NAME_SZ   (8)
#define CONDITION_1             (0)
 
// Example structure 
typedef struct {
  uint32_t Member_0;
  uint32_t Member_1;
} StructA_t;
 
// Structure of variable size 
typedef struct {
  uint32_t Var_0;
 
  #if (CONDITION_0 == 1)
   StructA_t Sample0;        // Conditionally included 
  #endif
  StructA_t Sample1;
  char Name[CONFIG_NAME_SZ];  // Variable size: size defined by CONFIG_NAME_SZ (default: CONFIG_NAME_SZ=4) 
 
  #if (CONDITION_1 == 1)
    uint32_t Var_1;           // Conditionally included 
  #endif
  uint32_t Var_2;
 
} StructOfVarSz;
StructofVarSz MyVarStruct;
```

**SCVD File**
```
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyView2" version="0.0.1"/>    <!-- name and version of the component  -->
  
  <typedefs>
    <typedef name="StructOfVarSz" size="32" import="MyVarStruct" info="Structure Of Variable Size">
      <member name="Var_0" type="uint32_t" offset="0" info="Variable 0 (always present)"/>
  
      <!-- StructA_t inlined -->
      <member name="Sample0_Member0" type="uint32_t"    info="Structure Sample0, member Member0 (included conditionally)"/>
      <member name="Sample0_Member1" type="uint32_t"    info="Structure Sample0, member Member1 (included conditionally)"/>
  
      <!-- StructA_t inlined -->
      <member name="Sample1_Member0" type="uint16_t"    info="Structure Sample1, member Member0 (always included)"/>
      <member name="Sample1_Member1" type="uint16_t"    info="Structure Sample1, member Member1 (always included)"/>
  
      <member name="Name"  type="uint8_t"  size="4"     info="Array Name, actual size=CONFIG_NAME_SZ"/>
      <member name="Var_1" type="uint32_t"              info="Variable 1 (conditionally included)"/>
      <member name="Var_2" type="uint32_t"              info="Variable 2 (always present)"/>
   </typedef>
  
   // After import (taking "Configuration defines" into account) the typedef above would have the following properties:
  
  <typedef name="StructOfVarSz" size="28" import="MyVarStruct" info="Size is updated">
    <member name="Var_0" type="uint32_t" offset="0" info=""/>
   
    <!-- StructA_t inlined -->
    <member name="Sample0_Member0" type="uint32_t" offset="-1" info=""/>
    <member name="Sample0_Member1" type="uint32_t" offset="-1" info=""/>
    
    <!-- StructA_t inlined -->
    <member name="Sample1_Member0" type="uint16_t" offset="4"  info=""/>
    <member name="Sample1_Member1" type="uint16_t" offset="8"  info=""/>
     
    <member name="Name"  type="uint8_t"  size="8"  offset="12" info="Size is updated (if possible)"/>
    <member name="Var_1" type="uint32_t"           offset="-1" info=""/>
    <member name="Var_2" type="uint32_t"           offset="20" info=""/>
  </typedef>
  
</component_viewer>
```
