---
id: "intr-c-17-s-useful-features-for-embedde-notable-changes-in-c-14"
type: "concept"
domain: "debug"
title: "C++17’s Useful Features for Embedded Systems: Notable Changes in C++14"
summary: "C++14 had smaller upgrades compared to the ones we saw when migrating to C++11 from C++03. Hence, there are only a few features in C++14 that you can use in an embedded system."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-17-cpp-17-for-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/cpp-17-for-embedded#notable-changes-in-c-14"
license: "CC-BY-SA-4.0"
mode: "V"
---

C++14 had smaller upgrades compared to the ones we saw when migrating to C++11 from C++03. Hence, there are only a few features in C++14 that you can use in an embedded system.

### Binary Literals

If you are frequently dealing with bitwise operations and modifying registers, you will love these literals. Some compilers had extensions that support such literals, but now they have a place in the actual standard.

```cpp
uint8_t a = 0b110;        // == 6
uint8_t b = 0b1111'1111;  // == 255
```

### Constraint relaxed *constexpr***

With C++14, the syntax you can use in a constexpr function is expanded. Check out [this post on StackOverflow](https://stackoverflow.com/a/31410986/10400598).
The constexpr is beneficial in the embedded world since it can make calculations at compile time and reduce some code to constants. Note that an expression can only be calculated during the compile-time if all its requirements can be determined during the compilation.

```cpp
constexpr int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
factorial(5); // == 120 (Calculated at compile time)
```
