---
id: "zep-kernel-objects-creating-new-kernel-object-types"
type: "concept"
domain: "rtos"
title: "Kernel Objects: Creating New Kernel Object Types"
summary: "When implementing new kernel features or driver subsystems, it may be necessary to define some new kernel object types. There are different steps needed for creating core kernel objects and new driver subsystems."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

When implementing new kernel features or driver subsystems, it may be necessary
to define some new kernel object types. There are different steps needed
for creating core kernel objects and new driver subsystems.


### Creating New Core Kernel Objects


* In `scripts/build/gen_kobject_list.py`, add the name of the struct to the
  :py`kobjects` list.

Instances of the new struct should now be tracked.


### Creating New Driver Subsystem Kernel Objects


All driver instances are `device`. They are differentiated by
what API struct they are set to.

* In `scripts/build/gen_kobject_list.py`, add the name of the API struct for the
  new subsystem to the :py`subsystems` list.

Driver instances of the new subsystem should now be tracked.
