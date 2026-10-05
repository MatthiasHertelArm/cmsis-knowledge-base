---
id: "intr-embedded-c-c-unit-testing-basics-final-thoughts"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Final Thoughts"
summary: "Unit testing was something that a co-worker of mine suggested to me 4 years ago when writing a complicated raw flash storage to filesystem migration for our firmware. After having spent a month doing cycling between the 1."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#final-thoughts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unit testing was something that a co-worker of mine suggested to me 4 years ago
when writing a complicated raw flash storage to filesystem migration for our
firmware. After having spent a month doing cycling between the **1.** Write
Code, **2.** Setup hardware, **3.** Test, which took **10 minutes** each
iteration, I invested 2 days writing a unit test and was able to shrink the test
cycle down to **2 seconds**. The rest of the project took two days.

Everyone has a moment where unit testing finally clicks for them and this was
mine.

I hope this post has been useful and that it has inspired you to consider
writing a unit test for your next new embedded software module.

> Want to keep reading? Check out our next post about unit testing, [Unit
> Testing with Mocks](https://interrupt.memfault.com/blog/unit-test-mocking).

You can find the examples shown in this post
[here](https://github.com/memfault/interrupt/tree/master/example/unit-testing).



{:.no_toc}
