---
id: "mbedtls-how-to-get-code-size-of-the-librar-usage"
type: "concept"
domain: "security"
title: "How to get code size of the library: Usage"
summary: "Output will be: > Footprint of standard configurations (minus net_sockets.c, timing.c, fs_io) > for bare-metal ARM Cortex-M3/M4 microcontrollers."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/code-size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/code-size.md#usage"
license: "Apache-2.0"
mode: "V"
---

./scripts/footprint.sh

Output will be:
>     Footprint of standard configurations (minus net_sockets.c, timing.c, fs_io)
>     for bare-metal ARM Cortex-M3/M4 microcontrollers.
>
>     Mbed TLS 2.4.1 (git head: af610a0baf)
>     arm-none-eabi-gcc (15:4.9.3+svn231177-1) 4.9.3 20150529 (prerelease)
>     CFLAGS=-Os -march=armv7-m -mthumb
>
>     default (include/mbedtls/config.h):
>        text	   data	bss	dec	hex	filename
>      250087	612	   9360	 260059	  3f7db	(TOTALS)
>
>     thread (configs/config-thread.h):
>        text	   data	bss	dec	hex	filename
>       58021	 19	 10	  58050	   e2c2	(TOTALS)
>
>     suite-b (configs/config-suite-b.h):
>        text	   data	bss	dec	hex	filename
>       79988	 88	 11	  80087	  138d7	(TOTALS)
>
>     psk (configs/config-ccm-psk-tls1_2.h):
>        text	   data	bss	dec	hex	filename
>       28115	 12	  4	  28131	   6de3	(TOTALS)

When you use Mbed TLS as a static library, you can optimize the linker to omit any unused symbol. You can find full symbol information in `mbedtls-footprint.zip`.
