---
id: "intr-bazel-build-system-for-embedded-pr-using-bazel"
type: "concept"
domain: "debug"
title: "Bazel Build System for Embedded Projects: Using Bazel"
summary: "Bazel is used as a command line tool. It has many commands and flags so I will not go through all, but here is a short overview of the most important ones."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-30-bazel-build-system-for-embedded-projects.md"
doc_source: "https://interrupt.memfault.com/blog/bazel-build-system-for-embedded-projects#using-bazel"
license: "CC-BY-SA-4.0"
mode: "V"
---

Bazel is used as a command line tool. It has many commands and flags so I will not go through all, but here is a short overview of the most important ones.

Building a target is done as follows:
```bash
bazel build //<package>:<target>
```
Where `<package>` is the path of the package to be built and `<target>` specifies one or more targets. For example `bazel build //my_dir:hello`, will build the target named `hello`, within the directory `my_dir`, or `bazel build //my_dir/...` will build all targets within the directory `my_dir`. Various declinations of this syntax make it less verbose, for example, the leading `//` can be omitted, and if the target name is the same as the package name, it can also be omitted.

Similarly, all tests targets can be tested with:
```bash
bazel test //my_dir/...
```
A test target is a Bazel rule that implements a `test` executable. Such rules are commonly named such as `cc_test`, `py_test`, etc.

An executable target can run with:
```bash
bazel run //my_dir:hello
```
An executable target is any Bazel rule that can be executed, so it also includes test targets. Executables that are not test targets are commonly named such as `cc_binary`, `py_binary`, etc.

Note that running `bazel test` or `bazel run` will also run `bazel build` if the target was not built or if any of the input files of the target have been altered.

Flags can also be used to change the behavior of a command. These flags can be passed as command line arguments, such as `bazel test //:my_target --runs_per_test=10` to execute a specific test 10 times, or `bazel build /:my_target --platforms=//platforms:esp32` to cross-compile a target for esp32.

These flags can be combined and can add up to a very verbose command line which makes it difficult to remember, type or even share. That is where the `.bazelrc` file comes in handy. Here is an example of a `.bazelrc` file:

```bash
# All options coming from this file will be announced on the terminal.
common --announce_rc

# If the file `.bazelrc.local`, exists it will be imported.
try-import .bazelrc.local

# Add timestamps to message.
common --show_timestamps

# If a command fails, print out the full command line.
build --verbose_failures

# Print the full error of the test that fails.
test --test_output=errors

# Configuration for "stress".
test:stress --runs_per_test=10
test:stress --notest_keep_going
```

Each flag are preceded by a command, which corresponds to the Bazel command to which it applies, or some may have specific meaning such as `common`, which applies to all Bazel commands, or `try-import`, which tries to import a file if it exists.

In addition, commands can be grouped into configs. This is represented here with `test:stress`. It means that when the user executes `bazel test --config=stress //:my_target`, the flags `--runs_per_test=10` and `--notest_keep_going` will be added to the command line.

In a mature project, this file can be very large, hence it is always a good practice to add at the beginning `common --announce_rc` to ensure that all the added commands are also announced on the standard output when the command is executed.

Now that we know the basis of what Bazel is and how to use it, let's deep dive into the subject.
