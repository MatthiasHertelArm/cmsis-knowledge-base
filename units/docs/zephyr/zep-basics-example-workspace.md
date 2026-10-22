---
id: "zep-basics-example-workspace"
type: "concept"
domain: "project"
title: "Basics: Example workspace"
summary: "If you've followed the getting_started, your local west workspace, which in this case is the folder named zephyrproject as well as all its subfolders, looks like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/basics.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/basics.rst"
license: "Apache-2.0"
mode: "V"
---

If you've followed the getting_started, your local
`west workspace`, which in this case is the folder named
`zephyrproject` as well as all its subfolders, looks like this:

```none

zephyrproject/                 # west topdir
├── .west/                     # marks the location of the topdir
│   └── config                 # per-workspace local configuration file
│
│   # The manifest repository, never modified by west after creation:
├── zephyr/                    # .git/ repo
│   ├── west.yml               # manifest file
│   └── [... other files ...]
│
│   # Projects managed by west:
├── modules/
│   └── lib/
│       └── zcbor/             # .git/ project
├── tools/
│   └── net-tools/             # .git/ project
└── [ ... other projects ...]
```
