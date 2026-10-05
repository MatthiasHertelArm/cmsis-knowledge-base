---
id: "intr-tools-for-firmware-code-size-optim-measuring-overall-code-size"
type: "concept"
domain: "debug"
title: "Tools for Firmware Code Size Optimization: Measuring overall code size"
summary: "The simplest way to measure code size is to inspect the different sections of your elf file. The ARM GCC toolchain comes with a handy utility to do just that: arm-none-eabi-size."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-06-best-firmware-size-tools.md"
doc_source: "https://interrupt.memfault.com/blog/best-firmware-size-tools#measuring-overall-code-size"
license: "CC-BY-SA-4.0"
mode: "V"
---

The simplest way to measure code size is to inspect the different sections of
your elf file. The ARM GCC toolchain comes with a handy utility to do just that:
`arm-none-eabi-size`.

Let's try running it on one of our ELF files:

```terminal
$ arm-none-eabi-size build/with-libc.elf
   text    data     bss     dec     hex filename
  10800     104    8272   19176    4ae8 build/with-libc.elf
```

So in this program we have:

- 10800 bytes of `text`, which is code
- 104 bytes of `data`, which is statically initialized memory
- 8272 bytes of `bss`, which is zero-initialized memory

Unfortunately, the output of this tool is a little misleading. You may think
that your program will occupy `10800` bytes of flash, but this is not the case.

Indeed if we modify our linker script to specify that our flash size is 10800
exactly:

```diff
diff --git a/with-libc/samd21g18a_flash.ld b/with-libc/samd21g18a_flash.ld
index a07cc82b..f49e73e2 100644
--- a/with-libc/samd21g18a_flash.ld
+++ b/with-libc/samd21g18a_flash.ld
@@ -3,7 +3,7 @@ OUTPUT_ARCH(arm)

 MEMORY
 {
-  rom      (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00040000
+  rom      (rx)  : ORIGIN = 0x00000000, LENGTH = 10800
   ram      (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00008000
 }
```

We end up overflowing our flash!

```terminal
$ make
[...]
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld:
build/with-libc.elf section `.data' will not fit in region `rom'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld:
region `rom' overflowed by 104 bytes
collect2: error: ld returned 1 exit status
make: *** [build/with-libc.elf] Error 1
```

The 104 bytes overflow hints at the cause: we are overflowing our flash by
the size of our `data` section. This is because initialization values for our
initialized static variables are stored in flash as well.

To avoid confusion, I prefer to use a small script to compute the sizes:

```bash
#!/bin/bash

if [  $# -le 2 ]
then
    echo "This script requires 3 arguments."
    echo -e "\nUsage:\nget-fw-size FILE MAX_FLASH_SIZE MAX_RAM_SIZE \n"
    exit 1
fi

file=$1
max_flash=$2
max_ram=$3

function print_region() {
    size=$1
    max_size=$2
    name=$3

    if [[ $max_size == 0x* ]];
    then
        max_size=$(echo ${max_size:2})
        max_size=$(( 16#$max_size ))
    fi

    pct=$(( 100 * $size / $max_size ))
    echo "$name used: $size / $max_size ($pct%)"
}

raw=$(arm-none-eabi-size $file)

text=$(echo $raw | cut -d ' ' -f 7)
data=$(echo $raw | cut -d ' ' -f 8)
bss=$(echo $raw | cut -d ' ' -f 9)

flash=$(($text + $data))
ram=$(($data + $bss))

print_region $flash $max_flash "Flash"
print_region $ram $max_ram "RAM"
```

which gives us:

```terminal
$ ./get-fw-size build/with-libc.elf 0x40000
0x8000
Flash used: 10904 / 262144 (4%)
RAM used: 8376 / 32768 (25%)
```

Stick that in your Makefiles, and you'll have the size as you build
your firmware.

Note that an alternative to running `size` is to add the `-Wl,--print-memory-usage`
link-time flag which will give you something that looks like this:

```terminal
Memory region         Used Size  Region Size  %age Used
             rom:       10800 B       256 KB      4.12%
             ram:        8376 B        32 KB     25.56%
```

This falls into the same pitfall as `size` in that it does not count `data`
against ROM, and gives us less info since it does not break RAM out into `data`
and `bss`.
