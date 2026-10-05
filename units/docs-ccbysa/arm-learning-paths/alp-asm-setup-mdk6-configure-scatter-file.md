---
id: "alp-asm-setup-mdk6-configure-scatter-file"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Setting up a Project in Keil Studio (VS Code): Configure scatter file"
summary: "Return to the CMSIS extension. The project is configured to use the ARMCM4_ac6.sct file as the scatter description file."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/setup_mdk6/#configure-scatter-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

Return to the `CMSIS` extension. The project is configured to use the `ARMCM4_ac6.sct` file as the scatter description file.

Click the file to create it with the following:

```text
LR_IROM1 0x00000000 0x00040000  {    ; load region size_region
    ER_IROM1 0x00000000 0x00040000  {  ; load address = execution address
        *.o (RESET, +First)
        *(InRoot$$Sections)
        .ANY (+RO)
        .ANY (+XO)
    }
    RW_IRAM1 0x20000000 0x00020000  {  ; RW data
        .ANY (+RW +ZI)
    }
    ARM_LIB_STACK 0x20020000 EMPTY 0x4000 {}
}
```
Close to save.
