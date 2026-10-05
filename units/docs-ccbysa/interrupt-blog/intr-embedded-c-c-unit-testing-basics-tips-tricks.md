---
id: "intr-embedded-c-c-unit-testing-basics-tips-tricks"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Tips & Tricks"
summary: "Most unit test frameworks will generate separate binaries for each .cpp unit test file written so that you can load them in a debugger (lldb or gdb)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#tips-tricks"
license: "CC-BY-SA-4.0"
mode: "V"
---

{:.no_toc}

### Debugging a Unit Test

Most unit test frameworks will generate separate binaries for each `.cpp` unit
test file written so that you can load them in a debugger (lldb or gdb).

```
$ lldb build/sum/sum_tests
(lldb) target create "build/sum/sum_tests"
Current executable set to 'build/sum/sum_tests' (x86_64).
(lldb) run
Process 257894 launched: 'build/sum/sum_tests' (x86_64)
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 0 ms)

Process 257894 exited with status = 0 (0x00000000)
```

{:.no_toc}

### Code Coverage

One of the wonderful parts about unit testing is that you can generate a code
coverage report. This shows which paths were covered in a given set of unit
tests, so you can be sure that the piece of code was tested in some capacity.
Note that code coverage doesn't measure the different behaviors a code path
**could take**, but only that a particular code path **was taken**.

To generate a coverage report for our minimal example, let's first install `lcov`.

```
# macOS
$ brew install lcov

# Linux
$ sudo apt install lcov
```

Next, we'll run our unit tests while testing for coverage.

```
$ make lcov
make -f minimal/tests/makefiles/Makefile_sum.mk
make[1]: Entering directory 'minimal/tests'
Running build/sum/sum_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 0 ms)

make[1]: Leaving directory 'minimal/tests'
lcov --base-directory . --directory . -c -o build/lcov.info --exclude "*cpputest/*" --exclude "*tests/*"

...

Overall coverage rate:
  lines......: 100.0% (2 of 2 lines)
    functions..: 100.0% (1 of 1 function)
```

You can see the very end reports a simple coverage report in the terminal, but a
more detailed report can be found in the HTML website that was generated. We can
open it from the terminal:

```
# macOS
$ open build/test_coverage/index.html

# Linux
$ firefox build/test_coverage/index.html
```

Below is the coverage report for our minimal example. It's quite basic because there isn't much code being tested. 



Below is a more realistic report from the Memfault Public SDK[^5].



{:.no_toc}

### Address Sanitizing

To raise use-after-free and buffer overflow errors in unit tests, use the
compiler option `-fsanitize=address` when compiling unit tests.

You can find out more about the Address Sanitizer by reading the
documentation[^6].
