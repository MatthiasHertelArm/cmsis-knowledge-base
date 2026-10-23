---
id: "ceed-cppcheck-console-output"
type: "concept"
domain: "test"
title: "Cppcheck: Console output"
summary: "These excerpts come from real runs. Build progress lines are left out."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#console-output"
license: "MIT"
mode: "V"
---

These excerpts come from real runs. Build progress lines are left out.

Each report logs a line as it is created. With an XML report, which
[`:fail_build:`](#fail_build) also implies, a tally of findings by severity
follows:

```
Creating Cppcheck text report...
Creating Cppcheck xml report...
Cppcheck findings: 1 error, 2 information, 1 style
```

A run without findings logs `Cppcheck found no issues.` in place of the tally.

With `:fail_build:` enabled, findings of a listed severity fail the build:

```
❌ BUILD FAILURE SUMMARY
 • [CPPCHECK] Cppcheck found 1 finding matching :cppcheck ↳ :fail_build_severities (1 error). See the report in build/artifacts/cppcheck.
```

With no report configured, Cppcheck does not run:

```
⚠️ WARNING: No Cppcheck reports are configured, so no analysis ran.
Add a report to :cppcheck ↳ :reports, or enable :cppcheck ↳ :fail_build.
```
