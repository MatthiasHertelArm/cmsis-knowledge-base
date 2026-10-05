---
id: "spec-package-boards-element-package-boards-board-memory"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/memory"
summary: "This element specifies memory regions that boards may add. Memory types are predefined and can be selected."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies memory regions that boards may add. Memory types are predefined and can be selected.

**Example**
```
</package>
  ...
  <boards>
    <board vendor="MyVendor" name="Board-1">
      <memory name="SRAM-EX" access="rwx" start="0x40000000" size="0x200000"/>
      <algorithm name="Flash/SRAM-EX.flm" start="0x40000000" size="0x200000" style="Keil"/>
    </board>
  </boards>
  ...
</package>
```

\n



| Parents | Element Chain |  |  |
|---|---|---|---|
| board | element_board |  |  |
| Attributes | Description | Type | Use |
| Pname | Processor identifier. This attribute **is for boards that use devices with multiple processors**. Only alphabetical characters, decimal digits, '-' and '_' are allowed. | RestrictedString | optional |
| name | Unique name of the memory to be used in conjunction with access . If a memory with the same name is already defined in a parent scope, the parent one is extended/overwritten. Backward compatibility: If no 'name' attribute is given but 'id' attribute is still present, the given 'id' attribute is used as the 'name'. | xs:string | optional |
| access | Access permission of the memory. See MemoryAccessTypeString for details. | MemoryAccessTypeString | optional |
| start | Base address of the memory using a hexadecimal value. | NonNegativeInteger | required |
| size | Size of the memory in bytes using a hexadecimal value. | NonNegativeInteger | required |
| default | Indicates a general purpose memory region, that does not require any special considerations (access speed, remapping, protection, etc.). If `true`, then the memory region will be used by the linker. Default value is `false`. | xs:boolean | optional |
| startup | If `true`, the startup code of the application will be placed into this memory region. Default value is `false`. | xs:boolean | optional |
| uninit | If `true`, the memory region shall be kept uninitialized (i.e. keep the memory state as is). Default value is `false`. | xs:boolean | optional |
| alias | Reference to another memory (by it's 'name' attribute) which shares the same physical memory. Some physical memory is made accessible via different addresses, for example, cached vs. non-cached accesses. This avoids the impression that the device has twice as much memory available. | xs:string | optional |
