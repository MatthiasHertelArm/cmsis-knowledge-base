---
id: "pyocd-session-options-list-cmsis-dap-probe-options"
type: "concept"
domain: "debug"
title: "Session options list: CMSIS-DAP probe options"
summary: "These session options are available when the CMSIS-DAP debug probe plugin is active."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/options.md#cmsis-dap-probe-options"
license: "Apache-2.0"
mode: "V"
---

These session options are available when the CMSIS-DAP debug probe plugin is active.



| Option Name | Type | Default | Description |
|---|---|---|---|
| cmsis_dap.deferred_transfers | bool | True | Whether to use deferred transfers in the CMSIS-DAP probe backend. By disabling deferred transfers, all writes take effect immediately. However, performance is negatively affected. |
| cmsis_dap.limit_packets | bool | False | Restrict CMSIS-DAP backend to using a single in-flight command at a time. This is useful on some systems where USB is problematic, in particular virtual machines. |
