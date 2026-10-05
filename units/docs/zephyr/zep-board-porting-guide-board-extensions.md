---
id: "zep-board-porting-guide-board-extensions"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Board extensions"
summary: "The board hardware model in Zephyr allows you to extend an existing board with new board variants. Such board extensions can be done in your custom repository and thus outside of the Zephyr repository."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

The board hardware model in Zephyr allows you to extend an existing board with
new board variants. Such board extensions can be done in your custom repository
and thus outside of the Zephyr repository.

Extending an existing board with an extra variant allows you to adjust an
existing board and thereby during build to select building for the existing,
unmodified board, or the new variant.

To extend an existing board, first create a `board.yml` in your extended
board. Make sure to use the directory structure described in
create-your-board-directory.

The skeleton of the board YAML file for extending a board is:

```yaml

board:
  extend: <existing-board-name>
  variants:
    - name: <new-variant>
      qualifier: <existing-qualifier>
```
When extending a board, your board directory should look like:

```none

boards/<VENDOR>/plank
├── board.yml
├── plank_<new-qualifiers>_defconfig
└── plank_<new-qualifiers>.dts
```
Replace `plank` with the real name of the board you extend.

In some cases you might want to also adjust additional settings, like the
`Kconfig.defconfig` or `Kconfig.{board}`.
Therefore it is also possible to provide the following in addition when
extending a board.

```none

boards/<VENDOR>/plank
├── board.cmake
├── Kconfig
├── Kconfig.plank
├── Kconfig.defconfig
└── plank_<new-qualifiers>.yaml
```
