---
id: "mcuboot-image-tool-vid-cid-calculation"
type: "concept"
domain: "boot-update"
title: "Image tool: VID/CID Calculation"
summary: "VID and CID are generated using UUIDv5 (SHA-1). VID: Generated using the standard DNS namespace: VID = UUIDv5(NAMESPACE_DNS, VID_String)"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/imgtool.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md#vid-cid-calculation"
license: "Apache-2.0"
mode: "V"
---

VID and CID are generated using UUIDv5 (SHA-1).   
VID: Generated using the standard DNS namespace:   
`VID = UUIDv5(NAMESPACE_DNS, VID_String)`

where `NAMESPACE_DNS = 6ba7b810-9dad-11d1-80b4-00c04fd430c8`.   

CID: When VID is available, the generated 16-byte VID UUID is used as the namespace:     
`CID = UUIDv5(VID_UUID, CID_String)`

### [UUIDv5 calculation](#UUIDv5-calculation):
```
SHA1(Namespace_UUID || UTF-8(Name))
        ↓
Take first 16 bytes
        ↓
Set UUID version = 5 and RFC 4122 variant
        ↓
16-byte UUID
```   
The resulting 16-byte VID and CID are stored directly as the payload of the UUID_VID and UUID_CID TLVs.
If VID/CID is already provided in raw UUID or 32-character hexadecimal format, it is directly converted to 16 bytes without UUIDv5 calculation
