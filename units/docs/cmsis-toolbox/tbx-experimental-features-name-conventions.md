---
id: "tbx-experimental-features-name-conventions"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Name Conventions"
summary: "Locations can be symbols or numeric addresses. An additional project or path to an image file may be specified."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

#### Location

Locations can be symbols or numeric addresses. An additional project or path to an image file may be specified.

Location Form                         | Description
:-------------------------------------|:------------------------------------
`symbol`                              | Finds matching symbols in all available symbol files.
`"sourcefile"::symbol`                | Finds matching symbols in a source file across all available symbol files.
`project\|symbol`                     | Finds matching symbols in symbol files from a specific project.
`project\|"sourcefile"::symbol`       | Finds matching symbols in a source file from a specific project.
`file-path\|symbol`                   | Finds matching symbols in symbol files from a specific image file.
`file-path\|"sourcefile"::symbol`     | Finds matching symbols in a source file from a specific image file.

ToDo: examples

#### References

References identify a node in the `ctrace.yml` that generated information in `ctrace-run.yml`. These nodes are used for diagnostics and for linking trace analysis results back to the trace setup.

**Examples:**

```yml
ref: <pname>/data#2        # refers to pname section, `data:` node, list node #2
ref: data#2                # `data:` node, list node #2
ref: instruction:start#0   # `instruction:` node, `start:` node, list node #0
```
