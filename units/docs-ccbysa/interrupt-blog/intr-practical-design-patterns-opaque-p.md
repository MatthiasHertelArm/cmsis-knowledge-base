---
id: "intr-practical-design-patterns-opaque-p"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C"
summary: "I've written a lot of C++ in my career, but I still prefer to design in C for most embedded projects (\"why\" is the subject of a much longer, rant-filled post)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers"
license: "CC-BY-SA-4.0"
mode: "V"
---

I've written a lot of C++ in my career, but I still prefer to design in
C for most embedded projects ("why" is the subject of a much longer, rant-filled post).
I'm not a big proponent of OOP in general,
but I do think having an "instance" of something which contains stateful data is a generally
useful thing for embedded software. For example, you may want to have several
instances of a ring buffer (aka circular FIFO queue) on your system.
Each instance contains stateful data,
like the current position of read and write pointers. What's the best way
to model this in C?



Objects are not a native concept in C, but you can achieve something
resembling objects by using a design pattern known as the "opaque pointer".
This post will show you what the pattern is, explain some of the finer
details, and provide guidance on when you should and shouldn't use it.



The opaque pointer is one of the most useful and frequently-encountered design
patterns in C.
Even if you are a die-hard C++ proponent (or *gasp* Rust!), the reality is
that there are, and will continue to be, a lot of embedded projects out there
written in C. And you may need to contribute to one of them.
