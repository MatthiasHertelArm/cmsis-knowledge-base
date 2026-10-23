---
id: "pyocd-session-options-list-j-link-probe-options"
type: "concept"
domain: "debug"
title: "Session options list: J-Link probe options"
summary: "These session options are available when the SEGGER J-Link debug probe plugin is active."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/options.md#j-link-probe-options"
license: "Apache-2.0"
mode: "V"
---

These session options are available when the SEGGER J-Link debug probe plugin is active.



| Option Name | Type | Default | Description |
|---|---|---|---|
| jlink.device | str | No default | If this option is set to a supported J-Link device name, then the J-Link will be asked connect using this name. Otherwise, when unset, the J-Link is configured for only the low-level CoreSight operations required by pyOCD. Ordinarily, it does not need to be set. |
| jlink.non_interactive | bool | True | Controls whether the J-Link DLL is allowed to present UI dialog boxes and its control panel. Note that dialog boxes will actually still be visible, but the default option will be chosen automatically after 5 seconds. Note: This has the effect of also silencing dialog boxes that appear when updating firmware / to confirm updating firmware. |
| jlink.power | bool | True | Enable target power when connecting via a JLink probe, and disable power when disconnecting. Default is True. |
