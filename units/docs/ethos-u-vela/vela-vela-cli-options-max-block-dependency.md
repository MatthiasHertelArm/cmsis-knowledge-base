---
id: "vela-vela-cli-options-max-block-dependency"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Max Block Dependency"
summary: "Set the maximum value that can be used for the block dependency delay between NPU kernel operations. A lower value may result in longer execution time. Type: Integer Default: 3 Choices: [0, 1, 2, 3]"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#max-block-dependency"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

**Deprecation notice:**
This option will be removed in next major release.

Set the maximum value that can be used for the block dependency delay between
NPU kernel operations.  A lower value may result in longer execution time.  
**Type: Integer**  
**Default: 3**  
**Choices: [0, 1, 2, 3]**  

```bash
vela network.tflite --max-block-dependency 0
```
