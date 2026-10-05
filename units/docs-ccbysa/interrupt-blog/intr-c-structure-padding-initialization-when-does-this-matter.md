---
id: "intr-c-structure-padding-initialization-when-does-this-matter"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: When does this matter?"
summary: "Alright! Now that we've got a description of struct padding, let's describe some cases where it makes a difference."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#when-does-this-matter"
license: "CC-BY-SA-4.0"
mode: "V"
---

Alright! Now that we've got a description of struct padding, let's describe some
cases where it makes a difference.

### Comparing padded structs

It's tempting to compare structs by using `memcmp`, as in the following:

```c
struct foo {
  uint32_t i;
  uint8_t b;
};

// Check 2 foos for equality
bool foo_are_equal(struct foo a, struct foo b) {
  const int result = memcmp(&a, &b, sizeof(a));
  return result == 0;
}

// Check if a foo matches a reference
bool foo_is_reference(struct foo a) {
  static const struct foo reference = {
    .i = 1234,
    .b = 56,
  };
  return foo_are_equal(a, reference);
}
```

HOWEVER, this may give incorrect results if the padding is not accounted for!

### Serializing structs outside the application

For example, writing a C struct into non-volatile storage:

```c
struct device_config {
  uint8_t device_config_version;
  uint64_t manufacture_date;
  uint8_t hardware_version;
  uint8_t serial_number[16];
};
```

If that data needs to be read by another piece of software, or if it potentially
will be migrated to a different struct layout (eg, a new field is added), it
might be prudent to pack the struct (either by hand or with
`__attribute__((packed))`), to simplify reasoning about the data structure.

### Security issues

The values in the padding space can potentially leak sensitive information if
the data structures are crossing trust boundaries. Specifically, the padding
space can contain data from objects that were previously allocated on the stack
(for example, an encryption key used to perform some cryptographic operation).

See the following articles for information on that subject:

- <https://lwn.net/Articles/417989/>
- <https://wiki.sei.cmu.edu/confluence/display/c/DCL39-C.+Avoid+information+leakage+when+passing+a+structure+across+a+trust+boundary>

### When it doesn't matter

If the structure is only ever accessed on a per-member basis, the padding
probably won't cause problems:

```c
struct foo {
  uint32_t i;
  uint8_t b;
};

// Check 2 foos for equality
bool foo_are_equal(struct foo a, struct foo b) {
  return (a.i == b.i) && (a.b == b.b);
}
```

Specifically, if the structure is only ever _internally_ used in the application
(never crosses a library or trust boundary, and is never serialized out to
external storage or over a communications interface), issues related to padding
may not be a problem.

Note that other languages may have different layout implementations for
composite types (see
[Rust](https://doc.rust-lang.org/1.59.0/reference/types/struct.html)), which may
complicate matters when moving raw C structs between different pieces of
software.
