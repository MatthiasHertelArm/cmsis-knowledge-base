---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-strings"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / strings"
summary: "As the name implies, strings will display all the strings in a binary. I typically use the tool in the following ways:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#strings"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

As the name implies, `strings` will display all the strings in a binary. I typically use the tool
in the following ways:

1. To check for security holes in a binary (i.e encryption keys, hard coded passwords, etc)
2. As a mechanism for quickly saving [code space](https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags). More often than not there are a couple
   unexpectedly long file names or command line strings in a binary that can be trimmed.

There's two particularly helpful arguments:

- `-d` - Causes only data sections (code in the actual binary) to be scanned rather than parts of
  the ELF that are not in the binary.
- `-n <number>` - Can be used to control the minimum string length scanned for.

#### Leveraging `strings` to Save Code Space

Let's take a look at the longest strings in the Zephyr `samples/net/wifi` application:

```bash
$ cd <zephyr_project>/samples/net/wifi
$ west build -b disco_l475_iot1

$ arm-none-eabi-strings -n5 -d build/zephyr/zephyr.elf |
   awk '{ print length, $0 }' | sort -n
// ...
94 Ctrl+a, Ctrl+b, Ctrl+c, Ctrl+d, Ctrl+e, Ctrl+f, Ctrl+k, Ctrl+l, Ctrl+n, Ctrl+p, Ctrl+u, Ctrl+w
96 'net dns <hostname> [A or AAAA]' queries IPv4 address (default) or IPv6 address for a host name.
99 'net ping [-c count] [-i interval ms] <host>' Send ICMPv4 or ICMPv6 Echo-Request to a network host.
104 'log disable <module_0> .. <module_n>' disables logs in specified modules (all if no modules specified).
130 'log enable <level> <module_0> ...  <module_n>' enables logs up to given level in specified modules (all if no modules specified).
148 Some terminals are not sending separate escape code for backspace and delete button. This command forces shell to interpret delete key as backspace.
159 Console gets terminal screen size or assumes 80 in case the readout fails. It must be executed after each terminal width change to ensure correct text display.
```

Neat! We've found a few long strings printed by the console that we could consider removing if we
were desperate to save some code space!
