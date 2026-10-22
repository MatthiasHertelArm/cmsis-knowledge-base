---
id: "ceed-cmock-mock-name-include-folder"
type: "concept"
domain: "test"
title: "`:cmock`: `:mock_name_include_folder`"
summary: "Names each mock’s include guard and Init(), Verify(), and Destroy() functions by the folder its #include names. A mock included as drivers/uart/mock_config.h (#include \"drivers/uart/mock_config.h\") gets functions such as drivers_uart_mock_config_Init(). A mock included without a folder keeps its plain name."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/cmock.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/#mock-name-include-folder"
license: "MIT"
mode: "V"
---

Names each mock’s include guard and `Init()`, `Verify()`, and `Destroy()`
functions by the folder its `#include` names. A mock included as
`drivers/uart/mock_config.h` (`#include "drivers/uart/mock_config.h"`) gets 
functions such as `drivers_uart_mock_config_Init()`. A mock included without
a folder keeps its plain name.

This is what lets one test file mock two headers sharing a filename, such as
`drivers/uart/config.h` and `drivers/spi/config.h`. Include each mock through
its own folder. Ceedling copies this setting into the test runner
configuration, so runners always call the names the mocks define.

**Default**: TRUE
