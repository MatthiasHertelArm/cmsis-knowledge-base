---
id: "intr-how-memory-usage-patterns-can-dera-background"
type: "concept"
domain: "debug"
title: "How Memory Usage Patterns Can Derail Real-time Performance: Background"
summary: "As the founder of Percussa, I have led the software and hardware engineering of our pro-audio consumer electronics products for nearly 20 years."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-29-memory-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/memory-debugging#background"
license: "CC-BY-SA-4.0"
mode: "V"
---

As the founder of Percussa, I have led the software and hardware engineering of
our pro-audio consumer electronics products for nearly 20 years. The first
product I developed was the
[AudioCubes](https://www.percussa.com/what-are-audiocubes/), a human-computer
interface, consisting of multiple smart wireless objects capable of detecting
each other’s location, orientation, and distance. The AudioCubes are a bare
metal DSP platform and do not run an off-the-shelf operating system.

Subsequently, I developed the
[Percussa Super Signal Processor (SSP)](https://www.percussa.com/super-signal-processor/),
a multichannel audio DSP platform, which was funded via Kickstarter for 314%.
The SSP is used by professional studio musicians and sound designers worldwide
and is a eurorack module (eurorack is a modular synthesizer standard). It is
installed into end users’ synthesizer racks or in recording studios. It offers a
library of DSP building blocks that can be chained together to create various
signal-processing chains for synthesizing new sounds or processing existing
sounds.

The SSP is a Linux-based platform based on a Rockchip SoC. In addition to
developing the hardware and bringing up the platform, I also developed the
real-time audio DSP software for the SSP. To deliver a great customer
experience, it was important to get consistent audio DSP performance from the
platform, avoiding the clicks and pops in the audio that can be caused by not
consistently meeting audio processing deadlines (i.e. completing audio callbacks
in time). Additionally, to fully benefit from the processing power of the
platform, DSP processing needs to be parallelized over multiple CPU cores (the
SoC in the SSP is a quad-core processor).



 


The audio DSP software I developed originally ran on Windows and Mac OSX
platforms using a popular C++ application framework for audio applications. My
strategy was to port the software to the new audio-embedded Linux platform (the
SSP).

This went fairly well, with most of my time spent designing and implementing
user interface code, menu systems, and code to parallelize DSP code across CPU
cores. My goal on my embedded Linux platform was to use the mainline kernel tree
to reduce maintenance costs.
