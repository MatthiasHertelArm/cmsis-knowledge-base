---
id: "intr-separating-unique-parameters-from-programming-a-device"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries: Programming a Device"
summary: "Loading hex files is supported by most loaders and debuggers. I chose to use JLink's excellent tools[^jlinkexe], but could just as well have used vendor toolchains such as nrfjprog from Nordic or Simplicity Commander from Silicon Labs."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters#programming-a-device"
license: "CC-BY-SA-4.0"
mode: "V"
---

Loading `hex` files is supported by most loaders and debuggers. I chose to use
JLink's excellent tools[^jlinkexe], but could just as well have used vendor
toolchains such as `nrfjprog` from Nordic or Simplicity Commander from Silicon
Labs.

The JLink command to load a hex file is `loadfile [path].hex\nr\nq`.

Rather than invoke JLink Commander directly, I tend to use a phony Make target
to flash my devices, but if you prefer to use something else that should be
easily achievable. We want our Make target to flash the firmware and the unique
parameters of our device, as well as moving a newly used set of parameters to
the "used" folder.

The Make target generates a J-Link Commander script that loads the
firmware and the keys of a specified device, then the target executes the
script, and moves the keys to the "used" folder if this is the first time they
have been used.

The Makefile I used can be found below.

```make
# Device name. Set develop as default
NODE_NAME=develop

# "used" or "free". Default to reusing a key since develop will most likely already be used
KEY_FOLDER=used

# flashing a free key will automatically place it in the used keys folder
.PHONY: flash
flash:
	@printf "device ATSAMR35J17\nspeed auto\nif SWD\nloadfile ./build/bin/firmware.hex\n" > flashScript.jlink
	@printf "loadfile ./keys/$(KEY_FOLDER)/$(NODE_NAME)/$(NODE_NAME).hex\nr\nq" >> flashScript.jlink
	JLinkExe -CommanderScript flashScript.jlink
ifeq ($(KEY_FOLDER), free))
	mv ./keys/free/$(NODE_NAME) ./keys/used/$(NODE_NAME)
endif
```

Flashing a new device can now be done by running:

```
$ make flash NODE_ID=<nodeid> KEY_FOLDER=free
```
