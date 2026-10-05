---
id: "intr-peeking-inside-cmsis-packs-reset-strategies"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: Reset Strategies"
summary: "The Pack Description (.pdsc) file can also contain optional debug sequences:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#reset-strategies"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Pack Description (`*.pdsc`) file can also contain optional debug sequences:

<https://www.keil.com/pack/doc/CMSIS/Pack/html/pdsc_family_pg.html#element_sequences>

For example, the Pack for the NXP RT685 chip contains a sequence for resetting
the external flash on the EVK board:

```bash
# download the RT685 Pack
❯ pyocd pack install rt685
# unzip the pack files
❯ mkdir rt685-pack
❯ unzip -d rt685-pack ~/.local/share/cmsis-pack-manager/NXP/MIMXRT685S_DFP/13.1.0.pack
```

The `NXP.MIMXRT685S_DFP.pdsc` file in this pack contains a few interesting reset
sequences.

### `ResetFlash`

This sequence pulses the Reset pin on the external flash chip on the EVK board.
The addresses written in the sequence are various memory-mapped peripheral
registers (Power/Clocking, GPIO), documented in the chip user manual.

```xml
<sequence name="ResetFlash" Pname="cm33">
  <block/>
    <control if="(__connection &amp; 0x01)">
      <block>
        //  Reset external flash if connection for target debug
        Write32(0x40004130, 0x130U);
        Write32(0x40021044, 0x4U);
        Write32(0x40020074, 0x4U);
        Write32(0x40102008, 0x1000U);
        Write32(0x40102288, 0x1000U);
        DAP_Delay(100);
        Write32(0x40102208, 0x1000U);
    </block>
  </control>
</sequence>
```

### `ResetSystem`

This sequence performs a system reset, applicable to the EVK. It does the
typical AIRCR reset for a Cortex-M processor, resets the external flash, sets a
watchpoint and waits for the chip to halt after reset.

```xml
<sequence name="ResetSystem" Pname="cm33">
  <block>
    __dp = 0;
    __ap = 0;
      // System Control Space (SCS) offset as defined in Armv6-M/Armv7-M.
      __var SCS_Addr   = 0xE000E000;
      __var AIRCR_Addr = SCS_Addr + 0xD0C;
      __var DHCSR_Addr = SCS_Addr + 0xDF0;
      __var DEMCR_Addr = SCS_Addr + 0xDFC;
      __var tmp;
      //Halt the core
      Write32(DHCSR_Addr, 0xA05F0003);
      //clear VECTOR CATCH and set TRCENA
      tmp = Read32(DEMCR_Addr);
      Write32(DEMCR_Addr, tmp | 0x1000000);
      Sequence("ResetFlash");
      // Set watch point at SYSTEM_STICK_CALIB access
      Write32(0xE0001020, 0x50002034);
      Write32(0xE0001028, 0x00000814);
      __errorcontrol = 1;
      // Execute SYSRESETREQ via AIRCR
      Write32(AIRCR_Addr, 0x05FA0004);
    Sequence("WaitForStopAfterReset");
      __errorcontrol = 0;
  </block>
</sequence>
```
