---
id: "view-elemhead-component-viewer-objects-8"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/out/.../item/print}"
summary: "print_spec are supported using the \" \" element. It works as child element of <item> \"item\" and allows conditional output formats."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

print_spec are supported using the "
" element. It works as child element of `<item>` "item" and allows conditional 
output formats.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<item>` | elem_item |  |  |
| Attributes | Description | Type | Use |
| cond | Conditional execution: element is executed when expression result is not `0`. If executed all consecutive " " elements are skipped. Default value is `1`. | xs:string | required |
| property | Shown in the **Property** column of the \cviewer window. Use specifiers to format the output. | xs:string | required |
| value | Shown in the **Value** column of the \cviewer window. Use specifiers to format the output. | xs:string | required |
| bold | Output in the **Value** column is displayed in **bold** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |
| alert | Output in the **Value** column is displayed in **red** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |


 
**Example:**
```
<object>
  <out name="FreeRTOS RTOS">
    <item property="Running Task" value="" cond="xSchedulerRunning">
       <item property="h: %x[pxCurrentTCB] %t[Running_TCB.pcTaskName]" value="">
       <item property="Stack Top"   value="%x[Running_TCB.pxTopOfStack]" />
       <item>
          <print cond="Running_TCB.StackOverflow == 0" property="Stack Available" value="%d[Running_TCB.StackAvailable] bytes"/>
          <print cond="Running_TCB.StackOverflow != 0" property="Stack Overflow"  value="%d[Running_TCB.StackAvailable] bytes" bold="1" alert="1"/>
       </item>
    </item>
  </out>
</object>
```
