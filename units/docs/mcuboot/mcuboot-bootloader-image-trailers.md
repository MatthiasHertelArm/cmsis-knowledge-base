---
id: "mcuboot-bootloader-image-trailers"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image trailers"
summary: "At startup, the bootloader determines the boot swap type by inspecting the image trailers. When using the term \"image trailers\" what is meant is the aggregate information provided by both image slot's trailers."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#image-trailers"
license: "Apache-2.0"
mode: "V"
---

At startup, the bootloader determines the boot swap type by inspecting the
image trailers.  When using the term "image trailers" what is meant is the
aggregate information provided by both image slot's trailers.

### [New swaps (non-resumes)](#new-swaps-non-resumes)

For new swaps, MCUboot must inspect a collection of fields to determine which
swap operation to perform.

The image trailers records are structured around the limitations imposed by
flash hardware. As a consequence, they do not have a very intuitive design, and
it is difficult to get a sense of the state of the device just by looking at the
image trailers.  It is better to map all the possible trailer states to the swap
types described above via a set of tables.  These tables are reproduced below.

---
***Note***

*An important caveat about the tables described below is that they must*
*be evaluated in the order presented here. Lower state numbers must have a*
*higher priority when testing the image trailers.*

---

```
    State I (swap using offset only)
                     | primary slot | secondary slot |
    -----------------+--------------+----------------|
               magic | Any          | Good           |
            image-ok | Any          | Unset          |
           copy-done | Any          | Set            |
    -----------------+--------------+----------------'
     result: BOOT_SWAP_TYPE_REVERT                   |
    -------------------------------------------------'

    State II
                     | primary slot | secondary slot |
    -----------------+--------------+----------------|
               magic | Any          | Good           |
            image-ok | Any          | Unset          |
           copy-done | Any          | Any            |
    -----------------+--------------+----------------'
     result: BOOT_SWAP_TYPE_TEST                     |
    -------------------------------------------------'


    State III
                     | primary slot | secondary slot |
    -----------------+--------------+----------------|
               magic | Any          | Good           |
            image-ok | Any          | 0x01           |
           copy-done | Any          | Any            |
    -----------------+--------------+----------------'
     result: BOOT_SWAP_TYPE_PERM                     |
    -------------------------------------------------'


    State IV
                     | primary slot | secondary slot |
    -----------------+--------------+----------------|
               magic | Good         | Any            |
            image-ok | 0xff         | Any            |
           copy-done | 0x01         | Any            |
    -----------------+--------------+----------------'
     result: BOOT_SWAP_TYPE_REVERT                   |
    -------------------------------------------------'
```

Any of the above three states results in MCUboot attempting to swap images.

Otherwise, MCUboot does not attempt to swap images, resulting in one of the
other three swap types, as illustrated by State IV.

```
    State V
                     | primary slot | secondary slot |
    -----------------+--------------+----------------|
               magic | Any          | Any            |
            image-ok | Any          | Any            |
           copy-done | Any          | Any            |
    -----------------+--------------+----------------'
     result: BOOT_SWAP_TYPE_NONE,                    |
             BOOT_SWAP_TYPE_FAIL, or                 |
             BOOT_SWAP_TYPE_PANIC                    |
    -------------------------------------------------'
```

In State V, when no errors occur, MCUboot will attempt to boot the contents of
the primary slot directly, and the result is `BOOT_SWAP_TYPE_NONE`. If the image
in the primary slot is not valid, the result is `BOOT_SWAP_TYPE_FAIL`. If a
fatal error occurs during boot, the result is `BOOT_SWAP_TYPE_PANIC`. If the
result is either `BOOT_SWAP_TYPE_FAIL` or `BOOT_SWAP_TYPE_PANIC`, MCUboot hangs
rather than booting an invalid or compromised image.

---
***Note***

*An important caveat to the above is the result when a swap is requested*
*and the image in the secondary slot fails to validate, due to a hashing or*
*signing error. This state behaves as State IV with the extra action of*
*marking the image in the primary slot as "OK", to prevent further attempts*
*to swap.*

---

### [Resumed swaps](#resumed-swaps)

If MCUboot determines that it is resuming an interrupted swap (i.e., a reset
occurred mid-swap), it fully determines the operation to resume by reading the
`swap info` field from the active trailer and extracting the swap type from bits
0-3. The set of tables in the previous section are not necessary in the resume
case.
