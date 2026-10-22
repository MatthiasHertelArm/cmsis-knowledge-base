---
id: "vela-vela-cli-options-optimise"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Optimise"
summary: "Set the optimisation strategy. The Size strategy prioritises lower memory usage. The Performance strategy prioritises inference speed and uses arena_cache_size as a memory target for performance optimisations, if specified either via the CLI option or a Vela configuration file."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#optimise"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Set the optimisation strategy. The Size strategy prioritises lower memory usage.
The Performance strategy prioritises inference speed and uses `arena_cache_size`
as a memory target for performance optimisations, if specified either via the CLI
option or a Vela configuration file.
**Type: String**  
**Default: Performance**  
**Choices: [Size, Performance]**  

```bash
vela network.tflite --optimise Size
```
