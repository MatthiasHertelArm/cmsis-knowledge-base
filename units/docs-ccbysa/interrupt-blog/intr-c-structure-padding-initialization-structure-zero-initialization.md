---
id: "intr-c-structure-padding-initialization-structure-zero-initialization"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: Structure (Zero) Initialization"
summary: "Given the above, it seems convenient to zero-initialize structures before using them. With C99 or later, it is common to make use of the following patterns with \"designated initializers\" for structure initialization:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#structure-zero-initialization"
license: "CC-BY-SA-4.0"
mode: "V"
---

Given the above, it seems convenient to zero-initialize structures before using
them. With C99 or later, it is common to make use of the following patterns with
"designated initializers" for structure initialization:

```c
struct foo {
  uint32_t i;
  uint8_t b;
};

// Initialize members of 'a' to specific values. Members not specifically
// initialized will be initialized per the 'static storage duration'
// initialization rules (eg pointers go to NULL, integers go to 0, floats go to
// 0.0, etc)
struct foo a = {
  .i = 1,
  // .b will be set to 0
};

// Initialize 'b' to all zeros. This is a common idiom that specifies a '0'
// constant as the initial value for the first member of the structure, then
// relies on the above rule to initialize the rest of the structure.
struct foo b = { 0 };
```

This looks great! However, it's not obvious (from looking at those snippets)
what the value loaded into the padding region will be.

The unfortunate answer is: _it depends_

The C11 standard, chapter §6.2.6.1/6 says this:

> When a value is stored in an object of structure or union type, including in a
> member object, the bytes of the object representation that correspond to any
> padding bytes take unspecified values.

See also <https://stackoverflow.com/a/37642061>

Objects with '_static_ storage duration' (`static` keyword, or external linkage
(defined at the outermost scope in a compilation unit)), **padding bits will be
initialized to 0**!

Objects with '_automatic_ storage duration' (locally-scoped objects) have
**undefined behavior** when it comes to padding bit initialization!

This means that there is no constraint on what values are set to those bits when
the object is initialized.
