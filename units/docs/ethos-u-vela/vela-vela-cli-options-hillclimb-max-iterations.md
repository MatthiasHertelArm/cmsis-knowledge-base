---
id: "vela-vela-cli-options-hillclimb-max-iterations"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / HillClimb Max Iterations"
summary: "Sets the maximum number of iterations the Hill Climb tensor allocator will run. This is a hard limit on the total number of iterations of the algorithm."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#hillclimb-max-iterations"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

**Deprecation notice:**
This option will be removed in next major release.

Sets the maximum number of iterations the Hill Climb tensor allocator will run.
This is a hard limit on the total number of iterations of the algorithm.
Reducing this value is unlikely to reduce the compilation time of a working
solution, and it may cause the algorithm to terminate before finding a workable
solution.  
**Type: Integer**  
**Default: 99999**

```bash
vela network.tflite --hillclimb-max-iterations 1000
```
