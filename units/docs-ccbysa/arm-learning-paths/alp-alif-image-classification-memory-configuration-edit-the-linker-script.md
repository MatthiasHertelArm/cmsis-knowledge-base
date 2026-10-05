---
id: "alp-alif-image-classification-memory-configuration-edit-the-linker-script"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Configure memory layout and flash settings: Edit the linker script"
summary: "Open device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration/#edit-the-linker-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open `device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src`.

Make the following three changes to this file.

### Add SRAM1 to the zero-initialization table

The application code places the 4 MB planned memory pool in SRAM1. The C runtime startup code needs to zero-initialize this region. Find the `.zero.table` section:

```text
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
#endif
```

Add two lines for SRAM1 immediately after:

```text
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
    LONG (ADDR(.bss.at_sram1))
    LONG (SIZEOF(.bss.at_sram1)/4)
#endif
```

### Add GOT sections to the data copy table

The precompiled ExecuTorch libraries use position-independent code (PIC), which relies on a Global Offset Table (GOT). The GOT must be copied from flash to RAM at startup, otherwise the table contains zeros and every indirect function call (including C++ vtable lookups) crashes with a BusFault.

Find the `.data.at_dtcm` section:

```text
  .data.at_dtcm : ALIGN(8)
  {
    *(vtable)
    *(.data)
    *(.data*)
    *arm_common_tables*(.data* .rodata*)

    KEEP(*(.jcr*))

    . = ALIGN(8);
```

Add the GOT entries after `KEEP(*(.jcr*))`:

```text
  .data.at_dtcm : ALIGN(8)
  {
    *(vtable)
    *(.data)
    *(.data*)
    *arm_common_tables*(.data* .rodata*)

    KEEP(*(.jcr*))

    /* GOT for PIC code in precompiled ExecuTorch libraries */
    *(.got)
    *(.got.plt)

    . = ALIGN(8);
```

**Note:**
This issue can be difficult to diagnose. Without these two lines, the firmware boots and loads the model, but crashes with a BusFault when ExecuTorch calls a virtual function. The GOT stores addresses for indirect calls. If the startup code doesn't copy it from flash to RAM, those lookups resolve to address zero and the CPU faults.


### Add SRAM section wildcards

The application code uses `__attribute__((section(".bss.at_sram0")))` to place memory pools in SRAM. The stock linker script only has specific named sections for LCD and camera buffers. You need wildcard patterns to catch the ExecuTorch pools.

Find the `.bss.at_sram0` section:

```text
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
  } > SRAM0
#endif
```

Replace it with expanded SRAM0 wildcards and a new SRAM1 section:

```text
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
    *(.bss.at_sram0)
    *(.bss.at_sram0.*)
  } > SRAM0

  .bss.at_sram1 (NOLOAD) : ALIGN(8)
  {
    *(.bss.at_sram1)
    *(.bss.at_sram1.*)
  } > SRAM1
#endif
```

After these changes, the memory layout is:

| Region | Size | Usage |
|--------|------|-------|
| MRAM | 5.5 MB | Code + model (~4.5 MB used) |
| ITCM | 256 KB | Fast code (~89% used) |
| DTCM | 1 MB | Stack (16 KB) + heap (64 KB) + GOT + data |
| SRAM0 | 4 MB | Method pool (1.5 MB) + temp pool (1.5 MB) + float input buffer (~588 KB) |
| SRAM1 | 4 MB | Planned memory buffers |
