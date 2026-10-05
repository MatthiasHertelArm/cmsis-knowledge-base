---
id: "intr-c-structure-padding-initialization-the-current-state"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: The Current State"
summary: "Let's consider the following 4 zero-initialization strategies for this structure:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#the-current-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's consider the following 4 zero-initialization strategies for this
structure:

```c
struct foo {
  uint32_t i;
  uint8_t b;
};
```

1. `memset` to zeros:

   ```c
   struct foo a;
   memset(&a, 0, sizeof(a));
   ```

2. individually set all members to 0:

   ```c
   struct foo a = {
     .i = 0,
     .b = 0,
   };
   ```

3. use `{ 0 }` zero-initializer

   ```c
   struct foo a = { 0 };
   ```

4. use `{}` GCC extension zero-initializer (_Note: this is quite
   poorly/non-documented for C - it IS valid C++ - but works in C on both GCC
   and clang. See [here](https://stackoverflow.com/a/54409687) and
   [here](https://gcc.gnu.org/legacy-ml/gcc/2019-07/msg00065.html)_)

   ```c
   struct foo a = {};
   ```

It turns out, the results for these vary between GCC and Clang and optimization
levels.

For the record, I'm testing using these compiler versions, on Ubuntu Linux 21.10
on 2022-02-28:

```bash
❯ clang --version
Ubuntu clang version 13.0.0-2

❯ gcc --version
gcc (Ubuntu 11.2.0-7ubuntu2) 11.2.0

# specific package versions:
❯ apt list clang gcc
Listing... Done
clang/impish,now 1:13.0-53~exp1 amd64 [installed]
gcc/impish,now 4:11.2.0-1ubuntu1 amd64 [installed]
```

Padding values under each strategy, optimization level, and compiler (_warning
boring tables below!_):

### Strategy 1, `memset`

| Strategy    | Optimization Level | Clang 13 | GCC 11 |
| ----------- | ------------------ | -------- | ------ |
| 1, `memset` | `0`                | zero     | zero   |
| 1, `memset` | `1`                | zero     | zero   |
| 1, `memset` | `2`                | zero     | zero   |
| 1, `memset` | `3`                | zero     | zero   |
| 1, `memset` | `s`                | zero     | zero   |

### Strategy 2, explicitly setting each struct member

| Strategy    | Optimization Level | Clang 13  | GCC 11    |
| ----------- | ------------------ | --------- | --------- |
| 2, explicit | `0`                | zero      | **unset** |
| 2, explicit | `1`                | **unset** | **unset** |
| 2, explicit | `2`                | zero      | **unset** |
| 2, explicit | `3`                | zero      | **unset** |
| 2, explicit | `s`                | **unset** | **unset** |

### Strategy 3, `{ 0 }`

| Strategy   | Optimization Level | Clang 13  | GCC 11 |
| ---------- | ------------------ | --------- | ------ |
| 3, `{ 0 }` | `0`                | zero      | zero   |
| 3, `{ 0 }` | `1`                | **unset** | zero   |
| 3, `{ 0 }` | `2`                | zero      | zero   |
| 3, `{ 0 }` | `3`                | zero      | zero   |
| 3, `{ 0 }` | `s`                | zero      | zero   |

### Strategy 4, `{ }` GCC extension

| Strategy | Optimization Level | Clang 13  | GCC 11 |
| -------- | ------------------ | --------- | ------ |
| 4, `{ }` | `0`                | zero      | zero   |
| 4, `{ }` | `1`                | **unset** | zero   |
| 4, `{ }` | `2`                | zero      | zero   |
| 4, `{ }` | `3`                | zero      | zero   |
| 4, `{ }` | `s`                | **unset** | zero   |

The main point is that it's not particularly consistent across compilers and
optimization levels 😱!

> You can find the example application used to generate the above data here on
> [Github](https://github.com/memfault/interrupt/tree/master/example/c-struct-padding-initialization/).

> I've also uploaded it to the wonderful Compiler Explorer if you want to take a
> look and quickly play around: <https://godbolt.org/z/b985G4ejT>
