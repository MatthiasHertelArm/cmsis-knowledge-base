---
id: "pyocd-installing-on-non-x86-platforms"
type: "concept"
domain: "debug"
title: "Installing on non-x86 platforms"
summary: "pyOCD itself is pure Python and should run on any platform with a modern Python installation. However, it has several dependencies with binary backends that cause trouble on non-x86 platforms or alternative operating systems (i.e., not macOS, Linux, or Windows)."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/installing_on_non_x86.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/installing_on_non_x86.md"
license: "Apache-2.0"
mode: "V"
---

pyOCD itself is pure Python and should run on any platform with a modern Python installation.
However, it has several dependencies with binary backends that cause trouble on non-x86 platforms or
alternative operating systems (i.e., not macOS, Linux, or Windows). The most common "non-standard"
system that users would like to run pyOCD on is the Raspberry Pi, as well as similar, Arm-based
single-board computers.
