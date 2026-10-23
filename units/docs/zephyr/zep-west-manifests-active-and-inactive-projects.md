---
id: "zep-west-manifests-active-and-inactive-projects"
type: "concept"
domain: "project"
title: "West Manifests: Active and Inactive Projects"
summary: "Projects defined in the west manifest can be inactive or active. The difference is that an inactive project is generally ignored by west."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

Projects defined in the west manifest can be *inactive* or *active*. The
difference is that an inactive project is generally ignored by west. For
example, `west update` will not update inactive projects, and `west list`
will not print information about them by default. As another example, any
west-manifest-import in an inactive project will be ignored by west.

There are two ways to make a project inactive:

1. Using the `manifest.project-filter` configuration option. If a project is
   made active or inactive using this option, then the rules related to making
   a project inactive using its `groups:` are ignored. That is, if a regular
   expression in `manifest.project-filter` applies to a project, the
   project's groups have no effect on whether it is active or inactive.

   See the entry for this option in west-config-index for details.

2. Otherwise, if a project has groups, and they are all disabled, then the
   project is inactive.

   See the following section for details.
