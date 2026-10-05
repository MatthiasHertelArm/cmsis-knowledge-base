---
id: "pyocd-user-scripts-introduction"
type: "concept"
domain: "debug"
title: "User scripts: Introduction"
summary: "pyOCD has support for customization through what are called user scripts. These are Python scripts that are loaded by pyOCD before it connects to the target."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/user_scripts.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/user_scripts.md#introduction"
license: "Apache-2.0"
mode: "V"
---

pyOCD has support for customization through what are called user scripts. These are Python scripts
that are loaded by pyOCD before it connects to the target. A user script can define functions that
are called as hooks at certain points in the connection lifetime, and can extend, modify, or
completely override the default behaviour.

If a file named `pyocd_user.py` or `.pyocd_user.py` is placed in the project directory, pyOCD will
automatically detect it and load it as a user script. If you prefer another name, you can set the
`user_script` session option, for example in a [config file]({% link _docs/configuration.md %}), or
by passing the `--script=<path>` command line argument. If a relative path is set either with the
option or command line, it will be searched for in the project directory.
