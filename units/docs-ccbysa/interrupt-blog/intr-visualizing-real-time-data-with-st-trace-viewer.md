---
id: "intr-visualizing-real-time-data-with-st-trace-viewer"
type: "concept"
domain: "debug"
title: "Visualizing Real-time Data With STMViewer: Trace Viewer"
summary: "Trace Viewer is a synchronous module used to visualize SWO trace data. This means we can visualize fast actions without worrying some data might be lost between sampling points."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-15-stm-viewer-debug.md"
doc_source: "https://interrupt.memfault.com/blog/stm-viewer-debug#trace-viewer"
license: "CC-BY-SA-4.0"
mode: "V"
---



Trace Viewer is a synchronous module used to visualize SWO trace data. This means we can visualize fast actions without worrying some data might be lost between sampling points. It does not require any configuration on the target since it is all done by the STMViewer using SWD. The only thing we have to do is to write data to the ITM->PORT[x] registers to send it. For example:

```c
ITM->PORT[0].u8 = 0xaa; //enter tag 0xaa - plot state high
foo();
ITM->PORT[0].u8 = 0xbb; //exit tag 0xbb - plot state low
```
can be used to profile a foo() function. Simple, isn't it? Of course, you can wrap the register writes in a macro, but I wanted to keep it as simple as possible. No extra includes are needed since ITM is defined in CMSIS headers.

On the other hand, this:

```c
float a = sin(10.0f * i);          // some high speed signal to trace
ITM->PORT[0].u32 = *(uint32_t*)&a; // type-punn to desired size: sizeof(float) = sizeof(uint32_t)
```
can be used to visualize a float value.

Each register write generates two frames on the SWO pin: a data frame and a relative timestamp frame. The data frame holds the channel value, size, and data, while the timestamp frame holds the time elapsed since the last frame, expressed in clock cycles. The variable length of these frames, especially the timestamp frame, makes it very effective in utilizing the available SWO bandwidth. More information on the SWO trace protocol can be found in the Armv7-M Reference Manual[^0].

For a complete quick start, please refer to [Trace Viewer](https://github.com/klonyyy/STMViewer#trace-viewer-1).

Let's now see a couple of real-life examples.

### Profiling function execution time

Let's check how long it takes to copy a buffer using a well-known memcpy function. I prepared a small demo of ten copy operations, each time 64 bytes larger than the last one:

```c
    volatile uint8_t dest[1024];
    volatile uint8_t src[1024];
    volatile uint16_t size = 1;

    for (size_t i = 0; i < 10; i++)
    {
        ITM->PORT[1].u16 = size;
        ITM->PORT[0].u8 = 0xaa;
        memcpy(dest, src, size);
        ITM->PORT[0].u8 = 0xbb;
        size += 64;

        for (size_t a = 0; a < 300; a++)
            __asm__ volatile("nop");
    }
```

Besides the memcpy profiling, we also log the current size on channel 1. As can be seen, there is also a small blocking delay to make the plot more readable. Here are the results:



After logging, you can use the markers to determine the time difference between points. Copying a single byte takes about 270 ns, whereas copying 577 bytes takes approximately 25.35 us at 160 MHz.

### Profiling multiple interrupts

This example will be similar to the previous one, except we will use multiple channels and try to observe lower-priority interrupts being preempted by higher-priority ones.

I've configured three timers and set their interrupt priorities: 0 (highest logical priority) for TIM7, 1 for TIM17, and 2 (lowest) for TIM6. I've included some dummy instructions in each interrupt to simulate some work being done.



We can observe how the highest priority execution halts all other interrupts, and only after it completes do the other interrupts resume. Particularly significant in such experiments is that the marker register writes used in Trace Viewer are atomic, preventing a higher-priority interrupt between data point generation. This also makes it a valuable tool for visualizing FreeRTOS threads.

### High-frequency ADC signal

Have you tried visualizing a high-frequency ADC signal from an embedded target? Some time ago, I had to check the step response of a low-level current controller for a motor. The current was sampled every 25 microseconds, making it quite challenging to visualize. I considered using a DAC and an oscilloscope or recording and replaying the data after the event and eventually went for the latter. Unfortunately, both methods were time-consuming and troublesome.

Let's see how TraceViewer can handle this task. We will record the current response of an inductor when a voltage step is applied to it:



Now, knowing the test voltage, calculating resistance, and measuring rise time, we can easily determine the inductance. No DAC setup or manually collecting the samples was needed!
