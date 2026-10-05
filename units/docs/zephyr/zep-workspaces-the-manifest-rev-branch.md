---
id: "zep-workspaces-the-manifest-rev-branch"
type: "concept"
domain: "project"
title: "Workspaces: The `manifest-rev` branch"
summary: "West creates and controls a Git branch named manifest-rev in each project. This branch points to the revision that the manifest file specified for the project at the time west-update was last run."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

West creates and controls a Git branch named `manifest-rev` in each
project. This branch points to the revision that the manifest file
specified for the project at the time west-update was last run.
Other workspace management commands may use `manifest-rev` as a reference
point for the upstream revision as of this latest update. Among other
purposes, the `manifest-rev` branch allows the manifest file to use SHAs
as project revisions.

Although `manifest-rev` is a normal Git branch, west will recreate and/or
reset it on the next update. For this reason, it is **dangerous**
to check it out or otherwise modify it yourself. For instance, any commits
you manually add to this branch may be lost the next time you run ``west
update``. Instead, check out a local branch with another name, and either
rebase it on top of a new `manifest-rev`, or merge `manifest-rev` into
it.


**Note:** West does not create a `manifest-rev` branch in the manifest repository, since west does not manage the manifest repository's branches or revisions.
