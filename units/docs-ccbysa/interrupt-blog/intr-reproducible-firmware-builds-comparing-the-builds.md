---
id: "intr-reproducible-firmware-builds-comparing-the-builds"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Comparing the builds"
summary: "It's confusing how one build crashes and the other does not. If we did not crash in the first build it must mean the s_heap structure was word aligned."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#comparing-the-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

#### Comparing the symbol address

It's confusing how one build crashes and the other does not. If we did not crash in the first build it must mean the `s_heap` structure was word aligned. We can confirm that with the `nm` utility which can be used to inspect symbol information:

```
$ cd /private/tmp
$ arm-none-eabi-nm -S -l dev/interrupt/example/reproducible-build/build/nrf52.elf | grep s_heap
200001ca 00000011 d s_heap	/private/tmp/dev/interrupt/example/reproducible-build/minimal_heap.c:13
$ arm-none-eabi-nm -S -l repos/interrupt/example/reproducible-build/build/nrf52.elf | grep s_heap
200001d4 00000011 d s_heap	/private/tmp/repos/interrupt/example/reproducible-build/minimal_heap.c:13
```

It appears the addresses are different between the builds. Are the sizes of the build the same?

#### Comparing the binary sizes

```
$ arm-none-eabi-size dev/interrupt/example/reproducible-build/build/nrf52.elf
   text    data     bss     dec     hex	filename
   6228     480   11688   18396    47dc	dev/interrupt/example/reproducible-build/build/nrf52.elf
(.venv) chrisc: /private/tmp/
$ arm-none-eabi-size repos/interrupt/example/reproducible-build/build/nrf52.elf
   text    data     bss     dec     hex	filename
   6228     492   11684   18404    47e4	repos/interrupt/example/reproducible-build/build/nrf52.elf
```

We can see that one build is larger than the other and it looks like most of that difference comes from the `.data` section.

#### Examining strings in the binary

When sizes differ, one of the first things I like to check is to see if there are any differences in the strings within the binary. We can easily examine this with `arm-none-eabi-strings`. The `-d` option can be used to only scan `.data` sections in the file (that is, skip over any debug info) & the `-n` argument can be used to control the minimum string length that will be detected. Let's try it out!

```bash
$ arm-none-eabi-strings -d dev/interrupt/example/reproducible-build/build/nrf52.elf -n 10
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/tasks.c
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/queue.c
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/timers.c
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/portable/GCC/ARM_CM4F/port.c
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/portable/MemMang/heap_1.c
```

So we see the entire filename path has made it into the build!

This generally happens when the `__FILE__` macro is used which is a fairly common occurrence (e.g. a lot of logging implementations and assert handlers use it). The `__FILE__` macro expands to "path by which the preprocessor opened the file"[^4]. In practice this is the path passed to the compiler when the `.c` file is compiled. You can try it out yourself by running a simple `test.c` file through the preprocessor.

```c
// contents of test.c file
const char *my_file_name = __FILE__;
```

To only invoke the preprocessor we can use the GCC `-E` argument:

```bash
$ /private/tmp/
$ arm-none-eabi-gcc -E test.c
[...]
const char *my_file_name = "test.c";
$ arm-none-eabi-gcc -E /private/tmp/test.c
[...]
const char *my_file_name = "/private/tmp/test.c";
$ arm-none-eabi-gcc -E ../tmp/test.c
[...]
const char *my_file_name = "../tmp/test.c";
```

The paths we see in `nrf52.elf` suggest our Makefile build commands must be passing absolute paths. Let's inspect the Makefile:

```bash
$(BUILD_DIR)/%.o: $(ROOT_DIR)/%.c Makefile | $(BUILD_DIR) $(DEP_DIR) $(FREERTOS_PORT_ROOT)
    @echo "Compiling $*.c"
    @mkdir -p $(dir $@)
    $(Q) arm-none-eabi-gcc $(DEP_CFLAGS) $(CFLAGS) $(INCLUDE_PATHS) -c -o $@ $<
```

The c file name is coming from `$<` on the last line which is makefile syntax for the first prerequisite of the target[^5]. This is indeed an absolute path. Instead let's utilize `$*` to get the value which was matched with `%`, which will be relative to the root directory of the repo. Let's apply the patch to fix that up:

```bash
$ cd /private/tmp/dev/interrupt/example/reproducible-build/
$ git apply 02-fix-compiler-invocation.patch
$ cd /private/tmp/repos/interrupt/example/reproducible-build/
$ git apply 02-fix-compiler-invocation.patch
```

Now let's look at the string output:

```bash
$ arm-none-eabi-strings -d build/nrf52.elf -n 10
freertos_kernel/tasks.c
freertos_kernel/queue.c
freertos_kernel/timers.c
freertos_kernel/portable/GCC/ARM_CM4F/port.c
freertos_kernel/portable/MemMang/heap_1.c
```

Great! We no longer have absolute paths in the binary.

As an alternative, the compiler flag
[`-ffile-prefix-map=old=new`](https://gcc.gnu.org/onlinedocs/gcc-12.1.0/gcc/Overall-Options.html#index-ffile-prefix-map)
performs a substitution for path prefix segments:

```bash
$ arm-none-eabi-gcc -ffile-prefix-map=/private/tmp=. -E /private/tmp/test.c
[...]
const char *my_file_name = "./test.c";
```

> Note: the `-ffile-prefix-map=old=new` was first added in GCC 8.1, although
> apparently without enough excitement to deserve a mention in the [release
> notes](https://gcc.gnu.org/gcc-8/changes.html)!


> This flag sets all `f*-prefix-map` settings, so it applies to debug info as
> well as macro (`__FILE__`) substitutions. Note that it does NOT as of yet get
> forwarded to `as` when invoked from the GCC frontend, so be sure to add
> `-Wa,--debug-prefix-map=old=new` if that applies (this is [likely a bug in
> GCC](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=93371), as
> `-fdebug-prefix-map=old=new` correctly forwards the arg to `as`).


> Clang also [supports the
> flag](https://releases.llvm.org/14.0.0/tools/clang/docs/ClangCommandLineReference.html#cmdoption-clang-ffile-prefix-map),
> as of [Clang
> 10](https://releases.llvm.org/10.0.0/tools/clang/docs/ReleaseNotes.html#new-compiler-flags).
