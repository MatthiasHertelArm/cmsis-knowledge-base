---
id: "mcuboot-bootloader-measured-boot-and-data-sharing"
type: "concept"
domain: "boot-update"
title: "Bootloader: Measured boot and data sharing"
summary: "MCUboot defines a mechanism for sharing boot status information (also known as measured boot) and an interface for sharing application specific information with the runtime software."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#measured-boot-and-data-sharing"
license: "Apache-2.0"
mode: "V"
---

MCUboot defines a mechanism for sharing boot status information (also known as
measured boot) and an interface for sharing application specific information
with the runtime software. If any of these are enabled the target must provide
a shared data area between the bootloader and runtime firmware and define the
following parameters:

```c
#define MCUBOOT_SHARED_DATA_BASE    <area_base_addr>
#define MCUBOOT_SHARED_DATA_SIZE    <area_size_in_bytes>
```

In the shared memory area all data entries are stored in a type-length-value
(TLV) format. Before adding the first data entry, the whole area is overwritten
with zeros and a TLV header is added at the beginning of the area during an
initialization phase. This TLV header contains a `tlv_magic` field with a value
of `SHARED_DATA_TLV_INFO_MAGIC` and a `tlv_tot_len` field which is indicating
the total length of shared TLV area including this header. The header is
followed by the the data TLV entries which are composed from a
`shared_data_tlv_entry` header and the data itself. In the data header there is
a `tlv_type` field which identifies the consumer of the entry (in the runtime
software) and specifies the subtype of that data item. More information about
the `tlv_type` field and data types can be found in the
`boot/bootutil/include/bootutil/boot_status.h` file. The type is followed by a
`tlv_len` field which indicates the size of the data entry in bytes, not
including the entry header. After this header structure comes the actual data.

```c
/** Shared data TLV header.  All fields in little endian. */
struct shared_data_tlv_header {
    uint16_t tlv_magic;
    uint16_t tlv_tot_len; /* size of whole TLV area (including this header) */
};

/** Shared data TLV entry header format. All fields in little endian. */
struct shared_data_tlv_entry {
    uint16_t tlv_type;
    uint16_t tlv_len; /* TLV data length (not including this header). */
};
```

The measured boot can be enabled with the `MCUBOOT_MEASURED_BOOT` config option.
When enabled, the `--boot_record` argument of the imgtool script must also be
used during the image signing process to add a BOOT_RECORD TLV to the image
manifest. This TLV contains the following attributes/measurements of the
image in CBOR encoded format:

  * Software type (role of the software component)
  * Software version
  * Signer ID (identifies the signing authority)
  * Measurement value (hash of the image)
  * Measurement type (algorithm used to calculate the measurement value)

The `sw_type` string that is passed as the `--boot_record` option's parameter
will be the value of the "Software type" attribute in the generated BOOT_RECORD
TLV. The target must also define the `MAX_BOOT_RECORD_SZ` macro which indicates
the maximum size of the CBOR encoded boot record in bytes.
During boot, MCUboot will look for these TLVs (in case of multiple images) in
the manifests of the active images (the latest and validated) and copy the CBOR
encoded binary data to the shared data area. Preserving all these image
attributes from the boot stage for use by later runtime services (such as an
attestation service) is known as a measured boot.

Setting the `MCUBOOT_DATA_SHARING` option enables the sharing of application
specific data using the same shared data area as for the measured boot. For
this, the target must provide a definition for the `boot_save_shared_data()`
function which is declared in `boot/bootutil/include/bootutil/boot_record.h`.
The `boot_add_data_to_shared_area()` function can be used for adding new TLV
entries to the shared data area. Alternatively, setting the
`MCUBOOT_DATA_SHARING_BOOTINFO` option will provide a default function for
this which saves information such as the maximum application size, bootloader
version (if available), running slot number, if recovery is part of MCUboot
and the signature type. Details of the TLVs for this information can be found
in `boot/bootutil/include/bootutil/boot_status.h` with `BLINFO_` prefixes.
