---
id: "intr-peeking-inside-cmsis-packs-flash-algorithms"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: Flash Algorithms"
summary: "One breadcrumb of information that can be useful (and is how PyOCD uses the Pack file to flash chips) is the flash algorithm, which is specified in the top-level .pdsc file. The .pdsc format is detailed here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#flash-algorithms"
license: "CC-BY-SA-4.0"
mode: "V"
---

One breadcrumb of information that can be useful (and is how PyOCD uses the Pack
file to flash chips) is the flash algorithm, which is specified in the top-level
`*.pdsc` file. The `*.pdsc` format is detailed here:

<https://www.keil.com/pack/doc/CMSIS/Pack/html/packFormat.html>

The file contains many interesting pieces of information. One particularly useful
one is the Flash Algorithms used to program a piece of hardware. Look for a
section of the XML with the `<algorithm>` tag, for example:

_Note: I added the comments explaining each section_

```xml

<device Dname="ATSAMD21E15BU">


<processor Dcore="Cortex-M0+"
           Dendian="Little-endian"
           Dmpu="NO_MPU"
           Dfpu="NO_FPU"/>


<compile header="samd21b/include/sam.h" define="__SAMD21E15BU__"/>


<debug svd="samd21b/svd/ATSAMD21E15BU.svd"/>


<memory id="IROM1"
        start="0x00000000"
        size="0x8000"
        default="1"
        startup="1"/>
<memory id="IROM2" start="0x00400000" size="0x400"/>
<memory id="IRAM1" start="0x20000000" size="0x1000" default="1"/>


<algorithm name="samd21b/keil/Flash/ATSAMD21_32.FLM"
           start="0x00000000"
           size="0x00008000"
           default="1"/>
<algorithm name="samd21b/keil/Flash/ATSAMD21_32_EEPROM.FLM"
           start="0x00400000"
           size="0x00000400"
           default="1"/>
```
