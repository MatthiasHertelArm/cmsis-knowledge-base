---
id: "zep-workspaces-topologies-supported"
type: "concept"
domain: "project"
title: "Workspaces: Topologies supported"
summary: "The following are example source code topologies supported by west."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

The following are example source code topologies supported by west.

- T1: star topology, zephyr is the manifest repository
- T2: star topology, a Zephyr application is the manifest repository
- T3: forest topology, freestanding manifest repository


### T1: Star topology, zephyr is the manifest repository


- The zephyr repository acts as the central repository and specifies
  its modules in its `west.yml`
- Analogy with existing mechanisms: Git submodules with zephyr as the
  super-project

This is the default. See west-workspace for how mainline Zephyr is an
example of this topology.


### T2: Star topology, application is the manifest repository


- Useful for those focused on a single application
- A repository containing a Zephyr application acts as the central repository
  and names other projects required to build it in its `west.yml`. This
  includes the zephyr repository and any modules.
- Analogy with existing mechanisms: Git submodules with the application as
  the super-project, zephyr and other projects as submodules

A workspace using this topology looks like this:

```none

west-workspace/
│
├── application/         # .git/     │
│   ├── CMakeLists.txt               │
│   ├── prj.conf                     │  never modified by west
│   ├── src/                         │
│   │   └── main.c                   │
│   └── west.yml         # main manifest with optional import(s) and override(s)
│                                    │
├── modules/
│   └── lib/
│       └── zcbor/       # .git/ project from either the main manifest or some import.
│
└── zephyr/              # .git/ project
    └── west.yml         # This can be partially imported with lower precedence or ignored.
                         # Only the 'manifest-rev' version can be imported.
```
Here is an example `application/west.yml` which uses
west-manifest-import, available since west 0.7, to import Zephyr v2.5.0
and its modules into the application manifest file:

```yaml

# Example T2 west.yml, using manifest imports.
manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  projects:
    - name: zephyr
      remote: zephyrproject-rtos
      revision: v2.5.0
      import: true
  self:
    path: application
```
You can still selectively "override" individual Zephyr modules if you use
`import:` in this way; see west-manifest-ex1.3 for an example.

Another way to do the same thing is to copy/paste `zephyr/west.yml`
to `application/west.yml`, adding an entry for the zephyr
project itself, like this:

```yaml

# Equivalent to the above, but with manually maintained Zephyr modules.
manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  defaults:
    remote: zephyrproject-rtos
  projects:
    - name: zephyr
      revision: v2.5.0
      west-commands: scripts/west-commands.yml
    - name: net-tools
      revision: some-sha-goes-here
      path: tools/net-tools
    # ... other Zephyr modules go here ...
  self:
    path: application
```
(The `west-commands` is there for west-build-flash-debug and other
Zephyr-specific west-extensions. It's not necessary when using
`import`.)

The main advantage to using `import` is not having to track the revisions of
imported projects separately. In the above example, using `import` means
Zephyr's module versions are automatically determined from the
`zephyr/west.yml` revision, instead of having to be copy/pasted (and
maintained) on their own.


### T3: Forest topology


- Useful for those supporting multiple independent applications or downstream
  distributions with no "central" repository
- A dedicated manifest repository which contains no Zephyr source code,
  and specifies a list of projects all at the same "level"
- Analogy with existing mechanisms: Google repo-based source distribution

A workspace using this topology looks like this:

```none

west-workspace/
├── app1/               # .git/ project
│   ├── CMakeLists.txt
│   ├── prj.conf
│   └── src/
│       └── main.c
├── app2/               # .git/ project
│   ├── CMakeLists.txt
│   ├── prj.conf
│   └── src/
│       └── main.c
├── manifest-repo/      # .git/ never modified by west
│   └── west.yml        # main manifest with optional import(s) and override(s)
├── modules/
│   └── lib/
│       └── zcbor/      # .git/ project from either the main manifest or
│                       #       from some import
│
└── zephyr/             # .git/ project
    └── west.yml        # This can be partially imported with lower precedence or ignored.
                        # Only the 'manifest-rev' version can be imported.
```
Here is an example T3 `manifest-repo/west.yml` which uses
west-manifest-import, available since west 0.7, to import Zephyr
v2.5.0 and its modules, then add the `app1` and `app2` projects:

```yaml

manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
    - name: your-git-server
      url-base: https://git.example.com/your-company
  defaults:
    remote: your-git-server
  projects:
    - name: zephyr
      remote: zephyrproject-rtos
      revision: v2.5.0
      import: true
    - name: app1
      revision: SOME_SHA_OR_BRANCH_OR_TAG
    - name: app2
      revision: ANOTHER_SHA_OR_BRANCH_OR_TAG
  self:
    path: manifest-repo
```
You can also do this "by hand" by copy/pasting `zephyr/west.yml`
as shown above for the T2 topology, with the same caveats.
