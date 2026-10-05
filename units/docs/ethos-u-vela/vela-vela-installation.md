---
id: "vela-vela-installation"
type: "concept"
domain: "edge-ai"
title: "Vela: Installation"
summary: "Vela runs on:  Apple macOS  Linux  Microsoft Windows"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:README.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/README.md#installation"
license: "Apache-2.0"
mode: "V"
---

Vela runs on:
* Apple macOS
* Linux
* Microsoft Windows

The simplest way to obtain Vela is to install it directly from [PyPi](https://pypi.org/project/ethos-u-vela/).
The following will install the latest released version:

```bash
pip3 install ethos-u-vela
```

### Requirements

If your system does not match one of the pre-built binary wheels on PyPi then
the installation process will attempt to build Vela from its source code.  To do
this it requires the following:
* Development version of Python 3 containing the Python/C API header files
   - e.g. `apt install python3.10-dev`
* C99 and C++17 capable compiler and toolchain
    - For Apple macOS; XCode or Command Line Tools are recommended,
      see <https://developer.apple.com/xcode/resources/> or `xcode-select --install`
    - For Linux operating systems; a GNU or Clang toolchain is recommended,
      e.g. `apt install build-essential`
    - For Microsoft Windows 10; the Microsoft Visual C++ 14.2 Build Tools are recommended,
      see <https://wiki.python.org/moin/WindowsCompilers>
* CMake
    - See <https://cmake.org/download/>

### Manually Building

The source code is available from [Arm's GitLab Instance](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela),
see [Building From Source](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/BUILD.md) for more details.

### Development builds

Development builds are also available as Python wheels in the GitLab Package
Registry. The development builds reflect the current state of the code and
are **not of release quality**.

#### Install the latest nightly build

```bash
pip3 install --pre --only-binary=ethos-u-vela \
  --index-url=https://gitlab.arm.com/api/v4/projects/10397/packages/pypi/simple \
  ethos-u-vela
```

#### Install a specific nightly build

```bash
pip3 install --only-binary=ethos-u-vela \
  --index-url=https://gitlab.arm.com/api/v4/projects/10397/packages/pypi/simple \
  "ethos-u-vela==<exact dev version>"
```

#### Discover available nightly versions

Use `pip index versions` with pre-releases enabled and restrict to wheels:

```bash
pip3 index versions --pre --only-binary=ethos-u-vela \
  --index-url=https://gitlab.arm.com/api/v4/projects/10397/packages/pypi/simple \
  ethos-u-vela
```

Or browse the Package Registry on GitLab:
https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/packages
