---
id: "spec-implement-debug-sequences-implement-reset-for-debug-access"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Implement reset for debug access"
summary: "This section explains reset debug sequences for systems with a single CPU. Multi-core specifics are covered in dbgsqnsmulticore."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

This section explains reset debug sequences for systems with a single CPU. Multi-core specifics are covered in dbg_sqns_multicore.

Reset is an important part of debug operation and is used to bring the device into a known state from which debug connection can be reliably established. Reset also allows users to debug their code from the very beginning. In the typical case when user initiates a debug session the debugger connects to the device, and resets the processor to ensure its fresh start, and then stops the CPU before user application is started.

Sometimes it is needed to connect to a running target ("hot debug") without any resets performed when establishing a debug connection. Since there is no resets this is out of scope for the current section.

The figure below shows an example reset flow in a debugger (copied from usage_of_sequences):



**CPU halt and ResetCatchSet**

In the flow shown above the debugger first decides whether to halt the processor after the reset or not. This decision depends on the project configuration but also on when and how the reset is requested (automatically by debugger during or after debug connect, or manually by user through IDE, etc.).

If processor halt after reset is needed then resetCatchSet sequence is executed before performing the reset operation. Default implementation of **ResetCatchSet** enables and configures Cortex-M Reset Vector Catch functionality so that the core is stopped right after reset thus allowing users to debug the program from the very start. In some cases **ResetCatchSet** needs to be overwritten, for example for dbg_sqns_boot.

**Reset types**

There are 3 predefined reset types and a custom reset type that debugger chooses from when performing a reset. The choice depends on the project configuration and defaultResetSequence value. Corresponding reset debug sequence is executed to perform required reset type.

The reset types are listed below with details described in the referenced documentation.

 - ResetHardware is a system-wide reset without debug domain executed via the dedicated debugger reset line, e.g. nRST.
 - ResetSystem is a software-triggered system-wide reset that preserves established debug connection.
 - ResetProcessor is a software-triggered local reset for a processor only.
 - **CustomResetName** sequence is used when a user-defined debug sequence is assigned to the defaultResetSequence attribute. This can be implemented when very special reset type is needed that cannot be performed by modifying predefined reset types.

**Resynchronize cached AP registers after reset**

A reset might clear AP registers such as the CSW. If the host debugger caches the AP CSW to accelerate memory accesses,
the cached value must be resynchronized before the next memory access. The following device-specific **ResetSystem** example
performs an explicit AP CSW read after the reset delay. As described in DebugRegisterCaching, `ReadAP` updates the
debugger's internal AP CSW cache with the value read from the target:

```
<sequence name="ResetSystem">
  <block>
    // System Control Space (SCS) offset as defined in Armv6-M/Armv7-M.
    __var SCS_Addr   = 0xE000E000;
    __var AIRCR_Addr = SCS_Addr + 0xD0C;
    __var DHCSR_Addr = SCS_Addr + 0xDF0;

    // Execute SYSRESETREQ via AIRCR.
    Write32(AIRCR_Addr, 0x05FA0004);

    // Delay for 100 ms to let the system reset complete.
    DAP_Delay(100000);

    // Read AP CSW from the target and refresh the debugger's internal cache.
    ReadAP(0x00);
  </block>

  <!-- Reset Recovery: Wait for DHCSR.S_RESET_ST bit to clear on read. -->
  <control while="(Read32(DHCSR_Addr) &amp; 0x02000000)" timeout="500000"/>
</sequence>
```


**CPU halt and ResetCatchClear**

After reset is performed and the processor is halted (on the breakpoint enabled in **ResetCatchSet)** the resetCatchClear sequence is executed. The default implementation may need to be overwritten to support bootloader as explained in dbg_sqns_boot.
