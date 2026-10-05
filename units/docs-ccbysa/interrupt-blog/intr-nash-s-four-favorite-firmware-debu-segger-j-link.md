---
id: "intr-nash-s-four-favorite-firmware-debu-segger-j-link"
type: "concept"
domain: "debug"
title: "Nash's Four Favorite Firmware Debug Tools: Segger J-Link"
summary: "What good is a microcontroller if you can't program it? Segger J-Link debug probes have slowly but surely established themselves as high quality programmers for firmware developers the world over."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-25-four-favorite-firmware-debug-tools.md"
doc_source: "https://interrupt.memfault.com/blog/four-favorite-firmware-debug-tools#segger-j-link"
license: "CC-BY-SA-4.0"
mode: "V"
---

What good is a microcontroller if you can't program it? Segger J-Link debug
probes have slowly but surely established themselves as high quality programmers
for firmware developers the world over.

### Nothin' but a J Thang

One of the lovely things about J-Links is the multitude of different software
interfaces for their probes. Here's a small sampling of the ways you can chat
with your J-Link:

- Command line (J-Link Commander) for daily driver usage
- GDB server interface
- Network interfaces, to allow for JTAG access behind an Ethernet switch
- Factory programmer for speed, verification
- Raw API to write your own

One of the areas in which Segger really shines is their documentation. Segger
distinguishes itself with high quality user manuals and application notes.
All J-Links come with a 400 page user manual that gives detailed explanations of
all functionality in associated software. Much as I love free software, it’s a
lovely reminder of how paid software incentivizes you to do a really good job on
the hard, not-fun parts of the work, like writing good documentation.

That's not to say that J-Link doesn't play nicely with free software! They are
more than capable of interfacing with OpenOCD. Sue Mohielden from River Loop
Security put together
[this handy guide](https://www.riverloopsecurity.com/blog/2021/07/hw-101-jtag-part3/)
showing how to connect to an arbitrary device using a J-Link. According to Sue's
guide, the proper command goes something like this:

```shell
sudo ./openocd -s ../tcl -f interface/jlink.cfg -f target/ath79.cfg -c "adapter speed 15000"
```

Configuring to your specific application is straightforward: simply sub out the
`target/ath79.cfg` argument for the config file of your target processor. This
can require a bit of rummaging round in the `openocd/target` install directory
to find the correct file. The exact location of this directory varies from
system to system. Mine is available at the following path on my Linux machine:
`/usr/share/openocd/scripts/target`. Some trial and error can also be required;
the config files sometimes support multiple processors, while the config file
naming schemes can be somewhat opaque.

This initial configuration process can feel a bit like searching for the proper
incantation for a particularly arcane spell. I have struggled with
getting OpenOCD working several times. Not to worry! After the umpteenth time of
getting grumpy with setup, I took down some notes on how to do it for the next
time.
[I pass it on to you, friends, that your brain sweat be saved for funner problems!](https://cushychicken.github.io/embedded-openocd-gdb/)

### Crash Rules Everything Around Me

Now, back to talking J-Links! The major drawback of the J-Link ecosystem has to
be price. The J-Link Base model clocks in at a hefty $450. The Pro Models top
out at just under $1200. That is a _lot_ of cash for what is, at the end of the
day, a programming tool. However, that price pays for a lot of things that most
open source debuggers can't provide:

- Faster downloading and readback
- Network interfaces
- Real Time Trace - Segger's fast semihosting/profiling library

Want to tinker around with some of these features, but lack the budget for a
full-fledged J-Link? There may be a way for you, the solo developer, to get your
hands on their exquisite kit for far cheaper. Segger offers very reasonably
priced versions of their probes as the J-Link EDU and J-Link EDU Mini. However,
you are prohibited from using them for commercial purposes if you get the EDU
models. No cheating! If you're monetizing your work, you should be ponying up
for the Base model at a minimum.

(figure: J-Link EDU Model)

The other minor irk I have with J-Links is their hardware interface. J-Link
designs haven't changed significantly in the decade I've been using them. They
were, and still are, a fairly stock 20 pin, 0.1" interface. This is a blessing
and a curse. On the one hand, it's easy to wire out the J-Link with 0.1" headers
to whatever target device pinout you desire. It's also easy to hack to better
suit your use case - see
[Jay Carlson's delightfully clever 3.3V power hack, for example](https://jaycarlson.net/2017/08/18/make-j-link-less-annoying-two-wire-3-3v-power-fix/).
On the other hand, it means that there's a whole constellation of adapter boards
needed to interface to the multitude of finer-pitched JTAG/SWD connectors. I
would recommend, at a minimum, getting something like
[this Olimex adapter](https://www.olimex.com/Products/ARM/JTAG/ARM-JTAG-20-10/),
which changes the 20-pin, 0.1" JTAG interface to the more common 10-pin, 0.05"
SWD interface common to many modern dev boards.

(figure: Olimex SWD Adapter)
