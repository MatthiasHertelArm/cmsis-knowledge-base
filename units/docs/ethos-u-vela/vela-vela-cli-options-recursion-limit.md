---
id: "vela-vela-cli-options-recursion-limit"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Recursion Limit"
summary: "Sets the Python internal limit to depth of recursion. It may be necessary to increase this from the default for very large networks due to the recursive nature of the graph traversal algorithm."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#recursion-limit"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

**Deprecation notice:**
This option will be removed in next major release.

Sets the Python internal limit to depth of recursion. It may be
necessary to increase this from the default for very large networks
due to the recursive nature of the graph traversal algorithm.
If Vela fails with a `RecursionError`, try increasing the limit using
this option to see if it resolves the issue.  
Please note that this option may not work as intended on Microsoft Windows
systems, as there is a hard limit on thread stack size.  
**Type: Integer**  
**Default: 1000**

```bash
vela network.tflite --recursion-limit 2000
```
