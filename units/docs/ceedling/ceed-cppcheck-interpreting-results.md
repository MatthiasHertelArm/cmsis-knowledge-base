---
id: "ceed-cppcheck-interpreting-results"
type: "concept"
domain: "test"
title: "Cppcheck: Interpreting results"
summary: "The tally in the console output counts findings by severity. Cppcheck assigns every finding one of six severities."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#interpreting-results"
license: "MIT"
mode: "V"
---

The tally in the [console output](#console-output) counts findings by severity.
Cppcheck assigns every finding one of six severities.

| Severity | Meaning |
|----------|---------|
| `error` | A definite defect, such as a double free or buffer overrun |
| `warning` | Likely a defect, worth review |
| `style` | Stylistic issue, including unused code |
| `performance` | Code that is correct but avoidably slow |
| `portability` | Behavior that differs across compilers or platforms |
| `information` | Notes about the analysis itself, such as missing includes |

Only `error` fails a build by default. Widen that with
[`:fail_build_severities:`](#fail_build_severities).

For finding-by-finding detail, open a configured report. The text report is
easiest to read at the terminal:

```shell
$ cat build/artifacts/cppcheck/CppcheckReport.txt
```

See [Cppcheck's manual][cppcheck-manual] for what each check means and how to
suppress findings you have reviewed.

[Cppcheck]:           https://cppcheck.sourceforge.io
[cppcheck-download]:  https://cppcheck.sourceforge.io/#download
[cppcheck-releases]:  https://github.com/danmar/cppcheck/releases
[cppcheck-manual]:    https://cppcheck.sourceforge.io/manual.pdf
[docker-hub]:         https://hub.docker.com/repository/docker/throwtheswitch/
