---
id: "view-value-output-dynamic-output-formats"
type: "concept"
domain: "trace"
title: "Value output: Examples / Dynamic output formats"
summary: "The following example shows how to dynamically change the output format of an <item> element using a child element."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example shows how to dynamically change the output format of an `<item>` element 
using a 
 child element.

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
          <item>
		    <print cond="MyFirstSymbol.hi &lt;= 100" property="Hi  [hex]"   value="%x[MyFirstSymbol.hi]"  info="Show HEX value of 'mysymbol.hi' bold="1" alert="1" />
            <print cond="MyFirstSymbol.hi &gt; 100"  property="Hi  [dec]"   value="%d[MyFirstSymbol.hi]"  info="Show decimal value of 'mysymbol.hi'" />
		  </item>

          <item property="Low [dec]"   value="%d[MyFirstSymbol.low]" info="Show decimal value of 'mysymbol.low'" />
          <item property="Low [hex]"   value="%x[MyFirstSymbol.low]" info="Show HEX value of 'mysymbol.low'" />
        </item>
      </out>
    </object>   
  </objects>
 
</component_viewer>
```

**Output**

Depending on the values, the item "Hi" is displayed as:
  - "Hi [hex]" and hex formant with **bold** and alert color red when the value is <= 100
  - "Hi [dec]" and decimal format when the value is > 100

" "Dynamic output format changes"
