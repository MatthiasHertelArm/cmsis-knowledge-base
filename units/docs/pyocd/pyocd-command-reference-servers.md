---
id: "pyocd-command-reference-servers"
type: "concept"
domain: "debug"
title: "Command reference: Servers"
summary: "Command reference: Servers"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/command_reference.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/command_reference.md#servers"
license: "Apache-2.0"
mode: "V"
---

##### `gdbserver`

**Usage**: gdbserver {start,stop,status} \
Control the gdbserver for the selected core. The action argument should be either 'start', 'stop', or 'status'. Use the 'gdbserver_port' and 'telnet_port' session options to control the ports the gdbserver uses.


##### `probeserver`

**Usage**: probeserver {start,stop,status} \
Control the debug probe server. The action argument should be either 'start', 'stop', or 'status. Use the 'probeserver.port' option to control the TCP port the server uses.
