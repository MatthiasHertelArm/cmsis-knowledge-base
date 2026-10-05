---
id: "intr-cortex-m-mcu-emulation-with-renode-installing-renode"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode: Installing Renode"
summary: "The Renode project releases installers for Windows, MacOS, and multiple Linux distributions. As of this writing, you can find the v1.9 release on Github."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode#installing-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Renode project releases installers for Windows, MacOS, and multiple Linux
distributions. As of this writing, you can find the v1.9 release on
[Github](https://github.com/renode/renode/releases/tag/v1.9.0).

This guide was written on MacOS, though it is not OS specific.

To verify your Renode installation, you can run one of the examples:

1. Open Renode, on MacOS I prefer to use the command line directly with `$ sh /Applications/Renode.app/Contents/MacOS/macos_run.command`
2. A Renode terminal window will open. Load the example with `start @scripts/single-node/stm32f4_discovery.resc`
   
3. A second terminal window should open, displaying serial output
   
