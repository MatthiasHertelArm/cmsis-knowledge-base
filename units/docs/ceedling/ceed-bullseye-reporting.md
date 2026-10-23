---
id: "ceed-bullseye-reporting"
type: "concept"
domain: "test"
title: "Bullseye: Reporting"
summary: "Bullseye is a single self-contained toolchain."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#reporting"
license: "MIT"
mode: "V"
---

Bullseye is a single self-contained toolchain.

### Console summaries

Two summaries print after a `bullseye:` task. Per-function detail lists each
function's invocation status and condition/decision coverage. Whole-file totals
follow as a single banner.

```
-------------------------------
BULLSEYE: CODE COVERAGE SUMMARY
-------------------------------
calc_never_used(int,int)       0 / 1 =   0%   0 /  6 =   0%
calc_classify(int)             1 / 1 = 100%   1 /  4 =  25%
------------------------  -----------------  --------------
Total                          1 / 2 =  50%   1 / 10 =  10%

-------------------------------
BULLSEYE: CODE COVERAGE SUMMARY
-------------------------------
FUNCTIONS: 50%
BRANCHES:  10%
```

The totals banner covers every function and branch recorded in the coverage
data file. It is not limited to what the current task invocation touched.

### Branch coverage detail

Enabling [`:branch_detail:`](#branch_detail) adds an annotated source listing.
Each probe is marked to the left of its source line.

```
--------------------------------
BULLSEYE: BRANCH COVERAGE DETAIL
--------------------------------
src/calc.c:
        1 #include "calc.h"
        2
X       3 int calc_classify(int n) {
-->T    4   if (n > 10) { return 1; }
-->     5   else if (n < 0) { return -1; }
        6   return 0;
        7 }
        8
-->     9 int calc_never_used(int a, int b) {
-->    10   if (
  -->           a &&
  -->                b) { return 1; }
       11   return 0;
       12 }
```

The markers carry specific meanings.

| Marker | Meaning |
|---|---|
| `X` | An executed function, switch label, try block, or loop body |
| `T` | A decision that evaluated true |
| `F` | A decision that evaluated false |
| `t` | A condition within a decision that evaluated true |
| `f` | A condition within a decision that evaluated false |
| `-->` | Incomplete coverage |
| `/` | An excluded probe |

Several probes on one line are distinguished by letter suffixes such as `19a`
and `19b`.

### HTML reports

A full interactive HTML report is generated to
`build/artifacts/bullseye/covhtml/`. Open `index.html` in a browser.

### XML reports

Enabling [`:xml_report:`](#xml_report) writes
`build/artifacts/bullseye/coverage.xml`. Cobertura format suits CI dashboards
that already consume it. Bullseye's native schema carries more detail,
including per-probe results.

### Report exclusions

Framework and test sources are excluded from reports automatically. Unity,
CMock, CException, files matching your test file prefix, and generated mocks
are all excluded. Aggregate percentages therefore reflect your production code.

Exclusions apply to console totals, HTML reports, and XML reports alike.

Bullseye calls the underlying concept a region. A region is an inclusion or
exclusion rule. Regions can match by filename, directory, function, or C++
class and namespace. This plugin uses filename-pattern exclusions only. See
[Bullseye's region reference][bullseye-regions] for the full syntax.
