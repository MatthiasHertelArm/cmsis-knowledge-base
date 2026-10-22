---
id: "ceed-plugin-overview-summaries-vs-reports"
type: "concept"
domain: "test"
title: "Plugin Overview: Summaries vs. Reports"
summary: "Coverage summaries and coverage reports provide different levels of fidelity and usability. Summaries are relatively unsophisticated while reports are sophisticated. As such, both provide different capabilities and levels of usability."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/gcov/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/#summaries-vs-reports"
license: "MIT"
mode: "V"
---

Coverage summaries and coverage reports provide different levels of fidelity
and usability. Summaries are relatively unsophisticated while reports are 
sophisticated. As such, both provide different capabilities and levels of 
usability.

### Coverage summaries

Optional coverage summaries are intentionally simple. They require no
configuration and, to oversimplify, are largely filtered output from the `gcov`
tool.

Coverage summaries are reported to the console for each source file exercised by
the tests executed by `gcov:` tasks. That is, coverage summaries correspond to
the tests executed, and in turn, the source code that your tests call. This
could be all tests (and thus all source code) or a subset of tests (and some
subset of source code). The `gcov` tool is run multiple times after test suite
execution in direct relation to the set of tests you ran with `gcov:` testing 
tasks. In short, the scope of coverage summaries is guaranteed to match the
test suite you run.

Coverage summaries do not include any sort of grand total, final tallies. This 
is the domain of full coverage reports.

Note that Ceedling can exercise the same source code under multiple scenarios
using multiple test files. Practically, this means that the same source file
may be listed in the coverage summaries more than once. That said, its coverage
statistics will be the same each time — the aggregate result of all tests that
exercised it.

### Coverage reports

Coverage reports provide both much more detail and better overviews of coverage
than the console-based coverage summaries. However, with this comes the need
for more sophisticated configuration and certain caveats on what is reported.

Later sections detail how to configure the reports this plugin can generate.

Of note is a consequence of how reports are generated and the limits of the
tools that do so. Reports are generated using coverage results on disk. The
report generation tools slurp up the coverage results they find in the `gcov/`
build output directory. This means that previous test suite runs can "pollute"
coverage reports. The solution is simple if blunt — run the `clobber` task
before running a coverage-instrumented test suite. This will yield a coverage
report with scope that matches that of the test suite you run.

Both the `gcovr` and `reportgeneator` reporting utilities include powerful
filters that can limit the scope of reports. Hypothetically, it’s possible for
coverage reports to have the same clear scope as coverage summaries. However,
in large projects, these filters would cause impractically long command lines.
Both tools provide configuration file options that would solve the command line
problem. However, this feature is "experimental" for `gcovr` and considerable 
work to implement for both reporting utilities. At present, running 
`ceedling clobber` before generating reports is the best option to ensure 
accurate reports.
