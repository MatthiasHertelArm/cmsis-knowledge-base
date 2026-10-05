---
id: "intr-defensive-programming-friend-or-fo-defensive-programming"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?: Defensive Programming"
summary: "Defensive programming is the practice of writing software to enable continuous operation after and while experiencing unplanned issues. A simple example is checking for NULL after calling malloc(), and ensuring that the program gracefully handles the case."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming#defensive-programming"
license: "CC-BY-SA-4.0"
mode: "V"
---

Defensive programming is the practice of writing software to enable continuous
operation after and while experiencing unplanned issues. A simple example is
checking for `NULL` after calling `malloc()`, and ensuring that the program
gracefully handles the case.

```c
void do_something(void) {
  uint8_t *buf = malloc(128);
  if (buf == NULL) {
    // handle this gracefully!
  }
}
```

Defensive programming sounds nice, and it is nice! The firmware that we write
should never catastrophically fail due to unforeseen circumstances if we don't
want it to.

Defensive programming really shines when interacting directly with hardware,
proprietary libraries, and external inputs that we don't have direct control
over. Hardware may have glitches or behave differently in various environments,
heavyweight libraries often are riddled with bugs, and the outside world will
send whatever it wants over communication protocols.

As with most things, defensive programming can be abused and the benefits become
outweighed by the negatives. If many modules are layered on top of one another,
each using defensive programming techniques, bugs can and will be created, lost,
and/or obscured.

### Problems with Defensive Programming

The key to defensive programming is to use it at the exterior interfaces of your
firmware. There should be a thin but sturdy wall of defensive programming
between the outside world and hardware, and then the majority of your code
inside the walls should be more aggressively checking for errors and yelling at
developers when they do the wrong thing.



  
  If code paths originate from or pass through the red zones, then defensive programming is a good approach.


For instance, let's assume we have an internal function,
`hash32_djb2(const char *str, size_t len)`, which takes in the string we should
hash and a length. This function is **never** going to be directly used by any
external consumers, which leaves only internal developers.

By having a check and return value like the following:

```c
uint32_t hash32_djb2(const char *str, int len)
{
  if (str == NULL) {
    // Invalid argument
    return 0;
  }
  ...
```

You are only shooting yourself and your fellow developers in the feet. If any
developer passes a `NULL` string to this function, it will return `0` and be
stored as a valid hash!

The `NULL` string argument is likely the developer's own bug, and they should
immediately become aware of the bug, or else it might slip into production.

This practice of writing code to aggressively surface errors is what is known as
"Offensive" Programming.
([Merriam Webster definition #1](https://www.merriam-webster.com/dictionary/offensive),
"making attack")
