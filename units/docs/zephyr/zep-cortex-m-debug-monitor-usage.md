---
id: "zep-cortex-m-debug-monitor-usage"
type: "concept"
domain: "debug"
title: "Cortex-M Debug Monitor: Usage"
summary: "When monitor mode debugging is enabled, entering a breakpoint will not halt the processor, but rather generate an interrupt with ISR implemented under z_arm_debug_monitor symbol."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/debugmon.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/debugmon.rst"
license: "Apache-2.0"
mode: "V"
---

When monitor mode debugging is enabled, entering a breakpoint will not halt the
processor, but rather generate an interrupt with ISR implemented under
`z_arm_debug_monitor` symbol.  `CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK` config configures this interrupt
to be the lowest available priority, which will allow other interrupts to execute
while processor spins on a breakpoint.


### Using SEGGER-provided ISR


The ready implementation provided with `CONFIG_SEGGER_DEBUGMON` provides functionality
required to debug in the monitor mode using regular GDB commands.
Steps to configure SEGGER debug monitor:

1. Build a sample with `CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK`` and `CONFIG_SEGGER_DEBUGMON`
   configs enabled.

2. Attach JLink GDB server to the target.
   Example linux command: `JLinkGDBServerCLExe -device <device> -if swd`.

3. Connect to the server with your GDB installation.
   Example linux command: `arm-none-eabi-gdb --ex="file build/zephyr.elf" --ex="target remote localhost:2331"`.

4. Enable monitor mode debugging in GDB using command: `monitor exec SetMonModeDebug=1`.

After these steps use regular gdb commands to debug your program.



### Using other custom ISR

In order to provide a custom debug monitor interrupt, override `z_arm_debug_monitor`
symbol. Additionally, manual configuration of some registers is required
(see debugmon sample).
