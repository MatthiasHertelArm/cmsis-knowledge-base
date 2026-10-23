---
id: "pyocd-debug-probes-selecting-the-debug-probe"
type: "concept"
domain: "debug"
title: "Debug probes: Selecting the debug probe"
summary: "All of the pyOCD subcommands that communicate with a target require the user to either implicitly or explicitly specify a debug probe."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/debug_probes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/debug_probes.md#selecting-the-debug-probe"
license: "Apache-2.0"
mode: "V"
---

All of the pyOCD subcommands that communicate with a target require the user to either implicitly or
explicitly specify a debug probe.

There are three ways the debug probe is selected:

1. Implicitly, if only one probe is connected to the host, pyOCD can use it automatically without further configuration.

2. If there is more than one probe connected and pyOCD is not told which to use, it will ask on the console. It presents
    the same list of probes reported by `pyocd list`, plus this question:

        Enter the number of the debug probe or 'q' to quit>

    and waits until a probe index is entered.

3. Explicitly, with the use of `-u UID` / `--uid=UID` / `--probe=UID` command line arguments. These arguments accept
    either a whole or partial unique ID.

If no probes are currently connected and pyOCD is executed without explicitly specifying the probe to use, it will
by default print a message asking for a probe to be connected and wait. If the `-W` / `--no-wait` argument is passed,
pyOCD will exit with an error instead.
