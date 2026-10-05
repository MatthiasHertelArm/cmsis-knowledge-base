---
id: "pyocd-python-api-notes"
type: "concept"
domain: "debug"
title: "python api: Notes"
summary: "You are encouraged to look through the code to see what additional functionality is available. The most interesting places to look at are:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md#notes"
license: "Apache-2.0"
mode: "V"
---

You are encouraged to look through the code to see what additional functionality is available. The
most interesting places to look at are:

- pyocd.core.target: defines Target class, which is the main API.
- pyocd.core.coresight_target: Represents the chip as a whole,
    provides access to DP and APs, as well as each of the cores.
- pyocd.coresight.cortex_m: CortexM class to control a core,
    implements Target API and adds some stuff.
- pyocd.flash.loader: high level flash programming of raw binary data.
- pyocd.flash.eraser: high level flash erasing.
- pyocd.flash.file_programmer: high level file programming.
- pyocd.flash.flash: low level flash programming API in the @ref pyocd.flash.flash.Flash "Flash"
    class. Each flash memory region has a @ref pyocd.flash.flash.Flash "Flash" class instance
    associated with it, accessible from the `flash` property on the region. To get the boot flash
    memory region, call `target.memory_map.get_boot_memory()`. The `flash` attribute of this region
    then returns the boot flash memory's @ref pyocd.flash.flash.Flash "Flash" instance.
