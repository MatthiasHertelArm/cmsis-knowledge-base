---
id: "intr-better-firmware-with-llvm-clang-installing-llvm-clang"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Installing LLVM/Clang"
summary: "The easiest way to get your hands on the latest release of the LLVM/Clang toolchain is to download the release for your OS from the \"Pre-Built Binaries\" section on the official website."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#installing-llvm-clang"
license: "CC-BY-SA-4.0"
mode: "V"
---

The easiest way to get your hands on the latest release of the LLVM/Clang toolchain is to download
the release for your OS from the
["Pre-Built Binaries" section](https://releases.llvm.org/download.html) on the official website.

In this article, we use LLVM 10.0.0:

```
# OSX
$ wget "https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang+llvm-10.0.0-x86_64-apple-darwin.tar.xz"
$ tar -xf clang+llvm-10.0.0-x86_64-apple-darwin.tar.xz

# Ubuntu
$ wget "https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz"
$ tar -xf clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz
```

Let's add the toolchain to our path:

```bash
# OSX
$ export PATH=`pwd`/clang+llvm-10.0.0-x86_64-apple-darwin/bin:$PATH

# Ubuntu
$ export PATH=`pwd`/clang+llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04/bin:$PATH
```

You can sanity check that the install is working by running `clang --version`:

```bash
$ clang --version
clang version 10.0.0
Target: x86_64-apple-darwin18.5.0
Thread model: posix
InstalledDir: <SHOULD MATCH PATH YOU JUST ADDED ABOVE>
```
