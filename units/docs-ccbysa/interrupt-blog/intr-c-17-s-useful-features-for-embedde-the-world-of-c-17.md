---
id: "intr-c-17-s-useful-features-for-embedde-the-world-of-c-17"
type: "concept"
domain: "debug"
title: "C++17’s Useful Features for Embedded Systems: The World of C++17"
summary: "In contrast to C++14, the C++17 standard changed the aura of C++ much more. Don’t get scared, you will still be able to continue using whatever you were using through this time."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-17-cpp-17-for-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/cpp-17-for-embedded#the-world-of-c-17"
license: "CC-BY-SA-4.0"
mode: "V"
---

In contrast to C++14, the C++17 standard changed the aura of C++ much more. Don’t get scared, you will still be able to continue using whatever you were using through this time. In addition to all you had before, you will now have a more powerful syntax and libraries with C++17.

### Attributes
Let’s start with these three new attributes: `[[fallthrough]]`, `[[nodiscard]]`, and `[[maybe_unused]]`. As they are only considered at compile-time, you don’t need to worry about their efficiency at all. They exist only to enhance your code development phase.

#### [[fallthrough]]

With this attribute, you can now merge the bodies of two adjacent case branches in a switch without getting any warnings from the compiler. By using it, you tell the compiler that the prior case body is non-terminated intentionally.

```cpp
switch (n) {
    case 1: [[fallthrough]]
        // ...
        // no `break;`
    case 2:
        // ...
        break;
}
```

#### [[nodiscard]]

I’m pretty sure you forgot to check the return value of your functions at least a hundred times. With this attribute, discarding the return values will become a reason for compiler warnings.

```cpp
[[nodiscard]] bool do_something() {
    return is_success; // true for success, false for failure
}

do_something(); /* warning: ignoring the return value of function declared with attribute 'nodiscard' */
```

#### [[maybe_unused]]

Are you tired of casting the unused variables to void to suppress the warnings? Then, try this attribute to get rid of that irritating warnings.

```cpp
void my_callback(std::string msg, [[maybe_unused]] bool error) {
    // Don't care if `msg` is an error message, just log it.
    log(msg);
}
```

### Power of Compile-Time
The power of checking things at compile-time fascinates me the most in C++. With C++17, this ability is further enhanced with some new features. Checking things without even deploying the code is quite beneficial when you think of the cumbersome debugging process in many embedded systems. Even transferring the executables to the target and preparing the environment for the execution and testing can be harsh and time-consuming. With compile-time programming, some parts of that tiring procedures can be eliminated.

#### Static Assertion without a message

You might think that we already had the `static_assert(..)` to check things at compile time. This time, the assertion mechanism works without providing an error message. This way, your code will look more clear.

```cpp
static_assert(false);
```

#### if constexpr

*One of my favorites!* By using `if constexpr`, we can write code that is instantiated depending on compile-time conditions.

```cpp
template<typename T>
auto length(const T& value) noexcept {
    if constexpr (std::integral<T>::value) { // is number
        return value;
    }
    else {
        return value.length();
    }
}

int main() noexcept {
    int a = 5;
    std::string b = "foo";

    std::cout << length(a) << ' ' << length(b) << '\n'; // Prints "5 3"
}
```

Before C++17, the above code would have needed to be two different functions for the string and integer inputs like below.

```cpp
int length(const int& value) noexcept {
    return value;
}
std::size_t length(const std::string& value) noexcept {
        return value.length();
}
```

#### constexpr lambda

If you also like using lambda expressions in your code, you will love this feature. Lambdas can also be invoked at compile-time by declaring them as constexpr.

```cpp
auto identity = [](int n) constexpr { return n; };

static_assert(identity(123) == 123);
```

### Syntactic Sugar
In C++17, there are some features that help you to write your code in more beautiful ways. Even though their existence doesn’t affect the runtime performance dramatically, you will like using them.

#### Fold Expressions

If you had a chance to use the variadic templates to elaborate a recursive algorithm with a variable amount of inputs or iterations, then you might face the issue of having to implement a terminator for that variadic template function. For example, the code below is written in C++11 and it accumulates the given numbers.

```cpp
int sum() { return 0; } // Termination function

template<typename ...Args>
int sum(const int& arg, Args... args) {
    return arg + sum(args...);
}
```
This code wouldn’t compile if we didn’t implement the terminator that doesn’t take any inputs. Thanks to the fold expressions, you don’t have to implement a terminator anymore and your code will look way better than the old one. See below.

```cpp
template<typename ...Args>
int sum(Args&&... args) {
    return (args + ...);
}
```

#### Nested Namespace

I don’t know how the committee of C++ didn’t think of this before. No need to explain actually, see the difference between the nested namespace definitions below in C++11 and C++17 respectively.
s
```cpp
// C++11
namespace A {
    namespace B {
        namespace C {
        int i;
        }
    }
}

// C++17
namespace A::B::C {
    int i;
}
```

#### Enhanced Conditional Statements

Wouldn’t it be more powerful if all conditional statements have the initialization section like the `for` statement has? With C++17, we now have the initialization part in conditional statements also.

This is one of the most powerful features I’ve seen so far since the variables that you create before entering a sequence of if-else statements or a switch-case will no more crowd in your local variable set.

```cpp
if (int i = 4; i % 2 == 0) {
    cout << i << " is even number" << endl;
}

switch (int i = rand() % 100; i) {
    default:
        cout << "i = " << i << endl;
        break;
}
```

#### Inline Variables

Before C++17, we had to instantiate the in-class static variables in the source file. With the inline variables, you can merge the declaration and the initial assignment inside the class definition as below.

```cpp
struct BabaMrb {
    static const int value = 10;
    static inline std::string className = "Hello Class";
}
```

### Miscellaneous
There are numerous other features in C++17 that I couldn’t classify easily. We will cover them in this section.

#### Guaranteed Copy Elision

Copy elision, *i.e. return value optimization*, is an optimization implemented by most compilers to prevent extra copies in certain situations. As of C++17, copy elision is guaranteed when an object is returned directly. In some situations, even a single copy operation affects the performance of a system, *e.g. systems with strict real-time requirements*. In such cases, it’s better to make certain that you avoid copying in order not to deteriorate system performance.

```cpp
struct C {
    C() { std::cout << "Default constructor" << std::endl; }
    C(const C&) { std::cout << "Copy constructor" << std::endl; }
};

C f() {
    return C();  // Definitely performs copy elision
}
C g() {
    C c;
    return c;    // May perform copy elision
}

int main() {
    C obj = f(); // Copy constructor isn't called
}
```

#### Shared Mutex

With the shared mutex, many readers can read an object on demand without locking it, while a write call will lock the object normally as you did before with a regular mutex. With that feature, read-only access operations will be faster as they will be able to occur simultaneously. [(Images)](https://ncona.com/2019/03/read-write-mutex-with-shared_mutex/)

#### Hardware Interference Size


This new library feature helps you to determine the L1 cache line size during compilation. With this feature, you will be able to align your structures, buffers, etc. according to the L1 cache line size.
For me, this would be helpful when I was implementing a low-level, bare-metal DMA driver for an ARM Cortex-A9 core with C++11 where I had to manage the coherency between the cache and main memory manually. If you would like to know further, please take a look at [this post](https://stackoverflow.com/questions/68949450/invalidating-a-specific-area-of-data-cache-without-flushing-its-content) of mine.

Although this feature is quite powerful, it isn’t implemented in any versions of GCC until version 12, so it is highly possible that your current compiler doesn’t even support it. Check out the code below to have a better understanding. You may need this feature one day.

```cpp
#ifdef __cpp_lib_hardware_interference_size // Undefined prior to C++17
    using std::hardware_constructive_interference_size;
    using std::hardware_destructive_interference_size;
#else
    // 64 bytes on x86-64 │ L1_CACHE_BYTES │ L1_CACHE_SHIFT │ __cacheline_aligned │ ...
    constexpr std::size_t hardware_constructive_interference_size   = 64;
    constexpr std::size_t hardware_destructive_interference_size    = 64;
#endif
struct alignas(hardware_constructive_interference_size) OneCacheLiner { // occupies one cache line
    std::atomic_uint64_t x{};
    std::atomic_uint64_t y{};
};
```
