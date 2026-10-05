---
id: "intr-nash-s-four-favorite-firmware-debu-ftdi-cable"
type: "concept"
domain: "debug"
title: "Nash's Four Favorite Firmware Debug Tools: FTDI Cable"
summary: "If there's an unsung hero of firmware development, it is the humble serial cable. Since the dawn of computing, the UART peripheral has been used as a debug port, a control bus for test systems, and a peripheral interface."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-25-four-favorite-firmware-debug-tools.md"
doc_source: "https://interrupt.memfault.com/blog/four-favorite-firmware-debug-tools#ftdi-cable"
license: "CC-BY-SA-4.0"
mode: "V"
---

If there's an unsung hero of firmware development, it is the humble serial
cable. Since the dawn of computing, the UART peripheral has been used as a debug
port, a control bus for test systems, and a peripheral interface. It is a
ubiquitous communication medium for embedded systems, and for the last two
decades, no serial cable has been more ubiquitous than those containing chips by
Future Technology Devices International, a.k.a FTDI.

(figure: There's a hero on your desktop.)

### Feeling Talkative, Developer Inquires?

The FTDI TTL-232R-3V3 debug cable is a very common thing to see plugged into a
developer machine, or lying tangled on an electronics workbench. Originally a
USB device company that made keyboards, joysticks, and mice, FTDI struck gold by
creating one of the first cheap, widely available USB-UART interface ICs. It's
an excellent example of a device that does one thing really, really well: it
converts USB signals to UART, and vice versa. That's it! (Here's
[a really neat interview Adafruit did with Fred Dart](https://blog.adafruit.com/2016/02/08/exclusive-interview-with-fred-dart-ceo-of-ftdi-ftdichip-ftdi-adafruit/),
one of the founders of FTDI. A fascinating look at some semiconductor history!)

(figure: Pay attention to this drawing.)

One of the most useful things about the FTDI cable is its ability to provide
target power in addition to comms. Each cable exposes a handy 5V output tapped
off of the host computer's 5V USB output. It's limited at an output of 100mA,
but this is more than enough for many bare metal microcontroller applications. A
simple on-target LDO stepping down to the proper IO voltage is enough to make
this useful to you!

### Now Don't Get It Twisted

If you are responsible for designing PCBs in addition to firmware development,
you probably know by now that it is a rite of passage to mix up the TX and RX
signals on the FTDI cable, or to reverse the cable pinout. Reversing the pinout
is generally a manageable headache. If there's no mechanical interference, you
can typically flip the cable over and be on your merry way. Mixing up the TX and
RX signals is a bit more of a headache. However, a set of zero ohm resistors on
the TX/RX lines near the connector is generally a good practice. Odds are, you
won't need them - but if you do, it's a heck of a lot easier than cutting and
splicing in a bit of impromptu trace surgery.

Having messed this up myself a time or two, I ended up making a known-good KiCAD
schematic containing the proper pinout for the FTDI cable. I also include a
little LDO for stepping down to 3.3V, for powering small MCU loads. This is a
fairly common SOT-23-5 LDO from Microchip (formerly Micrel); other parts exist
in footprint-compatible form factor if you need 2.5V, 1.8V, or lower VDDIO
levels. You can find these schematics
[on GitHub.](https://github.com/Cushychicken/ftdi_good_pinout)

I've built and tested several designs with this, and have yet to have a headache
with it when using it for debugging purposes. I bequeath it to you, that you may
never need to splice Rx/Tx between 0402 footprints again!
