---
id: "pyocd-target-family-usage-notes-hdsc"
type: "concept"
domain: "debug"
title: "Target family usage notes: HDSC"
summary: "Target family usage notes: HDSC"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/target_family_notes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/target_family_notes.md#hdsc"
license: "Apache-2.0"
mode: "V"
---

### HC32L110
The documentation for this chip states that no external pull-up resistors are required on the SWD lines due to the internal pull-up
hardware. Testing has found this to be largely inaccurate. Most debug probes will require an external 4.7kΩ pull-up resistor 
between Ports P27/P31 and V+.
