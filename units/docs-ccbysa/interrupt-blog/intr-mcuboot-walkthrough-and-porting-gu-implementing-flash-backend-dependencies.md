---
id: "intr-mcuboot-walkthrough-and-porting-gu-implementing-flash-backend-dependencies"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Porting MCUboot / Implementing Flash Backend Dependencies"
summary: "With a layout decided upon, we can start to fill in our stub implementations in mcuboot_port.c. The first step will be defining our \"flash areas\":"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#implementing-flash-backend-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Porting MCUboot_

With a layout decided upon, we can start to fill in our stub implementations in `mcuboot_port.c`. The first step will be defining our "flash areas":

```c
// mcuboot_port.c

#define BOOTLOADER_START_ADDRESS 0x0
#define BOOTLOADER_SIZE (32 * 1024)
#define APPLICATION_PRIMARY_START_ADDRESS (32 * 1024)
#define APPLICATION_SECONDARY_START_ADDRESS (APPLICATION_PRIMARY_START_ADDRESS + APPLICATION_SIZE)
#define APPLICATION_SIZE (128 * 1024)

static const struct flash_area bootloader = {
  .fa_id = FLASH_AREA_BOOTLOADER,
  .fa_device_id = FLASH_DEVICE_INTERNAL_FLASH,
  .fa_off = BOOTLOADER_START_ADDRESS,
  .fa_size = BOOTLOADER_SIZE,
};

static const struct flash_area primary_img0 = {
  .fa_id = FLASH_AREA_IMAGE_PRIMARY(0),
  .fa_device_id = FLASH_DEVICE_INTERNAL_FLASH,
  .fa_off = APPLICATION_PRIMARY_START_ADDRESS,
  .fa_size = APPLICATION_SIZE,
};

static const struct flash_area secondary_img0 = {
  .fa_id = FLASH_AREA_IMAGE_SECONDARY(0),
  .fa_device_id = FLASH_DEVICE_INTERNAL_FLASH,
  .fa_off = APPLICATION_SECONDARY_START_ADDRESS,
  .fa_size = APPLICATION_SIZE,
};

static const struct flash_area *s_flash_areas[] = {
  &bootloader,
  &primary_img0,
  &secondary_img0,
};
```

where,

- `fa_id` is a **unique** id for the flash area being referenced. MCUboot will be accessing the primary & secondary slots for our images but should never touch the bootloader region. The actual "id" used is entirely up to us. MCUboot looks up the id using the `FLASH_AREA_IMAGE_PRIMARY/SECONDARY` macros.
- `fa_device_id` is a unique identifier for the flash storage. If there are multiple backing storages in use, this gives us a way to implement different behavior based on the storage being accessed. For our example setup, we will only have one device id to represent internal flash.
- `fa_off` - is the offset within the flash area device where the slot starts. We will use this
  value in dependency function implementations to determine what physical address to write to within the flash.
- `fa_size` is the total space available in the slot.

> Note these regions must all be defined along erase sector boundaries for upgrades to work correctly and to avoid corrupting adjacent slots!

#### Implementing `flash_area_open` / `flash_area_close`

This is how MCUboot determines information about flash areas being written to / read from. The "id" passed into the function is the "slot" it would like to try and read. In our setup, since we have defined all the flash regions statically at compile time, we can walk through the structure and return the appropriate information to the library:

```c
#define ARRAY_SIZE(arr) sizeof(arr)/sizeof(arr[0])

static const struct flash_area *prv_lookup_flash_area(uint8_t id) {
  for (size_t i = 0; i < ARRAY_SIZE(s_flash_areas); i++) {
    const struct flash_area *area = s_flash_areas[i];
    if (id == area->fa_id) {
      return area;
    }
  }
  return NULL;
}

int flash_area_open(uint8_t id, const struct flash_area **area_outp) {
  MCUBOOT_LOG_DBG("%s: ID=%d", __func__, (int)id);

  const struct flash_area *area = prv_lookup_flash_area(id);
  *area_outp = area;
  return area != NULL ? 0 : -1;
}

void flash_area_close(const struct flash_area *fa) {
  // no cleanup to do for this flash part
}
```

#### Implementing `flash_area_id_from_multi_image_slot`

MCUboot needs to be able to resolve the "flash area id" to read from a given image index and slot id.
The "slot" argument is set to 0 when looking up the primary slot and 1 to lookup the secondary slot.

```c
int flash_area_id_from_multi_image_slot(int image_index, int slot) {
    switch (slot) {
      case 0:
        return FLASH_AREA_IMAGE_PRIMARY(image_index);
      case 1:
        return FLASH_AREA_IMAGE_SECONDARY(image_index);
    }

    MCUBOOT_LOG_ERR("Unexpected Request: image_index=%d, slot=%d", image_index, slot);
    return -1; /* flash_area_open will fail on that */
}
```

> If you are using the `MCUBOOT_SWAP_USING_SCRATCH=1` configuration, the `FLASH_AREA_IMAGE_SCRATCH`
> slot identifier may also be passed in the "slot" argument and will need to be handled.

```c
int flash_area_id_from_image_slot(int slot) {
  return flash_area_id_from_multi_image_slot(0, slot);
}
```

#### Implementing `flash_area_align`, `flash_area_erased_val`, `flash_area_get_sectors`

There are several dependencies used to describe various flash device properties. These are used by
MCUboot so it can issue erase and write requests that comply with the flash device in use. For the NRF52 internal flash, we have:

```c
#define FLASH_SECTOR_SIZE 4096

size_t flash_area_align(const struct flash_area *area) {
  // the smallest unit a flash write can occur along.
  // Note: Image trailers will be scaled by this size
  return 4;
}

uint8_t flash_area_erased_val(const struct flash_area *area) {
  // the value a byte reads when erased on storage.
  return 0xff;
}

int flash_area_get_sectors(int fa_id, uint32_t *count,
                           struct flash_sector *sectors) {
  const struct flash_area *fa = prv_lookup_flash_area(fa_id);
  if (fa->fa_device_id != FLASH_DEVICE_INTERNAL_FLASH) {
    return -1;
  }

  // All sectors for the NRF52 are the same size
  const size_t sector_size = FLASH_SECTOR_SIZE;
  uint32_t total_count = 0;
  for (size_t off = 0; off < fa->fa_size; off += sector_size) {
    // Note: Offset here is relative to flash area, not device
    sectors[total_count].fs_off = off;
    sectors[total_count].fs_size = sector_size;
    total_count++;
  }

  *count = total_count;
  return 0;
}
```

#### Implementing `flash_area_read`, `flash_area_write`, `flash_area_erase`

Finally, we need to implement the APIs that MCUboot uses to program flash. The example application
used in this article has a minimal flash driver implementation for the NRF52 in
`minimal_nrf52_flash.c`. The functions are all named `example_internal_flash_*`. Most vendor SDKs
provide something similar that you could use for these implementations.

For initial bringup, we will also add:
* Diagnostic logging so we can see what addresses writes and erases are being issued to
* A validation pass that makes sure writes and erases are working as expected. A bug in how we are performing program operations is generally the most common reason an image will fail to install so best to catch it at the source.

Taking all that into account, we have the following:

```c
//! Useful for bringup to make sure the write
//! and erase operations are behaving as expected
#define VALIDATE_PROGRAM_OP 1

int flash_area_read(const struct flash_area *fa, uint32_t off, void *dst,
                    uint32_t len) {
  if (fa->fa_device_id != FLASH_DEVICE_INTERNAL_FLASH) {
    return -1;
  }

  const uint32_t end_offset = off + len;
  if (end_offset > fa->fa_size) {
    MCUBOOT_LOG_ERR("%s: Out of Bounds (0x%x vs 0x%x)", __func__, end_offset, fa->fa_size);
    return -1;
  }

  // internal flash is memory mapped so just dereference the address
  void *addr = (void *)(fa->fa_off + off);
  memcpy(dst, addr, len);

  return 0;
}

int flash_area_write(const struct flash_area *fa, uint32_t off, const void *src,
                     uint32_t len) {
  if (fa->fa_device_id != FLASH_DEVICE_INTERNAL_FLASH) {
    return -1;
  }

  const uint32_t end_offset = off + len;
  if (end_offset > fa->fa_size) {
    MCUBOOT_LOG_ERR("%s: Out of Bounds (0x%x vs 0x%x)", __func__, end_offset, fa->fa_size);
    return -1;
  }

  const uint32_t addr = fa->fa_off + off;
  MCUBOOT_LOG_DBG("%s: Addr: 0x%08x Length: %d", __func__, (int)addr, (int)len);
  example_internal_flash_write(addr, src, len);

#if VALIDATE_PROGRAM_OP
  if (memcmp((void *)addr, src, len) != 0) {
    MCUBOOT_LOG_ERR("%s: Program Failed", __func__);
    assert(0);
  }
#endif

  return 0;
}

int flash_area_erase(const struct flash_area *fa, uint32_t off, uint32_t len) {
  if (fa->fa_device_id != FLASH_DEVICE_INTERNAL_FLASH) {
    return -1;
  }

  if ((len % FLASH_SECTOR_SIZE) != 0 || (off % FLASH_SECTOR_SIZE) != 0) {
    MCUBOOT_LOG_ERR("%s: Not aligned on sector Offset: 0x%x Length: 0x%x", __func__,
                    (int)off, (int)len);
    return -1;
  }

  const uint32_t start_addr = fa->fa_off + off;
  MCUBOOT_LOG_DBG("%s: Addr: 0x%08x Length: %d", __func__, (int)start_addr, (int)len);

  for (size_t i = 0; i < len; i+= FLASH_SECTOR_SIZE) {
    const uint32_t addr = start_addr + i;
    example_internal_flash_erase_sector(addr);
  }

#if VALIDATE_PROGRAM_OP
  for (size_t i = 0; i < len; i++) {
    uint8_t *val = (void *)(start_addr + i);
    if (*val != 0xff) {
      MCUBOOT_LOG_ERR("%s: Erase at 0x%x Failed", __func__, (int)val);
      assert(0);
    }
  }
#endif

  return 0;
}
```

#### Implementing `example_assert_handler`

Lastly, we need to provide an implementation for the custom assert handler we added. For example:

```c
void example_assert_handler(const char *file, int line) {
  EXAMPLE_LOG("ASSERT: File: %s Line: %d", file, line);
  __builtin_trap();
}
```
