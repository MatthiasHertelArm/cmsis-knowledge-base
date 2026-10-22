---
id: "ceed-fake-function-framework-for-ceedli-cmock-configuration"
type: "concept"
domain: "test"
title: "Fake Function Framework for Ceedling: CMock configuration"
summary: "We still use some CMock configuration options for setting things like the mock prefix and for including additional header files in the mock files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/fff.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/fff/#cmock-configuration"
license: "MIT"
mode: "V"
---

We still use some CMock configuration options for setting things like the mock prefix and for including additional header files in the mock files.

```yaml
:cmock:
    :mock_prefix: mock_
        :includes:
            - ...
        :includes_h_pre_orig_header:
            - ...
        :includes_h_post_orig_header:
            - ...
        :includes_c_pre_header:
            - ...
        :includes_c_post_header:
```

### Fakes of same-named headers

With `:cmock` ↳ `:mock_name_include_folder` enabled, Ceedling’s default, a fake
included through a folder is named by that folder, as a CMock mock is. A fake
included as `drivers/uart/mock_config.h` (`#include "drivers/uart/mock_config.h"`) 
is written to that folder below the test’s mock directory, and its `Init()`, 
`Verify()`, and `Destroy()` functions become `drivers_uart_mock_config_Init()` 
and so on. One test file can then fake two headers sharing a filename by 
including each through its own folder.

The fakes of the functions themselves keep the functions’ own names, so the 
two headers must not declare the same function.
