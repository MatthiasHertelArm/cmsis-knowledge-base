---
id: "view-elemhead-component-viewer"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer}"
summary: "The element \\elem{component_viewer} provides the outermost frame of the description. All elements are described within this scope."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The element \elem{component_viewer} provides the outermost frame of the description. All elements are described within this scope.



| Parent Element | Element Chain |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| root | Document root |  |  |  |  |  |  |
| Attributes | Description | Type | Use |  |  |  |  |
| xmlns:xs | Specifies the underlying XML schema to which the SCVD schema is compliant. Has to be set to: `"http://www.w3.org/2001/XMLSchema-instance"`. | xs:decimal | required |  |  |  |  |
| xs:noNamespaceSchemaLocation | Specifies the file name of the SCVD Schema: `"Component_Viewer.xsd"`. | xs:string | required |  |  |  |  |
| schemaVersion | Specifies the compliant SCVD schema version (for example, `"1.1"`). | xs:string | required |  |  |  |  |
| Child Elements | Description | Type | Occurrence |  |  |  |  |
| `<component>` | Name of the component and version of this SCVD file. | ComponentsType | 0..1 |  |  |  |  |
| `<typedefs>` | Group element for one or more `<typedef>` elements. | TypedefsType | 0..1 | `<objects>` | Group element for one or more `<object>` elements. | ObjectsType | 0..1 |
| `<events>` | Group element for one or more `<event>` elements. | EventsType | 0..1 |  |  |  |  |



**Example:**
```
<?xml version="1.0" encoding="utf-8"?>
 
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance "xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  
  <component name="MyView" version="0.0.1"/>    <!-- name and version of the component  -->
  
  <typedefs>
    <typedef  name="MyType"                    size="8"  info="This is MyType with 2 members">
      <member name="hi"      type="uint32_t" offset="0"  info="member hi"/>
      <member name="low"     type="uint32_t" offset="4"  info="member low"/>
    </typedef>
  </typedefs>
  
  <objects>
    <object name="MyObject">
      <read name="MySymbol" type="MyType" symbol="mysymbol" const="0"/>
  
      <out name="MyObjectView">
        <item property="MyObject">
          <item property="Low" value="%x[MySymbol.low]"/>
          <item property="Hi"  value="%d[MySymbol.hi]"/>
        </item>
      </out>
    </object>
  </objects>
  
</component_viewer>
```
