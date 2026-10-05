---
id: "intr-tools-for-firmware-code-size-optim-digging-into-functions"
type: "concept"
domain: "debug"
title: "Tools for Firmware Code Size Optimization: Digging into functions"
summary: "The above tells us how much code space we are using, but not why. To answer the latter, we need to go deeper."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-06-best-firmware-size-tools.md"
doc_source: "https://interrupt.memfault.com/blog/best-firmware-size-tools#digging-into-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

The above tells us _how much_ code space we are using, but not _why_. To answer
the latter, we need to go deeper.

This is where another tool bundled with the GNU ARM toolchain comes in handy:
`arm-none-eabi-nm`.

`nm` allows us to print out all of the symbols in an ELF file, and with the
`--size` option it will also print the size of each symbol, and even sort them
by size if you specify `--size-sort`.

So if we want to dig into what symbols consume the most code space, we simply
do:

```terminal
$ arm-none-eabi-nm --print-size --size-sort --radix=d build/with-libc.elf | tail -30
00004420 00000100 T _write
00006948 00000112 T __sinit
00002096 00000118 T _sercom_get_sync_baud_val
00002684 00000124 T sercom_set_gclk_generator
00009864 00000128 T _fflush_r
00010112 00000136 T __smakebuf_r
00007060 00000144 T __sfp
00005676 00000144 T system_gclk_chan_disable
00010304 00000148 T _free_r
00009104 00000172 T __swbuf_r
00000000 00000180 T exception_table
00005112 00000180 T system_clock_source_get_hz
00007276 00000188 T _malloc_r
00003894 00000190 t usart_get_config_defaults
00005352 00000196 T system_gclk_gen_get_hz
00003332 00000200 T Reset_Handler
00001636 00000214 T usart_read_wait
00008164 00000218 T _printf_common
00001872 00000224 t long_division
00009316 00000236 T __swsetup_r
00006320 00000266 T __udivsi3
00005984 00000272 t _system_pinmux_config
00009588 00000276 T __sflush_r
00001122 00000416 T usart_init
00002808 00000444 T _sercom_get_default_pad
00002216 00000468 T _sercom_get_async_baud_val
00008384 00000532 T _printf_i
00007544 00000620 T _vfiprintf_r
00007544 00000620 T _vfprintf_r
00000430 00000692 t _usart_set_config
```

Note: you can also add `-l` to get filename & line # for each symbol.

Here we see that our largest symbol is `_usart_set_config` which uses 692
bytes of flash.
