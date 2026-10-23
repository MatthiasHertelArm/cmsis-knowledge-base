---
id: "zep-board-porting-guide-custom-revision-cmake-files"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Custom revision.cmake files"
summary: "Some boards may not use board revisions supported natively by Zephyr. For example string revisions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Some boards may not use board revisions supported natively by Zephyr.
For example string revisions.

One reason why Zephyr doesn't support string revisions is that strings can take
many forms and it's not always clear if the given strings are just strings, such
as `blue`, `green`, `red`, etc. or if they provide an order which can be
matched against higher or lower revisions, such as `alpha`, `beta``,
`gamma`.

Due to the sheer number of possibilities with strings, including the possibility
of doing regex matches internally, then string revisions must be done using
`custom` revision type.

To indicate to the build system that `custom` revisions are used, the format
field in the `revision` section of the `board.yml` must be written as:

```yaml

board:
  revision:
    format: custom
```
When using custom revisions then a `revision.cmake` must be created in the
board directory.

The `revision.cmake` will be included by the build system when building
for the board and it is the responsibility of the file to validate the revision
specified by the user.

The `BOARD_REVISION` variable holds the revision value specified by the
user.

To signal to the build system that it should use a different revision than the
one specified by the user, `revision.cmake` can set the CMake variable
`ACTIVE_BOARD_REVISION` to the revision to use instead. The corresponding
Kconfig files and devicetree overlays must be named
`<board>_<ACTIVE_BOARD_REVISION>_defconfig` and
`<board>_<ACTIVE_BOARD_REVISION>.overlay`.
