---
id: "intr-code-size-optimization-gcc-compile-changing-the-optimization-level"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Changing the optimization level"
summary: "Compilers have the difficult task of optimizing a program around multiple axes. Namely: 1. Program performance - the speed at which the program executes 2. Compilation time - the time it takes to compile the program 3."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#changing-the-optimization-level"
license: "CC-BY-SA-4.0"
mode: "V"
---

Compilers have the difficult task of optimizing a program around multiple axes.
Namely:
1. Program performance - the speed at which the program executes
2. Compilation time - the time it takes to compile the program
3. Code size - the size of the compiled program
4. Debug-ability - how easily a program can be debugged

You would be hard pressed to choose trade-offs that work for every application: a
math library may care about performance, while firmware code may care about code
size. To that end, GCC bundles its optimizations into buckets which can be
selected via the Optimize
Options[^2].

The linked documentation does a great job of explaining the options, but I’ll go
over them briefly here:
* `-O0` : optimize for compile time and debug-ability. Most performance
  optimizations are disabled. This is the default for GCC.
* `-O1`: pick the low hanging fruit in terms of performance, without impacting
  compilation time too much.
* `-O2`: optimize for performance more aggressively, but not at the cost of
  larger code size.
* `-O3`: optimize for performance at all cost, no matter the code size or
  compilation time impact.
* `-Ofast` a.k.a. ludicrous mode: take off the guard rails, and disregard strict
  C standard compliance in the name of speed. This may lead to invalid programs.
* `-Os` optimize for code size. This uses `O2` as the baseline, but disables
  some optimizations. For example, it will not inline[^3] code if that leads to
a size increase.


Compiled with GCC’s default (`-O0`), our example clocks in at a whooping 108KiB
of code:

```
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
 111072	    296	  98008	 209376	  331e0	build/ch.elf
Creating build/ch.list
```

Our baseline in the previous section uses ChibiOS’s default of `-O2`. You’ll
have guessed by now that we can do better by using `-Os`:

```
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  62956	    232	  98072	 161260	  275ec	build/ch.elf
Creating build/ch.list
```

61KiB! This is 47KiB smaller than the default GCC settings, and 10KiB smaller
than the default project settings.

### What if my program is performance sensitive?

Parts of your program may be too performance-sensitive to compile them with
`-Os`. At Pebble, this was the case for our text layout code, which was critical
to hitting our target frame rate when scrolling through a notification. This is
generally only true for a few very specific functions or files.

GCC offers two methods to selectively tweak the optimization level: at the file
level, or at the function level.

If you want to set optimization level for a single function, you can use the
`optimize` function attribute:

```c
void __attribute__((optimize("O3"))) fast_function(void) {
    // ...
}
```

For a whole file, you can use the `optimize` pragma:
```c
#pragma GCC push_options
#pragma GCC optimize ("O3")

/*
 * Code that needs optimizing
 */

#pragma GCC pop_options
```

Note that the `push_options` and `pop_options` pragmas are needed to make sure
the rest of the file is compiled with the regular options.
