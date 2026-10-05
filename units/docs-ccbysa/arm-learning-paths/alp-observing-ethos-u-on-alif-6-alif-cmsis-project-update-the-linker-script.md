---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-update-the-linker-script"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Update the linker script"
summary: "Open device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#update-the-linker-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open `device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src`.

On Cortex-M systems, the Data Tightly Coupled Memory (DTCM) is a small, fast RAM region connected closely to the CPU. By default, the linker script sends most `.bss` data to DTCM. 

ExecuTorch uses large memory pools, so this data must be routed to SRAM0 and SRAM1 instead. Without this change, the linker reports that `.bss` does not fit in DTCM.

Make the following changes.

### Add SRAM1 to the zero-initialization table

Find the following block in `.zero.table`:

```ld
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
#endif
```

Replace it with the following:

```ld
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
    LONG (ADDR(.bss.at_sram1))
    LONG (SIZEOF(.bss.at_sram1)/4)
#endif
```

This block tells the startup code to clear both SRAM0 and SRAM1 `.bss` sections before `main()` runs.

### Add GOT sections to .data.at_dtcm

Find the following block in `.data.at_dtcm`:

```ld
    KEEP(*(.jcr*))
    . = ALIGN(8);
```

Replace it with the following:

```ld
    KEEP(*(.jcr*))
    *(.got)
    *(.got.plt)
    . = ALIGN(8);
```

The ExecuTorch C++ libraries can use a GOT (Global Offset Table). These entries must be copied into RAM at startup.

### Route ExecuTorch buffers to SRAM0 and SRAM1

Find the following existing block:

```ld
#if __HAS_BULK_SRAM
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
  } > SRAM0
#endif
```

Replace it with the following:

```ld
#if __HAS_BULK_SRAM
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

This block must appear before the generic `.bss` section. Otherwise, sections such as `.bss.at_sram0` and `.bss.at_sram1` are caught by `*(.bss.*)` and placed in DTCM.

The project structure is now ready.
