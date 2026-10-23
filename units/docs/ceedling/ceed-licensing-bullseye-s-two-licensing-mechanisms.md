---
id: "ceed-licensing-bullseye-s-two-licensing-mechanisms"
type: "concept"
domain: "test"
title: "Licensing: Bullseye's two licensing mechanisms"
summary: "Bullseye licenses activate two different ways. Which one applies depends on the license you were issued. This plugin does not choose between them."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/licensing.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing/#bullseye-s-two-licensing-mechanisms"
license: "MIT"
mode: "V"
---

Bullseye licenses activate two different ways. Which one applies depends on the
license you were issued. This plugin does not choose between them.

### Node-locked and unlimited licenses

These activate once, at installation. Pass your license key to Bullseye's
installer.

```shell
 > sudo ./install --key <licenseKey> --search "$PATH"
```

Activation state is written into the installation itself. Every user on that
machine can then run Bullseye's tools. Nothing per-project or per-build is
involved, and no plugin setting applies.

`--prefix <dir>` installs somewhere other than `/opt`. That avoids needing
root.

```shell
 > ./install --prefix ~/bullseye --key <licenseKey> --search "$PATH"
```

### Floating and evaluation licenses

These share a limited pool of concurrent licenses. The pool is tracked in a
single shared file called the license manager file. Bullseye's `covlmgr` tool
administers it.

Bullseye states that the license manager cannot be used with an unlimited
license. It works with floating and evaluation licenses only.

A license administrator creates the file once, on a network location that
supports file locking.

```shell
 > ./install --key <licenseKey> --create /server/BullseyeCoverageLicenseManager
```

Each client then points at that existing file.

```shell
 > covlmgr --file /server/BullseyeCoverageLicenseManager --use
```

Other useful `covlmgr` actions follow.

| Command | Purpose |
|---|---|
| `covlmgr --status` | Report current license utilization |
| `covlmgr --add <key>` | Add a license key to the file |
| `covlmgr --create --file <path>` | Create a license manager file |
| `covlmgr --use --file <path>` | Point this client at an existing file |
| `covlmgr --clear` | Reset utilization and release all licenses |

See [Bullseye's license manager documentation][bullseye-license-manager] for
full detail.

#### Configuring the license manager file

Set `:license_manager_file` to your shared file's path. The plugin sets the
`COVLM` environment variable to this value for every Bullseye tool it invokes.

```yaml
:bullseye:
  :license_manager_file: /path/to/shared/bullseye.lmgr
```

**Default:** unset

Leave this unset for a node-locked or unlimited license. It has no effect on
those.

#### Recovering a license after a killed build

A license is consumed for the duration of each Bullseye program. It is released
when that program exits. A program that is killed holds its license for 10
minutes before automatic release.

Interrupting a build can therefore leave a license checked out. Run
`covlmgr --clear` to release everything immediately, or wait out the 10 minutes.
