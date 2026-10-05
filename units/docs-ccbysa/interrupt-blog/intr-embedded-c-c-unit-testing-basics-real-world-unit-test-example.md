---
id: "intr-embedded-c-c-unit-testing-basics-real-world-unit-test-example"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example"
summary: "Let's come up with a more complicated example which more accurately mirrors what a developer on a firmware team would experience."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#real-world-unit-test-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's come up with a more complicated example which more accurately mirrors what
a developer on a firmware team would experience. This example uses a stub, a
fake, `setup()` and `teardown()` functions, and it also compiles `littlefs` in
its entirety, a filesystem by ARM designed for microcontrollers[^4].

{:.no_toc}
