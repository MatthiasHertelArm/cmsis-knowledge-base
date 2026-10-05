---
id: "intr-proper-release-versioning-goes-a-l-git-revisions"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way: Git Revisions"
summary: "The second piece of metadata that we want to include in our firmware is a Git revision or Git tag, such as d287bc7311."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning#git-revisions"
license: "CC-BY-SA-4.0"
mode: "V"
---

The second piece of metadata that we want to include in our firmware is a Git revision or Git tag, such as `d287bc7311`.

By having the Git revision baked into the firmware, we can determine which software the binary is based upon, which would help us when we are trying to triage bugs by performing a [git bisect](https://interrupt.memfault.com/blog/git-bisect) or rebuilding old firmwares (provided we have [reproducible builds](https://interrupt.memfault.com/blog/reproducible-firmware-builds)).

You can call `git describe` to acquire the Git revision SHA with a `+` on the end if the project had a dirty state (local modifications) when called.

```
$ git describe --match ForceNone --abbrev=10 --always --dirty="+"
8bb5d7f162+
```

The use of `--match ForceNone` is because I just want the SHA and the dirty signifier and nothing else.

If you'd like to also include a tag and number of commits from the last tag like some projects have, you can use the following command:

```
$ git describe --tags --always --dirty="+" --abbrev=10
1.2.3-18-gdcf62a8fff
```

Refer to the `git describe` [documentation](https://git-scm.com/docs/git-describe) for more information.

### Adding Git Revision

To add a Git SHA to a firmware, we do the work within our build system or Makefile in our case.

```Makefile
GIT_REVISION := \"$(shell git describe --match ForceNone --abbrev=10 --always --dirty="+")\"
DEFINES += GIT_REVISION=$(GIT_REVISION)
CFLAGS += $(foreach d,$(DEFINES),-D$(d))
```

From here, you can create a file that uses the macro `GIT_REVISION` and it will be populated with the output of the shell command.

### Missing Pieces of the Git Revision

The Git revision, just like the SemVer version, is missing the ability to identify unique builds of the firmware. Two developers could each build the Git revision `d287bc7311` and push binaries to an update server and we'd have no way of knowing they are two different builds or know how to tie them back to the source.

We need yet another piece of build information! Last but not least, let's chat about GNU Build ID's.
