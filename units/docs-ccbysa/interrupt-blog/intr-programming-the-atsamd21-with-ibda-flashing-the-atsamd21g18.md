---
id: "intr-programming-the-atsamd21-with-ibda-flashing-the-atsamd21g18"
type: "concept"
domain: "debug"
title: "Programming the ATSAMD21 with IBDAP: Flashing the atsamd21g18"
summary: "Both the Arduino M0 pro and the Metro M0 Express boards come with fancy bootloaders that let you update your firmware over USB. Most people will be thrilled to use that."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-04-25-getting-started-with-ibdap-and-atsamd21g18.md"
doc_source: "https://interrupt.memfault.com/blog/getting-started-with-ibdap-and-atsamd21g18#flashing-the-atsamd21g18"
license: "CC-BY-SA-4.0"
mode: "V"
---

Both the Arduino M0 pro and the Metro M0 Express boards come with fancy
bootloaders that let you [update your firmware over
USB](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/uf2-bootloader-details).
Most people will be thrilled to use that.

If - like me - you're trying to build your own bootloader, things get a bit more
complicated.

First, it's best to check that you're able to talk to the board over the debug
interface. Use a [SWD Ribbon cable](https://www.adafruit.com/product/1675) to
connect the IBDAP dongle to your board (you want to use the TGT_DBG port on the
dongle). OpenOCD already has config files for CMSIS-DAP and the ATSAMD family,
so you just need to source them and run openocd:

```terminal
$ openocd -c "source [find interface/cmsis-dap.cfg]; source [find
target/at91samdXX.cfg]"
Open On-Chip Debugger 0.10.0
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "swd". To override use
'transport select <transport>'.
none srst_pulls_trst
adapter speed: 400 kHz
cortex_m reset_config sysresetreq
Info : CMSIS-DAP: SWD  Supported
Info : CMSIS-DAP: Interface Initialised (SWD)
Info : CMSIS-DAP: FW Version = 1.0
Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1
Info : CMSIS-DAP: Interface ready
Info : clock speed 400 kHz
Info : SWD DPIDR 0x0bc11477
Info : at91samd.cpu: hardware has 4 breakpoints, 2 watchpoints
```

So far so good. Let's now write an openocd.cfg file to load our firmware:

```config
# Load the configuration for the MCU over CMSIS-DAP
source [find interface/cmsis-dap.cfg]
source [find target/at91samdXX.cfg]
# Flash the firmware
program your-firmware-file.bin
# Read it back and verify it
verify
# Reset the board
reset
# Close the openocd server
shutdow
```

These are all general openocd command documented [on their
website](http://openocd.org/doc/html/General-Commands.html).

Not so fast...

```terminal
** Programming Started **
auto erase enabled
Info : SAMD MCU: SAMD21G18A (256KB Flash, 32KB RAM)
Error: SAMD: NVM lock error
Error: Failed to erase row containing 00000000
Error: SAMD: failed to erase sector 0
Error: failed erasing sectors 0 to 0
embedded:startup.tcl:476: Error: ** Programming Failed **
```

It turns out our MCU can write protect bootloader pages, so that a firmware bug
does not overwrite the bootloader and brick the device. You can read all about
it in section 9.4 of the
[SAMD20 family datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/60001504B.pdf).
Typically, boot protection can be overcome with a chip erase, but that did not do the trick
here.

To disable it, we need to zero out the `BOOTPROT` bits (0:2) in the NVM User Row,
which is a fancy name for a non-volatile, 64-bit register at address `0x804000`.

Conveniently, openOCD has a MCU specific command just for this, documented
[here](http://openocd.org/doc-release/html/Flash-Commands.html)! Let's add it to
our script.

```config
# Load the configuration for the MCU over CMSIS-DAP
source [find interface/cmsis-dap.cfg]
source [find target/at91samdXX.cfg]
# Init openocd
init
# Reset & Halt the chip
reset
halt
# Unlock the bootloade regions
at91samd bootloader 0
# Reset the chip
reset
# Flash the firmware
program your-firmware-file.bin
# Read it back and verify it
verify
# Reset the board
reset
# Close the openocd server
shutdow
```

And off we go!

```terminal
** Programming Started **
auto erase enabled
Info : SAMD MCU: SAMD21G18A (256KB Flash, 32KB RAM)
wrote 16384 bytes from file build/minimal/minimal.bin in 3.695003s (4.330 KiB/s)
** Programming Finished **
** Verify Started **
verified 1252 bytes in 0.207606s (5.889 KiB/s)
** Verified OK **
** Resetting Target **
shutdown command invoked
```
