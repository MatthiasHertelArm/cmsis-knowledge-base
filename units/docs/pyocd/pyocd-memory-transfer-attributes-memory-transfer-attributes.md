---
id: "pyocd-memory-transfer-attributes-memory-transfer-attributes"
type: "concept"
domain: "debug"
title: "Memory transfer attributes: Memory transfer attributes"
summary: "For Arm devices, the MEM-AP used to perform memory transfers is responsible for specifying what attributes are set when the transfer is performed. The AHB and AXI bus protocol standards define the set of possible transfer attributes."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/memory_attributes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/memory_attributes.md#memory-transfer-attributes"
license: "Apache-2.0"
mode: "V"
---

For Arm devices, the MEM-AP used to perform memory transfers is responsible for specifying what attributes are set when the transfer is performed. The AHB and AXI bus protocol standards define the set of possible transfer attributes. Then, which attributes are actually implemented varies greatly depending on the CPU type and MEM-AP type and variant.

The AHB-AP HPROT bits used with Cortex-M devices are shown here. "HPROT" is the name of the AHB protocol bus that carries the attributes along with the memory transfer request.

  HPROT      | (1) Enabled | (0) Disabled
-------------|-------------|-----------------
  `HPROT[0]` | data access | instr fetch
  `HPROT[1]` | privileged | user
  `HPROT[2]` | bufferable | non bufferable
  `HPROT[3]` | cacheable/modifable | non cacheable
  `HPROT[4]` | lookup in cache | no cache
  `HPROT[5]` | allocate in cache | no allocate in cache
  `HPROT[6]` | shareable | non shareable

Not all bits are implemented on all core/MEM-AP variants; each MEM-AP version implements slightly different sets of these options. For instance, the standard CM3 and CM4 MEM-AP only implements `HPROT[1]` (privileged/user). Check the documentation for your target and CPU(s) to verify available attributes.

AXI-AP attributes are much more complex and are not documented here.

Note that Cortex-M7 and other M-profile cores that use an AXI bus use an AHB-AP as the debugger interface, so the table above still applies. The core converts AHB attributes to AXI attributes internally if the debugger's memory transfer request needs to be sent on the downstream AXI bus.
