---
id: "tfm-initial-attestation-service-integr-boot-loader-interface"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Boot loader interface"
summary: "It is recommended to have a secure boot loader in the boot chain, which is capable of measuring the runtime firmware components (calculates the hash value of firmware images) and provide other attributes of these (version, type, etc)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#boot-loader-interface"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

It is **recommended** to have a secure boot loader in the boot chain, which is
capable of measuring the runtime firmware components (calculates the hash value
of firmware images) and provide other attributes of these (version, type, etc).
If the used boot loader is not capable of sharing these information with the
runtime software then the `BOOT_DATA_AVAILABLE` compiler flag **must** be
set to OFF (see Related compile time options).

The shared data between boot loader and runtime software is TLV encoded. The
definition of TLV structure is described in `bl2/include/tfm_boot_status.h`.
The shared data is stored in a well known location in secure internal memory
and this is a contract between boot loader and runtime SW.

The structure of shared data must be the following:

-  At the beginning there must be a header: `struct shared_data_tlv_header`
   This contains a magic number and a size field which covers the entire size
   of the shared data area including this header.

```c

struct shared_data_tlv_header {
    uint16_t tlv_magic;
    uint16_t tlv_tot_len;
};
```
-  The header is followed by the entries which are composed from an
   entry header structure: `struct shared_data_tlv_entry` and the data. In
   the entry header there is a type and a length field. The `tlv_type` field
   identifies the consumer of the entry in the runtime software and specify the
   subtype of that data item. The `tlv_len` field covers the length of the
   data (not including the size of the entry header).

   After the entry header structure comes the actual data.

```c

struct shared_data_tlv_entry {
    uint16_t tlv_type;
    uint16_t tlv_len;
};
```
-  Arbitrary number and size of data entry can be in the shared memory
   area.

The figure below gives an overview about the `tlv_type` field in the entry
header. The `tlv_type` is always composed from a major and a minor number.
Major number identifies the addressee in runtime software, which the data entry
is sent to. Minor number is used to encode more info about the data entry. The
actual definition of minor number could change per major number. In case of boot
status data, which is going to be processed by initial attestation service,
the minor number is split further to two part: `sw_module` and `claim`. The
`sw_module` identifies the SW component in the system which the data item
belongs to and the `claim` part identifies the exact type of the data.

`tlv_type` description::
```
|------------------------------------------------ |
|                  tlv_type (16 bits)             |
|-------------------------------------------------|
|   tlv_major(4 bits)   |   tlv_minor(12 bits)    |
|-------------------------------------------------|
| MAJOR_IAS   | sw_module(6 bits) | claim(6 bits) |
|-------------------------------------------------|
| MAJOR_CORE  |          TBD                      |
|-------------------------------------------------|
```
Overall structure of shared data::
```
---------------------------------------------------------------
| Magic number(uint16_t) | Shared data total length(uint16_t) |
---------------------------------------------------------------
| Major_type(4 bits) | Minor_type(12 bits) | Length(uint16_t) |
---------------------------------------------------------------
|                         Raw data                            |
---------------------------------------------------------------
|                              .                              |
|                              .                              |
|                              .                              |
---------------------------------------------------------------
| Major_type(4 bits) | Minor_type(12 bits) | Length(uint16_t) |
---------------------------------------------------------------
|                         Raw data                            |
---------------------------------------------------------------
```
