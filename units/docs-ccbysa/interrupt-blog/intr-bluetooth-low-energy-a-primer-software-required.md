---
id: "intr-bluetooth-low-energy-a-primer-software-required"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Implementation of a BLE Peripheral (nRF52 example) / Software required:"
summary: "Part of: Implementation of a BLE Peripheral (nRF52 example)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#software-required"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementation of a BLE Peripheral (nRF52 example)_

Here's a list of the software packages required for following the steps in this tutorial:

- [Nordic Semiconductor's nRF5 SDK](https://www.nordicsemi.com/Software-and-Tools/Software/nRF5-SDK/Download#infotabs) (we'll be using SDK version 15.3.0).
- [Nordic Semiconductor's nRF5 Command Line Tools for macOS](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF5-Command-Line-Tools/Download#infotabs) (we'll be using version 9.8.1).
- [SEGGER J-Link Software for macOS](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack) (we'll be using version V6.44g).
- [GNU Arm Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads) (we'll be using version 7-2017-q4-major which is recommended by Nordic per [this article](https://devzone.nordicsemi.com/b/blog/posts/using-gdb-with-nordic-devices)).
- [CoolTerm serial terminal program](https://freeware.the-meiers.org/CoolTermMac.zip) (or any other serial terminal program).
- Xcode Command Line Tools — [For installation steps, I found this tutorial quite helpful and easy to follow](https://www.embarcadero.com/starthere/berlin/mobdevsetup/ios/en/installing_the_xcode_command_line_tools_on_a_mac.html).
- A BLE Central mobile app such as **nRF Connect** ([iOS](https://apps.apple.com/us/app/nrf-connect/id1054362403) or [Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en_US)) or **LightBlue** ([iOS](https://apps.apple.com/us/app/lightblue-explorer/id557428110) or [Android](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer&hl=en_US))
