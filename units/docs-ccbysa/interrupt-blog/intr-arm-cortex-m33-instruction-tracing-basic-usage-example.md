---
id: "intr-arm-cortex-m33-instruction-tracing-basic-usage-example"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Example Project / Basic Usage Example"
summary: "The default mode for the test application does nothing exciting but will serve as a good way to sanity check our decoder is working as expected. When the application starts up, it enters an infinite loop."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#basic-usage-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Example Project_

The default mode for the test application does nothing exciting but will serve as a good way to sanity check our decoder is working as expected. When the application starts up, it enters an infinite loop. The loop halts with a breakpoint instruction every five iterations:

```c
__attribute__((optimize("O0")))
void infinite_loop(void) {
  volatile int i;
  while (1) {
    i++;

    if ((i % 5) == 0) {
      __asm("bkpt 6");
    }
  }
}

int main(void) {
   // ...
   mtb_enable(8192);
   // ...
   infinite_loop();
```

Let's start the application and wait till the first breakpoint is hit:

```
$ make flash
Resetting target
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
infinite_loop () at ./main.c:157
157       __asm("bkpt 6");
```

We can dump the disassembly of this loop to get a sense of what we expect to be recorded by the MTB:

```
(gdb) disassemble infinite_loop
Dump of assembler code for function infinite_loop:
    0x20000324 <+0>:	push	{r7}
    0x20000326 <+2>:	sub	sp, #12
    0x20000328 <+4>:	add	r7, sp, #0
    0x2000032a <+6>:	ldr	r3, [r7, #4]
    0x2000032c <+8>:	adds	r3, #1
    0x2000032e <+10>:	str	r3, [r7, #4]
    0x20000330 <+12>:	ldr	r1, [r7, #4]
    0x20000332 <+14>:	ldr	r3, [pc, #28]	; (0x20000350 <infinite_loop+44>)
    0x20000334 <+16>:	smull	r2, r3, r3, r1
    0x20000338 <+20>:	asrs	r2, r3, #1
    0x2000033a <+22>:	asrs	r3, r1, #31
    0x2000033c <+24>:	subs	r2, r2, r3
    0x2000033e <+26>:	mov	r3, r2
    0x20000340 <+28>:	lsls	r3, r3, #2
    0x20000342 <+30>:	add	r3, r2
    0x20000344 <+32>:	subs	r2, r1, r3
    0x20000346 <+34>:	cmp	r2, #0
*   0x20000348 <+36>:	bne.n	0x2000032a <infinite_loop+6>
    0x2000034a <+38>:	bkpt	0x0006
*   0x2000034c <+40>:	b.n	0x2000032a <infinite_loop+6>
    0x2000034e <+42>:	nop
    0x20000350 <+44>:	str	r7, [r4, #100]	; 0x64
    0x20000352 <+46>:	str	r6, [r4, #100]	; 0x64
```

Remember that the MTB only logs instructions when the PC is not sequential so out of the 23 instructions above only 2 of them should wind up emitting events (`0x20000348` & `0x2000034c`).

Let's load our python gdb script and take a look at the decoded data!

```
(gdb) mtb
Begin Trace Session
>S: 0x20000510 - mtb_enable @ ./mtb.c:35
 D: 0x20000368 - main @ ./main.c:168
>S: 0x2000036e - main @ ./main.c:169
 D: 0x20000324 - infinite_loop @ ./main.c:151
>S: 0x20000348 - infinite_loop @ ./main.c:156
 D: 0x2000032a - infinite_loop @ ./main.c:154
>S: 0x20000348 - infinite_loop @ ./main.c:156
 D: 0x2000032a - infinite_loop @ ./main.c:154
>S: 0x20000348 - infinite_loop @ ./main.c:156
 D: 0x2000032a - infinite_loop @ ./main.c:154
>S: 0x20000348 - infinite_loop @ ./main.c:156
 D: 0x2000032a - infinite_loop @ ./main.c:154
```

Neat, what we are looking at here is a trace of the entire instruction flow up to the breakpoint.

If we want to view the exact instructions executed we can take the destination address from the previous packet and the source from the next packet and disassemble the range with gdb. We see the `0x20000348` we identified above has been recorded in the trace.

For example for the first `D` -> `S` transition we have above:

```
(gdb) disassemble/s 0x20000368,0x2000036e+4
Dump of assembler code from 0x20000368 to 0x20000372:
./main.c:
173   if (g_trace_example_config == 0) {
   0x20000368 <main+20>:	ldr	r3, [pc, #96]	; (0x200003cc <main+120>)
   0x2000036a <main+22>:	ldr	r3, [r3, #0]
   0x2000036c <main+24>:	cbnz	r3, 0x20000372 <main+30>

174     infinite_loop();
   0x2000036e <main+26>:	bl	0x20000324 <infinite_loop>
End of assembler dump.
```

And for the second we have:

```
(gdb) disassemble/s 0x20000324,0x20000348+4
Dump of assembler code from 0x20000324 to 0x2000034c:
./main.c:
153	void infinite_loop(void) {
   0x20000324 <infinite_loop+0>:	push	{r7}
   0x20000326 <infinite_loop+2>:	sub	sp, #12
   0x20000328 <infinite_loop+4>:	add	r7, sp, #0

154   volatile int i;
155   while (1) {
156     i++;
   0x2000032a <infinite_loop+6>:	ldr	r3, [r7, #4]
   0x2000032c <infinite_loop+8>:	adds	r3, #1
   0x2000032e <infinite_loop+10>:	str	r3, [r7, #4]

157
158     if ((i % 5) == 0) {
   0x20000330 <infinite_loop+12>:	ldr	r1, [r7, #4]
   0x20000332 <infinite_loop+14>:	ldr	r3, [pc, #28]	; (0x20000350 <infinite_loop+44>)
   0x20000334 <infinite_loop+16>:	smull	r2, r3, r3, r1
   0x20000338 <infinite_loop+20>:	asrs	r2, r3, #1
   0x2000033a <infinite_loop+22>:	asrs	r3, r1, #31
   0x2000033c <infinite_loop+24>:	subs	r2, r2, r3
   0x2000033e <infinite_loop+26>:	mov	r3, r2
   0x20000340 <infinite_loop+28>:	lsls	r3, r3, #2
   0x20000342 <infinite_loop+30>:	add	r3, r2
   0x20000344 <infinite_loop+32>:	subs	r2, r1, r3
   0x20000346 <infinite_loop+34>:	cmp	r2, #0
   0x20000348 <infinite_loop+36>:	bne.n	0x2000032a <infinite_loop+6>
```

Neat, so two trace packets (16 bytes of data) tells us the exact last 23 instructions which were
executed by the processor! Both ranges examined end with branch instructions so our decoder appears to be working as expected!
