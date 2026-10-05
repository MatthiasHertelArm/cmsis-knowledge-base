---
id: "intr-why-std-this-thread-sleep-for-is-b-is-usleep-broken-in-idf-v5"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: Is `usleep()` broken in IDF v5?"
summary: "Did Espressif actually implement usleep() wrong? Yes. It needs to be fixed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#is-usleep-broken-in-idf-v5"
license: "CC-BY-SA-4.0"
mode: "V"
---

Did Espressif actually implement `usleep()` wrong? Yes. It needs to be fixed.

For periods at or longer than the system tick, `usleep()` can return before the
specified time. It shouldn't do that. It must error on the side of sleeping too
long to ensure it _never_ sleeps too little. So yes, it is broken in my view.
`stdlibc++` isn't to blame.

Since `usleep()` is sometimes short by 1 system tick period, we could just add
another tick count to our calculations. That would sometimes cause `usleep()` to
take longer, but never shorter than the specified time. This would prevent
`__sleep_for()` from calling `usleep()` a second time with a fraction of a
system tick period, so no more blocking busy wait.

We can be a little more sophisticated by taking a cue from the newer
`__sleep_for()` and keep checking the monotonic clock. Something like this:

```c
int usleep(useconds_t us)
{
    const int64_t us_per_tick = portTICK_PERIOD_MS * 1000;
    if (us < us_per_tick) {
        esp_rom_delay_us((uint32_t) us);
    } else {
        /* vTaskDelay may return up to (n-1) tick periods due to the tick ISR
           being asynchronous to the call. We must sleep at least the specified
           time, or longer. Checking the monotonic clock allows making an
           additional call to vTaskDelay when needed to ensure minimal time is
           actually slept. Adding `us_per_tick - 1` prevents ever passing 0 to
           vTaskDelay().
        */
        uint64_t now_us = esp_time_impl_get_time();
        uint64_t target_us = now_us + us;
        do {
            vTaskDelay((((target_us - now_us) + us_per_tick - 1) / us_per_tick));
            now_us = esp_time_impl_get_time();
        } while (now_us < target_us);
    }
    return 0;
}
```

With this approach, short sleep times are precise (as they always were), and
longer sleep times are non-blocking and always as long or longer than the
requested time. By testing the monotonic clock, the extra tick is only applied
when needed.

I opened a [PR](https://github.com/espressif/esp-idf/pull/15132) with this
change to IDF. Hopefully it gets approved.

Since I didn't want to work with a custom, patched IDF, I replaced all calls to
`std::this_thread::sleep_for()` with our own function. It has the same default
signature, with the option to specify a "sleep strategy." We can now force the
custom `sleep_for()` to busy wait or to yield:

```c++
enum class SleepStrategy {
    Default,            // Platform decides when to use busy wait vs. yield
    PreciseBusyWait,    // Busy wait, which is usually very precise
    EfficientYield      // Efficiently yield to other threads, but will often sleep longer than specified
};

template<typename _Rep, typename _Period>
static void sleep_for(const std::chrono::duration<_Rep, _Period>& rtime, SleepStrategy strat = SleepStrategy::Default) {

    static constexpr int64_t us_per_tick = portTICK_PERIOD_MS * 1000;
    if (rtime <= rtime.zero()) return;
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(rtime).count();

    if (strat == SleepStrategy::Default && (us < us_per_tick)) {
        // Mimic how std::this_thread::sleep_for() would act, which is to
        // (eventually) call usleep() after going through libstdc++. We only do
        // this for periods less than a tick because for longer periods the
        // implementation is broken (often returns in shorter than specified
        // time). If `usleep()` is fixed then we will update this to always call
        // it for the default strategy.
        usleep(us);
        return;
    }

    uint64_t now_us = esp_timer_get_time();
    const uint64_t target_us = now_us + us;
    do {
        if (strat == SleepStrategy::PreciseBusyWait) {
            // This is an "internal and unstable API" according to ESP, but
            // `usleep()` is just a wrapper for it anyway. If it does change,
            // this function needs to be updated.
            esp_rom_delay_us(target_us - now_us);
        } else {
            // Ensure we never call vTaskDelay(0)
            static constexpr int prevent_zero_ticks = us_per_tick - 1;
            vTaskDelay((TickType_t)(((target_us - now_us) + prevent_zero_ticks) / us_per_tick));
        }
        // Validate against monotonic clock
        now_us = esp_timer_get_time();
    } while (now_us < target_us);
}
```

This approach gives us the minimal change needed to ensure things work correctly
while allowing more control over how to perform the sleep when using C++.
