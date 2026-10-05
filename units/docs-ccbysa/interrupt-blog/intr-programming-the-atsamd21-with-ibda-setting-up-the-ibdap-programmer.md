---
id: "intr-programming-the-atsamd21-with-ibda-setting-up-the-ibdap-programmer"
type: "concept"
domain: "debug"
title: "Programming the ATSAMD21 with IBDAP: Setting up the IBDAP programmer"
summary: "I had recently picked up an IBDAP programmer from Adafruit. This is a simple CMSIS-DAP device based on the LPC11u35 chipset."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-04-25-getting-started-with-ibdap-and-atsamd21g18.md"
doc_source: "https://interrupt.memfault.com/blog/getting-started-with-ibdap-and-atsamd21g18#setting-up-the-ibdap-programmer"
license: "CC-BY-SA-4.0"
mode: "V"
---

I had recently picked up an [IBDAP](https://www.adafruit.com/product/2764)
programmer from Adafruit. This is a simple CMSIS-DAP device based on the
LPC11u35 chipset.

In order to work as a CMSIS-DAP device, the dongle needs to be flashed with a
firmware from the supplier. Unfortunately, the company behind the dongle seems to have gone out of business.
Its documentation, firmware binaries, and github repositories have all vanished
from the internet.

I found out via a forum post that mbed's
[SWDAP](https://os.mbed.com/platforms/SWDAP-LPC11U35/) firmware precompiled for
LPC1768 works fine on this board. From there, the steps were relatively
straightforward:

1. Download the pre-built firmware.
```terminal
$ wget https://os.mbed.com/media/uploads/chris/lpc11u35_swdap_lpc1768_if_crc.bin
```
2. Connect the dongle over USB.
3. Put the dongle in DFU mode by pressing both the RESET and ISP buttons. It
   should now appear as a USB drive named "CRP DISABLD".
3. Copy the firmware over to the drive. On my Mac this was best achieved with
   `dd`.
```terminal
$ dd if=lpc11u35_swdap_lpc1768_if_crc.bin of=/Volumes/CRP\ DISABLD/firmware.bin
conv=notrunc
```
Note that simply dragging the firmware over did not work because it fits exactly
within the flash and OSX wants some overhead, erroring out with "not enough space".
4. Reset the dongle by pressing the RESET button.
5. Verify that it now enumerates as a USB drive named "DAPLINK".

You are now the proud owner of a functional IBDAP programmer!
