---
id: "intr-tracking-firmware-code-size"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size"
summary: "This is the terminal output of my nightmares."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas"
license: "CC-BY-SA-4.0"
mode: "V"
---

```
arm-none-eabi-ld: firmware.elf section `.text' will not fit in region `ROM'
arm-none-eabi-ld:: region `ROM' overflowed by 16 bytes
make: error: arm-none-eabi-ld returned 1 exit status
make: *** [firmware.elf] Error 1
```

This is the terminal output of my nightmares. It frequently means a halt in
productivity and sends engineers scrambling to save 100 bytes wherever they can,
all while trying to meet the deadlines and requirements set forth by the Product
team.

Fortunately, this message doesn't always have to come as a surprise. Where I've
worked in the past, we had the tools and infrastructure in place to know when we
would run out of code space, as well as where it all went. These tools were
immensely helpful when our team at Pebble was trying to
[cram an 653kB firmware into a 448kB ROM region](http://web.archive.org/web/20160308073714/https://blog.getpebble.com/2015/12/09/3ontintin/).

Below is an example of a type of dashboard we had. When we approached 5kB
remaining in our firmware image, we knew what to do.





In this post, I will show you how to set up a code size dashboard for your
project. I'll cover why should track code size, how to do it, and the steps to
calculate code size deltas on every pull requests to keep it to a minimum.



> If you want to skip ahead to see what we'll be building in the post, check out
> this example
> [code size dashboard for the Zephyr Project](https://zephyr-codesizes.herokuapp.com/public/dashboards/rsertKgwMwqHWzE24G4QUvbZhEe72x4hhsqMSqts?org_slug=default).
