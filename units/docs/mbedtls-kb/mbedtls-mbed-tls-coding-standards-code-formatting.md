---
id: "mbedtls-mbed-tls-coding-standards-code-formatting"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Code Formatting"
summary: "In order to maintain a consistent coding style, the C code in Mbed TLS is formatted with Uncrustify. The reference version of Uncrustify is 0.75.1; older or newer versions are not suitable because they give different results."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/mbedtls-coding-standards.md#code-formatting"
license: "Apache-2.0"
mode: "V"
---

### Enforcement with uncrustify

In order to maintain a consistent coding style, the C code in Mbed TLS is formatted with [Uncrustify](https://github.com/uncrustify/uncrustify). The reference version of Uncrustify is 0.75.1; older or newer versions are not suitable because they give different results. See the [“Installing uncrustify”](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/uncrustify.md#installing-uncrustify) article for some tips.

#### Code style check script

A test on the continuous integration systems verifies that the C code has the expected style. The script [`scripts/code_style.py`](https://github.com/Mbed-TLS/mbedtls/blob/development/scripts/code_style.py) can check or fix the coding style.

To check that the coding style is correct (for example before submitting a pull request):
```sh
scripts/code_style.py
```

To enforce the coding style on specific files:
```sh
scripts/code_style.py --fix library/file_i_edited.c tests/suites/test_suite_i_also_edited.function
```

To enforce the coding style on all files checked into Git:
```sh
scripts/code_style.py --fix
```

#### Exceptions to enforcement

The automatic tool usually does a good job of making the code presentable, but it can sometimes make mistakes. It is possible to disable enforcement for a fragment of code by placing it between comments containing `*INDENT-OFF*` and `*INDENT-ON*` (despite the name, this controls all style enforcement, not just indentation). Do this only in egregious cases.

```c
    // normal code here
/* *INDENT-OFF* */
    // weird code here
/* *INDENT-ON* */
    // normal code here
```

Code in the `3rdparty` directory generally retains its original style, and is not subject to enforcement.

### K&R

Mbed TLS generally follows the style of *The C Programming Language*, Second Edition, 1988, by Brian Kernighan and Dennis Ritchie (“K&R2”). The main deviations are:

* Indentation is 4 spaces (like K&R2, not 5 spaces like K&R1). Do not use tabs.
* `case` is indented one level further than `switch`.
* The body of `if`, `for` or `while` must be on a separate line and surrounded with braces, even if it's a single statement.

### Indentation

Mbed TLS source code files use 4 spaces for indentation, **not tabs**, with a preferred maximum line length of 80 characters.

`case` is indented one level further than `switch`.

```c
switch (x) {
    case 0:
        zero();
        break;
    ...
}
```

Labels are indented at the same level as the enclosing block.
```c
int f()
{
    ...code...
    if (ret != 0) {
        goto exit;
    }
    ...code...
exit:
    ...cleanup...
    return ret;
}
```

Every code statement should be on its own line, except in `for` loop headers.

### Space placement

Put a space in the following places:

* Around binary operators: `(x + y) * z`
* After a comma: `f(x, y)`
* Before the asterisk in a pointer type: `int *p`
* Between `if`, `switch`, `while`, `for` and the opening parenthesis: `if (f(x))`
* Outside curly braces: `do { ... } while (!done)`, `struct mystruct s = { 0 }`
* Inside the curly braces around initializers: `int a[] = { 1, 2, 3 };`

Do not put a space in the following places:

* After the function or macro name in a function or macro call: `f(x, y)`
* Inside parentheses: `if (f(sizeof(int), (int) y))`
* Inside square brackets: `a[i + 1]`
* Before a comma: `f(x, y)`
* After a prefix unary operator: `if (!condition)`, `++x`
* Before a postfix unary operator: `x++`
* Between an array and the following opening bracket: `int a[2];`, `a[i]`
* Around field access symbols: `s.a`, `p->a`
* After the asterisk in a pointer type: `int *p`
* Between the asterisks double pointers types or derefences: `char **p`, `x + **p`

### Use of parentheses

`sizeof` expressions always use parentheses even when it is not necessary (when taking the size of an object):
```c
    memset(buf, 0, sizeof(buf));
```

### Usage and placement of braces

Braces (curly brackets) are **mandatory in control statements** such as `if`, `while`, `for`, even when the content is a simple statement.

Opening braces around compound statements are on the same line as the control statement if there is one. The closing brace has the same indentation as the line with the opening brace. It is generally alone on their line, except when followed by `else` or by the `while` of a `do ... while` statement.

```c
    do {
        x += f();
        if (x == 0) {
            continue;
        }
        x += g();
    } while (condition);
```

As an exception, **the opening brace of a function definition is on its own line**, in the leftmost column. This helps editors and other tools that treat non-indented braces as delimiting toplevel blocks.

```c
int f(void)
{
    return 42;
}
```

In compound type declarations, the opening brace is on the same line as the `struct`, `union` or `enum` keyword. The closing brace is on a separate line with the final semicolon.

```c
typedef struct {
    int x;
    int y;
} pair_t;
```

Compound initializers can be on a single line if they fit.

```c
pair_t z = { 1, 2 };
```

### Formatting of lists

When a function or macro call doesn't fit on a single line, put one argument per line or a sensible grouping per line. For example, in the snippet below, `input_buffer` and `input_size` are on a line of their own even though the call could fit on two lines instead of three if they were separated:
```c
    function_with_a_very_long_name(parameter1, parameter2,
                                   input_buffer, input_size,
                                   output_buffer, output_size);
```

Lists of items other than function arguments should generally have one item per line. Exceptions:

* It's ok to write simple structure initializers on a single line.
* In an array initialized with numerical data, pack a sensible and consistent number of items per line. The number of items per line should be a power of 2 to faciliate counting.

In lists of items such array initializers and enum definitions, do include the optional comma after the last element. This simplifies merging, reordering, etc.
```c
typedef enum {
    FOO_1,
    FOO_2,      // <- do put a comma here
} foo_t;
```
Exceptions: you can and omit the trailing comma in structure initializers that fit on one line, or if the last element must always remain last (e.g. a null terminator).

### Preprocessor directives

When using preprocessor directives to enable or disable parts of the code, use `#if defined` instead of `#ifdef`. Add a comment to the `#endif` directive if the distance to the opening directive is bigger than a few lines or contains other directives:
```c
#if defined(MBEDTLS_HAVE_FEATURE)
/* ten lines of code or other directives */
#endif /* MBEDTLS_HAVE_FEATURE */
```
