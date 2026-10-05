---
id: "view-elemhead-component-viewer-objects-5"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/.../readlist}"
summary: "Read a list of structured elements from application program memory in the target system. This list can be used in expressions or <out> elements. The structured element is based on a data type that is defined with <typedef>."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Read a list of structured elements from application program memory in the target system. This list can be used in expressions or `<out>` elements.
The structured element is based on a data type that is defined with `<typedef>`. This `<typedef>` may contain temporary variables defined with `<var>` that are used for calculations 
(temporary variables are not read from the target system).

The individual data type elements of the \elem{readlist} are referenced using **_name[index].member_**.  
\elem{readlist} manages two predefined member variables with the following names:
  - **_name_._count**       &mdash; number of list items. Used as index limit, valid index values are: `(0 .. number-1)`.
  - **_name[index]_._addr** &mdash; start address of the list item that was read from target memory.

The attribute \attr{symbol} together with \attr{offset} specifies the start address in target memory of the list. When attribute \attr{based}:
  - is not specified or false (`based="1"`) the target memory content is interpreted as a structured element.
  - is true (`based="1"`) the target memory content is interpreted as pointer to a structured element.

\elem{readlist} is able to read:
  - an array where the \attr{count} specifies the number of items read from the array.
  - linked list elements where the \attr{next} specifies the link pointer.

\elem{readlist} can be used multiple times to add list items. The attribute `init="1"` clears the list and any list items collected on previous \elem{readlist} calls is discarded.
  
**Note:** The maximum number of list items is limited to `1024`.



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    `<object>` | 
    /component_viewer/objects/object | 
  

  | 
    \refelem{elem_list,list} | 
    /component_viewer/objects/object/.../list | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of the list variable for usage in scvd_expression. | 
    xs:string | 
    required | 
  

  | 
    type | 
    A scalar data type or complex data type defined with `<typedef>`.
    xs:string | 
    required | 
  

  | 
    count | 
    Number of list items to read from an array. Default value is `1`.  | 
    xs:string | 
    optional | 
  

  | 
    next | 
    Name of a _member_ element in the list that is used as next pointer. This is used to read a linked list. \elem{readlist} stops reading on a `NULL` pointer.
        The maximum number of list items is limited to `1024`.  | 
    xs:string | 
    optional | 
  

  | 
    symbol | 
    Symbol name used to calculate the memory address in the target system.
    xs:string | 
    optional | 
  

  | 
    offset | 
    Offset to the memory address specified with \attr{symbol} address. If \attr{symbol} is not specified it is the memory address. 
        Default value is `0`.
    xs:string | 
    optional | 
  

  | 
    const | 
    When `const="1"` the memory is read when the `<object>` is created the first time. Default value is `0`.
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
    init | 
    When `init="1"` previous read items in the list are discarded. Default value is `0`. | 
    xs:boolean | 
    optional | 
  

  | 
    based | 
    When `based="1"` the \attr{symbol} and \attr{offset} specifies a pointer (or pointer array). Default value is `0`. | 
    xs:boolean | 
    optional | 
  



**Example**

C source file:
```
typedef struct _MyList {
	struct _MyList    *nextL;
	uint32_t          valueL;
	char              *nameL;
} MyList;
 
__USED MyList ValueC     = { NULL,    50, "List Value C" };
__USED MyList ValueB     = { &ValueC, 12, "List Value B" };
__USED MyList ValueA     = { &ValueB,  4, "List Value A" };
__USED MyList *ListStart = &ValueA;
 
__USED MyList ValueArray[3] = { { NULL,  10, "Value[0]" }, 
                                { NULL,  20, "Value[1]" }, 
                                { NULL,  30, "Value[2]" },  };
 																
__USED MyList *pArray[5] = { &ValueA, &ValueB, &ValueC, &ValueArray[0], &ValueArray[1] };
```

The data type of the list is defined with `<typedef>`. The `<var>` element is a variable used to store a string.
```
  <typedefs>
    <typedef name="MyList" size="12" >
      <member name="nextL"   type="*MyList"  offset="0" />
      <member name="valueL"  type="uint32_t" offset="4" />
      <member name="nameL"   type="uint32_t" offset="8" />
	  <var    name="nameS"   type="int8_t"   size="20"  />
    </typedef>
  </typedefs>
```

Read the linked list starting with **ValueA:**
```
<readlist name="MyListA" type="MyList" symbol="ValueA" next="nextL" />
```

Read the linked list starting with head pointer **ListStart:**
```
<readlist name="MyListB" type="MyList" symbol="ListStart" based="1" next="nextL" />
```

Clear a previous list and read **ValueA,** **ValueB,** and **ValueArray.**
```
<readlist name="MyListC" type="MyList" symbol="ValueA" init="1"                          /> 
<readlist name="MyListC" type="MyList" symbol="ValueB"                                   />
<readlist name="MyListC" type="MyList" symbol="ValueArray" count="__size_of(ValueArray)" />
```

Read the list based on the pointers stored in **pArray:**
```
<readlist name="MyListD" type="MyList" symbol="pArray" based="1" count="__size_of(pArray)" />
```

Read the **pArray** using `<read>` and read the list items addressed with pArray[1] and pArray[2].
```
<read name="pArray" type="*MyList" symbol="pArray" count="__size_of(pArray)" /> 
<readlist name="MyListE" type="MyList" offset="pArray[1]"  />
<readlist name="MyListE" type="MyList" offset="pArray[2]"  />
```
