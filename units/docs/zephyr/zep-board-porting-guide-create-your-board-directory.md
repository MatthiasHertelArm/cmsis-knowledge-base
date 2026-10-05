---
id: "zep-board-porting-guide-create-your-board-directory"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Create your board directory"
summary: "Once you've found an existing board that uses your SoC, you can usually start by copy/pasting its board directory and changing its contents for your hardware."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Once you've found an existing board that uses your SoC, you can usually start
by copy/pasting its board directory and changing its contents for your
hardware.

You need to give your board a unique name. Run `west boards` for a list of
names that are already taken, and pick something new. Let's say your board is
called `plank` (please don't actually use that name).

Start by creating the board directory `zephyr/boards/<VENDOR>/plank`, where
`<VENDOR>` is your vendor subdirectory. (You don't have to put your
board directory in the zephyr repository, but it's the easiest way to get
started. See custom_board_definition for documentation on moving your
board directory to a separate repository once it's working.)


**Note:** A `<VENDOR>` subdirectory is mandatory if contributing your board to Zephyr, but if your board is placed in a local repo, then any folder structure under `<your-repo>/boards` is permitted. If the vendor is defined in the list in that vendor prefix as `<VENDOR>`. `others` may be used as vendor prefix if the vendor is not defined.


**Note:** The board directory name does not need to match the name of the board. Multiple boards can even be defined in one directory.

Your board directory should look like this:

```none

boards/<VENDOR>/plank
├── board.yml
├── board.cmake
├── CMakeLists.txt
├── doc
│   ├── plank.webp
│   └── index.rst
├── Kconfig.plank
├── Kconfig.defconfig
├── plank_<qualifiers>_defconfig
├── plank_<qualifiers>.dts
└── plank_<qualifiers>.yaml
```
Replace `plank` with your board's name, of course.

The mandatory files are:

#. `board.yml`: a YAML file describing the high-level meta data of the
   boards such as the boards names, their SoCs, and variants.
   CPU clusters for multi-core SoCs are not described in this file as they are
   inherited from the SoC's YAML description.

#. `plank_<qualifiers>.dts`: a hardware description
   in devicetree format. This declares your SoC, connectors,
   and any other hardware components such as LEDs, buttons, sensors, or
   communication peripherals (USB, Bluetooth controller, etc).

#. `Kconfig.plank`: the base software configuration for selecting SoC and
   other board and SoC related settings. Kconfig settings outside of the board
   and SoC tree must not be selected. To select general Zephyr Kconfig settings
   the `Kconfig` file must be used.


The optional files are:

- `Kconfig`, `Kconfig.defconfig` software configuration in
  kconfig formats. This provides default settings for software features
  and peripheral drivers.
- `plank_defconfig` and `plank_<qualifiers>_defconfig`: software
  configuration in Kconfig `.conf` format.
- `board.cmake`: used for flash-and-debug-support
- `CMakeLists.txt`: if you need to add additional source files to
  your build.
- `doc/index.rst`, `doc/plank.webp`: documentation for and a picture
  of your board. You only need this if you're contributing-your-board to
  Zephyr.
- `plank_<qualifiers>.yaml`: a YAML file with miscellaneous metadata used
  by the twister_script.

Board qualifiers of the form `<soc>/<cpucluster>/<variant>` are normalized so
that `/ is replaced with ` when used for filenames, for example:
`soc1/foo` becomes `soc1_foo` when used in filenames.
