---
id: "intr-nash-s-four-favorite-firmware-debu-fluke-multimeter"
type: "concept"
domain: "debug"
title: "Nash's Four Favorite Firmware Debug Tools: Fluke Multimeter"
summary: "A multimeter is an essential piece of embedded debug equipment. No multimeter is quite as well known as the Fluke handheld 100 series of meters. This is partly by design - their iconic yellow and gray look is trademarked."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-25-four-favorite-firmware-debug-tools.md"
doc_source: "https://interrupt.memfault.com/blog/four-favorite-firmware-debug-tools#fluke-multimeter"
license: "CC-BY-SA-4.0"
mode: "V"
---

A multimeter is an essential piece of embedded debug equipment. No multimeter is
quite as well known as the Fluke handheld 100 series of meters. This is partly
by design - their iconic yellow and gray look is trademarked.
([For good reason, too!](https://www.sparkfun.com/news/1430)) I particularly
love my Fluke 117 handheld meter. It's a handy tool for all sorts of
nuts-and-bolts electrical measurements: current, voltage, DC, AC, autoranging,
resistance, capacitance, diode IV ratings, beep for continuity, and a whole host
of other features that I can't think of unless I go dig the manual out of a
drawer. What's not to love?

(figure: The closest you'll ever get to an "action shot" with a Fluke meter)

### The Good Parts

A multimeter is a great way to answer all sorts of table stakes questions about
your embedded system - for example:

- Is this chip receiving power?
- Are all of the voltage regulators powered?
- Are these two nets shorted?
- Is the reset line asserted/deasserted?
- Is some control line in its proper high/low state?
- How much current is being sunk into my board? (Be careful with this one -
  beyond 10A, you don't have a fuse to save you if things get hot!)
- Is my DAC putting out any analog signal at all?
- What's the quiescent voltage of this ADC input?

Any decent multimeter is capable of this. However, the Fluke models include a
wealth of creature comforts that make it a joy to use:

- an "auto off” feature that shuts the meter off after a certain idle period, to
  conserve battery (I've killed many a 9V battery by forgetting to turn off
  cheaper meters I've owned.)
- a backlit display that's easy to turn on and off at the tap of a button
- a plastic kickstand, so it can stand upright on a tabletop or workbench
- probe clips on the back side of the casing, and a handy soft carrying case
- features for magnetic hanging loops (which I've never used but look
  thrillingly cool
  [if you need to hang your meter from a ferromagnetic rail](https://www.fluke.com/en-us/product/accessories/magnetic-hangers-utility-tools/tpak))

It's details like this that really elevate Fluke above a generic DMM from
Amazon.

### The Limitations

While extremely versatile, a multimeter can't do everything. They are only
designed for measuring relatively static signals. You can only get an accurate
voltage reading with a multimeter when the target is at a steady state. A
toggling GPIO, for example, will show a voltage reading on your meter as a
function of its duty cycle. This is because most multimeters are built around a
type of
[integrating data converter](https://en.wikipedia.org/wiki/Integrating_ADC)
called a dual-slope ADC. Dual slope ADCs have several key advantages: they are
very robust to component tolerances, easy to auto-zero/auto-calibrate, and
consume very little power. What they trade off to do this is bandwidth. Dual
slope ADCs are not fast. A relatively pedestrian SAR ADC can take a million
samples per second. In contrast, a slope-integrating converter generally cannot
exceed a hundred samples per second. This slower speed comes with its own
advantages, however: better noise performance, and better notch rejection of
unwanted frequencies - particularly those at 50 Hz and 60Hz. If your integrating
converter itch isn't well scratched yet, Maxim Integrated has
[an excellent tech note](https://www.maximintegrated.com/en/design/technical-documents/tutorials/1/1041.html)
describing dual slope ADC theory of operation in great detail.

One last note: the handheld models of multimeter tend to be fairly low
precision. You'll have a hard time measuring anything below 0.01 digits of
voltage, current, or resistance. If you need a lower level of detail - say, for
measuring precision shunt resistors - a benchtop six digit multimeter from
Keithley or similar is a better bet. However, this level of precision is not
typically required for garden variety embedded work.
