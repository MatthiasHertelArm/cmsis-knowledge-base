---
id: "view-elemhead-component-viewer-events-e"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/events/event/../print}"
summary: "print_spec are supported using the \" \" element. It works as child element of <event> and allows conditional output."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

print_spec are supported using the "
" element. It works as child element of `<event>` and allows conditional output.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<event>` | elem_event |  |  |
| Attributes | Description | Type | Use |
| cond | Conditional execution: element is executed when expression result is not `0`. If executed all consecutive " " elements are skipped. Default value is `1`. | xs:string | required |
| property | Shown in the **Property** column of the \erecorder window. Use specifiers to format the output. | xs:string | required |
| value | Shown in the **Value** column of the \erecorder window. Use specifiers to format the output. | xs:string | required |
| bold | Output in the **Value** column is displayed in **bold** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |
| alert | Output in the **Value** column is displayed in **red** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |


 
**Example:**
On "ShowNetAddress" event print IP address in different format depending whether it is IPv4 or IPv6 network.
```
<event id="15 + 0xD100" level="Op" property="ShowNetAddress" info="Display IP address and port number">
 <print cond="!(val1 & 0x1)"       property="ShowNetAddress" value="ip=%I[val1, NetAddr:addr], port=%d[val1, NetAddr:port]"/>
 <print cond=" (val1 & 0x1)"       property="ShowNetAddress" value="ip=%J[val1, NetAddr:addr], port=%d[val1, NetAddr:port]"/>
</event>
```
