---
id: "spec-package-devices-family-element-package-devices-family-flashinfo"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../flashinfo"
summary: "Specify Flash information that the debugger can use to erase and program Flash memories without the use of target RAM based Flash download algorithms."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify Flash information that the debugger can use to erase and program Flash memories without the use
of target RAM based Flash download algorithms.

The **FlashInit,** **FlashUninit,** **FlashEraseSector,** **FlashEraseChip,** and **FlashProgramPage**
debug sequences require one or more corresponding **flashinfo** regions, which supply the memory layout
and programming parameters. Defining one or more **flashinfo** regions does not require any flash debug sequences to be
implemented. If no flash debug sequences are implemented, the debugger ignores all such regions.


The child elements \`<block>` and \`<gap>` describe the memory and programming layout of a flash device:
- The first child element has the base address `start`.
- The base address of the second child element is `start` incremented by the size of the first child element.
- The base address of all following child elements calculates respectively.

Flash information can be defined on various levels. Multiple \`<flashinfo>` elements are possible. If the memory range is
identical, the one on the lower level takes precedence. Overlap of Flash information ranges is not allowed.

**Example**
```
<device ... >
  ...
    <!-- Flash Device Info for this device -->
    <flashinfo name="Internal Flash 1" start="0" pagesize="64" emptyval="0xFFFFFFFF" filler="0xFFFFFFFF" ptime="3000" etime="3000" Pname="Cortex-M23">
      <block count="1"  size="0x100" arg="0"/>
      <block count="10" size="0x100" arg="0"/>
      <gap size="0x10000" />
      <block count="2"  size="0x100" arg="1" />
    </flashinfo>
  ...
</device>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| name | Name of the specified flash device. | xs:string | required |
| start | Base address of the specified flash device as mapped into target memory system. | NonNegativeInteger | required |
| pagesize | Programming page size. | NonNegativeInteger | required |
| blankval | Expected memory value for unprogrammed address ranges (64-bit value). The access size used to read back programmed memory defines the number of least significant bytes of this value that are compared. Defaults to `0xFFFFFFFFFFFFFFFF` if not specified. | NonNegativeInteger | optional |
| filler | Value that a debugger uses to fill the remainder of a programming page (64-bit value). The access size used in FlashWriteBuffer defines the number of least significant bytes of this value to write. Defaults to `0xFFFFFFFFFFFFFFFF` if not specified. | NonNegativeInteger | optional |
| ptime | Timeout in milliseconds for programming a page. Defaults to `100` if not specified. | xs:unsignedInt | optional |
| etime | Timeout in milliseconds for erasing a sector. Defaults to `300` if not specified. | xs:unsignedInt | optional |
| Pname | Processor identifier. This attribute **is mandatory for devices that embed multiple processors that require different algorithms**. Only alphabetical characters, decimal digits, '-' and '_' are allowed. | RestrictedString | optional |
| Child Elements | Description | Type | Occurrence |
| block | element_flashblock | FlashInfoBlockType | 0..* |
| gap | element_flashgap | FlashInfoGapType | 0..* |



\delim
