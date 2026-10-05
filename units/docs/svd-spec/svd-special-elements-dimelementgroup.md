---
id: "svd-special-elements-dimelementgroup"
type: "concept"
domain: "pack"
title: "Special Elements: dimElementGroup"
summary: "The elements below appear on various levels and can be used to define arrays and lists in the code. Single descriptions get duplicated automatically into an array or a list. The subsequent is true for all elements of type dimableIdentifierType."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_special.html"
license: "Apache-2.0"
mode: "V"
---

The elements below appear on various levels and can be used to define arrays and lists in the code.
Single descriptions get duplicated automatically into an array or a list.
The subsequent is true for all elements of type **dimableIdentifierType.**

 - To create arrays, use the placeholder _[%%s]_ at the end of a \tagem{name} and \tagem{displayName}.
   Do not define \tagem{dimIndex} in this case!
 - To create lists, use the placeholder _%%s_ anywhere within or at the end of a \tagem{name} and \tagem{displayName}.

**Note:**
Some of the \tagem{name} and \tagem{displayName} elements can use both placeholders (_[%%s]_, _%%s_), others just one.
Refer to `<peripheral>`, `<register>`, `<cluster>`, and `<field>` for details.




| Parent Element | Element Chain |  |  |
|---|---|---|---|
| ` ` | elem_peripheral |  |  |
| `<register>` | elem_register |  |  |
| `<cluster>` | elem_cluster |  |  |
| `<field>` | elem_field |  |  |
| Grouped Elements | Description | Type | Occurrence |
| dim | Defines the number of elements in an array or list. | scaledNonNegativeInteger | 1..1 |
| dimIncrement | Specify the address increment between two neighboring array or list members in the address map. | scaledNonNegativeInteger | 1..1 |
| dimIndex | Specify the strings that substitue the placeholder %%s within \tagem{name} and \tagem{displayName}. By default, \tagem{dimIndex} is a value starting with `0`. \n**Remark:** Do not define \tagem{dimIndex} when using the placeholder [%%s] in \tagem{name} or \tagem{displayName}. | dimIndexType | 0..1 |
| dimName | Specify the name of the C-type structure. If not defined, then the entry in the \tagem{name} element is used. | identifierType | 0..1 |
| `<dimArrayIndex>` | Grouping element to create enumerations in the header file. | dimArrayIndexType | 0..1 |



**Example:**
The examples creates definitions for registers.

```xml
...
<register>
    <dim>6</dim>
    <dimIncrement>4</dimIncrement>
    <dimIndex>A,B,C,D,E,Z</dimIndex>
    <name>GPIO_%s_CTRL</name>
...
</register>
```

The code above generates the list:
=> GPIO_A_CTRL, GPIO_B_CTRL, GPIO_C_CTRL, GPIO_D_CTRL, GPIO_E_CTRL, GPIO_Z_CTRL


```xml
...
<register>
    <dim>4</dim>
    <dimIncrement>4</dimIncrement>
    <dimIndex>3-6</dimIndex>
    <name>IRQ%s</name>
...
</register>
```

The example above generates the list: => IRQ3, IRQ4, IRQ5, IRQ6


```xml
...
<register>
    <dim>4</dim>
    <dimIncrement>4</dimIncrement>
    <name>MyArr[%s]</name>
...
</register>
```

The example above generates the array: => MyArr[4]

\delim_sec


### /device/peripherals/peripheral/.../dimArrayIndex element


This information is used for generating an _enum_ in the device header file. The debugger may use
this information to display the identifier string as well as the description. Just like symbolic constants
making source code more readable, the system view in the debugger becomes more instructive.

**Example:**
```
...
<dimArrayIndex>
  <headerEnumName>FSMC_EnumArray</headerEnumName>
  <enumeratedValue>
    <name>UART0</name>
    <description>UART0 Peripheral</description>
    <value>0</value>
  </enumeratedValue>
  <enumeratedValue>
    <name>TIMER0</name>
    <description>TIMER0 Peripheral</description>
    <value>1</value>
  </enumeratedValue>
</dimArrayIndex>
...
```


**/device/peripherals/peripheral/.../dimArrayIndex**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| ` ` | elem_peripheral |  |  |
| `<register>` | elem_register |  |  |
| `<cluster>` | elem_cluster |  |  |
| Child Elements | Description | Type | Occurrence |
| headerEnumName | Specify the base name of enumerations. Overwrites the hierarchical enumeration type in the device header file. User is responsible for uniqueness across description. The headerfile generator uses the name of a peripheral or cluster as the base name for enumeration types. If \tagem{headerEnumName} element is specfied, then this string is used. | identifierType | 0..1 |
| `<enumeratedValue>` | Specify the values contained in the enumeration. | enumeratedValueType | 1..* |



\delim_sec
