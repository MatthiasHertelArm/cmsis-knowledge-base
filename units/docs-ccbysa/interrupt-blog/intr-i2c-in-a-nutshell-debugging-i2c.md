---
id: "intr-i2c-in-a-nutshell-debugging-i2c"
type: "concept"
domain: "debug"
title: "I2C in a Nutshell: Debugging I2C"
summary: "While I2C is a robust and simple protocol, firmware engineers find themselves debugging unresponsive devices on most projects."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-22-i2c-in-a-nutshell.md"
doc_source: "https://interrupt.memfault.com/blog/i2c-in-a-nutshell#debugging-i2c"
license: "CC-BY-SA-4.0"
mode: "V"
---

While I2C is a robust and simple protocol, firmware engineers find themselves
debugging unresponsive devices on most projects.

Consider the following scenario: you just received a new board and are doing
bringup. You've implemented a simple I2C transaction to read the chip ID of a
slave device, but are getting back an error (or all 0s).

Let's walk through what could be going wrong.

### Incompatible Devices

The first thing to check is that the master and slave devices are compatible
with each other. While I2C is a standard, there are a couple of extensions to it
which are not always implemented by every device on the bus.

Specifically, we've seen two optional features which can lead to problems:
1. 400Kbps bus speed: the original I2C standard specified a bus speed of 100Kbps,
   but many modern devices support the optional 400Kbps mode. If your master
device clocks data in at 400Kbps but your slave only supports 100Kbps, the slave
may not respond.
2. Clock stretching: clock stretching is an optional feature of the standard,
   and some slave devices do not support it.

Check your datasheets, and if needed disable optional features on your master
device. In doubt, slow the clock down to 100Kbps and disable clock stretching in
firmware while configuring your I2C peripheral.

### Misconfigured Peripherals

Next, you will want to grab a logic analyzer and probe the SDA and SCL signals.
We're partial to Saleae devices, which come with an easy to set up I2C
decoder[^2].

Looking at a recording of those lines, you should see the SCL line pulse when
data is being sent. You can set a trigger on a high to low transition of the
clock line if that is easier.

If the line stays permanently low, time to check the pull-ups (see the "Line
Pull-Up" section below).
If the lines stay high, the I2C peripheral in your MCU is likely misconfigured. Check the
code again:
1. Are you checking the return value of the I2C initialization and read/write
   functions? Some peripheral configurations are invalid and will emit errors.
For example, a specific I2C peripheral may only be able to map to specific pins.
Initializing it with the wrong pins will lead to an error.
2. Is your I2C init function being called? Connect your debugger and set a
   breakpoint in it. Make sure it completes properly.
3. Are all the necessary clocks enabled? I2C peripherals rely on specific PLLs
   or other clocks to generate their signal. Check your silicon vendor's
application notes and make sure you've got the right set of peripherals enabled.

If your logic analyzer trace looks like I2C traffic, time to dig deeper into
addresses.

### I2C Address Issues

Often times, you will see the following on your logic analyzer:

`<script type="WaveDrom">`
{ signal :
  [
    { name: "SDA",  wave: "101.0.1.01.01."},
    { name: "SCL",  wave: "1.n.........h."},
    { name: "bits", wave: "x==========x=x",  data: ["S", "1", "1", "0", "0", "1", "1","0","1","1","P"]},
    { name: "data", wave: "x.=......==x..", data: ["Address: 0x66","W", "N"]}
  ],
}
`</script>`

An address is sent on the bus, but it is NACK-ed. Note that NACK is the default
state of the lines, so often times it just means: nobody answered.

The first thing to check is: is the address correct? Your logic analyzer will
often decode it as a byte, so you will need to shift it down by one bit to
recover the 7-bit address. For example, 7-bit address 0x18 would show up as 0x30
in a byte with the lsb set to 0. Check that address against your device's
datasheet.

Some devices have configurable addresses. Check your schematic to make sure
configuration pins are pulled up or down as you would expect them.

Last, make sure you do not have address conflicts on your bus. Create a
spreadsheet with the addresses of all the devices on the bus, and check for
duplicates.

If the address is correct and there are no duplicates, the problem is likely
with the slave device. Go to "Slave device disabled or not working".

### Slave device disabled or not working

If the address is correct but the slave device does not ACK it, it is likely not
working properly. More often than not, this is because it is not powered or held
in reset. Grab your voltmeter and start checking pins:
* Is the power supply of your slave device enabled? You may need to turn on a
  regulator or toggle a MOSFET.
* Is the chip power the correct voltage?
* Does your slave device have a reset pin? Check that pin and make sure reset is
  not asserted.
* Does it have an I2C-enable pin? Is that in the correct state?

If all the voltages are correct, test another board or replace the IC. Perhaps
an electrostatic discharge damaged your device. If that does not resolve your
issue, go to "Line Pull-Up".

### Line Pull-Up

I2C relies on resistors to pull the lines up to the logic HIGH voltage.
These resistors may be missing, have too high a resistance, or be connected to a
rail at the wrong voltage.

To find it, grab an oscilloscope and probe both the SDA and SCL lines. First,
set the oscilloscope in free-running mode and check the voltage:
* If it is consistently 0, pull-up resistors either are missing, or a device is
  holding the bus low. Check the layout, and verify the pullups are on the
board. If they are, start removing I2C devices from the bus by depopulating
them until the line rises back to high.
* If it is consistently high, devices are not attempting to communicate over
  I2C. See the "Misconfigured I2C Peripherals" section.
* Is the voltage correct? Some devices operate at 5V, some at 3.3V, and some
  even at 1.8V. If a device is expecting a different voltage, it will need to
be connected to the bus through a level translator.

If it is toggling, set your oscilloscope to trigger on an edge, and look at the
signal. It will likely look like one of these two scope shots shared on
StackExchange [^3]:




Notice how the second image has sharp, square pulses while the first image has
rounded ones? This is your tell. Round pulses are an indications that your
pull-ups are too weak. Your logic analyzer might decode them just fine, but an
I2C device may have trouble with them.

I2C buses accumulate capacitances when traces are long and devices are
added to the bus. You may need stronger pull-ups to overcome it. Counter intuitively, a stronger pull-up is a weaker resistor. In doubt, go to 2K
resistors. You will waste a bit of power, but your I2C signal will look great.

### Flowchart

To make the process easier, we've put together a flowchart summarizing the I2C
debugging process. You can find it below, or download it
[here]().
