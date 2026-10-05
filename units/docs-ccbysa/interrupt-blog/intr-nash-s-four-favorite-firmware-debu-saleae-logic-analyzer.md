---
id: "intr-nash-s-four-favorite-firmware-debu-saleae-logic-analyzer"
type: "concept"
domain: "debug"
title: "Nash's Four Favorite Firmware Debug Tools: Saleae Logic Analyzer"
summary: "So, if you've got a system driving a lot of toggling IO, and you need to figure out what's going on, what are you gonna do? Your multimeter, as we've just said, isn't gonna cut it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-25-four-favorite-firmware-debug-tools.md"
doc_source: "https://interrupt.memfault.com/blog/four-favorite-firmware-debug-tools#saleae-logic-analyzer"
license: "CC-BY-SA-4.0"
mode: "V"
---

So, if you've got a system driving a lot of toggling IO, and you need to figure
out what's going on, what are you gonna do? Your multimeter, as we've just said,
isn't gonna cut it.

An oscilloscope could certainly do the job. You can easily evaluate whether an
IO is toggling, and measure time-based parameters like duty cycle and rise time.
However, being embedded people, we generally care about interchip
communications: things like UART, I2C, and SPI transactions. You can view these
on oscilloscopes, but they are painful to decode by hand. Almost all scope
vendors offer decoder packages, but they are expensive, and generally not
bundled together. You have to pay a few hundred dollars a pop to unlock UART,
then SPI, then I2C, and so forth for the smorgasbord of digital
signals you need to monitor. On top of that, the UI for many scopes is clunky.
Digital protocol decoders can be a pain to configure and steer using only the
rudimentary knobs and buttons common to most scope UIs. Remote desktops aren't
much better - these tend to be laggy and difficult to drive.

What you really need is a logic analyzer - one that plays nicely with your
development machine.

Fortunately for you, me, and the rest of us embedded folks, this machine exists.

The Saleae Logic Pro16 is, without a doubt, the best logic analyzer on the
market for embedded systems.

(figure: Saleae Logic Pro 16)

### Logic is the Beginning of Wisdom

Unlike a scope, where addon decoder packages need to be purchased, protocol
analysis is baked into the Saleae by default. The device can decode UART, SPI,
and I2C straight out of the box, along with a whole host of other, more obscure
protocols. It can handle CAN, 1Wire, I2S, JTAG, SWD, and a whole slew of digital
comms with aplomb! It's also perfectly capable of triggering and reading
individual asynchronous IO signals as well. Not sure what you're looking for on
your I2C bus? No problem! Set another IO on your MCU to trigger at a known point
in time before the I2C transaction, and the Saleae will do the work of capturing
all signals involved.

The Saleae device itself is, quite literally, a black box. (Well, unless you get
a pink one like I did.) UI and control happen, instead, through a delightful,
easy-to-use GUI. Logic, Saleae's desktop software, makes it a breeze to navigate
logic captures, apply protocol analyzers, and find regions of interest.
Scrolling, zooming, and measuring the time between edges is delightful and simple.
Surprisingly, this is still true with a touch screen laptop. It was a joy to use
a Saleae with my touchscreen-enabled daily driver from a few jobs ago. A big
rewrite of Saleae's firmware and desktop application over the last few years has
made the system real-time capable, too!

(figure: SPI Capture in Logic 2.0)

Saleae also has handy scripting utilities baked into the device.
[A Socket API with Python and C# bindings](https://support.saleae.com/saleae-api-and-sdk/socket-api)
allows you to call all sorts of functionality from your favorite programming
environment. The Python wrapper even comes with
[handy command line functionality.](https://github.com/saleae/python-saleae-cli)

### Illogical

The Saleae is a great tool, but it isn't perfect. It's only tolerant of low
voltage IO signals. Anything between 1.2V and 5V, it can handle with no
problems. Use it on higher voltage signals, and you're gonna have a bad time.
It's also limited to doing relatively low bandwidth digital signals - it caps
out at 500MS/s. This is more than adequate for most routine firmware protocols,
but for higher speed signals like RGMII, USB3.0, or PCIe, you're going to need a
more specialized piece of equipment.

Additionally - being a logic analyzer, you need to take care that you're not
accidentally degrading the signals you're monitoring. This can be particularly
tricky on faster signal buses, where edge rates of signals are shrinking into
single digit nanoseconds. (This author was recently re-educated on this
matter by a quad SPI bus running at 30MHz.) All is not lost, though! There are a
few relatively simple things you can do to eke out all the signal bandwidth you
can out of your Saleae:

- Be sure to include the paired ground test lead when connecting the Saleae to
  your target board.
- Twist the ground connection together with the signal wire. That way, you're
  keeping the impedance of the Saleae's test leads as low as possible.
- Get rid of the grabber clip if you can. Solder a length of 0.1" header to your
  target net, and plug the test lead directly to the header.
- Even better: ask your board designer to drop a set of 0.1" headers onto the
  board. SMT is preferable if you have the space. An SMT header causes less
  interruption of the ground plane and reduces the chance of causing signal
  integrity problems due to your debug probe connection.

(figure: Saleae Logic Pro 16)

The picture above shows my Logic Pro 16 attached to the SPI bus of a little open
source [signal generator board](https://github.com/Cushychicken/bfunc) I
designed in early 2020. It demonstrates the steps you can take to get optimum
performance when sampling speedy digital signals with your Saleae.

To me, Saleae is the best of breed in portable logic analyzers. They certainly
aren't the only device of their kind, though! The Digilent Analog Discovery 2,
Ian Lesnet's Bus Pirate, and Great Scott Gadgets's GreatFET One can all do
similar things to the Saleae. These devices also have the advantage of being a
lot more affordable than the Logic series, which starts at $479 USD for the
Logic 8.
