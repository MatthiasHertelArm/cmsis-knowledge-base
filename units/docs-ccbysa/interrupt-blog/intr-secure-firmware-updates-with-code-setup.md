---
id: "intr-secure-firmware-updates-with-code-setup"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Firmware Signing Implementation / Setup"
summary: "Part of: Firmware Signing Implementation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Firmware Signing Implementation_

Like we did our previous post, the [Firmware Update Cookbook](https://interrupt.memfault.com/blog/device-firmware-update-cookbook), we use [Renode](https://interrupt.memfault.com/blog/intro-to-renode) to run the examples in this post. The previous post contains detailed instructions, but in short:

```
# Clone the repository & navigate to the example
$ git clone https://github.com/memfault/interrupt.git
$ cd examples/fwup-signing

# Build project and start Renode
$ make && ./start.sh
```

One change we did make from previous posts is run in headless mode. This is done
by invoking Renode with the following flags:

```
mono64 $RENODE_EXE_PATH renode-config.resc --port 4444 --disable-xwt
```

We can then use telnet to connect to the Renode console:

```
$ telnet localhost 4444
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Renode, version 1.9.0.28660 (cd1a61a4-202006301553)

(monitor) i $CWD/renode-config.resc
(STM32F429) start
Starting emulation...
(STM32F429) q
Renode is quitting
```

Similarly, we route the device UART to a telnet port rather than a graphical
window by adding two lines to our `renode-config.resc`:

```
emulation CreateServerSocketTerminal 4445 "externalUART"
connector Connect sysbus.uart2 externalUART
```

We can then access our emulated device's UART via telnet as well:

```
$ telnet localhost 4445
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Bootloader started
Valid public key
Invalid signature
Booting slot 1
Shared memory uinitialized, setting magic
Loader STARTED - version 1.0.0 (4015f0a)
Booting slot 2
App STARTED - version 1.0.1 (4015f0a) - CRC 0x1b11019d
```
