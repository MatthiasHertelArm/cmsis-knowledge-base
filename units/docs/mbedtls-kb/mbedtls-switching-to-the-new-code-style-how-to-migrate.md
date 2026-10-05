---
id: "mbedtls-switching-to-the-new-code-style-how-to-migrate"
type: "concept"
domain: "security"
title: "Switching to the new code style: How to migrate"
summary: "Please have the following tools and files available:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/rewrite-branch-for-coding-style.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/rewrite-branch-for-coding-style.md#how-to-migrate"
license: "Apache-2.0"
mode: "V"
---

### Requirements

Please have the following tools and files available:

* Git 2.17.0 or newer.
* [Uncrustify](https://github.com/uncrustify/uncrustify) 0.75.1. Please note that older or newer versions are not suitable because they give different results. See the [“Installing uncrustify”](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/uncrustify.md#installing-uncrustify) article for some tips.
* Python 3.6 or newer.
* A Git worktree containing the branch of Mbed TLS you want to migrate.
* A local copy of [the branch rewriting script `mbedtls-rewrite-branch-style`](https://github.com/Mbed-TLS/mbedtls-docs/raw/main/tools/bin/mbedtls-rewrite-branch-style). Preferably use the most recent version, since it may have received bug fixes. You can check out the [`mbedtls-docs` repository](https://github.com/Mbed-TLS/mbedtls-docs).

### Simple migration

Prerequisites:

* You have the tools and files listed under [“Requirements”](#requirements) above.
* You have a Git branch `mywork` which branched from `development` before the code style switch. (For work on Mbed TLS 2.28, replace `development` by `mbedtls-2.28` throughout these instructions.)
* The current directory is a Git working directory with `mywork` checked out, and with a remote called `upstream` pointing to [the official Mbed TLS repository](https://github.com/Mbed-TLS/mbedtls).

Run the following command in a terminal, from the Git working directory with `mywork` checked out:

```sh
python3 ~/Downloads/mbedtls-rewrite-branch-style
```

If all goes well, you have successfully migrated `mywork`. You can force-push it to your fork of Mbed TLS (`git push --force-with-lease origin mywork`).

A backup of the old branch is available under the name `old-code-style/mywork`.

If all does not go well, please consult the [known limitations](#known-limitations) and the [troubleshooting section](#troubleshooting) section.

### Trial migration

The following procedure does not modify any existing Git working directory and does not rewrite any existing branch name. It explains how to migrate a branch `mywork` which branched from `development` before the code style switch. (For work on Mbed TLS 2.28, replace `development` by `mbedtls-2.28` throughout these instructions.). The result of the migration will be placed into a branch called `new-code-style/mywork` (it must not exist yet).

Run the following commands from any Git working directory. Adjust `~/Downloads` to the path containing the rewrite script, and `upstream` to the name of a Git remote pointing to [the official Mbed TLS repository](https://github.com/Mbed-TLS/mbedtls).

```sh
python3 ~/Downloads/mbedtls-rewrite-branch-style --onto upstream/development --new-branch-name new-code-style/mywork mywork
```

If all goes well, the branch `new-code-style/mywork` contains the migrated content of `mywork`.

If all does not go well, please consult the [known limitations](#known-limitations) and the [troubleshooting section](#troubleshooting) section.
