---
id: "intr-how-memory-usage-patterns-can-dera-audio-issue-diagnosis"
type: "concept"
domain: "debug"
title: "How Memory Usage Patterns Can Derail Real-time Performance: Audio Issue Diagnosis"
summary: "As I started testing and debugging my application, I kept running into issues where the audio output was regularly interrupted, resulting in an audible click. What could possibly be wrong with my code that might cause this?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-29-memory-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/memory-debugging#audio-issue-diagnosis"
license: "CC-BY-SA-4.0"
mode: "V"
---

As I started testing and debugging my application, I kept running into issues
where the audio output was regularly interrupted, resulting in an audible click.
What could possibly be wrong with my code that might cause this? I started
thinking about the reasons my audio callback could take too long to return, the
locks in my code, and whether the audio callback could be pre-empted by the
operating system, causing it to return too late and miss its real-time
“deadline.”

Eventually, I decided to use a profiler to figure out what was going on and
turned to the excellent [Tracy Profiler](https://github.com/wolfpld/tracy),
which is open source and free. Tracy is easy to integrate with your code,
allowing you to define different zones for tracing and profiling. The Tracy
profiling GUI application can connect over the network with your embedded
platform and receive trace information in real time. This helps speed up
development and debugging. Tracy also comes with a command-line capture tool you
can use to capture the trace directly to disk instead of sending it over the
network to your workstation.

I typically do not enable Tracy in release builds shipped to customers and only
use it when I’m trying to find a problem with the real-time behavior of my
software. I use compiler switches (`-D`) to enable Tracy, as described in the
[Tracy manual (PDF warning)](https://github.com/wolfpld/tracy/releases/latest/download/tracy.pdf),
which also describes how to control the amount of data collected. This is
important, as you do not want to generate so much tracing data that it starts to
get in the way of determining the real problem at hand.

With the help of Tracy, I discovered that my audio callback was occasionally
taking too long to return. This happened often enough that it was a real
problem.



 


At the top of the screen in Tracy, you can see which CPU cores the threads are
being scheduled on (note the four “lanes” in the above screenshot, since the
software is running on a quad-core CPU). At the bottom of the screen, you can
see the different nested zones that I defined in my source code, with Tracy
measuring the time spent in each. The zones allow you to understand which areas
of your code are the most problematic and need review.

You can see in the above screenshot an instance when the ALSA callback takes
much longer than normal. What was interesting was that the issue always seemed
to be connected to a memory-related function call. Right above the zones at the
bottom, you can see a series of blue dots. When hovering over them, these dots
showed the same memory-related function repeatedly, indicating that the CPU was
spending an unusually long time in this function. Additionally, the yellow graph
at the bottom shows memory usage constantly increasing or decreasing, resulting
in the zig-zag pattern being plotted.

However, I had paid close attention to the code in my audio callback and DSP
worker threads and I was fairly confident I was not doing any kind of dynamic
memory allocation in my audio or DSP threads.

As I dug deeper, I noticed that my audio thread was being pre-empted by kernel
threads.



 


While I don't have an exact copy of the pre-emption from this instance, I have
an example screenshot above which is very similar. In this case, you can see
that the ALSA thread is being pre-empted with a memory-related function call
appearing at the bottom of the screen shortly before the scheduling of kernel
threads.

> Note: Tracy can sample Linux kernel call stacks in addition to your
> application call stacks to give an even deeper look at what the kernel is
> doing. Refer to the Tracy manual to understand the requirements for this.

Eventually, I started examining the memory usage behavior of my application and
discovered that the third-party application framework I was using had its own
memory management classes. Under the hood, `malloc()` was being called to
allocate blocks of very small sizes -- some as small as 4 bytes! These classes
were used all over the code base in the framework -- and thus in my application,
which was based on the framework. I had unwittingly invited dynamic memory
allocation in places due to the way the framework was architected.

Because of the frequency with which these calls happened, it resulted in memory
fragmentation, which explained why some memory-related function calls took so
long to return. Fragmentation can result in memory-related function calls taking
much longer than normal and/or the Linux kernel pre-empting your thread(s) while
it performs its cleanup.

By analyzing the call stacks, combined with callbacks taking unusually long to
return, excessive time spent in memory-related functions, and the scheduling of
kernel threads, you can get an idea of whether your application’s memory usage
patterns might be causing issues.

In my particular case, my application’s memory usage patterns caused my
callbacks and other code to take too long to return, resulting in missed
real-time deadlines and audio clicks.
