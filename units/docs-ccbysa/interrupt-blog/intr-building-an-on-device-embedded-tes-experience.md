---
id: "intr-building-an-on-device-embedded-tes-experience"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Experience"
summary: "It is pretty limited, but I am happy with the prototype. I am sure that I will refactor the library in the future, as there are prominent places to be improved but so far it behaves well enough."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#experience"
license: "CC-BY-SA-4.0"
mode: "V"
---

It is pretty limited, but I am happy with the prototype.
I am sure that I will refactor the library in the future, as there are prominent places to be improved but so far it behaves well enough.
It gives me a simple way to test and develop various ways to control the smart servomotor I am working on.
(Note: yes, this is one of the cases of "oh, I need to develop a library so I can do a project"...)

What could be developed more in the future and what pains me so far is:
 - it still does not report 100% of the possible errors on the side of the testing library - I have to go through the codebase and be more strict
 - it can't handle exceptions - while it should not rely on them, I think the library should respect them. That means in case the test throws an exception. It should not stop the reactor.
 - data exchange can be improved - what can be exchanged as of now is quite limited. I suppose I can provide more types to send and receive.
 - memory resource - uses internal emlabcpp mechanism that is underdeveloped, that definitely would benefit from more work.
 - more experience in CI - I think I am on a good track to having automatized tests in CI that are flashed to real hardware somewhere in the laboratory. That could show the limits of the library.
