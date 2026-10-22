---
id: "pyocd-open-cmsis-pack-support-debug-access-sequences"
type: "concept"
domain: "debug"
title: "Open-CMSIS-Pack support: Debug access sequences"
summary: "Debug access sequences, simply called \"debug sequences\" below, contain a set of instructions to tell the debugger how to perform different debug related activities such as connect, reset, configuring the device for trace, and so on."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/open_cmsis_pack_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/open_cmsis_pack_support.md#debug-access-sequences"
license: "Apache-2.0"
mode: "V"
---

Debug access sequences, simply called "debug sequences" below, contain a set of instructions to tell the debugger how to perform different debug related activities such as connect, reset, configuring the device for trace, and so on. Silicon vendors can provide debug sequences for cases where their device has special control requirements or nonstandard behaviours. Many devices do not need debug sequences, and they are entirely optional.

A set of standard debug sequences is defined by the [Open-CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec) specification to be executed by the debugger when performing certain activities. Some of these standard sequences have pre-defined behavior performed by the debugger if the DFP does not override that sequence. Others sequences exist only to allow the DFP to insert custom actions.

In addition to the standard debug sequences, a DFP can define its own custom sequences. These can be called like subroutines by other sequences.

Any debug sequence can be customised per CPU core.


### Debug variables

Debug sequences frequently make use of configurable variables called debug variables, or debugvars for short. Depending on the debug sequence, these variables can be modified to change the values written into registers, adjust timeouts, or for other, similar purposes. In other debuggers such as Keil MDK, debugvars are read from a `.dbgconf` file. In pyOCD, this is handled through the `pack.debug_sequences.debugvars` session option described below.

The `pack.debug_sequences.debugvars` session option must be set to a string containing C-style variable assignment statements. C-compatible integer expressions are allowed, and can refer to previously defined variables. Only those debug variables whose value is being changed need to be assigned a value; others will retain their default value. This option is one that you'd normally set in a yaml config file rather than the command line.

All debugvars defined by the CMSIS-Pack and their configured value are logged (at the Info log level) during target connection.

This is an example of output for an ST Microelectronics STM32H750 MCU (target type name `stm32h750ibtx`) from the Keil.STM32H7_DFP pack:

```
0001360 I debugvar 'DbgMCU_APB1L_Fz1' = 0xffffffff (4294967295) [pack_target]
0001360 I debugvar 'DbgMCU_APB2_Fz1' = 0xffffffff (4294967295) [pack_target]
0001360 I debugvar 'DbgMCU_APB3_Fz1' = 0xffffffff (4294967295) [pack_target]
0001360 I debugvar 'DbgMCU_APB4_Fz1' = 0xffffffff (4294967295) [pack_target]
0001361 I debugvar 'DbgMCU_CR' = 0x7 (7) [pack_target]
0001361 I debugvar 'TraceClk_Pin' = 0x40002 (262146) [pack_target]
0001361 I debugvar 'TraceD0_Pin' = 0x40003 (262147) [pack_target]
0001361 I debugvar 'TraceD1_Pin' = 0x40004 (262148) [pack_target]
0001361 I debugvar 'TraceD2_Pin' = 0x40005 (262149) [pack_target]
0001361 I debugvar 'TraceD3_Pin' = 0x40006 (262150) [pack_target]
```

To override some `DBGMCU` register values configured by the above target, this could be added to the `pyocd.yaml` [configuration file]({% link _docs/configuration.md %}):

```yaml
pack.debug_sequences.debugvars: |
  DbgMCU_APB1L_Fz1 = 0xffffffff;
  DbgMCU_APB2_Fz1 = 0xffffffff;
  DbgMCU_APB3_Fz1 = 0xffffffff;
  DbgMCU_APB4_Fz1 = 0xffffffff;
```

If the `pack.debug_sequences.debugvars` session option is modified during a connection, the new debugvar values will be used for any further debug sequence invocations. However, changes to a configuration file on disk will not be reloaded at runtime.


### Disabling debug sequences

Like any software, DFPs and any contained debug sequences can have bugs. There may also be other cases where disabling a debug sequence is useful. PyOCD can be configured to disable debug sequences either as a whole or individually by using the following session options.

#### `pack.debug_sequences.enable`

This boolean session option globally controls debug sequence support. It defaults to True; setting to False will disable running of all debug sequences defined by the DFP for the chosen target.

#### `pack.debug_sequences.disabled_sequences`

If specific debug sequences need to be disabled, they can be specified with this option. From the command line, the value must be a comma-separated list of sequence names. When set in a YAML config file, the value must be a YAML list of sequence names (instead of a single comma-separated string value).

Disabled sequences can be restricted to a given core by appending a colon and processor name to the sequence's name (e.g., "ResetProcessor:cm4").

Only top-level sequences can be disabled individually. If a debug sequence is called from another sequence it will always be executed even if listed in this option.
