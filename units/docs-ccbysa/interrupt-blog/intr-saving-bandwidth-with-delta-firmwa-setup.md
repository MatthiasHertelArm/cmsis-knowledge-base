---
id: "intr-saving-bandwidth-with-delta-firmwa-setup"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Implementation / Setup"
summary: "Like we did in our previous posts, we use Renode to run the examples in this post. We are using a virtualized STM32 on which we are running a complete firmware image."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Delta Updates Implementation_

Like we did in our previous posts, we use [Renode](https://interrupt.memfault.com/blog/intro-to-renode) to run the examples in this post. We are using a
virtualized STM32 on which we are running a complete firmware image. The
previous post contains detailed instructions, but in short:

```
# Clone the repository & navigate to the example
$ git clone https://github.com/memfault/interrupt.git
$ cd examples/fwup-delta

# Build project and start Renode
$ make && ./start.sh
```

You can then find the Renode monitor via telnet and start the simulation:

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

You can also tail the device's USART output via telnet:

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
