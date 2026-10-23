---
id: "vela-vela-cli-options-enable-debug-database"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Enable Debug Database"
summary: "The neural network debug database allows tracking of optimisations from the input network graph to the output command stream."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#enable-debug-database"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

The neural network debug database allows tracking of optimisations from the
input network graph to the output command stream.  Set this option to enable the
calculation and writing of an XML file that contains the network debug database
tables to the output directory.  

```bash
vela network.tflite --enable-debug-db
```
