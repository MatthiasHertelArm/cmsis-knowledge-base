---
id: "pyocd-configuring-logging-basic-control"
type: "concept"
domain: "debug"
title: "Configuring logging: Basic control"
summary: "For most users, the command line --verbose/-v and --quiet/-q arguments provide sufficient control over logging. These arguments can be listed multiple times. Each use increases or decreases the logging verbosity level."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuring_logging.md#basic-control"
license: "Apache-2.0"
mode: "V"
---

For most users, the command line `--verbose`/`-v` and `--quiet`/`-q` arguments provide sufficient control
over logging. These arguments can be listed multiple times. Each use increases or decreases the
logging verbosity level. For example, a single `--verbose` moves `pyocd flash` from the default
level of WARNING to INFO.
