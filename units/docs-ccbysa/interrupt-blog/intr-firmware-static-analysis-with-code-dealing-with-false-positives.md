---
id: "intr-firmware-static-analysis-with-code-dealing-with-false-positives"
type: "concept"
domain: "debug"
title: "Firmware Static Analysis with CodeChecker: Dealing with false positives"
summary: "The first time you run CodeChecker, you will get a good number of false positives. Most of the time this will be due to a code path which cannot actually happen in your program but is plausible to the analyzer."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-19-static-analysis-with-codechecker.md"
doc_source: "https://interrupt.memfault.com/blog/static-analysis-with-codechecker#dealing-with-false-positives"
license: "CC-BY-SA-4.0"
mode: "V"
---

The first time you run CodeChecker, you will get a good number of false
positives. Most of the time this will be due to a code path which cannot
actually happen in your program but is plausible to the analyzer.

There are two ways to deal with false positives: adding `assert` calls to your
code, and annotating the offending code paths with CodeChecker specific
comments.

### Adding asserts

First, you should try adding `assert` calls to your code. Most projects have an
`assert` function which can be used to crash the program if an assumption is
violated (i.e. something that should never happen, happens). ChibiOS has such a
function, which it calls  `osalDbgAssert`.

By adding assertions to your code, you tell the static analyzer that those code
paths are invalid and it will not exercise them. For example, if you have:

```c
osalDbgAssert(p != NULL, "invalid null pointer")
*p = 123;

```

CodeChecker will thereafter assume `p` is non-null and won’t report the
following line as a null pointer dereference.

For CodeChecker to identify a function as being an assertion, you need to
annotate it with the `noreturn` attribute. This is done with the
`__attribute__` keyword:

```c
void foo(void) __attribute__((noreturn));
```

### CodeChecker annotations

If all else fails, you can add comments to tell CodeChecker to ignore an issue.
This is done by adding `codechecker_suppress` to your comment. For example:

```c
void test() {
  int x;
  // codechecker_suppress [all] this is a false positive
  x = 1;
}
```

The following code would emit a “dead store” error without the comment. The
syntax of the comment is as follow:

```
// codechecker_suppress [<checkers>] <note>
```

Where `checkers` is the list of checkers to disable (`all` for all checkers),
and `note` is a comment or note to explain why you disabled it.

While CodeChecker’s database can be used to track false positive, it is
recommended to use comments and asserts as well so you do not lose all that
state in the event the database is lost or reset.
