---
id: "spec-debug-description-examples-of-non-standard-debug-access-se"
type: "concept"
domain: "pack"
title: "Debug Description: Examples of non-standard debug access sequences"
summary: "This section provides examples of user-implemented predefined debug access sequences."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

This section provides examples of user-implemented predefined debug access sequences.


### User implementation of TraceStart sequence


```
<sequence name="TraceStart">
  <block>
    __var value      = 0;
  
    //Enable SWO
    value = Read8(0x40004D2A);
    Write8(0x40004D2A, (value | 0x20));         // Set the register
    value = Read8(0x40004D2C);
    Write8(0x40004D2C, (value &amp; (~0x20)));  // Clear the register
  </block>
</sequence>
```



### User implementation of DebugDeviceUnlock sequence


```
<sequence name="DebugDeviceUnlock">
  <block>
    __var DAuthUserInput   = 0;
    __var DAUTHSTATUS_Val  = 0;
    __var DHCSR_Val        = 0;
    __var SecureDebugEna   = 0;
    __var SecureDebugAvail = 0;
    __var DAuthVal         = 0;
    __var Status           = 0;  // AP Status value
 
    DAUTHSTATUS_Val  = Read32(0xE000EFB8);
    DHCSR_Val        = Read32(0xE000EDF0);
    DAP_Delay(100000);
    SecureDebugAvail = (DAUTHSTATUS_Val &amp; 0x00000020) ? 1 : 0;  // SID: Secure Invasive Debug Implemented
    Status = ReadAP(0x0);                                           // Read Status register
  </block>
 
  <control if="SecureDebugAvail" info="Configure Debug Authentication if Security Extensions available">
    <block>
      SecureDebugEna = ((DHCSR_Val &amp; 0x00100000) || ((DAUTHSTATUS_Val &amp; 0x00000030) == 0x00000030)) ? 1 : 0;
    </block>
 
    <control if="DAuthFixed">
      <block>
        // Debug Authentication as per Debug Configuration File
        DAuthVal = DAuthConfig;
      </block>
    </control>
    <control if="DAuthFixed == 0">
      <block>
        DAuthUserInput = Query(1, "Enable Secure Debug?", 3);
      </block>
      <control if="DAuthUserInput == 3">
        <block>
          // Enable Secure Debug
          DAuthVal = 0xF;
        </block>
      </control>
      <control if="DAuthUserInput != 3">
        <block>
          // Disable Secure Debug
          DAuthVal = 0x3;
        </block>
      </control>
    </control>
 
    <control if="SecureDebugEna">
      <block>
        // Setup Secure Debug
        Write32(0x50007000, DAuthVal);
      </block>
    </control>
    <control if="SecureDebugEna == 0">
      <control if="DAuthVal &amp; 0x4">
        <block>
          Query(0, "Cannot configure Debug Authentication, secure debug disabled! Please reboot FPGA!", 1);
        </block>
      </control>
    </control>
  </control>
</sequence>
```



### User implementation of hardware reset sequence


```
<sequence name="HWReset">
  <block>
    __var protType = __protocol &amp; 0x0000FFFF;
  </block>
 
  <!-- JTAG variant-->
  <control if="protType == 1">
    <block atomic="true">
      // HW Reset Pulse
      DAP_SWJ_Pins(0x00, 0x80, 0);
      DAP_Delay(50000);
      DAP_SWJ_Pins(0x80, 0x80, 0);
 
      // Wait at least 200us
      DAP_Delay(200);
 
      // Register to SSW (Start-up Software) within 2ms
 
      // JTAG Reset
      DAP_JTAG_Sequence(6, 1, 0x7F);
      DAP_JTAG_Sequence(1, 0, 0x01);
 
      // Request Debug and System Power-Up
      WriteDP(0x4, 0x50000F00);
 
      // Init DP SELECT register
      WriteDP(0x8, 0x00000000);
 
      // Init AP CSW register
      WriteAP(0x00, 0x23000052);
 
      // Set TAR register to DHCSR address
      WriteAP(0x4, 0xE000EDF0);
 
      // Enable core debug (finishes tool register process)
      WriteAP(0xC, 0xA05F0001);
 
      // SSW will configure a HW BP0 at User Code start
    </block>
  </control>
  
  ...
  
</sequence>
```



### Calling sequences in a control block


```
...
<control if="siliconRevision &gt;= 3" >
  <block>                                                 
    Sequence("SecurityUnlock");                           // Execute TAP Sequence according to SiliconRevision
    Sequence("Set_JTAG_CTL");
    Sequence("WaitIdleState");
    Sequence("SetIDCODES");
  </block>
</control>
...
```



### Selecting an FLM algorithm for flash operations


The optional **FlashEraseSetup** and **FlashProgramSetup** sequences are evaluated only for erase and program phases associated
with flashinfo regions. They are not used when the target defines no **flashinfo** regions. The sequences
can select an FLM algorithm for an erase or program phase. The debugger provides **__FlashAddr** and **__FlashLen** to identify the
requested address range. The following examples select an FLM only when the complete range is within the external flash region.
When the condition is false, the corresponding operation uses the flash debug sequences.


#### FlashEraseSetup example


```
<sequence name="FlashEraseSetup">
  <control if="(__FlashAddr &gt;= 0x60000000) &amp;&amp; ((__FlashAddr + __FlashLen) &lt;= 0x61000000)"
           info="Select FLM for external flash erase">
    <block>
      FlashLoadAlgorithm("$S/Flash/ExternalFlash.FLM", 0x20000000, 0x00008000);
    </block>
  </control>
</sequence>
```



#### FlashProgramSetup example


```
<sequence name="FlashProgramSetup">
  <control if="(__FlashAddr &gt;= 0x60000000) &amp;&amp; ((__FlashAddr + __FlashLen) &lt;= 0x61000000)"
           info="Select FLM for external flash programming">
    <block>
      FlashLoadAlgorithm("$S/Flash/ExternalFlash.FLM", 0x20000000, 0x00008000);
    </block>
  </control>
</sequence>
```
