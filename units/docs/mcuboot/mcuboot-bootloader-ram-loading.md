---
id: "mcuboot-bootloader-ram-loading"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image slots / RAM loading"
summary: "In ram-load mode the slots are equal. Like the direct-xip mode, this mode also selects the newest image by reading the image version numbers in the image headers."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#ram-loading"
license: "Apache-2.0"
mode: "V"
---

_Part of: Image slots_

In ram-load mode the slots are equal. Like the direct-xip mode, this mode
also selects the newest image by reading the image version numbers in the image
headers. But instead of executing it in place, the newest image is copied to the
RAM for execution. The load address, the location in RAM where the image is
copied to, is stored in the image header. The ram-load upgrade mode can be
useful when there is no internal flash in the SoC, but there is a big enough
internal RAM to hold the images. Usually in this case the images are stored
in an external storage device. Execution from external storage has some
drawbacks (lower execution speed, image is exposed to attacks) therefore the
image is always copied to the internal RAM before the authentication and
execution. Ram-load mode requires the image to be built to be executed from
the RAM address range instead of the storage device address range. If
ram-load is enabled then platform must define the following parameters:

```c
#define IMAGE_EXECUTABLE_RAM_START    <area_base_addr>
#define IMAGE_EXECUTABLE_RAM_SIZE     <area_size_in_bytes>
```

For multiple image load if multiple ram regions are used platform must define
the `MULTIPLE_EXECUTABLE_RAM_REGIONS` flag instead and implement the following
function:

```c
int boot_get_image_exec_ram_info(uint32_t image_id,
                                 uint32_t *exec_ram_start,
                                 uint32_t *exec_ram_size)
```

When ram-load is enabled, the `--load-addr <addr>` option of the `imgtool`
script must also be used when signing the images. This option set the `RAM_LOAD`
flag in the image header which indicates that the image should be loaded to the
RAM and also set the load address in the image header.

When the encryption option is enabled (`MCUBOOT_ENC_IMAGES`) along with ram-load
the image is checked for encryption. If the image is not encrypted, RAM loading
happens as described above. If the image is encrypted, it is copied in RAM at
the provided address and then decrypted. Finally, the decrypted image is
authenticated in RAM and executed.

Similar to direct-xip, ram-load mode also supports a "revert" mechanism.
This mechanism works in the same manner as the direct-xip revert mechanism does,
so please see the [corresponding section](#direct-xip-ram-load-revert) for
more details.
