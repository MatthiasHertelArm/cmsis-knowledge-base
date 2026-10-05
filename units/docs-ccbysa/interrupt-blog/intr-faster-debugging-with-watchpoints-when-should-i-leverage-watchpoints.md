---
id: "intr-faster-debugging-with-watchpoints-when-should-i-leverage-watchpoints"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: When should I leverage watchpoints?"
summary: "There's a variety of scenarios where watchpoints can be used creatively for debug. Let's walk through a couple of the most common use-cases through examples!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#when-should-i-leverage-watchpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a variety of scenarios where watchpoints can be used creatively for debug.
Let's walk through a couple of the most common use-cases through examples!

### Memory Corruption

Consider the following (albeit contrived) accelerometer driver:

```c
// accel.h
//! Processes raw accelerometer readings
void accel_process_reading(int x, int y, int z);

//! Prototype for handler invoked each time accel data
//! is processed
typedef void (*AccelSampleProcessedCallback)(void);

//! Register handler to be called when an accel
//! sample is processed
void accel_register_watcher(
    AccelSampleProcessedCallback data_processed_cb);
```

On boot, we register a watcher that gets notified as new accel samples are processed:

```c
// main.c
void accel_data_processed(void) {
  EXAMPLE_LOG("Accel Sample Processing Complete!");
  ...
}

int main(void) {
  prv_enable_vfp();
  uart_boot();

  accel_register_watcher(accel_data_processed);
  graphics_boot(s_graphics_buf, sizeof(s_graphics_buf));
  ...
}
```

Our (contrived) "driver" looks like this:

```c
static AccelSampleProcessedCallback s_data_processed_cb = NULL;

void accel_register_watcher(
    AccelSampleProcessedCallback data_processed_cb) {
  s_data_processed_cb = data_processed_cb;
}

void accel_process_reading(int x, int y, int z) {
  EXAMPLE_LOG("Processing Accel Reading ...");
  if (s_data_processed_cb == NULL) {
    return;
  }

  // ... process raw readings ...

  // notify consumer new data is available
  s_data_processed_cb();
}
```

I've wired up the `accel_example` CLI command to call `accel_process_reading()` so we can test it out:

```bash
shell> accel_example
accel_handle_reading()
# Debugger should have halted!
```

In GDB, we see:

```
(gdb)
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000950 in HardFault_Handler ()
```

That's strange, this code is extremely simple. What happened?! Let's add some breakpoints in the accel driver code to investigate.

```
(gdb) mon reset
(gdb) continue
(gdb) break accel_register_sample_handler
(gdb) break accel_example
(gdb) c
Continuing.

Breakpoint 1, accel_register_watcher (data_processed_cb=0x469 <accel_data_processed>) at ./src/accel_fake.c:17
17      AccelSampleProcessedCallback data_processed_cb) {
(gdb)
```

It looks like we are registering the handler, `accel_data_processed`, as expected. Let's continue and call accel_example again and we should hit our second breakpoint:

```bash
shell> accel_example
# debugger should have halted at
# accel_process_reading()
```

```
Breakpoint 2, accel_process_reading (x=x@entry=7, y=y@entry=1, z=z@entry=1) at ./src/accel_fake.c:22
22    EXAMPLE_LOG("Processing Accel Reading ...");
(gdb) p s_data_processed_cb
$3 = (AccelSampleProcessedCallback) 0xffeeffee
```

We see `s_data_processed_cb` looks like a bogus address, `0xffeeffee`, but we verified it was set correctly on boot. Confusing! Let's add a watchpoint to track down when the variable is getting set:

```
(gdb) watch *(uint32_t*)&s_data_processed_cb
(gdb) mon reset
(gdb) c


Hardware watchpoint 1: *(uint32_t*)&s_data_processed_cb

Old value = 4293853166
New value = 0
0x00000a6a in prv_cinit () at ./src/startup.c:33
33    for (uint32_t *dst = &_sbss; dst < &_ebss;) {
```

This makes sense, `s_data_processed_cb` is getting set to zero when we initialize BSS. Onward ...

```
(gdb) continue

Hardware watchpoint 1: *(uint32_t*)&s_data_processed_cb

Old value = 0
New value = 1129
0x000002e2 in accel_register_watcher (data_processed_cb=0x469 <accel_data_processed>) at ./src/accel_fake.c:18
18    s_data_processed_cb = data_processed_cb;
```

This also makes sense, this is where we set the correct value. Onward ...

```
(gdb)

Hardware watchpoint 1: *(uint32_t*)&s_data_processed_cb

Old value = 1129
New value = 65518
0x0000040e in graphics_boot (buf=buf@entry=0x20002080 <s_graphics_buf>, len=len@entry=4) at ./src/graphics_fake.c:5
5     for (size_t i = 0; i < len; i++) {
```

This is suspicious! `s_data_processed_cb` is getting updated from our graphics stack?! Let's examine the code

```
(gdb) list graphics_boot

4	void graphics_boot(uint16_t *buf, size_t len) {
5     for (size_t i = 0; i < len; i++) {
6       buf[i] = 0xffee;
7     }
```

The fact that we are writing over `s_data_processed_cb` suggests the `len` parameter above may be
incorrect and we are writing past the end of the array.


```
(gdb) list s_graphics_buf
[...]
40	static uint16_t s_graphics_buf[2];
[...]
```

Now we can see the issue!


`s_graphics_buf` is `uint16_t` array with two entries. The for loop in `graphics_boot` is
setting each entry in the array to `0xffee`. However, when we review the call to `graphics_boot`,
we see the size of the buffer,`sizeof(s_graphics_buf)`, was passed instead of the array length,
`sizeof(s_graphics_buf) / sizeof(s_graphics_buf[0])`:

```c
  graphics_boot(s_graphics_buf, sizeof(s_graphics_buf));
```

This means the for loop is writing at indexes 2 & 3 which is past the end of the array and we are clobbering memory!

We can confirm in GDB that `s_registered_handler` has been allocated right after `s_graphics_buf` and is getting corrupted:

```
(gdb) x/a s_graphics_buf
0x20002080 <s_graphics_buf>:	0xffeeffee
(gdb)
0x20002084 <s_registered_handler>:	0xffee
```

Sweet, using a watchpoint just saved a bunch of time traipsing through code to find this bug!

### Stack Overflows

Watchpoints can also aid in halting execution before a stack overflow occurs. Let's run a different command in the app, `math_example`, and investigate:

```bash
shell> math_example
Running math_function()
# Debugger should have halted
```

```bash
Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000998 in HardFault_Handler ()
(gdb) x/a $sp
0x1fffffd0:	0x0 <g_pfnVectors>
```

Yikes, we have hit another hardfault. What's interesting here is our stack pointer, `$sp`, ran off the end of RAM, `0x2000.0000`. This suggests a stack overflow took place. It's hard to see what happened because we ran off valid RAM and so not all the register state will be on the stack.

> Note: For a deeper dive into debugging Cortex-M faults in general, check out [our post on the topic](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug).

Since the overflow is reproducible, let's see if we can intercept before the overflow and get a stack trace.
We will install a watchpoint near the bottom of the stack:

```
(gdb) mon reset
(gdb) continue
(gdb) watch *(uint32_t*)0x20000010
(gdb) c
```

```
shell> math_example
# Debugger should have halted
```

```
(gdb)
Old value = 0
New value = 536870936
0x00000734 in math_function (n=799, n@entry=-1) at ./src/shell_commands.c:95
95	int math_function(int n) {
(gdb) bt
#0  0x00000734 in math_function (n=799, n@entry=-1) at ./src/shell_commands.c:95
#1  0x00000786 in math_function (n=0, n@entry=-1) at ./src/shell_commands.c:107
#2  0x00000786 in math_function (n=0, n@entry=-1) at ./src/shell_commands.c:107
[...]
#202 0x000007d6 in prv_math_example (argc=<optimized out>, argv=<optimized out>) at ./src/shell_commands.c:141
#203 0x000006c2 in prv_process () at ./src/shell.c:117
#204 shell_receive_char (c=<optimized out>) at ./src/shell.c:143
#205 0x00000928 in shell_processing_loop () at ./src/shell_port.c:60
#206 0x00000462 in main () at ./src/main.c:51
```

So we have a recursive function in this case that's blowing through our stack! Using the watchpoint made it much easier to root cause the code path triggering the overflow.
