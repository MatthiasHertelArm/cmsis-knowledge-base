---
id: "zep-history-and-motivation-rationale-for-a-custom-tool"
type: "concept"
domain: "project"
title: "History and Motivation: Rationale for a custom tool"
summary: "Some of west's features are similar to those provided by Git Submodules and Google's repo."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/why.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/why.rst"
license: "Apache-2.0"
mode: "V"
---

Some of west's features are similar to those provided by
[Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) and
Google's [repo](https://gerrit.googlesource.com/git-repo/).

Existing tools were considered during west's initial design and development.
None were found suitable for Zephyr's requirements. In particular, these were
examined in detail:

* Google repo

  - Does not cleanly support using zephyr as the manifest repository (**R4**)
  - Python 2 only
  - Does not play well with Windows
  - Assumes Gerrit is used for code review

* Git submodules

  - Does not fully support **R1**, since the externally maintained repositories
    would still need to be inside the main zephyr Git tree
  - Does not support **R3**, since downstream copies would need to either
    delete or replace submodule definitions
  - Does not support continuous tracking of the latest `HEAD` in external
    repositories (**R4**)
  - Requires hardcoding of the paths/locations of the external repositories
