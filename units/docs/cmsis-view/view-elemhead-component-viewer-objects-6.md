---
id: "view-elemhead-component-viewer-objects-6"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/out}"
summary: "\\elemhead{component_viewer/objects/object/out}"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define the output for an object.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<object>` | elem_object |  |  |
| Attributes | Description | Type | Use |
| name | The name used for menu titles and window titles of the \cviewer. | xs:string | optional |
| value | Is the assigned value. | xs:string | optional |
| type | Value type. One of the data_type. | xs:string | optional |
| cond | Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| \spref{elem_item,item} | Output a line to the Component Viewer window. | ItemType | 0..* |
| \spref{elem_listout,list} | Iterate a loop (for or while construct). | ListType | 0..* |


 
**Example:**
```
    <object>
      <out name="System and Threads"  cond="__Symbol_exists ('os_active_TCB')">     <!-- Window title -->
        <item property="System" cond="__Symbol_exists ('os_active_TCB')">
          <item property="Tick Timer"                value="%T[((float) clockrate / 1000)] mSec" />
          <item property="Round Robin Timeout"       value="%T[((float) (rrobin &amp; 0xFFFF) * (float) clockrate / 1000)] mSec" />
  
          <item property="Test values" >
            <item property="__Running=%d[__Running]"               value="%t[__Running ? 'Yes' : 'No']" />
            <item property="__Symbol_exists ('os_active_TCB')"     value="%t[__Symbol_exists ('os_active_TCB') ? 'Yes' : 'No']" />
          </item>
        </item>
       </out>
    </object>
```
