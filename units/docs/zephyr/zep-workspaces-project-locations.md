---
id: "zep-workspaces-project-locations"
type: "concept"
domain: "project"
title: "Workspaces: Project locations"
summary: "Projects can be located anywhere inside the workspace, but they may not \"escape\" it."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

Projects can be located anywhere inside the workspace, but they may not
"escape" it.

In other words, project repositories need not be located in subdirectories of
the manifest repository or as immediate subdirectories of the topdir. However,
projects must have paths inside the workspace.

You may replace a project's repository directory within the workspace with a
symbolic link to elsewhere on your computer, but west will not do this for you.
