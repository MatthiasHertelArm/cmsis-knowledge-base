---
id: "intr-how-do-breakpoints-even-work-gdb-breakpoint-handling"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: GDB Breakpoint Handling"
summary: "Let's start by taking a look at how breakpoints are handled with GDB."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#gdb-breakpoint-handling"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's start by taking a look at how breakpoints are handled with GDB.

> A full discussion of debug interfaces is outside the scope of this article but more details can be found in [our post on the topic](https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces). We'll recap the parts relevant to this post below.

At a high level, `gdb` (the "client") interfaces with the embedded MCU via a `gdbserver` (in our case SEGGER's JLinkGDBServer). The protocol talked between the gdb "client" and the gdb "server" is referred to as "GDB Remote Serial Protocol" (**GDB RSP**)[^4].

If we take a look at the GDB RSP docs we will find that the ['z' packets](https://sourceware.org/gdb/onlinedocs/gdb/Packets.html#index-z-packet) are used to configure breakpoints.

#### GDB RSP Breakpoint Command

The format of the commands are `‘Z/z type,addr,kind’` where:

| GDB Remote Serial Packet | Operation                            |
| ------------------------ | ------------------------------------ |
| `Z0,addr,kind`           | Add Software Breakpoint at `addr`    |
| `z0,addr,kind`           | Remove Software Breakpoint at `addr` |
| `Z1,addr,kind`           | Add Hardware Breakpoint at `addr`    |
| `z1,addr,kind`           | Remove Hardware Breakpoint at `addr` |

`kind` is architecture specific but for ARM it indicates what instruction to use. (The instruction changes depending on whether the MCU uses the ARM or Thumb instruction set).[^9]

> NOTE: The use of "software" breakpoint in GDB RSP is a bit of a misnomer. The gdbserver can choose how to best install the breakpoint. For example, the server may opt to install a "software" breakpoint as a hardware breakpoint if there are still ones available.

### Debugging GDB Remote Serial Protocol

With that out of the way, let's take a look at the actual **GDB RSP** commands that get sent over the wire when we install a breakpoint. Conveniently GDB has a builtin debug command, `set debug remote 1`, which can be used to enable printing of every single command sent between the client and server!

To facilitate breakpoint testing, I've added `dummy_function_1` through `dummy_function_9` to my
program that we can set breakpoints for. All the functions do is print the name of the
function being executed:

```c
void dummy_function_3(void) {
  EXAMPLE_LOG("stub function '%s' called", __func__);
}
```

I also added `dump_dummy_funcs` to the firmware CLI to print information about them all:

```
shell> dump_dummy_funcs
dummy_function_1: Starts at 0x240. First Instruction = 0x48024901
dummy_function_2: Starts at 0x250. First Instruction = 0x48024901
dummy_function_3: Starts at 0x260. First Instruction = 0x48024901
dummy_function_4: Starts at 0x270. First Instruction = 0x48024901
dummy_function_5: Starts at 0x280. First Instruction = 0x48024901
dummy_function_6: Starts at 0x290. First Instruction = 0x48024901
dummy_function_7: Starts at 0x2a0. First Instruction = 0x48024901
dummy_function_8: Starts at 0x2b0. First Instruction = 0x48024901
dummy_function_9: Starts at 0x2c0. First Instruction = 0x48024901
dummy_function_ram: Starts at 0x20000000. First Instruction = 0x48024901
```

We dump the name and address to make it easier to correlate the function address with the **GDB RSP** and we dump
the first couple instructions so we can easily check if a software breakpoint was installed (if the
code was patched, the first instruction will change).

We can confirm that after a flash bootup, the info printed via the CLI matches what we see when
dumping the info from the ELF file. For example:

```bash
$ arm-none-eabi-objdump --disassemble=dummy_function_1 build/nrf52.elf
[...]
00000240 <dummy_function_1>:
 240:	4901        ldr	r1, [pc, #4]	; (248 <dummy_function_1+0x8>)
 242:	4802        ldr	r0, [pc, #8]	; (24c <dummy_function_1+0xc>)
```

`dummy_function_1` "Starts at 0x240" and "Instruction = 0x48024901" captures the first two 16-bit
instructions `0x4901` (`ldr r1, [pc, #4]`) and `0x4802` (`ldr r0, [pc, #8]`).

#### GDB RSP while Setting Breakpoints

Let's flip on **GDB RSP** debug tracing, install a breakpoint, and see what happens.

```bash
(gdb) set debug remote 1
(gdb) break dummy_function_1
Sending packet: $m80,4#35...Packet received: 2de9f341
Sending packet: $m240,40#93...Packet received:[...]
Sending packet: $m248,4#6b...Packet received: 2f730000
Sending packet: $m248,4#6b...Packet received: 2f730000
Sending packet: $m240,2#61...Packet received: 0149
Breakpoint 1 at 0x240: file stub_functions.c, line 4.
```

We see some [`m` packets](https://sourceware.org/gdb/onlinedocs/gdb/Packets.html#index-m-packet)
(`m addr,length`). These are used for requesting reads of memory but no breakpoint set commands?! Let's `continue` and see what happens:

```bash
(gdb) continue
Continuing.
(gdb) c
Continuing.
==> Sending packet: $Z0,240,2#aa...Packet received: OK
==> Packet Z0 (software-breakpoint) is supported
Sending packet: $vCont?#49...Packet received:
Packet vCont (verbose-resume) is NOT supported
Sending packet: $Hc0#db...Packet received: OK
Sending packet: $c#63...
```

We see a `$Z0,240,2` request issued which means "install a software breakpoint at address 0x240". This matches the address of `dummy_function_1` so that's what we'd expect! It looks like breakpoints are only installed when we resume.

#### GDB RSP when a Breakpoint Triggers

Now let's actually cause the breakpoint to be triggered by executing the function we installed the
breakpoint on. I've added a CLI command to the example project, `call_dummy_funcs` that simply
calls all the `dummy_function_*` routines in a row:

```
shell> call_dummy_funcs
[... GDB should have halted ...]
```

```bash
Sending packet: $c#63...Packet received: T05hwbreak:;thread:0000DEAD;
Sending packet: $g#67...Packet received:[...]
Sending packet: $qfThreadInfo#bb...Packet received: m0000dead
Sending packet: $qsThreadInfo#c8...Packet received: l
===>Sending packet: $z0,240,2#ca...Packet received: OK

Breakpoint 1, Sending packet: $m240,4#63...Packet received: 01490248
dummy_function_1 () at dummy_functions.c:4
4     EXAMPLE_LOG("stub function '%s' called", __func__);
```

We can see from the trace above that a breakpoint debug event took place. This is conveyed by the
[`T AA n1:r1;n2:r2;…`](https://sourceware.org/gdb/onlinedocs/gdb/Stop-Reply-Packets.html#Stop-Reply-Packets)
Stop Reply Packet where `T` indicates a signal was received and `hwbreak` indicates a hardware
breakpoint was hit.

> Note: The `thread:0000DEAD` conveys the "thread" the signal was generated on where 0000DEAD is the
> [thread-id](https://sourceware.org/gdb/onlinedocs/gdb/Packets.html#thread_002did-syntax). Since we are running a baremetal system, I think someone at SEGGER just had
> some fun and used `0xdead` as the id. In GDB the only place you see it reflected is as the "Target
> Id" when running `info threads`:
>
> ```
> (gdb) info threads
>  Id   Target Id         Frame
> * 1  Thread 57005 dummy_function_1 () at dummy_functions.c:4
> (gdb) p/x 57005
> $1 = 0xdead
> (gdb)
> ```

We also see a request to remove the breakpoint was sent (`$z0,240,2`). That's strange. We expect the breakpoint to keep firing once it has been installed. Let's continue from the breakpoint and see what happens:

#### GDB RSP when a Continuing After a Breakpoint Trigger

```bash
(gdb) c
Continuing.
Sending packet: $Hcdead#39...Packet received: OK
===>Sending packet: $s#73... Packet received: T05hwbreak:;thread:0000DEAD;
Sending packet: $g#67...Packet received: [...]
===>Sending packet: $Z0,240,2#aa...Packet received: OK
Sending packet: $Hc0#db...Packet received: OK
===>Sending packet: $c#63...
```

Breaking it down:

- an [`s` packet](https://sourceware.org/gdb/current/onlinedocs/gdb/Packets.html#index-s-packet) is sent to indicate that the debugger is requesting a single step
- The MCU generates a debug event and gdb receives a halt signal again (`T05hwbreak` packet).
- Our breakpoint on `dummy_function_1` is re-installed (`$Z0,240,2`).
- The continuation we requested in the first place is issued with the [`c` packet](https://sourceware.org/gdb/current/onlinedocs/gdb/Packets.html#index-c-packet).

Thinking about this, it starts to make sense. If GDB hadn't removed the breakpoint, the breakpoint
we had set would repeatedly fire when we try to continue. By single-stepping over the instruction while breakpoints are disabled we can get past the instruction which caused the breakpoint and re-enable all the breakpoints before we miss any new ones.

The other advantage of removing and adding back breakpoints anytime the system is halted is it reduces the probability of the debugger getting killed and leaving the system in a state where breakpoints are left installed.

> Fun Fact: GDB doesn't send the `s` packet for single-stepping on all targets. Some targets (such as arm-elf-linux-\*) use "software single stepping" where GDB will determine the next instruction itself and install a hardware breakpoint at that location. This can be useful if native single stepping is not supported. You can check if this mode is in use by dumping the gdb-specific arch information, `maintenance print architecture`, and looking to see if `gdbarch_software_single_step_p` is not a NULL pointer.
