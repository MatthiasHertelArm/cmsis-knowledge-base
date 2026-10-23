---
id: "ceed-licensing-checking-license-status"
type: "concept"
domain: "test"
title: "Licensing: Checking license status"
summary: "Run this task at any time to report your license state."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/licensing.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing/#checking-license-status"
license: "MIT"
mode: "V"
---

Run this task at any time to report your license state.

```shell
 > ceedling bullseye:license
```

It reports your license number, its expiry date, and license manager
utilization.

```
------------------------
BULLSEYE: LICENSE STATUS
------------------------
BullseyeCoverage License Manager Administration 9.25.9 Linux-x64 License 123456 License will expire 2028-04-06
License manager disabled
```

`License manager disabled` is the expected result for an unlimited license.
Those licenses cannot use the license manager at all. It is not a problem to
fix.

This task is the first thing to try when a Bullseye tool fails for no obvious
reason. An expired or missing license surfaces only as an opaque tool failure.
Ceedling points you here when one of its own Bullseye report tools fails.
