---
id: "spec-implement-debug-sequences-enable-device-specific-debug-configurati"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Enable device-specific debug configurations"
summary: "The debug configuration options available in the debug IDEs mostly cover quite generic scenarios applicable to a wide set of devices and architectures, for example whether to use reset for debug connection and what type of reset, whether …"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

The debug configuration options available in the debug IDEs mostly cover quite generic scenarios applicable to a wide set of devices and architectures, for example whether to use reset for debug connection and what type of reset, whether to stop after debug connection or not and so on. dbg_setup_access describes how to use debug descriptions to specify the configuration options available for the device and how to pre-select the default values.

But often there is a need to provide developers with some debug configuration options that are very device-specific. This can vary from simple SWO pin and clock source selection for tracing to more complex bootloader configuration or secure debug provisioning and multi-core system debug.

The `<debugvars>` element allows to define custom global debug access variables. Their values can also be made configurable via  a project-specific debug configuration file (***.dbgconf**). It is recommended to implement this file with Configuration Wizard annotations to enable simple graphical configuration view. default_sequences can be overwritten where needed and use the custom debug variables. If a user-defined global access variable is not specified in the *.dbgconf file, then the value provided in the variable definition in the pdsc file is applied.

Documentation for the `<debugvars>` provides an example for trace SWO pin selection via a *.dbgconf file. Below is also an example that uses a custom global debug variable **Dbg_CR** for specifying whether the program shall stop after bootloader execution or not:

** Use of debugvars in a pdsc file: **

```
...
  <debugvars configfile="Debug/LPC84x.dbgconf">>
    __var Dbg_CR = 0x00000000;  // DBG_CR, with default value 0x00000000
  </debugvars>
  ...
    // ResetCatchSet Sequence LPC84x
    <sequence name="ResetCatchSet">
      ... // initial setup

      <control if="Dbg_CR == 0x00000000" info="Stop after bootloader disabled">
        <block>
          value = Read32(DEMCR_Addr);
          Write32(DEMCR_Addr, (value | 0x00000001));                     // Enable Reset Vector Catch in DEMCR
        </block>
      </control>

      <control if="Dbg_CR == 0x00000001" info="Stop after bootloader enabled">
        <block>
          value = Read32(DEMCR_Addr);
          Write32(DEMCR_Addr, (value &amp; (~0x00000001)));              // Disable Reset Vector Catch in DEMCR
        </block>
      </control>
      ...
    </sequence>
  ...
```

***.dbgconf file: source code**
```

// <<< Use Configuration Wizard in Context Menu >>>

// <h>Debug Configuration
//   <o.0>    StopAfterBootloader       <i> Stop after Bootloader
// </h>
Dbg_CR = 0x00000001;

// <<< end of configuration section >>>

```

***.dbgconf file: Configuration Wizard view**



In the same way custom debug variables can be used to provide configuration for device-specific debug registers that then can be programmed via debug sequences.
