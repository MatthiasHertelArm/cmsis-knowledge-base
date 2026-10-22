---
id: "ceed-ceedling-s-command-line-application-commands"
type: "concept"
domain: "test"
title: "Ceedling’s Command Line: Application commands"
summary: "Ceedling provides robust command line help for application commands. Execute ceedling help for a summary view of all application commands. Execute ceedling help <command> for detailed help."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/command-line/#application-commands"
license: "MIT"
mode: "V"
---

Ceedling provides robust command line help for application commands.
Execute `ceedling help` for a summary view of all application commands.
Execute `ceedling help <command>` for detailed help.

Because the built-in command line help is thorough, the following sections
do not provide exhaustive details.

### `ceedling [no arguments]`

Runs the default build tasks. Unless set in the project file, Ceedling 
uses a default task of `test:all`. To override this behavior, set your 
own default tasks in the project file (see later section).

_No parameters._

---

### `ceedling <tasks...>`

Runs the named tasks (e.g. `ceedling test:all`). Various option flags exist 
to control project configuration loading, verbosity levels, logging, test 
task filters, etc.

See [next section](#build-plugin-tasks) to understand the build & 
plugin tasks this application command is able to execute. Parameters are 
the same as those for `ceedling build`, below.

---

### `ceedling build [TASKS...]`

`build` is an optional alias for the preceding (i.e. `ceedling test:all` 
is equivalent to `ceedling build test:all`). The command actually executed
is `ceedling build` under-the-hood. To maintain Ceedling’s historical
command line convention, special rigging causes the `build` application
command to be optional.

`TASKS` are zero or more build operations created from your project 
configuration. If no tasks are provided, built-in default tasks or your 
`:project` ↳ `:default_tasks` will be executed.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | `-p` | Loads the filepath as your base project configuration | none |
| `--mixin` | `-m` | Merges the configuration mixin by name, filepath, or inline YAML (`=` sigil). Repeatable. | `[]` |
| `--verbosity` | `-v` | Sets logging level | `normal` |
| `--log` | | Enable logging to `<build path>/logs/ceedling.log` | unset |
| `--logfile` | `-l` | Enables logging to specified filepath (supersedes `--log`) | `''` (none) |
| `--graceful-fail` | | Force exit code of 0 for unit test failures | unset |
| `--test-case` | | Filter for individual unit test names | `''` (none) |
| `--exclude-test-case` | | Prevent matched unit test names from running | `''` (none) |
| `--force-test-rerun` | | Run test executables and report fresh results even if unchanged | `false` (disabled) |
| `--ruby-replacement` | | Enables inline Ruby string expansion (`#{...}`) in project configuration | `false` (disabled) |

---

### `ceedling dumpconfig [FILEPATH] [SECTIONS...]`

Process project configuration and write final result to a YAML file.

`FILEPATH` is a required path to a destination YAML file, unless `--stdout` is 
set (see below). A nonexistent path will be created.

`SECTIONS` is an optional config “path” that extracts a portion of a 
configuration. The top-level YAML container will be the path’s last 
element. Example: `ceedling dumpconfig my/path/config.yml tools test_compiler`.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | `-p` | Loads the filepath as your base project configuration | none |
| `--mixin` | `-m` | Merges the configuration mixin by name, filepath, or inline YAML (`=` sigil). Repeatable. | `[]` |
| `--app` | | Runs Ceedling application and its config manipulations | `true` |
| `--stdout` | | Writes YAML to standard output instead of `FILEPATH`, for consuming tools | `false` (disabled) |
| `--ruby-replacement` | | Enables inline Ruby string expansion (`#{...}`) in project configuration | `false` (disabled) |

Use `--stdout` when a consuming tool wants Ceedling’s fully resolved 
configuration piped directly into its own process rather than written to 
a temp file and read back. Omit `FILEPATH` when using this flag — any 
positional arguments given are treated as `SECTIONS` instead:

```
ceedling dumpconfig --stdout tools test_compiler
```

---

### `ceedling check`

Loads and processes your project configuration with full logging — the 
same loading, merging, manipulation, and validation a real build would 
perform — but executes no build tasks and writes no files. Useful for 
confirming a configuration is well-formed.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | `-p` | Loads the filepath as your base project configuration | none |
| `--mixin` | `-m` | Merges the configuration mixin by name, filepath, or inline YAML (`=` sigil). Repeatable. | `[]` |
| `--ruby-replacement` | | Enables inline Ruby string expansion (`#{...}`) in project configuration | `false` (disabled) |

---

### `ceedling environment`

Lists project related environment variables:

* All environment variable names and string values added to your 
  environment from within Ceedling and through the `:environment`
  section of your configuration. This is especially helpful in 
  verifying the evaluation of any string replacement expressions in
  your `:environment` config entries. (Requires the `--ruby-replacement`
  flag if any [inline Ruby string expansion][inline-ruby-string-expansion]
  is present — see linked section for details.)
* All existing Ceedling-related environment variables set before you
  ran Ceedling from the command line.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | `-p` | Loads the filepath as your base project configuration | none |
| `--mixin` | `-m` | Merges the configuration mixin by name, filepath, or inline YAML (`=` sigil). Repeatable. | `[]` |
| `--ruby-replacement` | | Enables inline Ruby string expansion (`#{...}`) in project configuration | `false` (disabled) |

---

### `ceedling example NAME [DEST]`

Extracts an example project from within Ceedling to your local 
filesystem. The available examples are listed with `ceedling examples`.

`NAME` is required to specify the example to extract and becomes the 
containing directory for the extracted project. `DEST` is an optional 
containing directory path (default is your working directory).

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--local` | | Install Ceedling plus supporting tools to vendor/ | `false` |
| `--docs` | | Copy all documentation to docs/ subdirectory of project | `false` |

---

### `ceedling examples`

Lists the available examples within Ceedling. To extract an example,
use `ceedling example`.

_No parameters._

---

### `ceedling help [COMMAND]`

Displays summary help for all application commands and detailed help 
for each command. `ceedling help` also loads your project 
configuration (if available) and lists all build tasks from it. 
`COMMAND` is optional and produces detailed help for a specific 
application command.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | `-p` | Loads the filepath as your base project configuration | none |
| `--mixin` | `-m` | Merges the configuration mixin by name, filepath, or inline YAML (`=` sigil). Repeatable. | `[]` |
| `--ruby-replacement` | | Enables inline Ruby string expansion (`#{...}`) in project configuration | `false` (disabled) |

---

### `ceedling new [DEST]`

Creates a new project structure. `DEST` is an optional root path for the 
new project (default is your working directory).

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--local` | | Install Ceedling plus supporting tools to vendor/ | `false` |
| `--docs` | | Copy all documentation to docs/ subdirectory of project | `false` |
| `--configs` | | Install starter project file in project root | `true` |
| `--ceedling-yml` | | Name starter project file `ceedling.yml` instead of historical default of `project.yml` | `false` |
| `--force` | | Ignore any existing project and recreate destination | `false` |
| `--gitsupport` | | Create .gitignore / .gitkeep files for convenience | `false` |

---

### `ceedling upgrade PATH`

Upgrade vendored installation of Ceedling for an existing project 
along with any locally installed documentation bundles. `PATH` is 
required and should be the root of the project to upgrade.

| Flag | Alias | Description | Default |
|---|---|---|---|
| `--project` | | Project filename used in the project-existence check | `project.yml` |

---

### `ceedling docs [DEST]`

Exports the Ceedling documentation bundle to the filesystem. `DEST` is 
an optional destination path (default is your working directory).

_No parameters._

---

### `ceedling version`

Displays version information for Ceedling and its components. Version output for Ceedling includes the Git Commit short SHA in Ceedling’s build identifier and Ceedling’s path of origin.

```
🌱 Welcome to Ceedling!

  Ceedling => #.#.#-<Short SHA>
  ----------------------
  <Ceedling install path>

  Build Frameworks
  ----------------------
       CMock => #.#.#
       Unity => #.#.#
  CException => #.#.#
```

If the short SHA information is unavailable such as in local development, the SHA is omitted. The source for this string is generated and captured in the Gem at the time of Ceedling’s automated build in CI.

_No parameters._

---
