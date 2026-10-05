---
id: "intr-reproducible-firmware-builds-checklist"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Checklist"
summary: "In summary, here are the steps to take in order to make a build reproducible:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#checklist"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

In summary, here are the steps to take in order to make a build reproducible:

First, compile your binary in two directories. If the binaries match, you are probably good! Otherwise, follow these strategies:

1. Include a [GNU Build ID](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware) in your binary so it's always easy to identify the build in use.
2. [Enforce that all builds use one version of a compiler](#enforce-compiler-for-build).
3. Compare ELFs and BINs for differences using the tips discussed in this article. Typical differences arise from including absolute paths, timestamps, or shell information in the final binary.
4. Utilize `-ffile-prefix-map=old=new` to normalize macro and debug info paths.

   _If the compiler is older, it may be necessary to instead use
   [`-fdebug-prefix-map=old=new`](#fdebug-prefix-map) to make sure any debug
   information emitted does not rely on absolute paths, and use relative paths
   in the build system or `-fmacro-prefix-map=old=new`_

5. At this point, builds will usually match for an embedded project. If they do not, it's likely non-determinism in one of the build tools being used is causing issues.[^11]

That's it!
