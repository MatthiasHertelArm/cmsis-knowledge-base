---
id: "view-value-output-i-j-m-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%I, \\%J, %M format specifier"
summary: "The following example show how to output MAC and IP addresses that are part of the user application using: - \\%I for IPv4 address information, example: 192.168.150.99."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example show how to output MAC and IP addresses that are part of the user application using:
 - **\%I** for IPv4 address information, example: `192.168.150.99`.
 - **\%J** for IPv6 address information, example: `2a00:ee0:d::13`
 - **\%M** for MAC address information, example: `1E-30-6C-A2-45-5F`

**C source file**
```
// \%I, \%J, %M Format Specifier
 uint8_t ip4_addr[4]  = {192, 168, 0, 1};
 uint8_t ip6_addr[16] = {0xFF, 0x02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x02 };
 uint8_t mac_addr[6]  = {0x5F, 0x3F, 0x10, 0xFF, 0x00, 0x01};
```

<***.SCVD file**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
   
  <objects>
    <object name="MyProgram">
<!-- \%I, \%J, %M Format Specifier -->	  
      <read name="IPv4val"     type="uint8_t" symbol="ip4_addr"  size="4"    />
      <read name="IPv6val"     type="uint8_t" symbol="ip6_addr"  size="16"   />
      <read name="MAC_val"     type="uint8_t" symbol="mac_addr"  size="6"    />
  
      <out name="MyProgram">
<!-- \%I, \%J, %M Format Specifier -->	  
        <item property="IPv4 format %%I"  value="ip4_addr=%I[IPv4val]" />
        <item property="IPv6 format %%J"  value="ip6_addr=%J[IPv6val]" />
        <item property="MAC format %%M"   value="mac_addr=%M[MAC_val]" />

      </out>
    </object>
  </objects>
   
</component_viewer>
```

**Output**
" "Output of \%I, \%J, %M format specifiers"
