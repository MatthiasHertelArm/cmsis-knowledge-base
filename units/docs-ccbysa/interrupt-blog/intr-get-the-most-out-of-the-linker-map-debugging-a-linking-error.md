---
id: "intr-get-the-most-out-of-the-linker-map-debugging-a-linking-error"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Debugging a linking error"
summary: "Map files are created while the built code (.o files) is linked together which means it can be used to resolve errors in the linking process. I remember working on a bootloader that was contained in a few Flash pages."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#debugging-a-linking-error"
license: "CC-BY-SA-4.0"
mode: "V"
---

Map files are created while the built code (`.o` files) is linked together which means it can be used to resolve errors in the linking process. I remember working on a bootloader that was contained in a few Flash pages. At some point, I wanted to use `atoi` but the bootloader didn't compile anymore because there was no more space available.

Using the previous example, let's say I now have only 0x800 bytes of Flash. Compiling the first example, without `atoi`, there are no issues. The second example however would overflow our small Flash:

```
    $ make
    Compiling file: main.c
    Linking target: _build/nrf52840_xxaa.out
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: _build/nrf52840_xxaa.out section `.text' will not fit in region `FLASH'
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: region FLASH overflowed with .data and user data
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: region `FLASH' overflowed by 208 bytes
    collect2: error: ld returned 1 exit status
    make: *** [_build/nrf52840_xxaa.out] Error 1
```

That's annoying! `atoi` is such a simple function... But as we have seen, it takes more Flash than we would expect using `libc_nano.a`.

Let's try to to implement our own version of `atoi`, it's not that difficult after all. Here is the result after compilation (config `CUSTOM_ATOI`):

```
    Linking target: _build/nrf52840_xxaa.out
       text	   data	    bss	    dec	    hex	filename
       1740	    108	     28	   1876	    754	_build/nrf52840_xxaa.out
```

Way better! The code can now be crammed into 0x800 bytes to meet our (fake) requirements 🥳.

---

Reading the map file will teach you a lot about the code you are working on, and it is the first step to better Firmware. Some tools are available to parse map files and have a summarized view of your program. I should mention Adafruit's, [using that source code](https://github.com/adafruit/linker-map-summary), for example.

Feel free to share your story with any interesting usage of the map files.
