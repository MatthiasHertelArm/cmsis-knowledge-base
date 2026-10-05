---
id: "intr-seamless-firmware-development-with-what-is-platformio"
type: "concept"
domain: "debug"
title: "Seamless firmware development with PlatformIO: What is PlatformIO?"
summary: "PlatformIO is a set of open source tools targeted at professional embedded developers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-08-seamless-firmware-with-platformio.md"
doc_source: "https://interrupt.memfault.com/blog/seamless-firmware-with-platformio#what-is-platformio"
license: "CC-BY-SA-4.0"
mode: "V"
---

PlatformIO is a set of open source tools targeted at professional embedded
developers.  Foremost of those tools is the PlatformIO Plugin for VSCode which
is used by hundreds of thousands of embedded developers to create, compile,
debug, and test embedded projects.

At its core, PlatformIO is made up of the following subsystems:
1. Project management: a tool to create, configure, and manage projects
2. Package management: a registry and a client to host libraries for embedded
   systems and easily add or remove them from a project
3. Build system: a build configuration and execution system. PlatformIO replaces
   make, cmake, and others.
4. Workflow automation: automation and integrations to debug, run unit tests,
   run static analyzers, and other tools for your project.

When it works, PlatformIO is magical. Want to start a project for STM32
STM32Cube, compiled with ARM GCC 5.2.1? No need to go find an SDK online, Simply
tweak a few configurations files, run a few CLI commands, and you're off too the
races. We do this in the next section of this article.

However, the set of supported targets can be hit or miss.

### Supported Targets

PlatformIO defines targets as a combination as three components:
1. The "platform", which is the MCU family. For example, both the STM32 and the
   nRF52 are supported platforms.
2. The "framework", which is the SDK being used on the project. This includes
   vendor SDK, such as the STM32Cube, as well as RTOS-es such as Zephyr or
FreeRTOS, true frameworks such as Arduino, and alternative APIs such as
libopencm3 and CMSIS.
3. The "board" which defines the specific board you are using. PlatformIO comes
   with hundreds of board configuration for popular development boards like the
STM32 Discovery boards.

The headline numbers are impressive: 41 platforms, 23 frameworks, and 924 boards
as of this writing.

However, reality is a bit less rosy: while some MCU families are extremely well
covered, others have very little support.

One important example is official vendor SDK. PlatformIO only supports the
vendor SDKs for the following MCUs, which it considers individual "frameworks":
* Espressif family (ESP8266, ESP32)
* Kendryte K210
* STM32
* Gigadevice GD32V
* SiFive FE310 and FU540

If you are able to piggy back on an RTOS, things look a bit better. For example,
you can create a Zephyr project with PlatformIO for Atmel SAM, Freescale
Kinetis, Nordic nRF5, NXP iMX RT, NXP LPC, Silabs EFM32, and STM32.

You can use the PlatformIO client to list supported frameworks, platforms, and
boards. The list changes regularly, as the project is very active. Here's the
command you want to run:

```
  # List platforms
  $ pio platform search

  # List frameworks
  $ pio platform frameworks

  # List boards
  $ pio boards
```

### Package Management

PlatformIO hosts a registry of embedded libraries which can be added to every
project. Popular libraries like the lwIP networking stack, the nanopb protocol
buffer implementation, or the mbedTLS SSL library are all available in one form
or another.

Here again, it is magical when it works. Simply add a library to your project by
calling `pio lib install` and rebuild your project. PlatformIO will fetch the
correct bundle, compile a static library, link it into your project, and expose
the header files.

However, the same issue with supported targets gets in the way of using
libraries. Each library lists frameworks and platforms it is compatible with,
and if yours is not listed you cannot use it. Of the more than 10,000 libraries
in the registry, only about 139 of them are compatible with the STM32 +
STM32Cube combo.

Anyone can publish a library to the repository, by following the excellent
online documentation[^library_docs].

Looking for packages is done with the `pio lib search` command. Here are a few
examples:

```
# Look for all libraries that support STM32 + STM32Cube
$ pio lib search -p stm32 -f STM32Cube
...
# Look for mbedtls
$ pio lib search -n mbedtls
...
```

Installing them is done with the `pio install` command.

### Build System

PlatformIO is an opinionated system, and as long as you follow its rules
building a project with it is seamless. Simply add your project source under
`src`, your header files under `include`, and your private libraries under
`lib`. Run `pio run`, and you're cooking with gas!

Under the hood, it uses the SCons[^scons] build system. Most of the
time, this is of no consequence to the user as plenty of configuration options
are exposed via the `platformio.ini` file used to configure each project.

For example, you can change compiler and linker flags by adding the
`build_flags` variable to your `platformio.ini`:

```
[env:release]
platform = ststm32
board = disco_f429zi
framework = stm32cube
build_flags = -Wall -Wl,--gc-sections
```

Should you need to customize your build beyond what the `.ini` file provides,
you will need to write SCons scripts which are invoked by the PlatformIO build
environment. SCons scripts are written in Python.

Two hooks are available for those scripts: a PRE hook which runs before the
build executes, a POST hook which runs after the build. You can use these hooks
to change the build instructions for individual files, pre-process some source
code, or post-process the build artifacts[^advanced_scripting].

While some may chafe at the need to learn yet another build system - I for one
still like my Makefiles - SCons is a mature and powerful build system.
