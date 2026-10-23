---
id: "zep-workspaces-the-refs-west-git-refs"
type: "concept"
domain: "project"
title: "Workspaces: The `refs/west/*` Git refs"
summary: "West also reserves all Git refs that begin with refs/west/ (such as refs/west/foo) for itself in local project repositories. Unlike manifest-rev, these refs are not regular branches."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

West also reserves all Git refs that begin with `refs/west/` (such as
`refs/west/foo`) for itself in local project repositories. Unlike
`manifest-rev`, these refs are not regular branches. West's behavior here is
an implementation detail; users should not rely on these refs' existence or
behavior.
