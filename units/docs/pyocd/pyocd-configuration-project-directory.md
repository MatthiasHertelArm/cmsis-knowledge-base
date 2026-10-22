---
id: "pyocd-configuration-project-directory"
type: "concept"
domain: "debug"
title: "Configuration: Project directory"
summary: "To help pyOCD automatically find configuration files and other resources, it has the concept of the project directory."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/configuration.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/configuration.md#project-directory"
license: "Apache-2.0"
mode: "V"
---

To help pyOCD automatically find configuration files and other resources, it has the concept of
the project directory.

When pyOCD looks for files such as the config file or a user script, it first expands '~'
references to the home directory. Then it checks whether the filename is absolute, and if so, it
uses the filename as-is. Otherwise, it looks for the file in the project directory.

By default, the project directory is simply the working directory where you ran the `pyocd` tool.
You can change the project directory to another location with the `-j`, `--project`, or `--dir` command line
arguments. This can be helpful if you are running pyOCD from another tool or application. The project
directory can also be set using the `PYOCD_PROJECT_DIR` environment variable. Command line arguments
have precedence over the environment variable.
