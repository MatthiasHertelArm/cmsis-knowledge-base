---
id: "intr-embedded-c-c-unit-testing-with-moc-mocks-in-detail"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Mocks in Detail"
summary: "A mock is a simulated function or module that mimics the behavior of a real implementation but is fully controlled by the unit test itself."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#mocks-in-detail"
license: "CC-BY-SA-4.0"
mode: "V"
---

A mock is a simulated function or module that mimics the behavior of a real
implementation but is fully controlled by the unit test itself. The programmer
can validate how many times a mock is called and verify the value of all
arguments passed into the mock. The programmer also dictates what actions the
mock takes, from calling other fakes or stubs, to returning particular return
values, or modifying certain output parameters.

Mocks are especially useful when testing failure paths that would likely never
happen, or be disastrous if they did happen. For example, a mock would be a good
choice if you are writing a vehicle software module that behaves differently if
the airbags have triggered or not. You _really_ would not want to have to test
this in QA every time you make a change.

Since mocks generally do not include any other dependencies, mocks are also the
best tool in the toolbox for isolating and testing every facet of the module
under test (strive for that 100% code coverage).

However, this strength is also a weakness. Using mocks everywhere becomes
cumbersome and verbose, given that every call, parameter, and return value has
to be explicitly defined or ignored. Everything in testing is a trade-off, and
choosing when to use mocks is no exception.

### When to Use Mocks

You should considering using a mock:

- When you only want to include single `.c` or `.cpp` source file under test.
- When you you need something more than a **stub**, but don't want to go through
  the trouble of modeling the subsystem behavior perfectly in a **fake**.
- When you have complex retry logic in a system and want to trigger every retry
  path.
- When you find yourself manually pre-programming return values while using a
  stub or a fake. I did this many times before finally understanding how to use
  a mock. I was doing something
  [like this](https://gist.github.com/tyhoff/54efe99dbcd3cb22fa244159dd9bc42c#file-test_kv_store_protocol_handlers-cpp-L22-L33).

Although it's not a binary decision or suggestion, I find that to reach 100%
code coverage on my projects or in particular files, I commonly have to use
mocks. 100% code coverage means that every branch in the codebase was taken at
least once, which in turn means that every one of the `(buffer == NULL)`
branches needs to be taken.

With a **stub**, I can't change the return values dynamically. With a **fake**,
the implementation should be functionally accurate to the real module, so it
would usually never fail.

That leaves me with a **mock**!

Here are some common use cases for mocks that we'll cover in this post:

- A malloc implementation that can be pre-programmed with return values (return
  real buffers vs NULL).
- A mock flash driver that returns error codes and forces different paths in a
  higher level module.
- A Bluetooth socket implementation that is fed artfully crafted packed data to
  instrument protocols.
