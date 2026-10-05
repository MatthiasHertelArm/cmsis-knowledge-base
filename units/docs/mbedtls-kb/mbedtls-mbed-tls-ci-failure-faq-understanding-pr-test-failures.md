---
id: "mbedtls-mbed-tls-ci-failure-faq-understanding-pr-test-failures"
type: "concept"
domain: "security"
title: "Mbed TLS CI failure FAQ: Understanding PR test failures"
summary: "If the PR tests fail, the status on GitHub is set to a string that lists failed components. Note that due to a GitHub limitation, the list of failed components may be truncated."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/understanding-ci-failures.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/understanding-ci-failures.md#understanding-pr-test-failures"
license: "Apache-2.0"
mode: "V"
---

### PR tests failed. Which components failed?

If the PR tests fail, the status on GitHub is set to a string that lists failed components. Note that due to a GitHub limitation, the list of failed components may be truncated. Click the “Details” link to see the full job breakdown.

The default view on Jenkins unfortunately truncates job names. For more convenient access to the names and logs of failed components:

1. Install the GreaseMonkey/TamperMonkey user script [JenkinsPipelineSteps](https://openuserjs.org/scripts/magnushakansson/JenkinsPipelineSteps).
2. Go to the Jenkins “classic” view by clicking the (figure: Go to classic) icon near the top right, then follow the “Pipeline Steps” link in the left column.

Alternatively, you can extract the list of failed components from the list of failed test cases. See [“PR tests failed. Can I get a detailed list?”](#pr-tests-failed-can-i-get-a-detailed-list).

### PR tests failed. Can I get a detailed list?

You can download the list of failed test cases as an artifact on Jenkins. For example, the list of failures for the first test run of pull request \#9999 is at
```
https://ci.trustedfirmware.org/job/mbed-tls-pr-head/job/PR-9999-head/1/artifact/failures.csv
```

If there are a large number of failures, the file will be compressed: add a `.xz` suffix to the URL.

The failure list consists of the lines of the [outcome file](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#outcome-analysis) where the status is FAIL.

### Analyzing `outcomes.csv` or `failures.csv`

Here are a few examples of Linux/macOS/Unix/WSL shell commands that can help.

#### In which components did this test case fail?

List the components where the test case “Test the thing” in `test_suite_foo` failed:
```
grep ';test_suite_foo;Test the thing;' failures.csv | cut -d ';' -f 2 | sort
```

Also list the components where it passed:
```
xzcat outcomes.csv.xz | grep ';test_suite_foo;Test the thing;' | grep -v ';SKIP;' | cut -d ';' -f 5,2 | sort
```

#### Which test cases failed at least once?

```
cut -d ';' -f 3,4 failures.csv | sort -u
```

### What is the configuration of this component?

Sometimes it can be hard to figure out exactly what configuration results from the code in `all.sh` and the rules to translate between PSA and legacy configuration options.

In a given build, you can run `programs/test/query_compile_time_config MBEDTLS_FOO; echo $?` to check whether `MBEDTLS_FOO` is enabled.

In the outcome file, the test suite reports the test case “Config: FOO” in `test_suite_config.*` as a PASS if the option FOO is enabled, and a SKIP if it is disabled. There are also test cases “Config: !FOO” which PASS if FOO is disabled and SKIP if it is enabled. Note that for some options, both FOO and !FOO are skipped if FOO has no effect because some other option is disabled.

### PR tests failed, but the failure list is empty!

Some failures are not recorded in the outcome file. In such cases, you need to look at the logs on Jenkins. Failures that are not recorded include:

* Static checks that don't involve a library build (code style, Python script checks, documentation build, etc.).
* Build failures in older branches (before [Mbed-TLS/mbedtls#9286](https://github.com/Mbed-TLS/mbedtls/pull/9286)).
* Checks that are run on a build that are not tests of the code, for example checking that a function is or is not present in a given configuration.
* At the time of writing, some minor test scripts do not record information in the outcome file, such as `*_demo.sh` and `tests/context_info.sh`.
* At the time of writing, Windows tests are not recorded in the outcome file.

### There are a lot of failures. Where do I start?

Most configurations are based on either the default configuration or the “full” configuration. The “full” configuration enables experimental and rarely-used features, and also toggles a few behavior change. Most importantly, in Mbed TLS 2.x and 3.x, `MBEDTLS_USE_PSA_CRYPTO` is disabled in the default configuration but enabled in “full”.

In terms of configurations, a suggested order is:

1. First, get the default configuration working.
2. Then the “full” configuration.
3. Then configurations that do not involve PSA drivers.
4. Finally, configurations involving PSA drivers.

### Outcome analysis failed

If you're unfamiliar with outcome analysis, please read the [outcome analysis section in the CI guide](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#outcome-analysis).

Outcome analysis may fail due to earlier failures, in which case you should resolve these failures and get updated CI results. In particular:

* Build failures or sanitizer crashes in some configuration may cause some test cases not to be executed.
* Failures in a driver build, or in the corresponding non-driver build (“reference”), may cause spurious differences to be reported.

The first step is generally to read the outcome analysis logs, which are available as an artifact, e.g.
```
https://ci.trustedfirmware.org/job/mbed-tls-pr-head/job/PR-999-head/1/artifact/result-analysis-analyze_outcomes.log.xz
```

If a test case is reported as not executed: in which configurations would you expect it to run? Pick one and dive into the code to figure out why it isn't executed. If there is a good reason to have a test case that is not executed, add an exception. File an issue if the reason is temporary.

If there is a reported difference between a driver build and its reference build: run the test case in both configurations, and try to figure out why the behavior is different. If the difference can't reasonably be avoided, add an exception.

If outcome analysis complains that something was found in the ignore list but didn't need to be ignored, remove the exception from the ignore list.
