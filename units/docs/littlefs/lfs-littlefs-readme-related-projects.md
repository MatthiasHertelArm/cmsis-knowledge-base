---
id: "lfs-littlefs-readme-related-projects"
type: "concept"
domain: "project"
title: "littlefs README: Related projects"
summary: "[BSD-3-Clause]: https://spdx.org/licenses/BSD-3-Clause.html [littlefs-fuse]: https://github.com/geky/littlefs-fuse [FUSE]: https://github.com/libfuse/libfuse [littlefs-js]: https://github.com/geky/littlefs-js [littlefs-js-demo]:http://littlefs.geky.net/demo.html [littlefs-python]: https://pypi.org/project/littlefs-python/ [littlefs-toy]: https://github.com/tjko/littlefs-toy [littlefs2-rust]: https://crates.io/crates/littlefs2 [nim-littlefs]: https://github.com/Graveflo/nim-littlefs [chamelon]: https://github.com/yomimono/chamelon [littlefs-disk-img-viewer]: https://github.com/tniessen/littlefs-disk-img-viewer [mklfs]: https://github.com/whitecatboard/Lua-RTOS-ESP32/tree/master/components/mklfs/src [mklittlefs]: https://github.com/earlephilhower/mklittlefs [pico-littlefs-usb]: https://github.com/oyama/pico-littlefs-usb [ramcrc32bd]: https://github.com/geky/ramcrc32bd [ramrsbd]: https://github.com/geky/ramrsbd [Mbed OS]: https://github.com/armmbed/mbed-os [LittleFileSystem]: https://os.mbed.com/docs/mbed-os/latest/apis/littlefilesystem.html [SPIFFS]: https://github.com/pellepl/spiffs …"
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#related-projects"
license: "BSD-3-Clause"
mode: "V"
---

- [littlefs-fuse] - A [FUSE] wrapper for littlefs. The project allows you to
  mount littlefs directly on a Linux machine. Can be useful for debugging
  littlefs if you have an SD card handy.

- [littlefs-js] - A javascript wrapper for littlefs. I'm not sure why you would
  want this, but it is handy for demos.  You can see it in action
  [here][littlefs-js-demo].
  
- [littlefs-python] - A Python wrapper for littlefs. The project allows you
  to create images of the filesystem on your PC. Check if littlefs will fit
  your needs, create images for a later download to the target memory or
  inspect the content of a binary image of the target memory.

- [littlefs-toy] - A command-line tool for creating and working with littlefs
  images. Uses syntax similar to tar command for ease of use. Supports working
  on littlefs images embedded inside another file (firmware image, etc).

- [littlefs2-rust] - A Rust wrapper for littlefs. This project allows you
  to use littlefs in a Rust-friendly API, reaping the benefits of Rust's memory
  safety and other guarantees.

- [nim-littlefs] - A Nim wrapper and API for littlefs. Includes a fuse
  implementation based on [littlefs-fuse]

- [chamelon] - A pure-OCaml implementation of (most of) littlefs, designed for
  use with the MirageOS library operating system project. It is interoperable
  with the reference implementation, with some caveats.

- [littlefs-disk-img-viewer] - A memory-efficient web application for viewing
  littlefs disk images in your web browser.

- [mklfs] - A command line tool for creating littlefs images. Used in the Lua
  RTOS ecosystem.

- [mklittlefs] - A command line tool for creating littlefs images. Used in the
  ESP8266 and RP2040 ecosystem.

- [pico-littlefs-usb] - An interface for littlefs that emulates a FAT12
  filesystem over USB. Allows mounting littlefs on a host PC without additional
  drivers.

- [ramcrc32bd] - An example block device using littlefs's 32-bit CRC for
  error-correction.

- [ramrsbd] - An example block device using Reed-Solomon codes for
  error-correction.

- [Mbed OS] - The easiest way to get started with littlefs is to jump into Mbed
  which already has block device drivers for most forms of embedded storage.
  littlefs is available in Mbed OS as the [LittleFileSystem] class.

- [SPIFFS] - Another excellent embedded filesystem for NOR flash. As a more
  traditional logging filesystem with full static wear-leveling, SPIFFS will
  likely outperform littlefs on small memories such as the internal flash on
  microcontrollers.

- [Dhara] - An interesting NAND flash translation layer designed for small
  MCUs. It offers static wear-leveling and power-resilience with only a fixed
  _O(|address|)_ pointer structure stored on each block and in RAM.

- [ChaN's FatFs] - A lightweight reimplementation of the infamous FAT filesystem
  for microcontroller-scale devices. Due to limitations of FAT it can't provide
  power-loss resilience, but it does allow easy interop with PCs.

[BSD-3-Clause]: https://spdx.org/licenses/BSD-3-Clause.html
[littlefs-fuse]: https://github.com/geky/littlefs-fuse
[FUSE]: https://github.com/libfuse/libfuse
[littlefs-js]: https://github.com/geky/littlefs-js
[littlefs-js-demo]:http://littlefs.geky.net/demo.html
[littlefs-python]: https://pypi.org/project/littlefs-python/
[littlefs-toy]: https://github.com/tjko/littlefs-toy
[littlefs2-rust]: https://crates.io/crates/littlefs2
[nim-littlefs]: https://github.com/Graveflo/nim-littlefs
[chamelon]: https://github.com/yomimono/chamelon
[littlefs-disk-img-viewer]: https://github.com/tniessen/littlefs-disk-img-viewer
[mklfs]: https://github.com/whitecatboard/Lua-RTOS-ESP32/tree/master/components/mklfs/src
[mklittlefs]: https://github.com/earlephilhower/mklittlefs
[pico-littlefs-usb]: https://github.com/oyama/pico-littlefs-usb
[ramcrc32bd]: https://github.com/geky/ramcrc32bd
[ramrsbd]: https://github.com/geky/ramrsbd
[Mbed OS]: https://github.com/armmbed/mbed-os
[LittleFileSystem]: https://os.mbed.com/docs/mbed-os/latest/apis/littlefilesystem.html
[SPIFFS]: https://github.com/pellepl/spiffs
[Dhara]: https://github.com/dlbeer/dhara
[ChaN's FatFs]: http://elm-chan.org/fsw/ff/00index_e.html
