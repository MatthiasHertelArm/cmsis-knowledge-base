---
id: "zep-board-porting-guide-multiple-board-revisions"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Multiple board revisions"
summary: "See application_board_version for basics on this feature from the user perspective."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

See application_board_version for basics on this feature from the user
perspective.

Board revisions are described in the `revision` entry of the
`board.yml`.

```yaml

board:
  revision:
    format: <major.minor.patch|letter|number|custom>
    default: <default-revision-value>
    exact: <true|false>
    revisions:
    - name: <revA>
    - name: <revB>
```
Zephyr natively supports the following revision formats:

- `major.minor.patch`: match a three digit revision, such as `1.2.3`.
- `number`: matches integer revisions
- `letter`: matches single letter revisions from `A` to `Z` only


### Fuzzy revision matching


Fuzzy revision matching is enabled per default.

If the user selects a revision between those available, the closest revision
number that is not larger than the user's choice is used. For example, if the
board `plank` defines revisions `0.5.0`, and `1.5.0` and the user builds
for `plank@0.7.0`, the build system will target revision `0.5.0`.

The build system will print this at CMake configuration time:

```console

-- Board: plank, Revision: 0.7.0 (Active: 0.5.0)
```
This allows you to only create revision configuration files for board revision
numbers that introduce incompatible changes.

Similarly for `letter` revision format, if revisions `A`, `D`, and `F`
are defined and the user builds for `plank@E`, the build system will target
revision `D`.


### Exact revision matching


Exact revision matching is enabled when `exact: true` is specified in the
revision section in `board.yml`.

When exact is defined then building for `plank@0.7.0` in the above example
will result in the following error message:

```console

Board revision `0.7.0` not found.  Please specify a valid board revision.
```

### Board revision configuration adjustment


When the user builds for board `plank@<revision>` it is possible to make
adjustments to the board's normal configuration.

As described in the default_board_configuration and
board_kconfig_files sections the board default configuration is created
from the files `<board>.dts` / `<board>_<qualifiers>.dts` and
`<board>_defconfig` / `<board>_<qualifiers>_defconfig`.
When building for a specific board revision, the above files are used as a
starting point and the following board files will be used in addition:

- `<board>_<qualifiers>_<revision>_defconfig`: a specific revision
  defconfig which is only used for the board and SOC / variants identified by
  `<board>_<qualifiers>`.

- `<board>_<qualifiers>_<revision>.overlay`: a specific revision dts
  overlay which is only used for the board and SOC / variants identified by
  `<board>_<qualifiers>`.

This split allows boards with multiple SoCs, multi-core SoCs, or variants to
place common revision adjustments which apply to all SoCs and variants in a
single file, while still providing the ability to place SoC or variant specific
adjustments in a dedicated revision file.

Using the `plank` board from previous sections, then we could have the following
revision adjustments:

```none

boards/zephyr/plank
├── plank_soc1_foo_1_5_0.overlay   # DTS overlay for plank board when building for soc1 variant foo on revision 1.5.0
└── plank_soc1_foo_1_5_0_defconfig # Kconfig adjustment for plank board when building for soc1 variant foo on revision 1.5.0
```
