---
id: "pyocd-adding-a-new-built-in-target-steps-to-add-a-new-board"
type: "concept"
domain: "debug"
title: "Adding a new built-in target: Steps to add a new board"
summary: "This section only applies if your board has an on-board debug probe that either:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/adding_new_targets.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/adding_new_targets.md#steps-to-add-a-new-board"
license: "Apache-2.0"
mode: "V"
---

This section only applies if your board has an on-board debug probe that either:

- Uses the [Arm DAPLink](https://github.com/ARMmbed/DAPLink) firmware. DAPLink presents the board ID
    as the first 4 characters of the USB serial number.
- Uses the STLinkV2-1 or STLinkV3 firmware and the board is Mbed-enabled. STLink presents the board ID
    as the first 4 characters of the code in the HTML file on the USB mass storage volume.

If neither applies, then pyOCD will be unable to automatically detect the board type. However, you
can still use the target by passing the `--target` argument to pyOCD.

Follow these steps:

1. Identify the 4-character board ID.

2. Insert a row into the `BOARD_ID_TO_INFO` table in `pyocd/board/board_ids.py` with the board ID,
    board name, target type, and test binary file name.

    The new row should look similar to this:

        "0205": BoardInfo(  "FRDM-KL28Z",           "kl28z",            "l1_kl28z.bin",         ),

    Be sure to insert the row in sorted order by board ID, and please align columns.

3. Place a test firmware binary file listed in the board info into the `test/data/binaries/`
    directory. The test firmware can be nothing more than a tiny LED blinky demo. It must not require
    any user input, and should provide immediate visual feedback that the code is successfully
    running, assuming there are LEDs on the board.
