---
id: "intr-mcuboot-walkthrough-and-porting-gu-resolving-undefined-references"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Porting MCUboot / Resolving Undefined References"
summary: "Finally, everything compiles! As expected, we see a number of undefined reference warnings emitted by the linker that we now need to work through!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#resolving-undefined-references"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Porting MCUboot_

Finally, everything compiles! As expected, we see a number of undefined reference warnings emitted
by the linker that we now need to work through!

```bash
make 2>&1 | rg ": undefined.*" -o | sort -u
: undefined reference to `_close'
: undefined reference to `_exit'
: undefined reference to `_fstat'
: undefined reference to `_getpid'
: undefined reference to `_isatty'
: undefined reference to `_kill'
: undefined reference to `_lseek'
: undefined reference to `_read'
: undefined reference to `_write'
: undefined reference to `flash_area_align'
: undefined reference to `flash_area_close'
: undefined reference to `flash_area_erase'
: undefined reference to `flash_area_erased_val'
: undefined reference to `flash_area_get_sectors'
: undefined reference to `flash_area_id_from_image_slot'
: undefined reference to `flash_area_id_from_multi_image_slot'
: undefined reference to `flash_area_open'
: undefined reference to `flash_area_read'
: undefined reference to `flash_area_write'
: undefined reference to `tc_sha256_final'
: undefined reference to `tc_sha256_init'
: undefined reference to `tc_sha256_update'
```

Examining the missing symbols we have three classes:

1. Missing Newlib platform dependency implementations. (We've seen these before in [our post about porting newlib](https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib)).
2. The `tc_sha256_*` are missing implementations for the Tincrypt backend we are using.
3. The `flash_*` dependency functions defined in `flash_map_backend.h` need to be filled in.

#### Remove Dependencies on Newlib stdio

This one is a little strange. Newlib calls like `_write`, `_read`, etc should only get pulled into a
build when there is a dependency on `stdio`. It would be surprising if MCUboot had a dependency like
this. One indirect source of these dependencies is Newlib's `assert()` implementation. Inspecting the MCUboot source, `<assert.h>` is included from a number of files.

However, what we can do instead is override the default assert handler by adding an override to `mcuboot_config.h` which causes `mcuboot_config/mcuboot_assert.h` to be included instead of `<assert.h>`:

```c
// mcuboot_config/mcuboot_config.h
#define MCUBOOT_HAVE_ASSERT_H 1
```

Let's override the default Newlib implementation with a lighter weight one and see if that removes
the Newlib porting dependencies:

```c
// mcuboot_config/mcuboot_assert.h
#pragma once

#include "hal/logging.h"

extern void example_assert_handler(const char *file, int line);

#define assert(exp) \
  do {                                                  \
    if (!(exp)) {                                       \
      example_assert_handler(__FILE__, __LINE__);       \
    }                                                   \
  } while (0)
```

Now let's recompile:

```bash
make  2>&1 | rg ": undefined.*" -o | sort -u
: undefined reference to `example_assert_handler'
: undefined reference to `flash_area_align'
: undefined reference to `flash_area_close'
: undefined reference to `flash_area_erase'
: undefined reference to `flash_area_erased_val'
: undefined reference to `flash_area_get_sectors'
: undefined reference to `flash_area_id_from_image_slot'
: undefined reference to `flash_area_id_from_multi_image_slot'
: undefined reference to `flash_area_open'
: undefined reference to `flash_area_read'
: undefined reference to `flash_area_write'
: undefined reference to `tc_sha256_final'
: undefined reference to `tc_sha256_init'
: undefined reference to `tc_sha256_update'
```

Sweet. All of the Newlib undefined references are gone.

#### Resolving Tinycrypt Dependencies

The `tc_*` calls are library calls into the Tinycrypt library (because we are using `MCUBOOT_USE_TINYCRYPT`). The exact dependencies will change depending on what is enabled in the bootloader (SHA256, Code Signing, Encryption). For the purposes of this initial port, we'll just be using SHA256 based validation to check for image corruption.

Tinycrypt can easily be added to a project by adding the sources to the Makefile. The library is
included as a submodule within the MCUboot repo so we can just pick it up from there:

```makefile
TINYCRYPT_DIR := $(ROOT_DIR)/external/MCUboot/ext/tinycrypt/lib
TINYCRYPT_SRC_DIR := $(TINYCRYPT_DIR)/source
TINYCRYPT_INC_DIR := $(TINYCRYPT_DIR)/include

TINYCRYPT_SRC_FILES += \
  $(TINYCRYPT_SRC_DIR)/aes_decrypt.c \
  $(TINYCRYPT_SRC_DIR)/aes_encrypt.c \
  $(TINYCRYPT_SRC_DIR)/cbc_mode.c \
  $(TINYCRYPT_SRC_DIR)/ccm_mode.c \
  $(TINYCRYPT_SRC_DIR)/cmac_mode.c \
  $(TINYCRYPT_SRC_DIR)/ctr_mode.c \
  $(TINYCRYPT_SRC_DIR)/ctr_prng.c \
  $(TINYCRYPT_SRC_DIR)/hmac.c \
  $(TINYCRYPT_SRC_DIR)/hmac_prng.c \
  $(TINYCRYPT_SRC_DIR)/sha256.c \
  $(TINYCRYPT_SRC_DIR)/utils.c

TINYCRYPT_INC_PATHS := -I$(TINYCRYPT_INC_DIR)
# [...]
SRC_FILES += $(TINYCRYPT_SRC_FILES)
INCLUDE_PATHS += $(TINYCRYPT_INC_PATHS)
```

We can rebuild and see the `tc_sha256*` dependencies have been resolved:

```bash
make  2>&1 | rg ": undefined.*" -o | sort -u
: undefined reference to `example_assert_handler'
: undefined reference to `flash_area_align'
: undefined reference to `flash_area_close'
: undefined reference to `flash_area_erase'
: undefined reference to `flash_area_erased_val'
: undefined reference to `flash_area_get_sectors'
: undefined reference to `flash_area_id_from_image_slot'
: undefined reference to `flash_area_id_from_multi_image_slot'
: undefined reference to `flash_area_open'
: undefined reference to `flash_area_read'
: undefined reference to `flash_area_write'
```

#### Resolving Flash Dependencies

Finally, we have gotten to the meat of the port, the flash dependencies required by MCUboot. Let's
add stub implementations for each of the dependency functions that just return error codes when
called.

```c
// mcu_port.c

#include <string.h>
#include <stdlib.h>

#include "flash_map_backend/flash_map_backend.h"
#include "os/os_heap.h"
#include "sysflash/sysflash.h"

#include "hal/logging.h"
#include "hal/internal_flash.h"

int flash_area_open(uint8_t id, const struct flash_area **area_outp) {
  return -1;
}

void flash_area_close(const struct flash_area *area) {
}

int flash_area_read(const struct flash_area *fa, uint32_t off, void *dst,
                    uint32_t len) {
  return -1;
}

int flash_area_write(const struct flash_area *fa, uint32_t off, const void *src,
                     uint32_t len) {
  return -1;
}

int flash_area_erase(const struct flash_area *fa, uint32_t off, uint32_t len) {
  return -1;
}

size_t flash_area_align(const struct flash_area *area) {
  return 1;
}

uint8_t flash_area_erased_val(const struct flash_area *area) {
  return 0xff;
}

int flash_area_get_sectors(int fa_id, uint32_t *count,
                           struct flash_sector *sectors) {
  return -1;
}

int flash_area_id_from_multi_image_slot(int image_index, int slot) {
  return -1;
}

int flash_area_id_from_image_slot(int slot) {
  return flash_area_id_from_multi_image_slot(0, slot);
}

void example_assert_handler(const char *file, int line) {
}
```


We can add the file to our build system

```
SRC_FILES += $(COMMON_SRC_DIR)/mcuboot_port.c
```

```
Linking library
Generated bootloader/build/nrf52-bootloader.elf
```

Success, we have a build!

At this point, we can use `arm-none-eabi-size` to get an approximation of how big our bootloader will be:

```
arm-none-eabi-size bootloader/build/nrf52-bootloader.elf
   text    data     bss     dec     hex	filename
   21295        108   14052   35455    8a7f	bootloader/build/nrf52-bootloader.elf
```

We can also flash the image on a running board and see what happens.

```
[WRN] Failed reading sectors; BOOT_MAX_IMG_SECTORS=128 - too small?
No bootable image found. Falling into Bootloader CLI:

shell>
```

As expected, `boot_go()` fails because we have not yet implemented the flash dependencies.
