---
id: "view-value-output-alert-and-bold-output"
type: "concept"
domain: "trace"
title: "Value output: Examples / alert and bold output"
summary: "The following example shows how to emphasis output with the bold and alert attribute of the <item> element."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example shows how to emphasis output with the **bold** and **alert** attribute of the
`<item>` element.

***.SCVD file**
```
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyFirstComponent" version="0.0.1"/>    <!-- name and version of the component  -->

  <typedefs>
    <typedef  name="MyGeneralType" info="This is MyType with 2 members" size="12">
      <member name="hi"   type="uint32_t"  offset="0"  info="member 'mysymbol.hi'"/>
      <member name="low"  type="uint32_t"  offset="4"  info="member 'mysymbol.low'"/>
    </typedef>
  </typedefs>

  <objects>
    <object name="MyFirstObject">
      <read name="MyFirstSymbol" type="MyGeneralType" symbol="mysymbol" const="0"/>
     
      <out name="My First Viewer">                                                        <!-- Window name -->
        <item property="Square of numbers [0..30]">                                       <!-- Property entry -->
                                                                                          <!-- These items extend the entry above -->
          <item property="Hi  [dec]"   value="%d[MyFirstSymbol.hi]"  info="Show decimal value of 'mysymbol.hi'"  alert="MyFirstSymbol.hi &gt; 100" />
          <item property="Low [dec]"   value="%d[MyFirstSymbol.low]" info="Show decimal value of 'mysymbol.low'" bold="MyFirstSymbol.low &lt; 20"/>
          <item property="Hi  [hex]"   value="%x[MyFirstSymbol.hi]"  info="Show HEX value of 'mysymbol.hi'"/>
          <item property="Low [hex]"   value="%x[MyFirstSymbol.low]" info="Show HEX value of 'mysymbol.low'"     bold="1" alert="1"/>
        </item>
      </out>
    </object>   
  </objects>
 
</component_viewer>
```

**Output**

Depending on the values, the item:
  - "Hi [dec]" is displayed in alert color red when the value is > 100
  - "Low [dec]" is displayed in **bold** when the value is < 20

The value "Low [hex]" is shown in red and **bold** (both attributes are set).

" "Output using bold and alert attributes"
