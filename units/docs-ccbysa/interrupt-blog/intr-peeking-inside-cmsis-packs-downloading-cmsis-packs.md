---
id: "intr-peeking-inside-cmsis-packs-downloading-cmsis-packs"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: Downloading CMSIS-Packs"
summary: "The list of published CMSIS-Packs is available here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#downloading-cmsis-packs"
license: "CC-BY-SA-4.0"
mode: "V"
---

The list of published CMSIS-Packs is available here:

> <https://developer.arm.com/tools-and-software/embedded/cmsis/cmsis-packs>

The `.pack` files can be downloaded directly from there.

However, there's another option for searching and retrieving CMSIS-Packs,
courtesy of one of my favorite tools: **PyOCD**

> PyOCD integrates CMSIS-Pack management as a way of accessing flash algorithms
> for chips not natively supported by the tool. It's a pretty awesome way to
> provide flashing support to a LOT of chips!

> To learn more, check out our [Deep Dive into ARM Cortex-M Debug Interfaces](https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces).

For example, if I wanted the CMSIS-Pack for an Atmel SAMD21 chip, I can run
these commands from my terminal:

```bash
# install pyocd using the python package manager, pip
❯ pip install pyocd
# search for my part
❯ pyocd pack find samd21
  Part            Vendor      Pack         Version   Installed
----------------------------------------------------------------
  ATSAMD21E15A    Microchip   SAMD21_DFP   3.5.132   True
  ATSAMD21E15B    Microchip   SAMD21_DFP   3.5.132   True
...
```

There are several chips supported by a single CMSIS-Pack in this case. I can
download the pack using the `install` command (it will match the correct pack
based on the shortened name I provide, or you can specify the exact chip name,
both are identical in this case but may be different for other chips):

```bash
❯ pyocd pack install samd21
Downloading packs (press Control-C to cancel):
    Microchip::SAMD21_DFP::3.5.132
Downloading descriptors (001/001)
```

Great! now that we've downloaded the pack... where is it and what do we do with
it?!

First we need to find it. PyOCD stores packs in a cache directory- we can use
this python one-liner to find out where that is:

```bash
❯ python -c 'import cmsis_pack_manager; print(cmsis_pack_manager.Cache(False, False).data_path)'
/home/noah/.local/share/cmsis-pack-manager

# on my system, it was under the home directory; see `man file-hierarchy`
# section on 'HOME DIRECTORY' for why it makes sense for PyOCD to use that!

# search that location for any *.pack files
❯ find "$(python -c 'import cmsis_pack_manager; print(cmsis_pack_manager.Cache(False, False).data_path)')" -name '*.pack'
/home/noah/.local/share/cmsis-pack-manager/Keil/STM32F4xx_DFP/2.15.0.pack
/home/noah/.local/share/cmsis-pack-manager/Microchip/SAMD21_DFP/3.5.132.pack

# I've got 2 pack files installed on my system. to extract one of them, I can
# unzip it somewhere
❯ mkdir -p /tmp/unpack
❯ cd /tmp/unpack
❯ unzip /home/noah/.local/share/cmsis-pack-manager/Microchip/SAMD21_DFP/3.5.132.pack
```

At this point, it's a bit of an exploration for the files we're interested in.
You can search for `*.svd` files, `*.FLM` files, linker scripts `*.ld`, CMSIS
header files, etc.
