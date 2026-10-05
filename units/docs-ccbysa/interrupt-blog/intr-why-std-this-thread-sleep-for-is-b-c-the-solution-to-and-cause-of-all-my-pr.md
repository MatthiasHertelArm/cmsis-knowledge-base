---
id: "intr-why-std-this-thread-sleep-for-is-b-c-the-solution-to-and-cause-of-all-my-pr"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: C++: the Solution to and Cause of All My Problems"
summary: "Alright then, so what does all this have to do with our issue related to a 10 millisecond delay? Well, I am not actually using vTaskDelay(1) directly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#c-the-solution-to-and-cause-of-all-my-problems"
license: "CC-BY-SA-4.0"
mode: "V"
---

Alright then, so what does all this have to do with our issue related to a 10
millisecond delay? Well, I am not actually using `vTaskDelay(1)` directly.
Instead, I am using C++ thread APIs, and therefore, the actual code causing all
the CPU usage is `std::this_thread::sleep_for(10ms)`.

Espressif provides
[good support](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/cplusplus.html)
for C++, including
[`std::thread`](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/cplusplus.html).
This allows us to write portable C++ code. But it's also where our problem lies.
So how does something like an ESP32 MCU support C++ threads anyway?

### `std::thread`, POSIX Threads, and FreeRTOS Tasks, oh my!

Espressif's IDF compiles with GCC and therefore uses
[The GNU C++ Library](https://gcc.gnu.org/onlinedocs/libstdc++/) (`libstdc++`).
`libstdc++`'s implementation of `std::thread` is built on top of
[`pthreads`](https://en.wikipedia.org/wiki/Pthreads), but it is up to the
platform to provide a `pthread` implementation. Espressif did just
[that](https://github.com/espressif/esp-idf/tree/v5.3.2/components/pthread),
including things like
[thread local storage](https://en.wikipedia.org/wiki/Thread-local_storage).

If you read the code you'll see that IDF's `pthreads` is using FreeRTOS APIs for
thread creation, synchronization, and all functionality found within
`std::this_thread`, such as
[`sleep_for()`](https://en.cppreference.com/w/cpp/thread/sleep_for).

If that's not enough, we also need to consider the
[C standard library](https://en.wikipedia.org/wiki/C_standard_library). IDF uses
[newlib](https://en.wikipedia.org/wiki/Newlib) and has custom platform
implementations of its sleeping functions. Thankfully, `newlib` is not
precompiled and you can easily find its source code in the `components/newlib`
directory of an IDF install.

My problem appears in IDF v5 because it upgraded GCC from 8.4 to 13.2, and
`libstdc++`'s implementation of `std::this_thread::sleep_for()` changed. But is
`libstdc++` really to blame? Let's see.

### IDF 4.x: `std::this_thread::sleep_for()`

Let's look at the working side of things first. When calling
`std::this_thread::sleep_for(10ms)` we first enter here:

```c++
/// sleep_for
template<typename _Rep, typename _Period>
inline void
sleep_for(const chrono::duration<_Rep, _Period>& __rtime)
{
  if (__rtime <= __rtime.zero())
    return;
  auto __s = chrono::duration_cast<chrono::seconds>(__rtime);
  auto __ns = chrono::duration_cast<chrono::nanoseconds>(__rtime - __s);
#ifdef _GLIBCXX_USE_NANOSLEEP
  __gthread_time_t __ts =
    {
      static_cast<std::time_t>(__s.count()),
      static_cast<long>(__ns.count())
    };
  while (::nanosleep(&__ts, &__ts) == -1 && errno == EINTR)
    { }
#else
  __sleep_for(__s, __ns);
#endif
}
```

If you are following along in your own IDF project, you can find the
`std::this_thread::sleep_for()` implementation in the ESP tools directory under
`xtensa-esp32-elf/esp-2021r2-patch5-8.4.0/xtensa-esp32-elf/xtensa-esp32-elf/include/c++/8.4.0/thread`
(or similar, depending on the version).

IDF does not define `_GLIBCXX_USE_NANOSLEEP`, so no `nanosleep()`. That
shouldn't be too surprising for an MCU implementation. Therefore, we go straight
to `__sleep_for(__s, __ns)`.

Here is GCC 8.4 C++11
[libstdc++](https://github.com/gcc-mirror/gcc/tree/releases/gcc-8.4.0/libstdc%2B%2B-v3)'s
code for
[`__sleep_for()`](https://github.com/gcc-mirror/gcc/blob/releases/gcc-8.4.0/libstdc%2B%2B-v3/src/c%2B%2B11/thread.cc#L186):

```c++
namespace this_thread
{
  void
  __sleep_for(chrono::seconds __s, chrono::nanoseconds __ns)
  {
#ifdef _GLIBCXX_USE_NANOSLEEP
    __gthread_time_t __ts =
      {
        static_cast<std::time_t>(__s.count()),
        static_cast<long>(__ns.count())
      };
    while (::nanosleep(&__ts, &__ts) == -1 && errno == EINTR)
      { }
#elif defined(_GLIBCXX_HAVE_SLEEP)
# ifdef _GLIBCXX_HAVE_USLEEP
    ::sleep(__s.count());
    if (__ns.count() > 0)
      {
        long __us = __ns.count() / 1000;
        if (__us == 0)
          __us = 1;
        ::usleep(__us);
      }
# else
    ::sleep(__s.count() + (__ns.count() >= 1000000));
# endif
#elif defined(_GLIBCXX_HAVE_WIN32_SLEEP)
    unsigned long ms = __ns.count() / 1000000;
    if (__ns.count() > 0 && ms == 0)
      ms = 1;
    ::Sleep(chrono::milliseconds(__s).count() + ms);
#endif
  }
}

_GLIBCXX_END_NAMESPACE_VERSION
} // namespace std
```

Let's clean it up by taking out the parts not compiled for the ESP32:

```c++
 __sleep_for(chrono::seconds __s, chrono::nanoseconds __ns)
  {
    ::sleep(__s.count());
    if (__ns.count() > 0)
      {
        long __us = __ns.count() / 1000;
        if (__us == 0)
          __us = 1;
        ::usleep(__us);
      }
  }
```

Pretty simple: get the number of seconds and call `sleep()`, then get the number
of microseconds and call `usleep()`. Both of these are calls into `newlib`. We
will get to those in a moment. First, let's look at the IDF v5's `sleep_for()`.

### IDF 5.x: `std::this_thread::sleep_for()`

Once again, `sleep_for()` is a wrapper for `__sleep_for()`. Here is the newer
code
([see online](https://github.com/gcc-mirror/gcc/blob/1c0ecf06c0c9f3268ba52d4027e9b78aae4acb51/libstdc%2B%2B-v3/src/c%2B%2B11/thread.cc#L235)):

```c++
__sleep_for(chrono::seconds __s, chrono::nanoseconds __ns)
  {
    const auto target = chrono::steady_clock::now() + __s + __ns;
    while (true)
      {
        unsigned secs = __s.count();
        if (__ns.count() > 0)
          {
            long us = __ns.count() / 1000;
            if (us == 0)
              us = 1;
            ::usleep(us);
          }
        if (secs > 0)
          {
            // Sleep in a loop to handle interruption by signals:
            while ((secs = ::sleep(secs)))
              { }
          }
        const auto now = chrono::steady_clock::now();
        if (now >= target)
          break;
        __s = chrono::duration_cast<chrono::seconds>(target - now);
        __ns = chrono::duration_cast<chrono::nanoseconds>(target - (now + __s));
    }
  }
```

Now we have a `while` loop. In it, `usleep()` is called, but afterward, there is
an explicit check to determine if the minimal amount of time has actually gone
by. The only way out of the loop is if `now` is at or after the `target` time.

Why the change? This is because `nanosleep()` may return early if a signal is
delivered to the thread during its sleep. The change is in
[commit cfef4c3](https://github.com/gcc-mirror/gcc/commit/cfef4c324ac300c0ad120f0fcee376159de84a0c),
with the relevant commit comment as the following:

```git
Loop while sleep call is interrupted and until steady_clock
 shows requested duration has elapsed.
```

ESP IDF doesn't support signals, so the change should have no impact on the
ESP32. Oh, but it does!
