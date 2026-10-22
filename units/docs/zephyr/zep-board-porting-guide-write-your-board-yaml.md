---
id: "zep-board-porting-guide-write-your-board-yaml"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Write your board YAML"
summary: "The board YAML file describes the board at a high level. This includes the SoC, board variants, and board revisions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

The board YAML file describes the board at a high level.
This includes the SoC, board variants, and board revisions.

Detailed configurations, such as hardware description and configuration are done
in devicetree and Kconfig.

The skeleton of the board YAML file is:

```yaml

board:
  name: <board-name>
  full_name: <board-full-name>
  vendor: <board-vendor>
  revision:
    format: <major.minor.patch|letter|number|custom>
    default: <default-revision-value>
    exact: <true|false>
    revisions:
    - name: <revA>
    - name: <revB>
      ...
  socs:
  - name: <soc-1>
    variants:
    - name: <variant-1>
    - name: <variant-2>
      variants:
      - name: <sub-variant-2-1>
        ...
  - name: <soc-2>
    ...
```
It is possible to have multiple boards located in the board folder.
If multiple boards are placed in the same board folder, then the file
`board.yml` must describe those in a list as:

```yaml

boards:
- name: <board-name-1>
  vendor: <board-vendor>
  full_name: <board-full-name>
  ...
- name: <board-name-2>
  vendor: <board-vendor>
  full_name: <board-full-name>
  ...
...
```
