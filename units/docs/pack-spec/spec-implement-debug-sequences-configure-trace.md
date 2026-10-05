---
id: "spec-implement-debug-sequences-configure-trace"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Configure trace"
summary: "A common case that requires use of debug access sequences is trace configuration. default_sequences have two trace-related sequences: TraceStart and TraceStop that are being called when trace is enabled in the project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

A common case that requires use of debug access sequences is trace configuration. default_sequences  have two trace-related sequences: TraceStart and TraceStop that are being called when trace is enabled in the project. The `TraceStart` sequence is executed at the end of the initial debug connection to the target and after device reset while `TraceStop` is executed at the beginning of debug disconnect.

By default these sequences are empty and often need to be implemented in the .pdsc file to support device-specific behavior, for example to differentiate configuration for 1-pin SWO trace and 5-pin ETM trace (TPIU).

If the parent sequences element specifies **traceSetup=`full`**,
the trace-related debug access sequences are expected to perform the complete trace sink and trace data
path setup and shutdown, rather than only device-specific additions to debugger-provided CoreSight handling.

For example:

```
<sequence name="TraceStart">
  <block>
    // obtain project trace configuration from global variable __traceout
    __var traceSWO  = (__traceout &amp; 0x1) != 0;
    __var traceTPIU = (__traceout &amp; 0x2) != 0;
  </block>

  <control if="traceSWO">
    <block>
      Sequence("EnableTraceSWO");
    </block>
  </control>

  <control if="traceTPIU">
    <block>
      Sequence("EnableTraceTPIU");
    </block>
  </control>
</sequence>
```

Note that the code above uses following features allowed in debug access sequences:

  - read access to a predefined global debug access variable __traceout.
  - implements the pre-defined debug sequence `TraceStart`
  - calls custom debug sequences `EnableTraceSWO` ,`EnableTraceTPIU`

Implementation of custom debug access sequences `traceEnableSWO` and `traceEnableTPIU` is a means to better structure the sequence implementations. Their content is highly vendor and device-specific. Common functionality of such sequences is to trace on the device, configure trace clock and assign trace pin(s). But the complexity of the code varies significantly depending on the device functionalities.

Below is a simple example of `EnableTraceSWO` for Microchip SAMS70 family, that also demonstrates the use of a user-defined global debug access variable (`TracePCK3)` configurable via a debug configuration file `SAMx7.dbgconf.` See dbg_sqns_dbgconf for additional information about custom global debug variables and *.dbgconf file.

```
...
<family Dfamily="SAMV70" Dvendor="Microchip:3">
  <debugvars configfile="samv70/keil/debug/SAMx7.dbgconf" version="1.0.0">
    // Debug Access Variables
    __var TracePCK3 = 0x00000000;                // Trace Clock Source Selection and Prescaler
  </debugvars>

  <sequence name="EnableTraceSWO">
    <block>
      Write32(0x400E06E4, 0x504D4300);           // Disable PMC write protection
      Write32(0x400E064C, TracePCK3);            // Select clock source and prescaler for PCK3
      Write32(0x400E0600, (1 &lt;&lt; 11));      // Enable PCK3
    </block>
  </sequence>
  ...

```

Some devices can require that trace clock is enabled already at DebugDeviceUnlock sequence to ensure that access to global trace components is available when reading the ROM table and processor features. In such cases corresponding functionality needs to be moved from **TraceStart** to **DebugDeviceUnlock** sequence and check if trace is enabled via the **__traceout** variable.
