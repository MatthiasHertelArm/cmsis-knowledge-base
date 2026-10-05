---
id: "intr-embedded-c-c-unit-testing-basics-setting-up-cpputest"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Setting Up CppUTest"
summary: "CppUTest is one of many C/C++ unit test frameworks, and the reason it was chosen is because of my familiarity with it and that it doesn't have any dependencies other than Make."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#setting-up-cpputest"
license: "CC-BY-SA-4.0"
mode: "V"
---

CppUTest is one of many C/C++ unit test frameworks, and the reason it was chosen
is because of my familiarity with it and that it doesn't have any dependencies
other than Make.

No matter what anyone says, the framework you use **does not** matter. As long
as the framework has the minimum features listed
[above](#framework-less-unit-tests), it is as good as any.

{:.no_toc}

### Initial Setup

We first need to install a pre-compiled version of CppUTest so we can easily run
tests without needing to compile the binary ourselves from source before every
test run. The easiest way to do this is to use your system's package manager.

On macOS, CppUTest can be installed using `brew`:

```
$ brew install cpputest
```

On Ubuntu, it can be installed using `apt`:

```
$ sudo apt install cpputest
```

{:.no_toc}

### Project CppUTest Harness

Since it is a decent amount of boilerplate due to the CppUTest harness setup
required, this example will start with a clone of the example repository and
then go over the components within it, briefly covering the CppUTest Makefiles.

Feel free to use the code in any way you like, and even copy it into your
project. It should build quite easily once some paths are patched up.

```
$ git clone https://github.com/memfault/interrupt.git
$ cd interrput/examples/unit-testing/minimal/tests

# macOS
$ make

# Ubuntu
$ make CPPUTEST_HOME=/usr TARGET_PLATFORM=x86_64-linux-gnu

compiling test_my_sum.cpp
compiling AllTests.cpp
...
Linking build/sum/sum_tests
Running build/sum/sum_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 1 ms)
```

To set CPPUTEST_HOME and TARGET_PLATFORM for your platform, edit the first few
lines of `MarkefileWorkerOverrides.mk`.

```
CPPUTEST_HOME ?= /usr/local/Cellar/cpputest/3.8
TARGET_PLATFORM ?=
```
