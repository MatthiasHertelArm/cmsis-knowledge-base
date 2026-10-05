---
id: "pyocd-session-options-list-cmsis-dap-probe-options"
type: "concept"
domain: "debug"
title: "Session options list: CMSIS-DAP probe options"
summary: "These session options are available when the CMSIS-DAP debug probe plugin is active."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#cmsis-dap-probe-options"
license: "Apache-2.0"
mode: "V"
---

These session options are available when the CMSIS-DAP debug probe plugin is active.

<table>

<tr><th>Option Name</th><th>Type</th><th>Default</th><th>Description</th></tr>

<tr><td>cmsis_dap.deferred_transfers</td>
<td>bool</td>
<td>True</td>
<td>
Whether to use deferred transfers in the CMSIS-DAP probe backend. By disabling deferred transfers,
all writes take effect immediately. However, performance is negatively affected.
</td></tr>

<tr><td>cmsis_dap.limit_packets</td>
<td>bool</td>
<td>False</td>
<td>
Restrict CMSIS-DAP backend to using a single in-flight command at a time. This is useful on some systems
where USB is problematic, in particular virtual machines.
</td></tr>

</table>
