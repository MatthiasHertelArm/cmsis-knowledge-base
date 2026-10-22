---
id: "pyocd-installing-permissions-issues"
type: "concept"
domain: "debug"
title: "Installing: Permissions issues"
summary: "Note that, depending on your operating system, you may run into permissions issues running these commands. You have a few options here:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/installing.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/installing.md#permissions-issues"
license: "Apache-2.0"
mode: "V"
---

Note that, depending on your operating system, you may run into permissions issues running these commands.
You have a few options here:

1. Install with [pipx](https://pypa.github.io/pipx/).
2. Run the command in a [virtualenv](https://virtualenv.pypa.io/en/latest/)
   local to a specific project working set.
3. Under Linux, run with `sudo -H` to install pyOCD and dependencies globally. On macOS, installing with sudo
    should never be required, although sometimes permissions/corrupted can become modified such that installing without
    using sudo fails.
4. Specify the `--user` option to install local to your user account.
