---
id: "zep-west-manifests-enabled-and-disabled-project-groups"
type: "concept"
domain: "project"
title: "West Manifests: Project Groups / Enabled and Disabled Project Groups"
summary: "All project groups are enabled by default. You can enable or disable groups in both your manifest file and west-config."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Groups_

All project groups are enabled by default. You can enable or disable groups in
both your manifest file and west-config.

Within a manifest file, `manifest: group-filter:` is a YAML list of groups to
enable and disable.

To enable a group, prefix its name with a plus sign (+). For example,
`groupA` is enabled in this manifest fragment:

```yaml

manifest:
  group-filter: [+groupA]
```
Although this is redundant for groups that are already enabled by default, it
can be used to override settings in an imported manifest file. See
west-group-filter-imports for more information.

To disable a group, prefix its name with a dash (-). For example, `groupA`
and `groupB` are disabled in this manifest fragment:

```yaml

manifest:
  group-filter: [-groupA,-groupB]
```

**Note:** Since `group-filter` is a YAML list, you could have written this fragment as follows: .. code-block:: yaml manifest: group-filter: - -groupA - -groupB However, this syntax is harder to read and therefore discouraged.

In addition to the manifest file, you can control which groups are enabled and
disabled using the `manifest.group-filter` configuration option. This option
is a comma-separated list of groups to enable and/or disable.

To enable a group, add its name to the list prefixed with `+`. To disable a
group, add its name prefixed with `-`. For example, setting
`manifest.group-filter` to `+groupA,-groupB` enables `groupA`, and
disables `groupB`.

The value of the configuration option overrides any data in the manifest file.
You can think of this as if the `manifest.group-filter` configuration option
is appended to the `manifest: group-filter:` list from YAML, with "last entry
wins" semantics.


#### Practical Example: Reducing Workspace Downloads


By default, `west update` fetches all active projects defined
in the manifest. Large workspaces may include optional modules,
vendor HALs, experimental components, or platform-specific
dependencies and vulnerabilities that are not required for every workflow.

Project groups can be used to control which grouped projects
are considered active during `west` operations.

For example, consider the following manifest fragment:

```yaml

manifest:
  projects:
    - name: hal_nordic
      groups:
        - nordic
    - name: hal_stm32
      groups:
        - stm32
    - name: experimental_lib
      groups:
        - optional
```
A workspace targeting Nordic devices can disable the
`stm32` and `optional` groups before running
`west update`:

```shell

west config manifest.group-filter -- "-stm32,-optional"
```
After configuring the filter, running:

```shell

west update
```
This skips projects that belong only to disabled groups.


**Note:** Project groups only affect projects explicitly assigned to matching groups in the manifest. Projects without matching group definitions remain active regardless of the configured `manifest.group-filter` value.


**Note:** Changing `manifest.group-filter` does not automatically remove repositories already cloned into the workspace. It affects whether projects are considered active during subsequent `west` operations.

This workflow can help reduce unnecessary downloads and
simplify workspace management in large multi-project
environments.
