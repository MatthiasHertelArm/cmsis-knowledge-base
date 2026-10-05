---
id: "pyocd-configuring-logging-logger-level-control"
type: "concept"
domain: "debug"
title: "Configuring logging: Logger-level control"
summary: "The --log-level / -L command line argument makes it easy to control logging at the level of individual loggers or groups of loggers."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuring_logging.md#logger-level-control"
license: "Apache-2.0"
mode: "V"
---

The `--log-level` / `-L` command line argument makes it easy to control logging at the level of individual loggers
or groups of loggers. The argument accepts a comma-separated list of logger names followed by an "=" sign and a
log level name (case-insensitive).

The logger names are actually glob-style patterns, as supported by many command line shells. This allows use of these
wildcards:

Pattern     | Meaning
------------|-----------------------------------
`*`         | matches everything
`?`         | matches any single character
`[seq]`     | matches any character in seq
`[!seq]`    | matches any character not in seq
`[*]`       | match literal "*"
`[?]`       | match literal "?"

The `--log-level` argument can be used more than once on a command line. The arguments are processed in the order they
appear, so later arguments can refine log level settings made by earlier arguments.

Setting the log level of parent loggers affects the level of all child loggers.

Examples:

- `-L 'pyocd.probe.*=debug'`: set all pyOCD debug probe modules to debug log level
- `-L pyocd.core.session,pyocd.core.options=info`: set two modules to info log level
- `-L '*.trace=debug -L *.jlink=warning'`: enable all trace loggers, but set JLink and its trace logger to warnings
    only

Note that you may need to place the value used with `--log-level` in quotes to prevent the shell from attempting to
expand wildcards as file names.
