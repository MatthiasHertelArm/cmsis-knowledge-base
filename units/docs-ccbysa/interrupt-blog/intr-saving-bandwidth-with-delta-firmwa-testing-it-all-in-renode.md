---
id: "intr-saving-bandwidth-with-delta-firmwa-testing-it-all-in-renode"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Implementation / Testing it all in Renode"
summary: "Once we've built all of our image, we simply need to start Renode by running the provided start.sh or mono64 Renode.exe renode-config.resc --port 4444 --disable-xwt."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#testing-it-all-in-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Delta Updates Implementation_

Once we've built all of our image, we simply need to start Renode by running the
provided `start.sh` or `mono64 Renode.exe renode-config.resc --port 4444
--disable-xwt`.

We then perform the update on the USART console:

```
➜  ~ telnet localhost 4445
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Bootloader started
Booting slot 1
Shared memory initialized, setting magic
Loader STARTED - version 1.0.0 (01b2209)
Booting slot 2
App STARTED - version 1.0.1 (01b2209) - CRC 0x77a58907

shell> dfu-mode
Rebooting into DFU mode
Bootloader started
Booting slot 1
Loader STARTED - version 1.0.0 (01b2209)
Entering DFU Mode

shell> do-dfu
Starting update
Patching data
Validating image
Checking signature
Committing image
Rebooting
Bootloader started
Booting slot 1
Loader STARTED - version 1.0.0 (01b2209)
Booting slot 2
App STARTED - version 1.0.1 (01b2209) - CRC 0xea1a3793

shell> This application was patched! <--- It worked!
```

We can see "This application was patched!" print after the update (but not
before). Everything is working!
