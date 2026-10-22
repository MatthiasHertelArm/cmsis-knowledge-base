---
id: "ceed-gcovr-configuration-plugin-configuration"
type: "concept"
domain: "test"
title: "GCovr Configuration: Plugin configuration"
summary: "The following options are exposed through your project configuration file, all beneath :gcov ↳ :gcovr. Only specify those you need or those whose defaults you need to override."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#plugin-configuration"
license: "MIT"
mode: "V"
---

The following options are exposed through your project configuration file, all
beneath `:gcov` ↳ `:gcovr`. Only specify those you need or those whose defaults
you need to override. You do not need to include all these options in your
Gcov plugin configuration.

### `:report_root`

The root directory of your source files. File names are reported relative to
this root. Ceedling does not derive a default `:report_include` from it —
`gcovr` itself only searches beneath `--root` when no `--filter` is given.

!!! warning "`gcovr` accepts only one reporting root path"
    `gcovr` accepts only a single path for `:report_root`. In unusual project
    layouts, you may need to specify as root a parent folder that includes 
    _all_ source files and selectively exclude paths or files from coverage 
    reporting (see `:report_exclude` and `:exclude_directories`).

**Default:** `"."` (the current directory)

---

### `:config_file`

Load the specified `gcovr` configuration file. (`gcovr --config`)

When `:config_file` is set, Ceedling passes only `--root` and `--config` to
`gcovr` and defers (nearly) all other configuration to the file. This prevents
Ceedling from overriding config file values with its CLI arguments.
`:report_root` is still applied because Ceedling may invoke `gcovr` from a
different working directory than your project root, and `:custom_args:` is
still applied too — the one way to pass Gcovr flags of your own alongside a
config file (see `:custom_args` below).

To preserve the plugin's base filtering behavior, include exclusion patterns
matching your project layout in the config file itself — see
[Gcovr configuration file](#gcovr-configuration-file) above.

**Default:** unset — Ceedling does not look for or autodetect a config file
on disk; `gcovr` itself is only ever told to load one when `:config_file` is
explicitly set.

---

### `:fail_under_line`

Exit with a status of 2 if the total line coverage is less than this minimum
percentage. Can be ORed with the exit status of other `:fail_under_*` options.
(`gcovr --fail-under-line`)

**Values:** `1`–`100`

---

### `:fail_under_branch`

Exit with a status of 4 if the total branch coverage is less than this minimum
percentage. Can be ORed with the exit status of other `:fail_under_*` options.
(`gcovr --fail-under-branch`)

**Values:** `1`–`100`

---

### `:fail_under_decision`

Exit with a status of 8 if the total decision coverage is less than this minimum
percentage. Can be ORed with the exit status of other `:fail_under_*` options.
(`gcovr --fail-under-decision`)

`gcovr` treats `--fail-under-decision` as a no-op without `--decisions` also
present — setting this option implies `:decisions` (below) automatically, so
it's never silently non-functional.

**Values:** `1`–`100`

**Requires:** `gcovr` 7.0 or higher

---

### `:decisions`

Report the decision coverage. For HTML, JSON, and the summary report.
(`gcovr --decisions`)

Implied automatically whenever `:fail_under_decision` is set.

**Requires:** `gcovr` 5.1 or higher

---

### `:fail_under_function`

Exit with a status of 16 if the total function coverage is less than this minimum
percentage. Can be ORed with the exit status of other `:fail_under_*` options.
(`gcovr --fail-under-function`)

**Values:** `1`–`100`

---

### `:exception_on_fail`

If any `:fail_under_*` option above is set and its condition is met, specifies
whether that condition should break the build. When disabled, Ceedling simply
logs a warning without breaking the build.

**Default:** `false`

---

### `:source_encoding`

Select the source file character encoding. (`gcovr --source-encoding`)

**Default:** the system default encoding (typically `UTF-8`)

---

### `:branches`

Report the branch coverage instead of the line coverage. Applies to the text
report only. Uses `gcovr --txt-metric branch` on `gcovr` 7.0+ (`--branches` is
deprecated as of 7.0, though still functional); `gcovr --branches` below it.

---

### `:sort_uncovered`

Sort entries by increasing number of uncovered lines. Applies to text and HTML
reports. Uses `gcovr --sort uncovered-number` on `gcovr` 7.0+ (`--sort-uncovered`
is deprecated as of 7.0, though still functional); `gcovr --sort-uncovered` below it.

---

### `:sort_percentage`

Sort entries by increasing percentage of uncovered lines. Applies to text and
HTML reports. Uses `gcovr --sort uncovered-percent` on `gcovr` 7.0+
(`--sort-percentage` is deprecated as of 7.0, though still functional);
`gcovr --sort-percentage` below it.

---

### `:print_summary`

Print a small report to stdout with line and branch percentage coverage. This
is in addition to any other configured reports. (`gcovr --print-summary`)

---

### `:report_include`

Keep only source files that match this filter. Filters are regular
expressions. (`gcovr --filter`)

This narrows which files are considered at all, but does not override
[Results filtering](#results-filtering)'s automatic exclusion defaults — a
file excluded by one of those three default patterns stays excluded even if
it also matches `:report_include`. See
[Overriding the defaults](#overriding-the-defaults) if you need to remove one
of them.

**Example:** `"^src"`

---

### `:report_exclude`

Exclude source files that match this filter. Filters are regular expressions.
(`gcovr --exclude`)

Ceedling automatically generates and prepends its own exclusion patterns for
test files, test support files, and generated/vendored build files — see
[Results filtering](#results-filtering) above for exactly what these cover
and why. Anything you provide here is combined with those defaults, not a
replacement for them — this option can only add further exclusions, never
remove or override one of the three defaults (e.g. to include test files in
results). See [Overriding the defaults](#overriding-the-defaults) for how to
do that instead.

**Example:** `"^vendor.*|^build.*|^test.*|^lib.*"`

---

### `:gcov_filter`

Keep only `.gcov` data files that match this filter. Filters are regular
expressions. (`gcovr --gcov-filter`)

---

### `:gcov_exclude`

Exclude `.gcov` data files that match this filter. Filters are regular
expressions. (`gcovr --gcov-exclude`)

---

### `:exclude_directories`

Exclude directories that match this filter while searching for raw coverage
files. Filters are regular expressions. (`gcovr --exclude-directories`)

---

### `:gcov_executable`

Use a particular `gcov` executable. This may be appropriate and necessary in
special circumstances — review Ceedling's options for modifying tools first.
(`gcovr --gcov-executable`)

---

### `:exclude_unreachable_branches`

Exclude branch coverage from lines without useful source code.
(`gcovr --exclude-unreachable-branches`)

---

### `:exclude_throw_branches`

For branch coverage, exclude branches that the compiler generates for
exception handling. (`gcovr --exclude-throw-branches`)

---

### `:merge_mode_function`

For `gcovr` 6.0+, multiple instances of the same function in coverage results
can cause a fatal error. Since Ceedling can test multiple build variations of
the same source function, this is a real risk. This option controls how
`gcovr` merges those repeated entries. See the
[gcovr merging docs](https://gcovr.com/en/stable/guide/merging.html) for all
valid values. Ignored on `gcovr` versions below 6.0.

**Default:** `merge-use-line-max` (`gcovr`'s own default, `strict`, raises an
exception for many Ceedling projects)

---

### `:use_gcov_files`

Use existing `.gcov` files for analysis instead of running `gcov` again.
(`gcovr --use-gcov-files`)

**Default:** `false`

---

### `:gcov_ignore_parse_errors`

Skip lines with parse errors in `.gcov` files instead of exiting with an
error. (`gcovr --gcov-ignore-parse-errors`)

---

### `:object_directory`

Override normal working directory detection for `.gcda`/`.gcno` files.
(`gcovr --object-directory`)

---

### `:keep`

Keep intermediate `.gcov` files after processing. (`gcovr --keep`)

---

### `:delete`

Delete `.gcda` files after processing. (`gcovr --delete`)

---

### `:threads`

Set the number of threads `gcovr` uses in parallel. (`gcovr -j`)

---

### `:custom_args`

Optional list of one or more raw command line arguments to pass to `gcovr`.
Useful as an escape hatch for any `gcovr` flag Ceedling has no named option
for (e.g. limiting `gcovr`'s search root).

Unlike every other option above, these arguments are still applied even when
`:config_file` is set — the one way to pass `gcovr` flags of your own
alongside a config file.

This does not, on its own, let you override
[Results filtering](#results-filtering)'s automatic exclusion defaults when
`:config_file` is unset — a raw `--filter`/`--exclude` passed here is just as
additive as [`:report_exclude`](#report_exclude); see
[Overriding the defaults](#overriding-the-defaults) for the one option that
actually does.

```yaml
:gcov:
  :gcovr:
    :custom_args:
      - <argument>
      - ...
```

**Default:** `[]`
