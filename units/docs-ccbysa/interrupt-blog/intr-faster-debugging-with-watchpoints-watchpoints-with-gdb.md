---
id: "intr-faster-debugging-with-watchpoints-watchpoints-with-gdb"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: Watchpoints with GDB"
summary: "Almost all debuggers expose some way to configure watchpoints via their interface. For GDB, this is done through the watch <expr> command, which will configure a watchpoint for the address described in <expr>."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#watchpoints-with-gdb"
license: "CC-BY-SA-4.0"
mode: "V"
---

Almost all debuggers expose some way to configure watchpoints via their interface. For GDB, this is done through the `watch <expr>` command, which will configure a watchpoint for the address described in `<expr>`. GDB also exposes a `rwatch` command (for data breakpoints on read accesses) and `awatch` (for data breakpoints on read or write accesses).

In the following sections we will walk through configurations and examples for monitoring changes to the following C variable.

```c
uint8_t g_array[17]
```

```
(gdb) p &g_array
$1 = (volatile uint8_t (*)[17]) 0x200029a0 <g_array>
```

### Commands

#### Watch for writes to a variable

```
(gdb) watch g_array
```

The above _should_ trigger a watchpoint when a write takes place anywhere in `g_array`.

> Tip: Watchpoint tracing is dependent on the functionality supported by the hardware. Watching
> data of completely arbitrary sizes is typically not supported by hardware. For best reliability
> on embedded systems, I recommend using watchpoints with sizes of native types (byte, half-word,
> and word). We will walk through these limitations for ARM Cortex-M in the sections below or you
> can find more details in the architecture reference manual. [^10]

#### Watch for writes to an address

```
(gdb) watch *(uint32_t *)0x200029a0
```

The above will trigger a watchpoint when a write takes place anywhere between `0x200029a0` & `0x200029a4`.

#### Watch for writes to an array

```
(gdb) watch *(uint8_t[2] *)0x200029a0
```

The above will trigger a watchpoint when a write takes place anywhere between `0x200029a0` & `0x200029a2`.


#### Watch for reads to an array

```
(gdb) rwatch *(uint8_t[2] *)0x200029a0
```

The above will trigger a watchpoint when a read takes place anywhere between `0x200029a0` &
`0x200029a2`.


### Example

The example app has two CLI commands we can use to test configuring watchpoints:

- `arr_read [idx]` to read a byte at the given index
- `arr_write [idx] [val]` to write a byte value at a given index.

#### Write Watchpoint Example

Let's start by configuring a write watchpoint on the first two bytes of `g_array`:

```
(gdb) watch *(uint8_t[2] *)0x200029a0
Hardware watchpoint 1: *(uint8_t[2] *)0x200029a0
(gdb) continue
```

We can then perform read and writes on `g_array` from the CLI:

```bash
shell> arr_read 0
Read - Addr: 0x200029a0, Index: 0, Value: 0x00000000
# Nothing happens on the read since we
# have only installed a "write" watchpoint
shell> arr_write 5 1
Write - Addr: 0x200029a5, Index: 5, Value: 0x00000001
# Nothing happened above because we
# are outside the range being watched
shell> arr_write 0 1
Write - Addr: 0x200029a0, Index: 0, Value: 0x00000001
# Debugger should have halted
```

In the last command we changed the value at array index 1 which should have triggered a halt:

```
(gdb) c
Continuing.

Hardware watchpoint 1: *(uint8_t[2] *)0x200029a0

Old value = "\000"
New value = "\001"
0x000008f6 in prv_arr_write () at ./src/shell_commands.c:153
153   return 0;
```

#### Read Watchpoint Example

We can also add a watchpoint that will only trigger on a read access using `rwatch`. Let's try it out:

```
(gdb) rwatch *(uint8_t[4] *)0x200029a0
(gdb) continue
```

Now if we try a read we will see a halt:

```bash
shell> arr_read 2
# Debugger should have halted
```

```
Hardware read watchpoint 2: *(uint8_t[4] *)0x200029a0

Value = "\001\000\000"
0x00000892 in prv_arr_read () at ./src/shell_commands.c:129
(gdb)
```

{: #gdb-implementation-quirks}

#### GDB Watchpoint Implementation Quirk

When you install a watchpoint with GDB it will immediately do a read of the current values for that range. Every time a hardware watchpoint event is generated it will re-read the region so it can show you the "New value" alongside the "Old value". If both values are equal, GDB will suppress the debug event generated and auto-resume the processor[^12]. This is generally not a problem but can be confusing if you are testing watchpoint functionality or actually want to track every access.
