---
id: "pyocd-target-support"
type: "concept"
domain: "debug"
title: "Target support"
summary: "Through both built-in support and CMSIS-Packs, pyOCD supports nearly every Cortex-M MCU that is available on the market."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/target_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/target_support.md"
license: "Apache-2.0"
mode: "V"
---

Through both built-in support and CMSIS-Packs, pyOCD supports nearly every Cortex-M MCU that is
available on the market.

In addition, because pyOCD dynamically inspects the target's debug infrastructure, basic
debug functionality is enabled for any target that correctly implement the CoreSight architecture.
