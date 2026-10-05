---
id: "zep-shell-rtt-backend-channel-selection"
type: "concept"
domain: "debug"
title: "Shell: RTT Backend Channel Selection"
summary: "Instead of using the shell as a logger backend, RTT shell backend and RTT log backend can also be used simultaneously, but over different channels."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

Instead of using the shell as a logger backend, RTT shell backend and RTT log
backend can also be used simultaneously, but over different channels. By
separating them, the log can be captured or monitored without shell output or
the shell may be scripted without log interference. Enabling both the Shell RTT
backend and the Log RTT backend does not work by default, because both default
to channel `0`. There are two options:

1. The Shell buffer can use an alternate channel, for example using
`CONFIG_SHELL_BACKEND_RTT_BUFFER` set to `1`.
This allows monitoring the log using `JLinkRTTViewer
<https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/#j-link-rtt-viewer>`_
while a script interfaces over channel 1.

2. The Log buffer can use an alternate channel, for example using
`CONFIG_LOG_BACKEND_RTT_BUFFER` set to `1`.
This allows interactive use of the shell through JLinkRTTViewer, while the log
is written to file.

See shell backends <backends_> for details on how to enable RTT as a Shell backend.
