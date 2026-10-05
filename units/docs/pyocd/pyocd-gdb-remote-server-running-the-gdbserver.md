---
id: "pyocd-gdb-remote-server-running-the-gdbserver"
type: "concept"
domain: "debug"
title: "gdb remote server: Running the gdbserver"
summary: "The usual way to start the gdbserver is by running pyocd gdbserver (or pyocd gdb) on the command line. The gdbserver will remain available as long as the pyocd process is running."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/gdbserver.md#running-the-gdbserver"
license: "Apache-2.0"
mode: "V"
---

The usual way to start the gdbserver is by running `pyocd gdbserver` (or `pyocd gdb`) on the command line. The gdbserver will remain available as long as the `pyocd` process is running.

If using an IDE like Microsoft Visual Studio Code or Eclipse Embedded with plugins that support pyOCD, the gdbserver will automatically be started when you launch a debug session. Alternatively, the plugin can be configured to connect to an already-running gdbserver.

From the commander, a gdbserver can be run with the [`gdbserver` command]({% link _docs/command_reference.md %}#gdbserver-1).

The default gdbserver TCP/IP port number is 3333. This can be changed using the `-p` / `--port` or the `gdbserver_port` session option.

### Multicore targets

pyOCD always runs separate gdbservers for each core on multicore devices. This requires separate gdb instances and debug sessions for the cores being debugged, but is the most reliable method since gdb doesn't support heterogenous multicore.

By default, a gdbserver is started for all cores on the target. This can be changed using the `--core` argument, which takes a comma-separated list of core numbers.

The TCP/IP port numbers for each core's gdbserver are determined by adding the core number to the base port number (see above). For a dual core device, core 0 uses the default base port of 3333, and core 1 uses port 3334.

See the [multicore debug documentation]({% link _docs/multicore_debug.md %}) for more information about multicore targets.
