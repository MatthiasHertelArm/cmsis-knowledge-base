---
id: "zep-additional-zephyr-extension-comman-working-with-patches-west-patch"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Working with patches: `west patch`"
summary: "The patch command allows users to apply patches to Zephyr or Zephyr modules in a controlled manner that makes automation and tracking easier for external applications that use the T2 star topology."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `patch` command allows users to apply patches to Zephyr or Zephyr modules
in a controlled manner that makes automation and tracking easier for external applications that
use the T2 star topology. The patches.yml file stores
metadata about patch files and fills-in the gaps between official Zephyr releases, so that users
can easily see the status of any upstreaming efforts, and determine which patches to drop before
upgrading to the next Zephyr release.

There are several sub-commands available to manage patches for Zephyr or other modules in the
workspace:

* `apply`: apply patches listed in `patches.yml`
* `reverse`: reverse patches listed in `patches.yml` that have been previously applied
* `clean`: remove all patches that have been applied, and reset to the manifest checkout state
* `list`: list all patches in `patches.yml`
* `gh-fetch`: fetch patches from a GitHub pull request

```none

west-workspace/
└── application/
   ...
   ├── west.yml
   └── zephyr
       ├── module.yml
       ├── patches
       │   ├── bootloader
       │   │   └── mcuboot
       │   │       └── my-tweak-for-mcuboot.patch
       │   └── zephyr
       │       └── my-zephyr-change.patch
       └── patches.yml
```
In this example, the west manifest file, `west.yml`, would pin to a
specific Zephyr revision (e.g. `v4.1.0`) and apply patches against that revision of Zephyr and
the specific revisions of other modules used in the application. However, this application needs
two changes in order to meet requirements; one for Zephyr and another for MCUBoot.

```yaml

patches:
  - path: zephyr/my-zephyr-change.patch
    sha256sum: c676cd376a4d19dc95ac4e44e179c253853d422b758688a583bb55c3c9137035
    module: zephyr
    author: Obi-Wan Kenobi
    email: obiwan@jedi.org
    date: 2025-05-04
    upstreamable: false
    comments: |
      An application-specific change we need for Zephyr.
  - path: bootloader/mcuboot/my-tweak-for-mcuboot.patch
    sha256sum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    module: mcuboot
    author: Darth Sidious
    email: sidious@sith.org
    date: 2025-05-04
    merge-pr: https://github.com/zephyrproject-rtos/zephyr/pull/<pr-number>
    issue: https://github.com/zephyrproject-rtos/zephyr/issues/<issue-number>
    merge-status: true
    merge-commit: 1234567890abcdef1234567890abcdef12345678
    merge-date: 2025-05-06
    apply-command: git apply
    comments: |
      A change to mcuboot that has been merged already. We can remove this
      patch when we are ready to upgrade to the next Zephyr release.
```
Patches can easily be applied in an automated manner. For example:

```bash

west init -m <manifest repo> <workspace>
cd <workspace>
west update
west patch apply
```
When it is time to update to a newer version of Zephyr, the `west.yml` file can be updated to
point at the next Zephyr release, e.g. `v4.2.0`. Patches that are no longer needed, like
`my-tweak-for-mcuboot.patch` in the example above, can be removed from `patches.yml` and from
the external application repository, and then the following commands can be run.

```bash

west patch clean
west update
west patch apply --roll-back # roll-back all patches if one does not apply cleanly
```
Optionally, patches can be reversed rather than cleaning all modules. This leaves non-conflicting,
unrelated edits to modules in place, but removes only the changes made by patches. This is useful
when developing patches and testing them in an application, but not wanting to clean all patches
and lose any manual edits made to the module.

```bash

west patch reverse
```
If a patch needs to be reworked, remember to update the `patches.yml` file with the new SHA256
checksum.

```bash

sha256sum zephyr/patches/zephyr/my-zephyr-change.patch
7d57ca78d5214f422172cc47fed9d0faa6d97a0796c02485bff0bf29455765e9
```
It is also possible to use `west patch gh-fetch` to fetch patches from a GitHub pull request and
automatically create or update the `patches.yml` file. This can be useful when the author already
has a number of changes captured in existing upstream pull requests.

```bash

west patch gh-fetch --owner zephyrproject-rtos --repo zephyr --pull-request <pr-number> \
  --module zephyr --split-commits
```
The above command will create the directory and file structure below, which includes patches for
each individual commit associated with the given pull request.

```none

zephyr
├── patches
│   ├── first-commit-from-pr.patch
│   ├── second-commit-from-pr.patch
│   └── third-commit-from-pr.patch
└── patches.yml
```
