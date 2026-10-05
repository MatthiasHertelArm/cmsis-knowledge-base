---
id: "intr-embedded-c-c-unit-testing-with-moc-final-thoughts"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Final Thoughts"
summary: "I'm a believer that proper unit testing and integration testing can prevent many of the firmware bugs that devices experience in the field."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#final-thoughts"
license: "CC-BY-SA-4.0"
mode: "V"
---

I'm a believer that proper unit testing and integration testing can prevent many
of the firmware bugs that devices experience in the field. Except for the
firmware code that directly pokes in register values into hardware, all of the
software that goes into embedded software can and should be unit testing in some
fashion.

If you have interesting stories or creative ways that you've used unit tests or
integration tests to validate your embedded software, I'd love to hear about
them in the comments!

You can find the examples shown in this post
[here](https://github.com/memfault/interrupt/tree/master/example/unit-testing).



{:.no_toc}
