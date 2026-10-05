---
id: "intr-automatically-format-and-lint-code-what-is-formatting-linting"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: What is formatting/linting?"
summary: "Imagine you want to transform the following snippet:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#what-is-formatting-linting"
license: "CC-BY-SA-4.0"
mode: "V"
---

Imagine you want to transform the following snippet:

```c
int  main (   int argc, char  ** argv)
   {
printf("hello!\n");
		return  0;}
```

into this, with the push of a button (or even automatically on save!):

```c
int main(int argc, char **argv) {
  printf("hello!\n");
  return 0;
}
```

That's what **formatting** tools can do. For the C language, some popular
formatters are:

- [clang-format](https://releases.llvm.org/15.0.0/tools/clang/docs/ClangFormat.html)
- [uncrustify](http://uncrustify.sourceforge.net/)
- [GNU Indent](https://www.gnu.org/software/indent/)
- [Astyle](http://astyle.sourceforge.net/)

**Linting** is a general term for various static analysis/style checking tools,
generally lighter (in terms of setup and computation) compared to full static
analysis. Typically these tools are designed to detect, for example:

- some simple bug categories (similar to extended compiler warnings)
- possible stylistic errors
  ([an example](https://releases.llvm.org/15.0.0/tools/clang/tools/extra/docs/clang-tidy/checks/bugprone/suspicious-missing-comma.html))
- security-related checks (eg. using `sprintf` instead of `snprintf`)

These types of tools are _very_ common in other software engineering domains
(for example, [ESLint](https://eslint.org/) for javascript), and many popular
projects use automated formatters/linters (Linux, Chromium for example).
