---
id: "pyocd-command-reference-values"
type: "concept"
domain: "debug"
title: "Command reference: Values"
summary: "Command reference: Values"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#values"
license: "Apache-2.0"
mode: "V"
---

##### `set`

**Usage**: set NAME VALUE \
Set a value.


##### `show`

**Usage**: show NAME \
Display a value.



Value details
-------------

##### `accessible-pins`

**Access**: read-write \
**Usage**: show accessible-pins, set accessible-pins VALUE \
Display which debug probe pins can be read and written with the 'pins' value.

##### `aps`

**Access**: read-only \
**Usage**: show aps \
List discovered Access Ports.

##### `cores`

**Access**: read-only \
**Usage**: show cores \
Information about CPU cores in the target.

##### `debug-sequences`

**Access**: read-only \
**Usage**: show debug-sequences \
Show the available debug sequences from the target's DFP. Only available for CMSIS-Pack based targets.

##### `fault`

**Access**: read-only \
**Usage**: show fault \
Fault status information. By default, only asserted fields are shown. Add -a to command to show all fields.

##### `frequency`

**Access**: write-only \
**Usage**: set frequency VALUE \
Set SWD or JTAG clock frequency in Hertz. A case-insensitive metric scale suffix of either 'k' or 'm' is allowed, as well as a trailing "Hz". There must be no space between the frequency and the suffix. For example, "2.5MHz" sets the clock to 2.5 MHz.

##### `graph`

**Access**: read-only \
**Usage**: show graph \
Print the target object graph.

##### `hnonsec`

**Access**: read-write \
**Usage**: show hnonsec, set hnonsec VALUE \
The current HNONSEC attribute value used by the selected MEM-AP. This value controls whether memory transactions are secure or nonsecure. The value is an integer, either 0 or secure or 1 for nonsecure.

##### `hprot`

**Aliases**: `memap_attr` \
**Access**: read-write \
**Usage**: show hprot, set hprot VALUE \
The current memory transfer attributes value used by the selected MEM-AP. This integer value controls attributes of memory transfers. It is a direct mapping of the AHB
or AXI attribute settings, depending on the type of MEM-AP. For AHB-APs, the value is HPROT[4:0].
For AXI-APs, the value is {AxPROT[2:0], AxCACHE[3:0]}, e.g. AxPROT in bits 6-4 and AxCACHE in
bits 3-0. Not all MEM-AP implementations support all attributes. See the Arm Technical Reference
Manual for your device's MEM-AP for details.

##### `locked`

**Access**: read-only \
**Usage**: show locked \
Report whether the target is locked.

##### `log`

**Access**: write-only \
**Usage**: set log VALUE \
Set log level to one of 'debug', 'info', 'warning', 'error', 'critical'. If pyocd module names are provided as arguments after the log level then only those modules will have their log level changed.

##### `map`

**Access**: read-only \
**Usage**: show map \
Target memory map.

##### `mem-ap`

**Access**: read-write \
**Usage**: show mem-ap, set mem-ap VALUE \
The currently selected MEM-AP used for memory read/write commands. When the selected core is changed by the 'core' command, the selected MEM-AP is changed to match. This overrides a user-selected MEM-AP if different from the AP for the newly selected core.

##### `nreset`

**Access**: read-write \
**Usage**: show nreset, set nreset VALUE \
Current nRESET signal state. Accepts a value of 0 or 1.

##### `option`

**Access**: read-write \
**Usage**: show option, set option VALUE \
The current value of one or more session options. When setting, each argument should follow the form "NAME[=VALUE]".

##### `peripherals`

**Access**: read-only \
**Usage**: show peripherals \
List of target peripheral instances.

##### `pins`

**Access**: read-write \
**Usage**: show pins, set pins VALUE \
Current debug probe protocol I/O pin states. The pins value is a mask containing the state of all accessible protocol pins. See the `accessible-pins` value for protocol pins that can be read and written by the connected debug probe.

##### `probe-uid`

**Aliases**: `uid` \
**Access**: read-only \
**Usage**: show probe-uid \
Target's unique ID.

##### `register-groups`

**Access**: read-only \
**Usage**: show register-groups \
Display available register groups for the selected core.

##### `reset-type`

**Access**: read-write \
**Usage**: show reset-type, set reset-type VALUE \
Show reset configuration and all available reset types for each core. Set current reset type.

##### `step-into-interrupts`

**Aliases**: `si` \
**Access**: read-write \
**Usage**: show step-into-interrupts, set step-into-interrupts VALUE \
Display whether interrupts are enabled when single stepping. Set to 1 to enable.

##### `target`

**Access**: read-only \
**Usage**: show target \
General target information.

##### `vector-catch`

**Aliases**: `vc` \
**Access**: read-write \
**Usage**: show vector-catch, set vector-catch VALUE \
Show current vector catch settings. When setting, the alue is a concatenation of one letter per enabled source in any order, or 'all' or 'none'. (h=hard fault, b=bus fault, m=mem fault, i=irq err, s=state err, c=check err, p=nocp, r=reset, a=all, n=none).
