---
id: "zep-kernel-objects-object-placement"
type: "concept"
domain: "rtos"
title: "Kernel Objects: Object Placement"
summary: "Kernel objects that are only used by supervisor threads have no restrictions and can be located anywhere in the binary, or even declared on stacks."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

Kernel objects that are only used by supervisor threads have no restrictions
and can be located anywhere in the binary, or even declared on stacks. However,
to prevent accidental or intentional corruption by user threads, they must
not be located in any memory that user threads have direct access to.

In order for a static kernel object to be usable by a user thread via system
call APIs, several conditions must be met on how the kernel object is declared:

* The object must be declared as a top-level global at build time, such that it
  appears in the ELF symbol table. It is permitted to declare kernel objects
  with static scope. The post-build script gen_kobject_list.py scans the
  generated ELF file to find kernel objects and places their memory addresses
  in a special table of kernel object metadata.  Kernel objects may be members
  of arrays or embedded within other data structures.

* Kernel objects must be located in memory reserved for the kernel. They
  must not be located in any memory partitions that are user-accessible.

* Any memory reserved for a kernel object must be used exclusively for that
  object. Kernel objects may not be members of a union data type.

Kernel objects that are found but do not meet the above conditions will not be
included in the generated table that is used to validate kernel object pointers
passed in from user mode.

The debug output of the gen_kobject_list.py script may be useful when
debugging why some object was unexpectedly not being tracked. This
information will be printed if the script is run with the `--verbose` flag,
or if the build system is invoked with verbose output.
