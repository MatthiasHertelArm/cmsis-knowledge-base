---
id: "intr-embedded-c-c-unit-testing-basics-framework-less-unit-tests"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Framework-less Unit Tests"
summary: "It is very common to initially write unit tests using one-off .c files. Below is an example of a test that is commonly found in firmware projects or written by the author of a piece of firmware code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#framework-less-unit-tests"
license: "CC-BY-SA-4.0"
mode: "V"
---

It is very common to initially write unit tests using one-off `.c` files. Below
is an example of a test that is commonly found in firmware projects or written
by the author of a piece of firmware code.

```c
#include <assert.h>

// In my_sum.c
int my_sum(int a, int b) {
  return a + b;
}

// In test_my_sum.c
int main(int argc, char *argv[]) {
  assert(2 == my_sum(1, 1));
  assert(-2 == my_sum(-1, -1));
  assert(0 == my_sum(0, 0));
  // ...
  return(0);
}
```

This works for a short period of time, but as a firmware project grows in
complexity, lines of code, and number of developers, there are a few things that
become a requirement.

- Running Unit Tests in Continuous Integration
- Reporting results of the tests, e.g. number of tests failed, runtime duration,
  etc.
- Reporting code coverage to give insight into how much of a codebase is unit
  tested[^2].
- Ability for a developer to create a new unit test easily and quickly.

The most scalable way to write unit tests in C is using a unit testing
framework, such as:

- [CppUTest](https://cpputest.github.io/)
- [Unity](http://www.throwtheswitch.org/unity)
- [Google Test](https://github.com/google/googletest)

Even though CppUTest and Google Test are written in C++, they can be used to
test C source code, as long as the C header files includes are wrapped with
`extern "C"`.

```c++
extern "C" {
  #include "my_sum.h"
}
```
