---
id: "intr-embedded-open-source-summit-2024-r-from-c-to-rust-bringing-rust-abstraction"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: From C to Rust: Bringing Rust abstractions to the Embedded Linux"
summary: "Fabien Parent, of Linaro, is a well known name of the community. I was curious to hear him talk about Rust. The talk did not disappoint."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#from-c-to-rust-bringing-rust-abstractions-to-the-embedded-linux"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=hmQr4fq6sH0&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=58&pp=iAQB)
- Recommended by: Thomas

Fabien Parent, of Linaro, is a well known name of the community. I was curious
to hear him talk about Rust. The talk did not disappoint.

Fabien starts with a good overview of what is available for Rust in the Kernel.
He explains that Rust is limited to the device drivers because “core” components
of the Kernel needs to remain compatible with all architectures and some of
these architectures are not supported by the LLVM backend used by rustc (LLVM is shiny and new but [the kernel built with gcc still supports more architectures](https://chat.openai.com/share/b275dd72-bc8b-4faf-8a10-6fd368210896)).

A big challenge for Rust kernel developers today is that although tooling was
merged, there is very little in terms of abstraction. So to develop a new device
driver in Rust, you first need to write some abstractions. Many people have
started working on this but this work is often left unmerged because code cannot
be merged in the kernel unless it’s actually used somewhere. Any serious device
driver will require many abstractions, making for some big patch requests that
are complicated, hard to review (especially by non-Rust developers) and hard to
merge.

At this point, you probably share a bit of my disappointment. The best lesson of
the talk was Fabian’s optimistic approach to all of this. Instead of giving up,
he put some thoughts into the best way to move everything forward. His strategy
is to find some small drivers (that do not exist today because just replacing C
code with Rust code is also not acceptable for merge) that require only a few
abstractions and to use them to progressively introduce Rust abstractions in the
Kernel.

I loved hearing this positive take on all of this. A good reminder that you can
sit and complain about the state of things or take it as a challenge ;)
