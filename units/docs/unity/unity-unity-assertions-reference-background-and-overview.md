---
id: "unity-unity-assertions-reference-background-and-overview"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: Background and Overview"
summary: "One way to think of Unity is simply as a rich collection of assertions you can use to establish whether your source code behaves the way you think it does."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#background-and-overview"
license: "MIT"
mode: "V"
---

### Super Condensed Version

- An assertion establishes truth (i.e. boolean True) for a single condition.
Upon boolean False, an assertion stops execution and reports the failure.
- Unity is mainly a rich collection of assertions and the support to gather up
and easily execute those assertions.
- The structure of Unity allows you to easily separate test assertions from
source code in, well, test code.
- Unity’s assertions:
  - Come in many, many flavors to handle different C types and assertion cases.
  - Use context to provide detailed and helpful failure messages.
  - Document types, expected values, and basic behavior in your source code for
free.

### Unity Is Several Things But Mainly It’s Assertions

One way to think of Unity is simply as a rich collection of assertions you can
use to establish whether your source code behaves the way you think it does.
Unity provides a framework to easily organize and execute those assertions in
test code separate from your source code.

### What’s an Assertion?

At their core, assertions are an establishment of truth - boolean truth. Was this
thing equal to that thing? Does that code doohickey have such-and-such property
or not? You get the idea. Assertions are executable code. Static analysis is a 
valuable approach to improving code quality, but it is not executing your code
in the way an assertion can. A failing assertion stops execution and reports an 
error through some appropriate I/O channel (e.g. stdout, GUI, output file, 
blinky light).

Fundamentally, for dynamic verification all you need is a single assertion
mechanism. In fact, that’s what the [assert() macro][] in C’s standard library
is for. So why not just use it? Well, we can do far better in the reporting
department. C’s `assert()` is pretty dumb as-is and is particularly poor for
handling common data types like arrays, structs, etc. And, without some other
support, it’s far too tempting to litter source code with C’s `assert()`’s. It’s
generally much cleaner, manageable, and more useful to separate test and source
code in the way Unity facilitates.

### Unity’s Assertions: Helpful Messages _and_ Free Source Code Documentation

Asserting a simple truth condition is valuable, but using the context of the
assertion is even more valuable. For instance, if you know you’re comparing bit
flags and not just integers, then why not use that context to give explicit,
readable, bit-level feedback when an assertion fails?

That’s what Unity’s collection of assertions do - capture context to give you
helpful, meaningful assertion failure messages. In fact, the assertions
themselves also serve as executable documentation about types and values in your
source code. So long as your tests remain current with your source and all those
tests pass, you have a detailed, up-to-date view of the intent and mechanisms in
your source code. And due to a wondrous mystery, well-tested code usually tends
to be well designed code.
