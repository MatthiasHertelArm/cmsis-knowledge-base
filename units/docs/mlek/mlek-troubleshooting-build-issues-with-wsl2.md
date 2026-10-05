---
id: "mlek-troubleshooting-build-issues-with-wsl2"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Build issues with WSL2"
summary: "Builds using Windows® Subsystem For Linux (WSL2) can run into issues if their environment's PATH variable has paths containing unescaped space characters. The error might look like:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#build-issues-with-wsl2"
license: "Apache-2.0"
mode: "V"
---

Builds using Windows® Subsystem For Linux (WSL2) can run into issues if their
environment's PATH variable has paths containing unescaped space characters.
The error might look like:

```
****Building TensorFlow Lite Micro library… /bin/sh: 1: Syntax error: “(” unexpected
 make[2]: *** [CMakeFiles/tensorflow_build.dir/build.make:71: CMakeFiles/tensorflow_build] Error 2
 make[1]: *** [CMakeFiles/Makefile2:537: CMakeFiles/tensorflow_build.dir/all] Error 2
 make[1]: *** Waiting for unfinished jobs…
```

The error here was caused by `C:/Program Files (x86)/` being part of the PATH.
To resolve this issue, remove any paths with spaces. Alternatively, if these
paths are required, escape them using `\` or enclose them with quotes.

Another example of a similar issue: [Discourse issue 171: Build error in makefile](https://discuss.mlplatform.org/t/build-error-in-makefile/171).
