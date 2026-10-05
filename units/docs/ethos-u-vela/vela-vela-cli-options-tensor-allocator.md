---
id: "vela-vela-cli-options-tensor-allocator"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Tensor Allocator"
summary: "Specify which allocator algorithm to use for non-constant NPU and CPU tensor allocation. Type: String Default: HillClimb Choices: [Greedy, LinearAlloc, HillClimb]"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#tensor-allocator"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

**Deprecation notice:**
The `Greedy` allocator choice will be removed in next major release.

Specify which allocator algorithm to use for non-constant NPU and CPU tensor
allocation.  
**Type: String**  
**Default: HillClimb**  
**Choices: [Greedy, LinearAlloc, HillClimb]**  

```bash
vela network.tflite --tensor-allocator=LinearAlloc
```
