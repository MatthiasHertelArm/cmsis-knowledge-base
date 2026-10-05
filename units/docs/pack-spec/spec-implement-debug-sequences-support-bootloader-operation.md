---
id: "spec-implement-debug-sequences-support-bootloader-operation"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Support bootloader operation"
summary: "Systems with built-in ROM bootloader often require special handling to ensure that debug is correctly started from the user application."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

Systems with built-in ROM bootloader often require special handling to ensure that debug is correctly started from the user application.

In particular the reset flow described in dbg_sqns_reset most likely needs special adjustments for bootloader operation. After device reset the bootloader gets executed first. The debugger needs to take that into account and stop the processor with a breakpoint just before the application is started. For some devices this is also essential because debug can be disabled during bootloader execution for asset protection purposes.

The default implementation of resetCatchSet sequence halts the core right after reset. This however would be before the bootloader is started and hence may be not relevant for application development or even not possible to debug if bootloader code is not available.

To overcome this problem the **ResetCatchSet** sequence needs to be overwritten in the .pdsc file of the Device Family Pack (DFP). In constrast to the default implementation the Reset Vector Catch shall be disabled allowing uninterrupted bootloader execution after reset. To halt the core before the application starts the sequence additionally sets a breakpoint at the Reset Vector, where the execution jumps to after bootloader is finished.


**Example 1: ResetCatchSet**

The code below gives an example for an Armv8-M system with the vector table placed at address 0x00000000:

```
<sequence name="ResetCatchSet">
  <block>
    __var DHCSR_Addr    = 0xE000EDF0;
    __var DEMCR_Addr    = 0xE000EDFC;
    __var FP_CTRL_Addr  = 0xE0002000;
    __var FP_COMP0_Addr = 0xE0002008;
    __var FPB_KEY       = 0x00000002;
    __var FPB_ENABLE    = 0x00000001;
    __var value         = 0;
    __var resetVect     = 0x00000000;

    value = Read32(DEMCR_Addr);
    Write32(DEMCR_Addr, (value &amp; ~0x00000001));    // Disable Reset Vector Catch

    resetVect = Read32(0x00000004);                     // Read Reset Vector
    Write32(FP_COMP0_Addr, (resetVect | FPB_ENABLE));   // Set BP0 to Reset Vector (ARMv8M)
    Write32(FP_CTRL_Addr,  (FPB_KEY   | FPB_ENABLE));   // Enable FPB
  </block>

  <block>
    Read32(DHCSR_Addr);                                 // Read DHCSR to clear potentially set DHCSR.S_RESET_ST bit
  </block>
</sequence>

```

After reset is performed and the processor is halted (on the breakpoint enabled in **ResetCatchSet)** the resetCatchClear sequence is executed. There in addition to the default functionality we need to clear the breakpoint introduced in the customized **ResetCatchSet** sequence.


**Example 1: ResetCatchClear **

Below is a **ResetCatchClear** function for an Armv8-M core that corresponds to the **ResetCatchSet** sequence shown in Example 1: ResetCatchSet:

```
<sequence name="ResetCatchClear">
  <block>
    __var DEMCR_Addr    = 0xE000EDFC;
    __var FP_CTRL_Addr  = 0xE0002000;
    __var FP_COMP0_Addr = 0xE0002008;
    __var FPB_KEY       = 0x00000002;
    __var value         = 0;

    value = Read32(DEMCR_Addr);
    Write32(DEMCR_Addr, (value &amp; ~0x00000001));     // Disable Reset Vector Catch in DEMCR

    Write32(FP_COMP0_Addr, 0x00000000);                 // Clear BP0
    Write32(FP_CTRL_Addr,  FPB_KEY   );                 // Disable FPB
  </block>
</sequence>
```



**Example 2: ResetCatchSet**

In some cases the **ResetCatchSet** sequence shall behave differently depending on where the obtained Reset Vector is located. Such differentiation can be introduced using XML **`<control>`** element. For example Cortex-M0/M0+/M1/M3/M4 cores have a FBP/BPU limitations that doesn't allow to set an FPB breakpoint for code memory  above 0x20000000. For systems that have firmware located above this address (mostly in large external flash) the debugger can just rely on the Reset Vector Catch to stop right after reset and can't jump to the reset vector. Here is corresponding debug sequence:

```
<sequence name="ResetCatchSet">
  <block>
    __var DHCSR_Addr = 0xE000EDF0;
    __var DEMCR_Addr = 0xE000EDFC;
    __var FPB_BKPT_H = 0x80000000;
    __var FPB_BKPT_L = 0x40000000;
    __var FPB_COMP_M = 0x1FFFFFFC;
    __var FPB_KEY    = 0x00000002;
    __var FPB_ENABLE = 0x00000001;
    __var value      = 0;
	__var resetVect  = 0x00000000;

    // Run over Bootloader
    value = Read32(DEMCR_Addr);
    Write32(DEMCR_Addr, (value &amp; ~0x00000001));    // Disable Reset Vector Catch

    Write32(0x40000000, 0x00000002);    // Map Flash to Vectors
    resetVect = Read32 (0x00000004);        // Read Reset Vector
  </block>

  <control if="resetVect &lt; 0x20000000" info="Set and enable breakpoint">
    <block>
	  //determine if instruction is at upper or lower half-word in an aligned 4-byte block
      value = ((resetVect &amp; 0x02) ? FPB_BKPT_H : FPB_BKPT_L) | (resetVect &amp; FPB_COMP_M) | FPB_ENABLE ;
      Write32(0xE0002008, value);       // Set BP0 to Reset Vector
      value = FPB_KEY | FPB_ENABLE;
      Write32(0xe0002000, value);       // Enable FPB
    </block>
  </control>

  <control if="resetVect &gt;= 0x20000000" info="Enable reset vector catch">
    <block>
      // Enable Reset Vector Catch in DEMCR
      value = Read32(DEMCR_Addr);
      Write32(DEMCR_Addr, (value | 0x00000001));
    </block>
  </control>

  <block>
    Read32(DHCSR_Addr);                   // Read DHCSR to clear potentially set DHCSR.S_RESET_ST bit
  </block>

</sequence>
```

**Example 2: ResetCatchClear**

The **ResetCatchClear** sequence from Example 1 can also be used with the Example 2: ResetCatchSet as there's no special handling additionally required.


**Example 3: Use the CPU halt indicator in ResetSystem**

The following custom Cortex-M implementation uses **__connection** bit 18 to force the CPU
to halt when requested by setting **C_HALT** in the Debug Halting Control and Status Register (DHCSR):

```
<sequence name="ResetSystem">
  <block>
    __var AIRCR_Addr = 0xE000ED0C;
    __var DHCSR_Addr = 0xE000EDF0;

    Write32(AIRCR_Addr, 0x05FA0004);  // Execute SYSRESETREQ via AIRCR
    DAP_Delay(100000);
  </block>

  <!-- Reset Recovery: Wait for DHCSR.S_RESET_ST bit to clear on read -->
  <control while="(Read32(DHCSR_Addr) &amp; 0x02000000)" timeout="500000"/>

  <!-- Force halt only if requested and DHCSR.S_HALT is clear -->
  <control if="(__connection &amp; 0x00040000) &amp;&amp; !(Read32(DHCSR_Addr) &amp; 0x00020000)">
    <block>
      // Write DBGKEY, C_DEBUGEN, and C_HALT to force debug halt
      Write32(DHCSR_Addr, 0xA05F0003);
    </block>
    <control while="!(Read32(DHCSR_Addr) &amp; 0x00020000)" timeout="500000"/>
  </control>
</sequence>
```

**Other modifications**

Additionally the reset behavior can be made configurable per project via custom global debug access variables and a *.dbgconf file. See dbg_sqns_dbgconf for additional details.

In some cases also the reset sequences (**ResetSystem,** **ResetProcessor,** **ResetHardware)** need to be adjusted to ensure proper bootloader handling. For example for debug authentication or bootloader configuration purposes. The actual implementation is very device and use case specific.
