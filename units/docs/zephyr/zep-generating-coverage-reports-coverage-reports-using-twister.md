---
id: "zep-generating-coverage-reports-coverage-reports-using-twister"
type: "concept"
domain: "test"
title: "Generating coverage reports: Coverage reports using Twister"
summary: "Zephyr's twister script can automatically generate a coverage report from the tests which were executed. You just need to invoke it with the --coverage command line option."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/coverage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/coverage.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's twister script can automatically
generate a coverage report from the tests which were executed.
You just need to invoke it with the `--coverage` command line option.

For example, you may invoke:

```console

$ west twister --coverage -p qemu_x86 -T tests/kernel
```
or:

```console

$ west twister --coverage -p native_sim -T tests/bluetooth
```
which will produce `twister-out/coverage/index.html` report as well as
the coverage data collected by `gcovr` tool in `twister-out/coverage.json`.

Other reports might be chosen with `--coverage-tool` and `--coverage-formats`
command line options.

To generate code coverage report including Zephyr sources as well as your application
code outside of Zephyr repository (see Application Types)
call Twister from your project directory with `--coverage-basedir $ZEPHYR_BASE`
command line option, for example:

```console

$ west twister --coverage -p native_sim --coverage-basedir $ZEPHYR_BASE -T your_project_dir
```

**Note:** By default, Twister calls `gcovr` tool which filters source files assuming real paths are everywhere with all symlinks resolved <gcovr_symlinks_>, so when your development environment has directories with symlinks then, to avoid incomplete `gcovr` reports, either your ZEPHYR_BASE should contain a real path, or `lcov` tool used instead of `gcovr` with additional Twister command line option `--coverage-tool lcov`.

The process differs for unit tests, which are built with the host
toolchain and require a different board:

```console

$ west twister --coverage -p unit_testing -T tests/unit
```
which produces a report in the same location as non-unit testing.


### Per-test coverage matrix


By default coverage is aggregated per test scenario. To attribute coverage
down to individual Ztest test cases -- for example to
answer "which tests exercised line X of `foo.c`" -- pass `--coverage-per-test`:

```console

$ west twister -p mps2/an385 -T tests/kernel --coverage --coverage-tool lcov \
    --coverage-per-test
```
This enables `CONFIG_ZTEST_COVERAGE_PER_TEST`, which resets the
gcov counters before each test case and dumps an isolated, test-tagged coverage
artifact after it. On platforms that support semihosting (ARM, RISC-V and Xtensa
targets under QEMU, such as `mps2/an385`) the per-test data is written straight
to the host filesystem, avoiding the large amount of serial console traffic that
per-test dumping would otherwise produce; other platforms fall back to the serial
console transport.

In addition to the usual aggregated coverage report, this produces:

* one `<scenario>.<test>.info` tracefile per test under each build's
  `coverage/tests/` directory, and
* `twister-out/coverage/test_matrix.json`, a machine-readable matrix with a
  `by_line` view (`{file: {line: [tests]}}`) and a `by_test` view
  (`{test: {file: [lines]}}`).

Per-test attribution is carried by the matrix (and its dashboard), not by the
aggregated lcov report: each instance's coverage is collapsed to a single
tracefile before aggregation, so the end-of-run reporting stays proportional to
the number of instances rather than the total number of test cases.


**Note:** `--coverage-per-test` requires the `lcov` coverage tool, because the matrix relies on lcov's per-test `TN` tracefile records; `gcovr` has no equivalent. It also implies `--coverage`.


#### Visualizing the matrix


`test_matrix.json` can be turned into a self-contained, interactive HTML
dashboard with the standalone `scripts/gen_test_matrix_dashboard.py`
script (it has no dependency on Twister and can be run on any previously
generated matrix):

```console

$ scripts/gen_test_matrix_dashboard.py -i twister-out/coverage/test_matrix.json
```
This writes `twister-out/coverage/test_matrix.html`, which lists -- per test
-- how many files and lines it covers and how many lines it covers *uniquely*
(that no other test reaches, useful for spotting redundant or load-bearing
tests), and lets you drill into the files a test covers or look up which tests
cover a given file and line.


### Using different toolchains


Twister looks at the environment variable `ZEPHYR_TOOLCHAIN_VARIANT`
to check which gcov tool to use by default. The following are used as the
default for the Twister `--gcov-tool` argument default:

+-----------+-----------------------+
| Toolchain | `--gcov-tool` value |
+-----------+-----------------------+
| host      | `gcov`              |
+-----------+-----------------------+
| llvm      | `llvm-cov gcov`     |
+-----------+-----------------------+
| zephyr    | `gcov`              |
+-----------+-----------------------+
