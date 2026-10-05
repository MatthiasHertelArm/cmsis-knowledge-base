---
id: "zep-workspaces-not-supported-workspace-topdir-as-git-re"
type: "concept"
domain: "project"
title: "Workspaces: Not supported: workspace topdir as .git repository"
summary: "Some users have asked for support making the workspace :ref:topdir <west-workspace> a git repository, like this example:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

Some users have asked for support making the workspace :ref:`topdir
<west-workspace>` a git repository, like this example:

```none

my-workspace/                  # workspace topdir
├── .git/                      # puts the entire workspace in a git repository
├── .west/                     # marks the location of the topdir
└── [ ... other projects ...]
```
This is **not** an officially supported topology. As a design decision, west
assumes that the workspace topdir itself is not a git repository.

You may be able to make something like this "work" for yourself and your own
goals. However, future versions of west might contain changes which can "break"
your setup.
