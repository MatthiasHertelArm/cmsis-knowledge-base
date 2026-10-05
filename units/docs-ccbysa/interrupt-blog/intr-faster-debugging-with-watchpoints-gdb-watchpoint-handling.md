---
id: "intr-faster-debugging-with-watchpoints-gdb-watchpoint-handling"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: How do watchpoints work? / GDB Watchpoint Handling"
summary: "Let's start by taking a look at how watchpoints are handled with GDB. We'll employ a similar strategy to what we used investigating how breakpoints work. We'll briefly recap the important parts here."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#gdb-watchpoint-handling"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How do watchpoints work?_

Let's start by taking a look at how watchpoints are handled with GDB. We'll employ a similar strategy to what we used investigating [how breakpoints work](https://interrupt.memfault.com/blog/cortex-m-breakpoints#gdb-breakpoint-handling). We'll briefly recap the important parts here.

At a high level, `gdb` (the "client") interfaces with the embedded MCU via a `gdbserver` (in our case SEGGER's JLinkGDBServer). The protocol talked between the gdb "client" and the gdb "server" is referred to as "GDB Remote Serial Protocol" (**GDB RSP**)[^4].

If we take a look at the GDB RSP docs we will find that the ['z' packets](https://sourceware.org/gdb/onlinedocs/gdb/Packets.html#index-z-packet) are used to configure watchpoints.

#### GDB RSP Watchpoint Command

The format for enabling and disabling watchpoints is `‘Z/z addr,kind’`. `kind` specifies the number of bytes after `addr` that will be watched and we have the following options:

| GDB Remote Serial Packet | Operation                                       |
| ------------------------ | ----------------------------------------------- |
| `Z2,addr,kind`           | Add Read Watchpoint at `addr`                   |
| `z2,addr,kind`           | Remove Read Watchpoint at `addr`                |
| `Z3,addr,kind`           | Add Write Watchpoint at `addr`                  |
| `z3,addr,kind`           | Remove Write Watchpoint at `addr`               |
| `Z4,addr,kind`           | Add Access (Read/Write) Watchpoint at `addr`    |
| `z4,addr,kind`           | Remove Access (Read/Write) Watchpoint at `addr` |

#### Debugging GDB Remote Serial Protocol

Now we can take a look at the actual **GDB RSP** commands that get sent over the wire when we install a watchpoint and compare against the table above. GDB has a builtin debug command, `set debug remote 1`, which can be used to dump this trace.

#### GDB RSP while Setting Watchpoints

Let's flip on **GDB RSP** debug tracing, install a watchpoint, and see what happens!

```
(gdb) set debug remote 1
(gdb) watch *(uint8_t[4] *)&g_array
Sending packet: $m200029a0,4#8b...Packet received: 00000000
Sending packet: $m200029a0,4#8b...Packet received: 00000000
Hardware watchpoint 2: *(uint8_t[4] *)&g_array
```

We see some [`m` packets](https://sourceware.org/gdb/onlinedocs/gdb/Packets.html#index-m-packet)
(`m addr,length`). These are used for requesting reads of memory but no watchpoint set commands yet.
These reads are used to cache the "old value" for the data range being watched that we discussed [above](#gdb-implementation-quirks).

Let's `continue` and see what happens:

```
(gdb) continue
Continuing.
Sending packet: $m200029a0,4#8b...Packet received: 00000000
=> Sending packet: $Z2,200029a0,4#d6...Packet received: OK
Packet Z2 (write-watchpoint) is supported
Sending packet: $c#63...
```

We see a `$Z2,200029a0,4` request issued which means "install a software watchpoint for writes between address 0x200029a0 - 0x200029a4". This matches the address of `g_array` so that's what we'd expect! It looks like watchpoints are only installed when we resume just like breakpoints.

#### GDB RSP when a Watchpoint Triggers

Now let's actually cause the watchpoint to be triggered by using the same `arr_write` command from above to write a new value into the array:

```
shell> arr_write 0 1
Write - Addr: 0x200029a0, Index: 0, Value: 0x00000001
# Debugger should have halted
```

```
=> Packet received: T05watch:200029A0;thread:0000DEAD;
...
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $z2,200029a0,4#f6...Packet received: OK
...
Sending packet: $s#73...Packet received: T05watch:00000000;thread:0000DEAD;
...
Sending packet: $m200029a0,4#8b...Packet received: 01000000
...

Hardware watchpoint 1: *(uint8_t[4] *)&g_array

Old value = "\000\000\000"
New value = "\001\000\000"
Sending packet: $m886,4#73...Packet received: e2e7a718
0x00000886 in prv_arr_write (Sending packet: $m20001f80,40#be...Packet received: c41b0000c30600009c280020a6280020a82800200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Sending packet: $m6c2,4#98...Packet received: b1e79428
argc=<optimized out>, argv=<optimized out>) at ./src/shell_commands.c:140
140   return 0;
```

We can see from the trace above that a watchpoint debug event took place. This is conveyed by the
[`T AA n1:r1;n2:r2;…`](https://sourceware.org/gdb/onlinedocs/gdb/Stop-Reply-Packets.html#Stop-Reply-Packets)
Stop Reply Packet where `T` indicates a signal was received and `watch` indicates a hardware
watchpoint was the event type.

There's also a single step (the `s` instruction). For Cortex-M's this doesn't serve any real purpose but watchpoints take a similar code path to breakpoints. For breakpoints, the single step _is_ necessary so we are likely just picking up the behavior for that.

##### Recovering Instruction Triggering Watchpoint

> TIP: When a watchpoint event is triggered the `$pc` has already advanced to the next instruction. With the additional single step we saw above, it means by the time the system halts we are two instructions past where the load or store occurred. In this particular example we can see it was a `strb` instruction that triggered the watchpoint by looking at the assembly in GDB:
>
> ```
> (gdb) disassemble $pc
> ...
> 0x000008f2 <+70>:	strb	r5, [r6, r4]
> 0x000008f4 <+72>:	movs	r0, #0
> => 0x000008f6 <+74>:	b.n	0x8be <prv_arr_write+18>
> ```

Finally, we see a request to remove the watchpoints was sent (`$z2,240,2`). Removing watchpoints
reduces the probability of the debugger getting killed and leaving the system in a state where watchpoints are left installed.

#### GDB RSP when Continuing After a Watchpoint Trigger

```bash
(gdb) c
Continuing.
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $Z2,200029a0,4#d6...Packet received: OK
Sending packet: $Hc0#db...Packet received: OK
Sending packet: $c#63...
```

Nothing too exciting here. We see that the watchpoint is re-enabled with the `Z2` command and the system is resumed.

#### Setting the same value

We can write the same value again and confirm the system does **not halt**. We can however see that there is GDB RSP traffic between the server and client handling the auto resumption:

```
shell> arr_write 0 1
Write - Addr: 0x200029a0, Index: 0, Value: 0x00000001
shell>
```

```
Packet received: T05watch:200029A0;thread:0000DEAD;
[...]
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $z2,200029a0,4#f6...Packet received: OK
Sending packet: $Hcdead#39...Packet received: OK
Sending packet: $s#73...Packet received: T05watch:00000000;thread:0000DEAD;
[...]
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $m200029a0,4#8b...Packet received: 01000000
Sending packet: $Z2,200029a0,4#d6...Packet received: OK
Sending packet: $Hc0#db...Packet received: OK
Sending packet: $c#63...
```
