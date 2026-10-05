---
id: "intr-faster-debugging-with-watchpoints-advanced-topics"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: Advanced Topics"
summary: "It's also possible to generate watchpoints from C code. Here's a function that does just that:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#advanced-topics"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Configuring Watchpoints in C Code

It's also possible to generate watchpoints from C code. Here's a function that does just that:

```c
void dwt_install_watchpoint(
    int comp_id, uint32_t func, uint32_t comp, uint32_t mask) {
  const size_t num_comparators = (DWT->CTRL>>28) & 0xF;
  if (comp_id > num_comparators) {
    EXAMPLE_LOG("Invalid COMP_ID of %d", comp_id);
    return;
  }

  sDwtCompCfg *config = &DWT->COMP_CONFIG[comp_id];
  config->COMP = comp;
  config->MASK = mask;
  // set last since this will enable the comparator
  config->FUNCTION = func;
}
```

For example, we can enable one over the first 16 bytes of the `g_array` at address `0x200029a0` that we were examining earlier:

```bash
shell> watchpoint_set 0 6 0x200029a0 4
# Access at offset 16 should not halt since we are only watching the first 16 bytes
shell> arr_write 16 1
Write - Addr: 0x200029b0, Index: 16, Value: 0x00000001

# Access to an array we are watch
shell> arr_write 15 2
Write - Addr: 0x200029af, Index: 15, Value: 0x00000002
# Debugger should have halted
```

As expected, our debugger halts:

```
Program received signal SIGTRAP, Trace/breakpoint trap.
prv_arr_write () at ./src/shell_commands.c:146
146   return 0;
(gdb)
```

One useful thing here is since the watchpoint is not registered through GDB or the gdbserver, the system will always halt when a watchpoint event is emitted by hardware. This means you can use watchpoint features not supported by the debugger (such as watchpoints of larger sizes).

### Extending Watchpoint Functionality with GDB Python

Since the DWT peripheral has some interesting configurations not natively supported with GDB, there's also an opportunity for us to extend the current behavior by making use of [GDB's Python API](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api)!

We'll add support for regular watchpoints with some extra validation to make sure we have requested a valid region and an example of a "data value" watchpoint under a `watch_ext` GDB CLI command. Below you can find the code needed in it's entirety:

```python
# gdb_watchpoint_ext.py
try:
    import gdb
except ImportError:
    raise Exception("This script can only be run within gdb!")

import argparse
import math
import struct


class DwtWatchpointException(Exception):
    pass


DWT_CTRL = 0xE0001000
DWT_COMP_BASE = 0xE0001020
DWT_MASK_BASE = 0xE0001024
DWT_FUNC_BASE = 0xE0001028


class Dwt:
    @staticmethod
    def _write_memory(addr, value):
        gdb.selected_inferior().write_memory(addr, struct.pack("<I", value))

    @classmethod
    def _write_dwt_comp_reg(cls, reg_base, comp_id, value):
        addr = reg_base + 16 * comp_id
        cls._write_memory(addr, value)

    @classmethod
    def set_addr_watchpoint(cls, addr, size):
        if addr % size != 0:
            raise DwtWatchpointException("Address needs to be aligned by size")
        if size & (size - 1) != 0:
            raise DwtWatchpointException("size must be power of 2")

        mask = int(math.log(size, 2))

        # For example purposes always use comparator 0 and overwrite
        # what was there previously.
        comp_id = 0
        cls._write_dwt_comp_reg(DWT_COMP_BASE, comp_id, addr)
        cls._write_dwt_comp_reg(DWT_MASK_BASE, comp_id, mask)
        func = 0x6  # Install a write watchpoint
        cls._write__write_dwt_comp_reg(DWT_FUNC_BASE, comp_id, func)

    @classmethod
    def set_data_value_watchpoint(cls, value, size):
        if size not in [1, 2, 4]:
            raise DwtWatchpointException(
                "Pattern watch must be a byte, half-word, or word in size"
            )

        # For values with a size less than a word, the value must be copied
        # into the other parts of the comparator register
        if size == 2:
            value = value | (value << 16)
        elif size == 1:
            value = value | value << 8 | value << 16 | value << 24

        # For Cortex-M4's data value matching is only supported in comparator 1
        comp_id = 1
        cls._write_dwt_comp_reg(DWT_COMP_BASE, comp_id, value)
        cls._write_dwt_comp_reg(DWT_MASK_BASE, comp_id, 0)

        # The range scanned can be filtered with other comparators
        # or disabled by setting the value to the comparator being
        # used. For this example, let's just disable:
        #   DATAVADDR0 (bits[19:16]) = comp_id
        #   DATAVADDR1 (bits[15:12]) = comp_id
        #
        # Rest of Config:
        #   DATAVSIZE (bits[11:10]) = size >> 1
        #   DATAVMATCH (bit[8]) = 1
        #     Encoding is 00 (byte), 01 (half-word), 10 (word)
        #   FUNCTION = 0x6 for a write-only watchpoint
        datavsize = (size >> 1) << 10
        func = (comp_id << 16) | (comp_id << 12) | (1 << 8) | datavsize | 0x6
        cls._write_dwt_comp_reg(DWT_FUNC_BASE, comp_id, func)


class GdbArgumentParseError(Exception):
    pass


class GdbArgumentParser(argparse.ArgumentParser):
    """Wrap argparse so gdb doesn't exit when a command fails """

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message)
        # Don't call sys.exit()
        raise GdbArgumentParseError()


class WatchpointExtensionCliCmd(gdb.Command):
    """Extension of  GDB's watch for Cortex-M """

    def __init__(self):
        super(WatchpointExtensionCliCmd, self).__init__("watch_ext", gdb.COMMAND_USER)

    def complete(self, text, word):
        # We expect the argument passed to be a symbol so fallback to the
        # internal tab-completion handler for symbols
        return gdb.COMPLETE_SYMBOL

    def invoke(self, unicode_args, from_tty):
        # We can pass args here and use Python CLI utilities like argparse
        # to do argument parsing
        parser = GdbArgumentParser(
            description="Additional Cortex-M Watchpoint Utilities"
        )

        parser.add_argument(
            "-c", "--comp", help="The memory address or value to watch for"
        )
        parser.add_argument("-s", "--size", help="The size to watch")
        parser.add_argument(
            "--compare-value",
            type=bool,
            help="Watch for value written instead of address written",
        )

        try:
            args = parser.parse_args(list(filter(None, unicode_args.split(" "))))
        except GdbArgumentParseError:
            return

        comp = int(args.comp, 0)
        size = int(args.size, 0)

        if not args.compare_value:
            print("Setting Address Watchpoint")
            Dwt.set_addr_watchpoint(comp, size)
        else:
            print("Setting Data Value Watchpoint")
            Dwt.set_data_value_watchpoint(comp, size)


WatchpointExtensionCliCmd()
```

The commands can be added to a GDB session by sourcing the script:

```
# Script is at $INTERRUPT_REPO/examples/watchpoints/gdb_watchpoint_ext.py
(gdb) source gdb_watchpoint_ext.py
```

This script implements two utilities:

- `watch_ext -c <address_to_watch> -s <size>`: This is equivalent to GDB's `watch *(uint8_t[`<size>`]
  *)<address_to_watch>` except that a helpful error is raised if the configuration requested is
  invalid due to the [limitations we discussed above](#watchpoint-limitations) and that the system
  will always halt on the write access rather than [only halting when a value changes](#gdb-implementation-quirks).
- `watch_ext -c <pattern_to_watch> -s <size> --compare-value`: This command will halt anytime
  `<pattern_to_watch>` is stored somewhere in RAM. The `size` is the size of the pattern and must
  be 1, 2, or 4 bytes. There's no way to configure something like this with GDB directly!

At the moment there is no command to disable the watchpoints once enabled or track "Old Value" and
"New Value" like GDB does natively. Both are do-able in GDB python and are left as an exercise to the reader.

### Data Value Watchpoint Example Using GDB Python

Inside the `math_example` CLI command, I've hidden a write of a special pattern when the recursion level is 10:

```c
  if (n == 10) {
    work_buf[0] = 0xbadcafe;
  }
```

Let's see if we can use the Cortex-M "data value" watchpoint functionality we added to the `watch_ext` command to halt when the `0xbadcafe` pattern is written:

#### Source the GDB Script

```
# Script is at $INTERRUPT_REPO/examples/watchpoints/gdb_watchpoint_ext.py
(gdb) source gdb_watchpoint_ext.py
(gdb) watch_ext --help
usage: [-h] [-c COMP] [-s SIZE] [--compare-value COMPARE_VALUE]

Additional Cortex-M Watchpoint Utilities

optional arguments:
  -h, --help            show this help message and exit
  -c COMP, --comp COMP  The memory address or value to watch for
  -s SIZE, --size SIZE  The size of the address to watch
  --compare-value COMPARE_VALUE
  Watch for value written instead of address written
```

#### Enable Data Value Watchpoint And Test

```
(gdb) watch_ext -c 0xbadcafe -s 4 --compare-value 1
Setting Data Value Watchpoint
(gdb) c
```

```bash
shell> math_example 30
Running math_function()
# Debugger should have halted
```

```
Program received signal SIGTRAP, Trace/breakpoint trap.
0x000007c6 in math_function (n=1006295455, n@entry=-1111622150) at ./src/shell_commands.c:82
82    for (size_t i = 0; i < sizeof(work_buf)/sizeof(work_buf[0]); i++) {
(gdb)
(gdb) p/x work_buf
$1 = {0xbadcafe, 0xa0a0a0a, 0xa0a0a0a}
```

Neat, we can see the system has halted on the write of the `0xbadcafe` pattern!
