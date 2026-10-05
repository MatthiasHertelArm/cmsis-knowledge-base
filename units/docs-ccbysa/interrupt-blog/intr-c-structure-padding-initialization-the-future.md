---
id: "intr-c-structure-padding-initialization-the-future"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: The Future 🌞"
summary: "I gave this away right at the start of the article, but somewhat unusually for C, there is change coming on this topic!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#the-future"
license: "CC-BY-SA-4.0"
mode: "V"
---

I gave this away
[right at the start of the article](https://thephd.dev/ever-closer-c23-improvements#consistent-warningless-and-intuitive-initialization-with--),
but somewhat unusually for C, there is change coming on this topic!

The proposed change for C23 is that the `= {}` (functionally equivalent to
`= { 0 }` on modern compilers) _will also initialize padding bits to 0_ 😎.

You can see the gory details in the following links:

- <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2900.htm>
- <https://github.com/ThePhD/future_cxx/issues/37>

This seems like a nice update to the standard that doesn't appear to impact
backwards-compatibility and just makes things better!
