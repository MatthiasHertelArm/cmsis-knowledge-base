---
id: "mbedtls-switching-to-the-new-code-style-migrating-existing-work-the-theory"
type: "concept"
domain: "security"
title: "Switching to the new code style: Migrating existing work: the theory"
summary: "If you started working on a branch of Mbed TLS with the old code style, any part of the code that has been both modified in your branch and restyled in the main branch will lead to a merge conflict."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/rewrite-branch-for-coding-style.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/rewrite-branch-for-coding-style.md#migrating-existing-work-the-theory"
license: "Apache-2.0"
mode: "V"
---

If you started working on a branch of Mbed TLS with the old code style, any part of the code that has been both modified in your branch and restyled in the main branch will lead to a merge conflict. To avoid that, you must migrate your work to the new style.

It is not enough to rewrite the final state of your work to the new format, because that will still be a merge conflict (between just restyling, and semantically meaningful work followed by restyling). You must rebase-and-restyle your branch. This document explains how and when.

The Mbed TLS project provides a script [`mbedtls-rewrite-branch-style`](https://github.com/Mbed-TLS/mbedtls-docs/raw/main/tools/bin/mbedtls-rewrite-branch-style) which takes a Git branch with work done in the old code style, and migrates it to the new code style. Suppose your work is in a branch `mywork`, and it's intended to be submitted to some target branch (such as `development`). The migration works in two phases:

1. First identify the new commits, and attach them to the commit preceding the code style switch. This is an ordinary Git rebase (`git rebase code-style-switch-commit~ mywork`).
2. Iterate over the commits from the `mywork` branch after it forks from the target branch. For each commit, construct a new commit whose content is the restyled content of the old commit, and form a chain starting at the code style switch commit.

Using diagrams in the same form as the Git manual, the original situation is:

```
      A---B---C mywork
     /
D---E---F---G---H target
            ^
            |
            "Switch to the new code style"
```

The first phase attaches `mywork` just before the code style switch commit G:

```
          A'---B'---C' mywork
         /
D---E---F---G---H target
            ^
            |
            "Switch to the new code style"
```

In the second phase, the migration successively constructs a new branch with restyled commits. First the migration restyles the content of A' to obtain A'':

```
            A'---B'---C' mywork
           /
          /   A'' new/mywork
         /   /
D---E---F---G---H target
            ^
            |
            "Switch to the new code style"
```

The process continues with B' and so on:

```
            A'---B'---C' mywork
           /
          /   A''---B'' new/mywork
         /   /
D---E---F---G---H target
            ^
            |
            "Switch to the new code style"
```

Once the migration reaches the end of the branch, it renames the new branch to the original name:

```
            A'---B'---C' old/mywork
           /
          /   A''---B''---C'' mywork
         /   /
D---E---F---G---H target
            ^
            |
            "Switch to the new code style"
```

The branch `mywork` can now be pushed to a pull request.
