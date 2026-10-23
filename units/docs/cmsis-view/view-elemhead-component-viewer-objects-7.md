---
id: "view-elemhead-component-viewer-objects-7"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/objects/object/out/.../item}"
summary: "Outputs a single line. Child elements create a display block [+] in the \\cviewer. The \\attr{property} and \\attr{value} can consist of ASCII characters and format specifiers."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Outputs a single line. Child elements create a display block [+] in the \cviewer.
The \attr{property} and \attr{value} can consist of ASCII characters and format specifiers.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<out>` | elem_out |  |  |
| \refelem{elem_listout,list} | elem_listout |  |  |
| `<item>` | elem_item (self reference) |  |  |
| Attributes | Description | Type | Use |
| property | Shown in the **Property** column of the \cviewer window. Use specifiers to format the output. | xs:string | optional |
| value | Shown in the **Value** column of the \cviewer window. Use specifiers to format the output. | xs:string | optional |
| info | Descriptive text, comment. Shown when hovered over the item in the \cviewer window. | xs:string | optional |
| cond | Conditional execution: element is executed when expression result is not `0`. Default value is `1`. | xs:string | optional |
| bold | Output in the **Value** column is displayed in **bold** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |
| alert | Output in the **Value** column is displayed in **red** when expression result is not `0`. Default value is `0`. See also alert_bold. | xs:string | optional |
| Child Element | Description | Type | Occurrence |
| `<item>` | Output a single line. An \elem{item} in an \elem{item} creates a tree structure in \cviewer. | ItemType | 0..* |
| \refelem{elem_listout,list} | Read complex variables, arrays, or linked lists. Walk through `<readlist>` arrays. | ListType | 0..* |
| \spref{elem_print,print} | Use different output formats for single line output lines. See print_spec. | PrintType | 0..* |


 
**Example:**
```
<object>
  <out name="System and Threads">                       <!-- Window title -->
    <item property="System">                            <!-- Creates a group item for the following items -->
      
      <item property="SystemTimer" cond="__Symbol_exists (&quot;os_active_TCB&quot;)">    <!-- small group -->
        <item property="Tick Timer" value="%T[((float) clockrate / 1000)] mSec" />         
      </item>
        // The "SystemTimer" property is only created when the condition is true,
        // that is when the user symbol "os_active_TCB" exists. Otherwise
        // the property is not created and any nested statements are skipped.
  
      <read name="USB_Desc"  type="uint8_t" symbol="usb_desc" size="128" const="1" />
        ...
      <item property="USB_Desc" value="%U[USB_Desc]" />
        // The property value will show a Keil-USB descriptor using the format -
        // { length, type, "descriptor_name" }, e.g. { 10, 3, "Keil" }.
 
    </item>
  </out>
</object>
```
