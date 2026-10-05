---
id: "intr-why-std-this-thread-sleep-for-is-b-why-so-slow-idf-v5"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: Why so slow IDF v5?"
summary: "One of my ESP32 projects was at version v4.4 of Espressif's IoT Development Framework (IDF). After about two days of work, the project compiled and ran in IDF v5.3. Except, something was not quite right. Things were sluggish."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#why-so-slow-idf-v5"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of my [ESP32](https://www.espressif.com/en/products/socs/esp32) projects was
at version v4.4 of Espressif's
[IoT Development Framework](https://www.espressif.com/en/products/sdks/esp-idf)
(IDF). After about two days of work, the project compiled and ran in IDF v5.3.
Except, something was not quite right. Things were sluggish. FreeRTOS's
[system state API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#_CPPv420uxTaskGetSystemStatePC12TaskStatus_tK11UBaseType_tPC27configRUN_TIME_COUNTER_TYPE)
indicated that one of the two Xtensa LX6 processors on the ESP32 was pinned at
100% usage. The culprits were two high-priority threads, both of which had a
relatively small loop with a 10 millisecond sleep between each iteration.

Sleeping for 10 milliseconds should leave plenty of time to do other things.
Plus, this code worked fine in IDF v4 without an issue. What did IDF v5 do?
