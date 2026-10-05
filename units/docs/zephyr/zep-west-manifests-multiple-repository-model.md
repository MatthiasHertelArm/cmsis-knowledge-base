---
id: "zep-west-manifests-multiple-repository-model"
type: "concept"
domain: "project"
title: "West Manifests: Multiple Repository Model"
summary: "West's view of the repositories in a west workspace, and their history, looks like the following figure (though some parts of this example are specific to upstream Zephyr's use of west):"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

West's view of the repositories in a `west workspace`, and their
history, looks like the following figure (though some parts of this example are
specific to upstream Zephyr's use of west):

The history of the manifest repository is the line of Git commits which is
"floating" on top of the gray plane. Parent commits point to child commits
using solid arrows. The plane below contains the Git commit history of the
repositories in the workspace, with each project repository boxed in by a
rectangle. Parent/child commit relationships in each repository are also shown
with solid arrows.

The commits in the manifest repository (again, for upstream Zephyr this is the
zephyr repository itself) each have a manifest file. The manifest file in each
commit specifies the corresponding commits which it expects in each of the
project repositories. This relationship is shown using dotted line arrows in the
diagram. Each dotted line arrow points from a commit in the manifest repository
to a corresponding commit in a project repository.

Notice the following important details:

- Projects can be added (like `P1` between manifest repository
  commits `D` and `E`) and removed (`P2` between the same
  manifest repository commits)

- Project and manifest repository histories don't have to move
  forwards or backwards together:

  - `P2` stays the same from `A → B`, as do `P1` and `P3` from ``F →
    G``.
  - `P3` moves forward from `A → B`.
  - `P3` moves backward from `C → D`.

  One use for moving backward in project history is to "revert" a regression by
  going back to a revision before it was introduced.

- Project repository commits can be "skipped": `P3` moves forward
  multiple commits in its history from `B → C`.

- In the above diagram, no project repository has two revisions "at
  the same time": every manifest file refers to exactly one commit in
  the projects it cares about. This can be relaxed by using a branch
  name as a manifest revision, at the cost of being able to bisect
  manifest repository history.
