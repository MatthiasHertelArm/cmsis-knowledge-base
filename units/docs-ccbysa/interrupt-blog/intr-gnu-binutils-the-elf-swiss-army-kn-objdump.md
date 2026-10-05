---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-objdump"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / objdump"
summary: "objdump is a general purpose utility that is most helpful when trying to examine the assembly in a binary. It's also my personal favorite! You can run objdump on the final ELF output or individual .o object files."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#objdump"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`objdump` is a general purpose utility that is most helpful when trying to examine the assembly in
a binary. It's also my personal favorite! You can run `objdump` on the final ELF output or
individual `.o` object files. While there are a number of options, most of the time the following
are most useful:

`-d` to display the assembly code for all executable sections.
`--disassemble=<symbol>` to display the assembly for just one function

Let's walk through a few examples of the types of questions we can answer with objdump.

#### Inspecting Stack Usage

Above we saw one of the biggest functions in the Zephyr ELF we were looking at was
`z_printk`. Let's check out the amount of stack it uses.

```bash
$ arm-none-eabi-objdump   -d build/zephyr/zephyr.elf
  --disassemble=eswifi_request_work | less
08003964 <eswifi_request_work>:
=> 8003964:       e92d 4ff0       stmdb   sp!, {r4, r5, r6, r7, r8, r9, sl, fp, lr}
   8003968:       f890 4071       ldrb.w  r4, [r0, #113]  ; 0x71
   800396c:       2c01            cmp     r4, #1
=> 800396e:       b08f            sub     sp, #60 ; 0x3c
   8003970:       4605            mov     r5, r0
   8003972:       f1a0 0698       sub.w   r6, r0, #152    ; 0x98
```

We can see a push of 9 registers and a subtraction of 60 bytes from `$sp` which tells us the stack
consumption for the function is around 96 bytes.

> If you are trying to do an in-depth stack usage analysis you can also use the GCC compiler flag,
> `-fstack-usage`. This will emit `.su` files alongside the `.o` files which contain information of
> stack utilization for all the functions in the object file. Some tools, such as
> [puncover](https://github.com/memfault/puncover), can also analyze `.su` files to determine worst-case
> stack depth for call chains.

#### Examining Optimizations

When looking at backtraces in a debugger, sometimes functions that should be in the backtrace are
not displayed. While the compiler tries its best to emit debug information that allows for the
backtraces to be recovered, certain optimizations (such as inlining) make this really
difficult. If a backtrace looks suspicious, I like to look at the assembly to see if inlining or other
types of optimizations may have taken place. Lets look at a simple example:

```c
static int prv_compute_power_sum(int count) {
  int result = 0;

  for (int i = 0; i < count; i++) {
    result += i * i;
  }

  return result;
}


int compute_power_sum(int count) {
  if (count < 0) {
    return -1;
  }

  return prv_compute_power_sum(count);
}
```

```bash
$ arm-none-eabi-objdump -d nrf52_example/build/nrf52.elf
   --disassemble=compute_power_sum

00000134 <compute_power_sum>:
     134:	1e02        subs	r2, r0, #0
     136:	db08        blt.n	14a <compute_power_sum+0x16>
     138:	2300        movs	r3, #0
     13a:	4618        mov	r0, r3
     13c:	429a        cmp	r2, r3
     13e:	d100        bne.n	142 <compute_power_sum+0xe>
     140:	4770        bx	lr
     142:	fb03 0003   mla	r0, r3, r3, r0
     146:	3301        adds	r3, #1
     148:	e7f8        b.n	13c <compute_power_sum+0x8>
     14a:	f04f 30ff   mov.w	r0, #4294967295	; 0xffffffff
     14e:	4770        bx	lr
```

Interesting, no calls to `prv_compute_power_sum()`. This tells us the call was inlined! We can also
use the `-S` option to display the source code the assembly was generated from.

> DISCLAIMER: While this can be helpful at times, the assembly to source code mapping isn't always correct.

```
00000134 <compute_power_sum>:

  return result;
}

int compute_power_sum(int count) {
  if (count < 0) {
     134:	1e02        subs	r2, r0, #0
     136:	db08        blt.n	14a <compute_power_sum+0x16>
  for (int i = 0; i < count; i++) {
     138:	2300        movs	r3, #0
  int result = 0;
     13a:	4618        mov	r0, r3
  for (int i = 0; i < count; i++) {
     13c:	429a        cmp	r2, r3
     13e:	d100        bne.n	142 <compute_power_sum+0xe>
     140:	4770        bx	lr
    result += i * i;
     142:	fb03 0003   mla	r0, r3, r3, r0
  for (int i = 0; i < count; i++) {
     146:	3301        adds	r3, #1
     148:	e7f8        b.n	13c <compute_power_sum+0x8>
    return -1;
     14a:	f04f 30ff   mov.w	r0, #4294967295	; 0xffffffff
  }

  return prv_compute_power_sum(count);
}
14e:	4770        bx	lr
```

#### Comparing Code Size

If you are crunched for space, it can be useful to understand what coding patterns are more
favorably optimized. This type of analysis can easily be run with `objdump`.

##### Pop Quiz: Which of the Following will Yield Smaller Code?

```c
const char *test_enum_to_str_v1(eTestEnum e) {
  switch (e) {
    case kTestEnum_Val1:
      return "Val1";
    case kTestEnum_Val2:
      return "Val2";
    case kTestEnum_Val3:
      return "Val3";
    case kTestEnum_Val4:
    default:
      return "Val4";
  }
}
```

```c
const char *test_enum_to_str_v2(eTestEnum e) {
  if (e == kTestEnum_Val1) {
    return "Val1";
  } else if (e == kTestEnum_Val2) {
    return "Val2";
  } else if (e == kTestEnum_Val3) {
    return "Val3";
  } else if (e == kTestEnum_Val4) {
    return "Val4";
  }
  return "Val4";
}
```

> NOTE: We've compiled both snippets with `-Os` to force a size based optimization

##### test_enum_to_str_v1 Assembly

```
$ arm-none-eabi-objdump -d nrf52_example/build/nrf52.elf \
   --disassemble=test_enum_to_str_v1
0000015c <test_enum_to_str_v1>:
 15c:	2802        cmp	r0, #2
 15e:	bf9a        itte	ls
 160:	4b02        ldrls	r3, [pc, #8]	; (16c <test_enum_to_str_v1+0x10>)
 162:	f853 0020   ldrls.w	r0, [r3, r0, lsl #2]
 166:	4802        ldrhi	r0, [pc, #8]	; (170 <test_enum_to_str_v1+0x14>)
 168:	4770        bx	lr
 16a:	bf00        nop
 16c:	20000020    .word	0x20000020
 170:	2000000a    .word	0x2000000a
```

##### test_enum_to_str_v2 Assembly

```
$ arm-none-eabi-objdump -d nrf52_example/build/nrf52.elf  \
   --disassemble=test_enum_to_str_v1
00000174 <test_enum_to_str_v2>:
 174:	b140        cbz	r0, 188 <test_enum_to_str_v2+0x14>
 176:	2801        cmp	r0, #1
 178:	d008        beq.n	18c <test_enum_to_str_v2+0x18>
 17a:	4b05        ldr	r3, [pc, #20]	; (190 <test_enum_to_str_v2+0x1c>)
 17c:	4a05        ldr	r2, [pc, #20]	; (194 <test_enum_to_str_v2+0x20>)
 17e:	2802        cmp	r0, #2
 180:	bf0c        ite	eq
 182:	4618        moveq	r0, r3
 184:	4610        movne	r0, r2
 186:	4770        bx	lr
 188:	4803        ldr	r0, [pc, #12]	; (198 <test_enum_to_str_v2+0x24>)
 18a:	4770        bx	lr
 18c:	4803        ldr	r0, [pc, #12]	; (19c <test_enum_to_str_v2+0x28>)
 18e:	4770        bx	lr
 190:	20000019    .word	0x20000019
 194:	2000000a    .word	0x2000000a
 198:	2000000f    .word	0x2000000f
 19c:	20000014    .word	0x20000014
```

Interesting, while both functions have the same behavior, the switch case based approach winds up
being 50% smaller! It looks like the compiler has optimized that approach better by using a lookup table
instead of branching.

> Note: This behavior is subject to change from compiler version to compiler version.

#### New Feature: Visualize Jumps

Binutils is constantly adding new features. While writing this post, I discovered a new option in
`objdump`, `--visualize-jumps`, that was just released in binutils 2.34. This option generates
ASCII art showing the branching flow within individual functions which will be very
helpful for following control flow when stepping through assembly:

```
$ binutils/objdump  --visualize-jumps=color
   --disassemble=test_enum_to_str_v2 nrf52_example/build/nrf52.elf
```


