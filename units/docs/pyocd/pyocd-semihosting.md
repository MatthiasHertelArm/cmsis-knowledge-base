---
id: "pyocd-semihosting"
type: "concept"
domain: "debug"
title: "Semihosting"
summary: "Semihosting is a technique for routing I/O requests performed on the target to the host. In addition to I/O, some other operations are supported."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/semihosting.md"
license: "Apache-2.0"
mode: "V"
---

Semihosting is a technique for routing I/O requests performed on the target to the host. In addition to I/O, some other
operations are supported. Most commonly, this means integration of the standard C library with the host's console and
file system. It allows you to log debug messages before you have peripheral drivers fully functioning or on hardware
that does not have other debug output capabilities. It can be used to redirect `printf()` and other standard I/O to or
from the host, read keyboard input, access configuration files, transfer data to and from the target, and so on.

The primary downside to semihosting is that it can be quite slow, depending on how it is used and considerations such
as the debug probe's latency and SWD/JTAG clock speed.

The [Arm semihosting documentation](https://developer.arm.com/documentation/dui0471/i/semihosting/what-is-semihosting-?lang=en)
has more information about semihosting.
