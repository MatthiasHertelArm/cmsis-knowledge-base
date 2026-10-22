---
id: "unity-unity-assertions-reference-advanced-asserting-details-on-tricky-ass"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: Advanced Asserting: Details On Tricky Assertions"
summary: "This section helps you understand how to deal with some of the trickier assertion situations you may run into. It will give you a glimpse into some of the under-the-hood details of Unity’s assertion mechanisms."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityAssertionsReference.md#advanced-asserting-details-on-tricky-assertions"
license: "MIT"
mode: "V"
---

This section helps you understand how to deal with some of the trickier
assertion situations you may run into. It will give you a glimpse into some of
the under-the-hood details of Unity’s assertion mechanisms. If you’re one of
those people who likes to know what is going on in the background, read on. If
not, feel free to ignore the rest of this document until you need it.

### How do the EQUAL assertions work for FLOAT and DOUBLE?

As you may know, directly checking for equality between a pair of floats or a
pair of doubles is sloppy at best and an outright no-no at worst. Floating point
values can often be represented in multiple ways, particularly after a series of
operations on a value. Initializing a variable to the value of 2.0 is likely to
result in a floating point representation of 2 x 20,but a series of
mathematical operations might result in a representation of 8 x 2-2
that also evaluates to a value of 2. At some point repeated operations cause
equality checks to fail.

So Unity doesn’t do direct floating point comparisons for equality. Instead, it
checks if two floating point values are “really close.” If you leave Unity
running with defaults, “really close” means “within a significant bit or two.”
Under the hood, `TEST_ASSERT_EQUAL_FLOAT` is really `TEST_ASSERT_FLOAT_WITHIN`
with the `delta` parameter calculated on the fly. For single precision, delta is
the expected value multiplied by 0.00001, producing a very small proportional
range around the expected value.

If you are expecting a value of 20,000.0 the delta is calculated to be 0.2. So
any value between 19,999.8 and 20,000.2 will satisfy the equality check. This
works out to be roughly a single bit of range for a single-precision number, and
that’s just about as tight a tolerance as you can reasonably get from a floating
point value.

So what happens when it’s zero? Zero - even more than other floating point
values - can be represented many different ways. It doesn’t matter if you have
0x20 or 0x263. It’s still zero, right? Luckily, if you subtract these 
values from each other, they will always produce a difference of zero, which 
will still fall between 0 plus or minus a delta of 0. So it still works!

Double precision floating point numbers use a much smaller multiplier, again
approximating a single bit of error.

If you don’t like these ranges and you want to make your floating point equality
assertions less strict, you can change these multipliers to whatever you like by
defining UNITY_FLOAT_PRECISION and UNITY_DOUBLE_PRECISION. See Unity
documentation for more.

### How do we deal with targets with non-standard int sizes?

It’s “fun” that C is a standard where something as fundamental as an integer
varies by target. According to the C standard, an `int` is to be the target’s
natural register size, and it should be at least 16-bits and a multiple of a
byte. It also guarantees an order of sizes:

```C
char <= short <= int <= long <= long long
```

Most often, `int` is 32-bits. In many cases in the embedded world, `int` is
16-bits. There are rare microcontrollers out there that have 24-bit integers,
and this remains perfectly standard C.

To make things even more interesting, there are compilers and targets out there
that have a hard choice to make. What if their natural register size is 10-bits
or 12-bits? Clearly they can’t fulfill _both_ the requirement to be at least
16-bits AND the requirement to match the natural register size. In these
situations, they often choose the natural register size, leaving us with
something like this:

```C
char (8 bit) <= short (12 bit) <= int (12 bit) <= long (16 bit)
```

Um… yikes. It’s obviously breaking a rule or two… but they had to break SOME
rules, so they made a choice.

When the C99 standard rolled around, it introduced alternate standard-size types.
It also introduced macros for pulling in MIN/MAX values for your integer types.
It’s glorious! Unfortunately, many embedded compilers can’t be relied upon to
use the C99 types (Sometimes because they have weird register sizes as described
above. Sometimes because they don’t feel like it?).

A goal of Unity from the beginning was to support every combination of
microcontroller or microprocessor and C compiler. Over time, we’ve gotten really
close to this. There are a few tricks that you should be aware of, though, if
you’re going to do this effectively on some of these more idiosyncratic targets.

First, when setting up Unity for a new target, you’re going to want to pay
special attention to the macros for automatically detecting types
(where available) or manually configuring them yourself. You can get information
on both of these in Unity’s documentation.

What about the times where you suddenly need to deal with something odd, like a
24-bit `int`? The simplest solution is to use the next size up. If you have a
24-bit `int`, configure Unity to use 32-bit integers. If you have a 12-bit
`int`, configure Unity to use 16 bits. There are two ways this is going to
affect you:

1. When Unity displays errors for you, it’s going to pad the upper unused bits
   with zeros.
2. You’re going to have to be careful of assertions that perform signed
   operations, particularly `TEST_ASSERT_INT_WITHIN`. Such assertions might wrap
   your `int` in the wrong place, and you could experience false failures. You can
   always back down to a simple `TEST_ASSERT` and do the operations yourself.

*Find The Latest of This And More at [ThrowTheSwitch.org][]*

[assert() macro]: http://en.wikipedia.org/wiki/Assert.h
[ThrowTheSwitch.org]: https://throwtheswitch.org
