---
id: "intr-tracing-logging-with-the-trice-lib-the-history-of-trice"
type: "concept"
domain: "debug"
title: "Tracing & Logging with the `TRICE` Library (Interrupts too!): The History of _Trice_"
summary: "Developing firmware means dealing with interrupts and timing. How do you check if an interrupt occurred? You might increment a counter and display it in a background loop with some printf-like function. What about time measurement?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-12-trice.md"
doc_source: "https://interrupt.memfault.com/blog/trice#the-history-of-trice"
license: "CC-BY-SA-4.0"
mode: "V"
---

Developing firmware means dealing with interrupts and timing. How do you check if an interrupt occurred? You might increment a counter and display it in a background loop with some printf-like function. What about time measurement? Set a digital output to 1 and 0 and connect a measurement device like an oscilloscope or [Saleae](https://www.saleae.com/).

I once was developing software for a real-time image processing device, and I had to hunt down what was causing a regression in processing time. A spare analog output with a video interrupt-synced oscilloscope gave me the needed information after I changed the analog output on several points in my algorithm. But this isn't ideal. I just want to deal with my programming tasks and not worry about connecting wires and extra instruments.

`printf` is so cool on a PC, but an embedded device often cannot use it for performance reasons. And thus began the quest to build something better.

My very first attempt was writing the format string `.const` offset together with its values in a FIFO during a log statement and to do the `printf` in the background. Unfortunately, this is compiler specific. I modified it to use the full string address instead of the offset, but that needed more buffer space. [Zephyr](https://docs.zephyrproject.org/latest/reference/logging/index.html), for example, does something like this and calls it "deferred logging".

Then, one day I had the idea to compute short checksums of the format strings in a pre-compile step and to use them as IDs in a list together with the format strings. That was a step forward but then I needed to write a supporting PC program to decode the information. I did that in C++ in an attempt to get something functional quickly, but I hated it, as I dislike C++ now because of all its nuts and bolts, not to mention the missing libraries issues when running it on a different PC. There was also the problem of conflicting generated short checksums. There was a way around it, but ID-based message filtering will never be possible with this issue.

The need became clear for controllable IDs and management options. I chose to implement the new solution using [Go](https://golang.org) as it was an as-fast-as-**C** language, easy to learn, promising high programming efficiency and portability. It would be interesting to try it out on a real PC project. This is the origin story of [_Trice_](https://github.com/rokath/trice).

_Trice_ grew, and as it got more usable, I decided to make it Open Source as a "Thank You" to the community.



> _Trice_ is also a [baby girl's name](https://www.babynamespedia.com/meaning/Trice), and our daughter designed the logo. The girl's pen symbolizes the `TRICE` macro for recording and the eyeglasses represent the PC tool **trice** for visualizing the logs.
