---
id: "intr-how-to-build-drivers-for-zephyr-adding-a-drivers-folder"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Adding a drivers folder"
summary: "You now should understand Kconfig, CMakeLists.txt, and module.yml. We're ready for driver development!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#adding-a-drivers-folder"
license: "CC-BY-SA-4.0"
mode: "V"
---

You now should understand `Kconfig`, `CMakeLists.txt`, and `module.yml`. We're ready for driver development!

 In my case, since my driver work is ongoing, I opted to use my own `drivers` folder in my main project repository. You can always opt to start developing your drivers in `zephyr/drivers`. This is likely a better location especially if you want to release the driver for others to use. The downside is that it requires more work!

In my case, here's what the directory structure looks like from my project repo:

```terminal
. # My Project Root located in /ncs/pyrinas/
├── CMakeLists.txt
├── Kconfig.pyrinas
├── drivers
│   ├── CMakeLists.txt
│   ├── Kconfig
│   └── rtc
│       ├── CMakeLists.txt
│       ├── Kconfig
│       └── pcf85063a
│           ├── CMakeLists.txt
│           ├── Kconfig
│           ├── pcf85063a.c
│           └── pcf85063a.h
├── west.yml
└── zephyr
    └── module.yml
```

You can see there's a pair of `CMakeLists.txt` and `Kconfig` at each level. You don't **have** to make a `CMakeLists.txt` and `Kconfig` at every level though. For example, if I wasn't planning on adding any more RTC drivers, I could stop at the `rtc` folder. You can see an example of this  below:

```cmake
zephyr_library()

zephyr_library_sources_ifdef(CONFIG_PCF85063A pcf85063a/pcf85063a.c)
```

In my case though, I opted to define `CMakeLists.txt` and `Kconfig` at every level.
