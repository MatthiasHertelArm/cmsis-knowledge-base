---
id: "pyocd-session-options-list-stlink-options"
type: "concept"
domain: "debug"
title: "Session options list: STLink options"
summary: "These session options are available when the STLink debug probe plugin is active."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#stlink-options"
license: "Apache-2.0"
mode: "V"
---

These session options are available when the STLink debug probe plugin is active.



| Option Name | Type | Default | Description |
|---|---|---|---|
| stlink.v3_prescaler | int | 1 | Sets the HCLK prescaler of an STLinkV3, changing performance versus power tradeoff. The value must be one of 1=high performance (default), 2=normal, or 4=low power. |
