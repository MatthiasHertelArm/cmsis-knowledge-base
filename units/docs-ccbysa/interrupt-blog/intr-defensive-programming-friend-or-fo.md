---
id: "intr-defensive-programming-friend-or-fo"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?"
summary: "One of the worst things about embedded development (especially in C) is receiving a return value of -1 or unknown_error from a function, with no other information about why the failure took place."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the worst things about embedded development (especially in C) is
receiving a return value of `-1` or `unknown_error` from a function, with no
other information about why the failure took place. It provides no information
about where the error bubbled up from!

We've all been here as embedded developers, bringing up new boards, drivers,
modules, and applications, wondering why and how we got into this mess. Root
causing these issues is like peeling an onion: each layer we dig through while
debugging, we smile a bit less and a few more tears are shed. These sorts of
issues are often a result of developer error, either calling functions out of
order, at the wrong time, or with incorrect arguments. They could also be
because the system was in a bad state, such as out of memory or deadlocked.

The firmware _knows_ there is an issue, and it likely knows _what the issue is_,
but yet it doesn't help solve the issue. The software was built with "Defensive
Programming" practices in mind, which allows for the firmware to keep running
even when incorrect behavior occurs.

Usually, I would prefer that the firmware crash, print a useful error, and guide
me exactly to where the issue is. This the guiding principle of "Offensive
Programming", which goes one step further than "Defensive Programming".



In this article, we'll dive into what defensive and offensive programming are,
where defensive programming falls short, how developers should think about using
them within embedded systems, and how the techniques of offensive programming
can surface bugs and help developers root cause them immediately at runtime.



By taking defensive and offensive programming to the extreme, you'll be able to
track down those 1 in 1,000-hour bugs, efficiently root cause them, and keep
your end-users happy. And, as a bonus, keep your sanity.

> To learn more about offensive and defensive programming best practices and ask
> me questions live, register for our [webinar on February 24, 2022](https://hubs.la/Q013SXmN0).
