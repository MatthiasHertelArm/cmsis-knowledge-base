---
id: "intr-embedded-open-source-summit-2024-r-rusty-swapping-rewriting-a-zswap-backend"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Rusty swapping: Rewriting a zswap backend in Rust"
summary: "Vitaly (Konsulko) shared his experience writing a kernel driver in Rust. After listening to Fabian talk the day before, I was curious to hear another take on Rust in the kernel."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#rusty-swapping-rewriting-a-zswap-backend-in-rust"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=WoXviWYsaOM&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=42&pp=iAQB)
- Recommended by: Thomas

Vitaly (Konsulko) shared his experience writing a kernel driver in Rust. After
listening to Fabian talk the day before, I was curious to hear another take on
Rust in the kernel. Vitaly shared his experience writing a new zswap backend in
the kernel. For fun, he wrote it both in C and Rust and compared the results.

His conclusions are similar to Fabian’s: Rust in the kernel is hardly ready for
prime time today. The Rust learning curve is a challenge, getting the tools set
up correctly seems like a major pain, collaborating with existing kernel C API
requires a lot of unsafe code which reduces the “memory safety” advantage of
Rust. And once again, figuring out the way to get Rust code merged seems to be
the biggest issue. One encouraging point was a slight improvement in performance
and size with the Rust version.
