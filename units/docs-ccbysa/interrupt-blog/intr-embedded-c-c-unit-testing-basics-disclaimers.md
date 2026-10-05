---
id: "intr-embedded-c-c-unit-testing-basics-disclaimers"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Disclaimers"
summary: "Unit tests in the embedded space is a controversial topics, so I want to clear set up expectations up front."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#disclaimers"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unit tests in the embedded space is a controversial topics, so I want to clear
set up expectations up front.

1. This post covers how to test embedded **software**. Testing firmware drivers
   and hardware is _very_ different and time is best spent writing functional
   and integration tests that run on target to validate hardware components. As
   soon as drivers are written and stable, switch to the unit test approaches
   provided in this post.
2. I do not suggest rewriting all of your code to accommodate unit tests, or
   writing tests for the current code base, but I heavily suggest writing unit
   tests for most **new** modules and heavily suggesting them in code reviews.
3. Integration tests and on-target tests have their place. This infrastructure
   is a **huge** time and money investment, and the tests run in minutes and
   hours. Keep these to a minimum at first to ensure hardware stability, and
   leave software stability to unit tests. If time allows, then build these
   types of tests.
