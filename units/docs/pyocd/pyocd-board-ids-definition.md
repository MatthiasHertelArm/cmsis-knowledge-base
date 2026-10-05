---
id: "pyocd-board-ids-definition"
type: "concept"
domain: "debug"
title: "Board IDs: Definition"
summary: "A board ID is a 4-character code that uniquely identifies a board. It also identifies an Mbed platform: the same ID is used for both (which is actually a problem for some use cases)."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/developer/board_ids.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/developer/board_ids.md#definition"
license: "Apache-2.0"
mode: "V"
---

A board ID is a 4-character code that uniquely identifies a board. It also identifies an Mbed platform: the same ID is used for both (which is actually a problem for some use cases).

Board ID definition:
- 4-character code.
  - Board IDs currently are all hex numeric, but it's actually a string.
  - There may be problems raised in some components if you tried to use a non-hex char.
- First 2 characters identify the vendor.
  - There are multiple cases of boards from different vendors being incorrectly allocated in another vendor's namespace, so this cannot solely be relied upon. It's only really useful for grouping of IDs.
- Reserved values::
  - "C0xx" is reserved for "community" boards, i.e. open source hardware and non-commercial projects.
  - "D0xx" is reserved for boards that are not also Mbed platforms, mostly DAPLink firmware.
  - "0000" is reserved to mean "no on-board target". That is, the debug probe is standalone must be connected to the target with a cable.

Currently these debug probe firmware support board IDs:
- [DAPLink](https://daplink.io/), via the first 4 chars of the USB serial number
- STLinkV2-1 and V3, via an `.htm` file on the associated USB mass storage volume and an STLink protocol command.
