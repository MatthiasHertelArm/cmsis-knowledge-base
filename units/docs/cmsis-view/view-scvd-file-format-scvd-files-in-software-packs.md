---
id: "view-scvd-file-format-scvd-files-in-software-packs"
type: "concept"
domain: "trace"
title: "SCVD file format: SCVD files in software packs"
summary: "Software components which are part of Software Packs may add related .SCVD files directly in the Package Description file (.pdsc) using the <file> element category other."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Software components which are part of Software Packs may add related *.SCVD files directly in the Package Description file (*.pdsc) using the `<file>` element category `other`.
In the *.pdsc file example below `Network.scvd` is added to the debugger when the component `:Network:Core` is selected. For details, refer to
**CMSIS-Pack - Pack Description (*.PDSC) Format**.

```
<component CClass="Network" Cgroup="Core">
  <files>
    <file category="library"  name="Network/Lib/ARM/Network.lib"/>
    <file category="other"    name="Network/Network.scvd"/>
  </files>
</component>
```
