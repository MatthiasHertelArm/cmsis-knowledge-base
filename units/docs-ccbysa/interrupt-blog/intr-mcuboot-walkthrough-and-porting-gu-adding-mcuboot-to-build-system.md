---
id: "intr-mcuboot-walkthrough-and-porting-gu-adding-mcuboot-to-build-system"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Porting MCUboot / Adding MCUboot to Build System"
summary: "The porting guide mentions we will need to call boot_go() from boot/bootutil/loader.c to determine the image to boot. Reading through the documentation bootutil is the \"library\" we will want to add to our bootloader."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#adding-mcuboot-to-build-system"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Porting MCUboot_

The porting guide mentions we will need to call `boot_go()` from `boot/bootutil/loader.c` to determine the image to boot. Reading through the documentation [bootutil](https://github.com/mcu-tools/mcuboot/tree/master/boot/bootutil) is the "library" we will want to add to our bootloader. Using CLI tools like `tree` and `ls` we can find this all lives in `boot/bootutil`

```
# tree boot/bootutil/
boot/bootutil/
├── include
│   └── bootutil
# [...]
└── src
# [...]
```

#### Add MCUboot bootutil sources and includes

As a starting point we can add those sources and the include directory to our build system:

```makefile
MCUBOOT_DIR := $(ROOT_DIR)/external/MCUboot/boot/bootutil
MCUBOOT_SRC_DIR := $(MCUBOOT_DIR)/src
MCUBOOT_INC_DIR := $(MCUBOOT_DIR)/include

MCUBOOT_SRC_FILES += \
  $(MCUBOOT_SRC_DIR)/boot_record.c \
  $(MCUBOOT_SRC_DIR)/bootutil_misc.c \
  $(MCUBOOT_SRC_DIR)/caps.c \
  $(MCUBOOT_SRC_DIR)/encrypted.c \
  $(MCUBOOT_SRC_DIR)/fault_injection_hardening.c \
  $(MCUBOOT_SRC_DIR)/fault_injection_hardening_delay_rng_mbedtls.c \
  $(MCUBOOT_SRC_DIR)/image_ec.c \
  $(MCUBOOT_SRC_DIR)/image_ec256.c \
  $(MCUBOOT_SRC_DIR)/image_ed25519.c \
  $(MCUBOOT_SRC_DIR)/image_rsa.c \
  $(MCUBOOT_SRC_DIR)/image_validate.c \
  $(MCUBOOT_SRC_DIR)/loader.c \
  $(MCUBOOT_SRC_DIR)/swap_misc.c \
  $(MCUBOOT_SRC_DIR)/swap_move.c \
  $(MCUBOOT_SRC_DIR)/swap_scratch.c \
  $(MCUBOOT_SRC_DIR)/tlv.c

# Also need mcuboot_config/ on path
MCUBOOT_INC_PATHS := -I$(MCUBOOT_INC_DIR)

# ...
SRC_FILES += $(MCUBOOT_SRC_FILES)
INCLUDE_PATHS += $(MCUBOOT_INC_PATHS)
```

#### Adding `mcuboot_config.h`

With the sources added, let's attempt to compile the sources and fix the fallout!

```
$ cd example/mcuboot/bootloader/
$ make

fault_injection_hardening.h:57:10: fatal error: mcuboot_config/mcuboot_config.h: No such file or directory
57 | #include "mcuboot_config/mcuboot_config.h"
```

Ah missing headers! The porting guide mentions that we need to provide a `mcuboot_config/mcuboot_config.h` configuration file. We can copy `samples/mcuboot_config/mcuboot_config.template.h` into our project and use that as a starting point.

I opted to place these files in `common/include` in the example project because some of the MCUboot library utilities will be called from our main application as well so it will need access to this header.

```bash
$ mkdir -p common/include/mcuboot_config
$ cp external/MCUboot/samples/mcuboot_config/mcuboot_config.template.h common/include/mcuboot_config/mcuboot_config.h
```

In our Makefile, we can add the new include path to build as follows:

```makefile
COMMON_DIR = $(ROOT_DIR)/common
# ...
INCLUDE_PATHS += -I$(COMMON_DIR)/include
```

#### Resolving sysflash.h and flash_map_backend.h dependencies

Attempting to compile again, we see more errors:

```
$ make
fatal error: sysflash/sysflash.h: No such file or directory
   32 | #include "sysflash/sysflash.h"
```

This one isn't explicitly mentioned in the MCUboot porting guide but it looks like we need to
create this header ourselves. Looking at some of the reference ports, this file will contain
mappings between the primary, secondary, & scratch slots and the flash areas they live in. Let's create a stub for now and come back to it:

```bash
$ mkdir -p common/include/sysflash
$ touch  common/include/sysflash/sysflash.h
```

Continuing onward we bump into another missing header!

```bash
$ make
fatal error: flash_map_backend/flash_map_backend.h: No such file or directory
   33 | #include "flash_map_backend/flash_map_backend.h"
   ```

There are some notes about this in the porting document about defining the flash interface. For the port, we need to create a `flash_map_backend.h` with these definitions.

> Oddly, these functions are not defined in a header in the library itself but it
> looks like we are expected to copy/paste them into a new file in our porting layer.

Here's what the file winds up looking like:

```c
// flash_map_backend/flash_map_backend.h
#pragma once

#include <inttypes.h>

struct flash_area {
  uint8_t  fa_id;         /** The slot/scratch identification */
  uint8_t  fa_device_id;  /** The device id (usually there's only one) */
  uint16_t pad16;
  uint32_t fa_off;        /** The flash offset from the beginning */
  uint32_t fa_size;       /** The size of this sector */
};

//! Structure describing a sector within a flash area.
struct flash_sector {
  //! Offset of this sector, from the start of its flash area (not device).
  uint32_t fs_off;

  //! Size of this sector, in bytes.
  uint32_t fs_size;
};

//! Opens the area for use. id is one of the `fa_id`s */
int flash_area_open(uint8_t id, const struct flash_area **area_outp);
void flash_area_close(const struct flash_area *fa);

//! Reads `len` bytes of flash memory at `off` to the buffer at `dst`
int flash_area_read(const struct flash_area *fa, uint32_t off,
                    void *dst, uint32_t len);
//! Writes `len` bytes of flash memory at `off` from the buffer at `src`
int flash_area_write(const struct flash_area *fa, uint32_t off,
                     const void *src, uint32_t len);
//! Erases `len` bytes of flash memory at `off`
int flash_area_erase(const struct flash_area *fa,
                     uint32_t off, uint32_t len);

//! Returns this `flash_area`s alignment
size_t flash_area_align(const struct flash_area *area);
//! Returns the value read from an erased flash area byte
uint8_t flash_area_erased_val(const struct flash_area *area);

//! Given flash area ID, return info about sectors within the area
int flash_area_get_sectors(int fa_id, uint32_t *count,
                           struct flash_sector *sectors);

//! Returns the `fa_id` for slot, where slot is 0 (primary) or 1 (secondary).
//!
//! `image_index` (0 or 1) is the index of the image. Image index is
//!  relevant only when multi-image support support is enabled
int flash_area_id_from_multi_image_slot(int image_index, int slot);
int flash_area_id_from_image_slot(int slot);
```

This part of the API was something I was curious about. There are a lot of ways flash layouts can
differ on embedded systems. For example, sometimes there are multiple flash devices (internal
flash, NOR flash, eMMC). Additionally, flash chips have different erase and write sizes. Furthermore, for
some flash devices, the sector sizes may differ within the same part. Scanning the header, it looks
like all of these description challenges are covered in the API design. Neat!

The last two dependency functions in the list give us a better idea of what needs to be provided in `sysflash/sysflash.h`. We need to define macros MCUboot uses to map between `image_index`and slot id (0=primary, 1=secondary) to the `fa_id` our port uses to identify a flash area. With that in mind we can go back and fill in that header:

```c
//! sysflash/sysflash.h

//! A user-defined identifier for different storage mediums
//! (i.e internal flash, external NOR flash, eMMC, etc)
#define FLASH_DEVICE_INTERNAL_FLASH 0

//! An arbitrarily high slot ID we will use to indicate that
//! there is not slot
#define FLASH_SLOT_DOES_NOT_EXIST 255

//! NB: MCUboot expects this define to exist but it's only used
//! if MCUBOOT_SWAP_USING_SCRATCH=1 is set
#define FLASH_AREA_IMAGE_SCRATCH FLASH_SLOT_DOES_NOT_EXIST

//! The slot we will use to track the bootloader allocation
#define FLASH_AREA_BOOTLOADER 0

//! A mapping to primary and secondary/upgrade slot
//! given an image_index. We'll plan to use
#define FLASH_AREA_IMAGE_PRIMARY(i) ((i == 0) ? 1 : 255)
#define FLASH_AREA_IMAGE_SECONDARY(i) ((i == 0) ? 2 : 255)
```

#### Adding mcuboot_logging.h

With the missing flash header dependencies now resolved, let's try compiling again:

``` bash
$ make
bootutil_log.h:29:10: fatal error: mcuboot_config/mcuboot_logging.h: No such file or directory
29 | #include <mcuboot_config/mcuboot_logging.h>
```

We've bumped into another piece not explicitly mentioned in the porting guide. MCUboot has a logging subsystem. We'll definitely want to have these implemented as we work on doing a bringup of MCUboot on our platform.

I created a minimal header using the Zephyr/MyNewt ports as a guide that plumbs into the "example" logging subsystem in our minimal application:

```c
#pragma once

#include "hal/logging.h"

#define MCUBOOT_LOG_MODULE_DECLARE(...)

#define MCUBOOT_LOG_ERR(_fmt, ...) \
  EXAMPLE_LOG("[ERR] " _fmt, ##__VA_ARGS__);
#define MCUBOOT_LOG_WRN(_fmt, ...) \
  EXAMPLE_LOG("[WRN] " _fmt, ##__VA_ARGS__);
#define MCUBOOT_LOG_INF(_fmt, ...) \
  EXAMPLE_LOG("[INF] " _fmt, ##__VA_ARGS__);
#define MCUBOOT_LOG_DBG(_fmt, ...) \
  EXAMPLE_LOG("[DBG] " _fmt, ##__VA_ARGS__);
  ```

#### Adding os_malloc.h

```bash
$ make
loader.c:38:10: fatal error: os/os_malloc.h: No such file or directory
   38 | #include <os/os_malloc.h>
```

It looks like there are a few dependencies within MCUboot on `malloc`.

> This is something we'd want to audit in more detail before shipping to understand the exact
> amount of space needed. For bootloaders, it is often favorable to have everything statically allocated.

It's nice that a header is exposed that lets us override implementations. In our case since the
example app is making use of the malloc provided by Newlib, we can just `#include <stdlib.h>`:

```c
#pragma once

#include <stdlib.h>
```
