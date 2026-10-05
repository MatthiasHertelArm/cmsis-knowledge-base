---
id: "zep-west-manifests-project-groups"
type: "concept"
domain: "project"
title: "West Manifests: Project Groups"
summary: "You can use the groups and group-filter keys briefly described above to place projects into groups, and to enable or disable groups."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

You can use the `groups` and `group-filter` keys briefly described
above to place projects into groups, and to
enable or disable groups.

For example, this lets you run a `west forall` command only on the projects
in the group by using `west forall --group`. This can also let you make
projects inactive; see the previous section for more information on inactive
projects.

The next section introduces project groups. The following section describes
west-enabled-disabled-groups. There are some basic examples in
west-project-group-examples. Finally, west-group-filter-imports
provides a simplified overview of how `group-filter` interacts with the
west-manifest-import feature.
