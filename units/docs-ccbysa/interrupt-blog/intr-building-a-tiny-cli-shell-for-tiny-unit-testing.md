---
id: "intr-building-a-tiny-cli-shell-for-tiny-unit-testing"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Unit Testing"
summary: "No new software is complete without tests, and the same applies for our command-line shell, even though it seems to be quite low-level."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#unit-testing"
license: "CC-BY-SA-4.0"
mode: "V"
---

No new software is complete without tests, and the same applies for our
command-line shell, even though it seems to be quite low-level. The purpose of
unit tests for a shell would be to ensure that each command never breaks for
developers or on build configurations that aren't used often, such a debug or
factory builds. Nobody wants to test 50 shell commands, so let unit tests do it!

I won't go very deep in this section, but I do want to give a rough idea of how
one would implement unit tests for a shell.

Using CppUTest and a similar structure to our previous [Unit Testing
Basics](https://interrupt.memfault.com/blog/unit-testing-basics) post, we arrive at the
following structure within our `part2/` example:

```
$ tree -L 2  part2/tests
part2/tests
├── Makefile
├── MakefileWorker.mk
├── MakefileWorkerOverrides.mk
├── makefiles
│   └── Makefile_test_shell_commands.mk
└── src
    ├── AllTests.cpp
    └── test_shell_commands.cpp
```

The only source file in `Makefile_test_shell_commands.mk` that we'll include is
`shell_commands.c` since we can mock everything else out.

```makefile
COMPONENT_NAME=test_shell_commands

SRC_FILES = \
  $(PROJECT_SRC_DIR)/shell_commands.c \

TEST_SRC_FILES = \
  $(UNITTEST_SRC_DIR)/test_shell_commands.cpp

include $(CPPUTEST_MAKFILE_INFRA)
```

The other file to look at is `test_shell_commands.cpp`, which is where our tests
reside.

Let's look at what a test for `cli_cmd_hello` would look like. We create our two
arguments, `argc` and `argv`. Next, we pass those directly into the function.
Finally, we ensure that the output was as we expected.

```c++
TEST(TestShellCommands, hello) {
  int argc = 1;
  char *argv[] = {
    (char *)"hello"
  };

  cli_cmd_hello(argc, argv);
  STRNCMP_EQUAL("Hello World!", s_resp_buffer, sizeof(s_resp_buffer));
}
```

How did we capture this output? By using a basic mock in our test.

```c++
static char s_resp_buffer[1024];

// Poor man's mock
void shell_put_line(const char *str) {
  strncpy(s_resp_buffer, str, sizeof(s_resp_buffer));
}
```

`cli_cmd_hello` outputs its response through a function called `shell_put_line`,
which we convert into a mock for the purposes of testing.

We can now run our simple test and verify it works!

```
$ cd part2/tests

$ make
/usr/bin/make -f interrupt/example/firmware-shell/part2/tests/makefiles/Makefile_test_shell_commands.mk
compiling test_shell_commands.cpp
compiling AllTests.cpp
compiling shell_commands.c
Building archive build/test_shell_commands/lib/libtest_shell_commands.a
a - build/test_shell_commands/objs/interrupt/example/firmware-shell/part2/shell_commands.o
Linking build/test_shell_commands/test_shell_commands_tests
Running build/test_shell_commands/test_shell_commands_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 0 ms)
```

For more reference, it's worth checking out how the
[Memfault Firmware SDK](https://github.com/memfault/memfault-firmware-sdk/blob/master/tests/src/test_memfault_demo_cli.cpp)
and
[Skip Scooter's Anchor](https://github.com/rideskip/anchor/tree/master/console/tests)
libraries test their command-line implementations.
