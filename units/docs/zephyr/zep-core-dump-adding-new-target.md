---
id: "zep-core-dump-adding-new-target"
type: "concept"
domain: "debug"
title: "Core Dump: Adding New Target"
summary: "The architecture-specific block is target specific and requires new dumping routine and parser for new targets. To add a new target, the following needs to be done:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/coredump.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/coredump.rst"
license: "Apache-2.0"
mode: "V"
---

The architecture-specific block is target specific and requires new
dumping routine and parser for new targets. To add a new target,
the following needs to be done:

#. Add a new target code to the `enum coredump_tgt_code` in
   `include/zephyr/debug/coredump.h`.
#. Implement `arch_coredump_tgt_code_get` simply to return
   the newly introduced target code.
#. Implement `arch_coredump_info_dump` to construct
   a target architecture block and call `coredump_buffer_output`
   to output the block to core dump backend.
#. Add a parser to the core dump GDB stub scripts under
   `scripts/coredump/gdbstubs/`

   #. Extends the `gdbstubs.gdbstub.GdbStub` class.
   #. During `__init__`, store the GDB signal corresponding to
      the exception reason in `self.gdb_signal`.
   #. Parse the architecture-specific block from
      `self.logfile.get_arch_data()`. This needs to match the format
      as implemented in step 3 (inside `arch_coredump_info_dump`).
   #. Implement the abstract method `handle_register_group_read_packet`
      where it returns the register group as GDB expected. Refer to
      GDB's code and documentation on what it is expecting for
      the new target.
   #. Optionally implement `handle_register_single_read_packet`
      for registers not covered in the `g` packet.

#. Extend `get_gdbstub()` in
   `scripts/coredump/gdbstubs/__init__.py` to return
   the newly implemented GDB stub.
