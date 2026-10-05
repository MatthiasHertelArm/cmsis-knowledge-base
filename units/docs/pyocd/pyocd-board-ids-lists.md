---
id: "pyocd-board-ids-lists"
type: "concept"
domain: "debug"
title: "Board IDs: Lists"
summary: "The BOARDIDTOINFO dict in pyOCD's boardids.py source file contains a list of board IDs known to pyOCD, with some extra data such as target type and test firmware file name. This is not a comprehensive list of board IDs, however."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/developer/board_ids.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/developer/board_ids.md#lists"
license: "Apache-2.0"
mode: "V"
---

The `BOARD_ID_TO_INFO` dict in pyOCD's [`board_ids.py`](https://github.com/pyocd/pyOCD/blob/main/pyocd/board/board_ids.py) source file contains a list of board IDs known to pyOCD, with some extra data such as target type and test firmware file name. This is not a comprehensive list of board IDs, however.

You can see the full list of public Mbed platforms at [https://os.mbed.com/api/v3/platforms/](https://os.mbed.com/api/v3/platforms/). The `productcode` key is the board ID. This list only reports boards that are Mbed platforms. Any non-Mbed-enabled boards with an allocated board ID are marked as hidden (because this database is also used to generate the [Mbed platforms](https://os.mbed.com/platforms/) web site), and thus will not be visible through this API. Be aware that the page take a _long_ time to fully load. A tool like `curl` may be used to download the page as JSON instead.
