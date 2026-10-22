---
id: "zep-built-in-commands-other-built-in-commands"
type: "concept"
domain: "project"
title: "Built-in commands: Other built-in commands"
summary: "Finally, here is a summary of other built-in commands."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/built-in.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/built-in.rst"
license: "Apache-2.0"
mode: "V"
---

Finally, here is a summary of other built-in commands.

- `west config`: get or set configuration options
- `west topdir`: print the top level directory of the west workspace
- `west help`: get help about a command, or print information about all
  commands in the workspace, including west-extensions

.. [#fetchall]

   West may fetch all refs from the Git server when given a SHA as a revision.
   This is because some Git servers have historically not allowed fetching
   SHAs directly.
