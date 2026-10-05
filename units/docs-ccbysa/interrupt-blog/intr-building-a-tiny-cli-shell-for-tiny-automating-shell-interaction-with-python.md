---
id: "intr-building-a-tiny-cli-shell-for-tiny-automating-shell-interaction-with-python"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Automating Shell Interaction with Python"
summary: "One of the neatest things about building a formatted and consistent shell interface is that you can then automate interactions with it!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#automating-shell-interaction-with-python"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the neatest things about building a formatted and consistent shell
interface is that you can then automate interactions with it! Using our example
code above running on our nRF52, the following code will connect to the serial
port, write the command `help`, capture the output, and print that to the user.

```python
#!/usr/bin/env python

import serial
import io

# Connect to a device matching what we want
port = list(list_ports.grep(r"/dev/cu.usbmodem*"))[0]
ser = serial.Serial(port.device, 115200, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# Write our command and send immediately
sio.write("hello\n")
sio.flush()

# Our serial implementation prints the input to the shell
command = sio.readline()
# Read the response on the next line
response = sio.readline()
# output to user
print(response)
```

Here's what happens when we run this script:

```
$ python auto_serial.py
Hello World!
```

This ability opens up a huge amount of automation opportunities. By using
scripts to interact with the shell, you can easily:

- Read the values of arbitrary variables and regions of RAM or flash for
  inspection without the use of a debugger.
- Send and receive files from a device's file system.
- Run a suite of automated tests, all of which are individual shell commands
  that return success codes.
- Perform before and after analysis on heaps, battery life, etc. when running
  automated tests.
- Manage a large number of devices connected to a single computer.

### Sharing Automation Scripts

I usually write one-off serial-port-based scripts when I'm frustrated at how
difficult it is to type a very long sequence of commands in, especially on a
firmware shell without history built-in.

Imagine something like:

```
$ wifi on
> OK
$ wifi set MyHotSpot WPA2 mysuperl0ngcomplicat3dpAssw0rd
> OK
$ wifi connect
> OK
```

Typing this in every time I change Wi-Fi hotspots will become tedious for me and
my teammates. In these cases, I suggest taking a few more minutes to productize
these scripts by adding them to a [project
CLI](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects) to easily
share them with others working on the same project.

This way, I could write a simple command that would accept the Wi-Fi hotspot
credentials, and the script would handle connecting to the serial port, running
the commands, and ensuring they were successful.

```
$ invoke wifi --ssid MyHotSpot --key mypassword
Turning on Wifi...
Setting Credentials...
Connecting to Wi-Fi...
Done!
```
