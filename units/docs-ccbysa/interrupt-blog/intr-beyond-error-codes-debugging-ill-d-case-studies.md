---
id: "intr-beyond-error-codes-debugging-ill-d-case-studies"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Case Studies"
summary: "I was in the middle of testing my port of Segger's Real Time Trace (RTT) to an implementation written in the up-and-coming Zig Programming Language."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#case-studies"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Case Study #1 - Creative Stack Clobbering

I was in the middle of testing my
[port of Segger's Real Time Trace (RTT)](https://github.com/haydenridd/zig-rtt)
to an implementation written in the up-and-coming Zig Programming Language. My
port (as well as the original RTT source code) has a feature that lets you
specify a linker section to place your RTT control block. The control block is
where the JLink probe writes/reads to enable transfer to/from the device. At
this point, I had validated all other use cases other than this manual control
block placement. Feeling very smart and very accomplished, I coded up the last
sanity check, where I put the RTT control block in a newly defined linker
section _at the end of RAM._ All of a sudden, reality started to crumble. Hard
faults began appearing after a couple of logging statements. Seemingly _what_ I
logged and _how much_ affected this program's crashing behavior.

#### Step 1 - See What Changed

Fortunately, it is quite obvious in this case. Placing the control block at the
end of RAM appears to break the code.

#### Step 2 - Utilize All Compiler Error Reporting Capabilities

Already done!

#### Step 3 - Utilize All MCU Error Reporting Capabilities

Also already done, and the error reporting, in this case, indicated "a hard
fault was occurring". I was using the Cortex M0+-based RP2040, so the hard fault
cause doesn't get any more specific.

#### Step 4 - Isolate the Problem Surface Area with Logging and/or Debugging

This step was pretty straightforward; I could initialize the control block
without issue, however, one or more logging statements initiate the hard fault.

#### Step 5 - Keep an Eye on Your Stack

I quickly noticed that near the point of failure, variables all of a sudden
started to have… wrong values. Wait… where is my stack again? Oh. _OH._ The
astute reader probably already guessed from context, but my stack was
_hard-coded_ to start _at the end of RAM._ I had gotten complacent with other
projects that used linker symbols to place the stack start and assumed that
defining a new linker section for the RTT control block would protect against
accidentally overriding the stack. This assumption was incorrect. I had created
a monster where entering my logging functions would push data onto the stack,
but writing bytes to my control block _would actively clobber said stack data._
Thus, oddball logging behavior where a couple of characters would transfer
successfully, followed by a hard fault.

### Case Study #2 - Undefined Fun Times

For the sake of simplicity, I had a class with two methods that looked something
like so:

```c
class ThisShouldBeFun {

  public:
  ...

  int first_function() {
    // Lots of sufficiently complicated code
  }

  void second_function() {
    // Has some side effect that changes the internal state of the class
  }
};
```

I had some odd behavior in my code, and after some debugging, I realized that
even though I was calling first_function, somehow second_function was getting
executed as well!?

#### Step 1 - See What Changed

I previously wasn't using first_function, although it had been added to the
class a while ago, so it didn't appear in any recent diffs.

#### Step 2 - Utilize All Compiler Error Reporting Capabilities

Observers probably already saw my error: I didn't include a return statement.
Per the [C++ standard](https://en.cppreference.com/w/cpp/language/return), a
non-void function terminating without returning a value is undefined behavior.
In my case, it appears as if that undefined behavior caused the next instruction
to be _the second function's address._ I can wave my hands a little bit about
the in-memory layout of C++ classes, and how this might have happened, but I've
never been able to replicate this in Godbolt. You'll just have to take my word
that in this specific corner of the universe, undefined behavior caused
first_function to terminate by calling second_function. The warning flag
`-Wreturn-type` (included in `-Wall`) would have saved me a major headache.

### Case Study #3 - The Mystery of the Missing Serial Bytes

I was on a project that had two boards that communicated with each other via
serial over UART. I was onboarding onto this project at the time, and an
existing issue I noticed was that a packet (these boards implemented Modbus)
would fail its CRC check and the command would have to be retried. Because of
this retry routine, the communication still functioned, albeit not as fast as it
could have. Eventually, and seemingly out of the blue, the number of CRC
failures in packets skyrocketed, making the communication unusable and demanding
immediate attention.

#### Step 1 - See What Changed

Trying to narrow down what changed was pretty maddening. None of the code
changes had anything to do with code that touched serial communication. And yet,
I could revert commits and get reliably "better" communication behavior, albeit
with occasional failures. There also seemed to be a bizarre time component where
serial communication would seem fine at first, but rapidly degraded after a
minute or two.

#### Step 2 - Utilize All Compiler Error Reporting Capabilities

Done, and no findings.

#### Step 3 - Utilize All MCU Error Reporting Capabilities

Done, and no findings (this issue wasn't generating hard faults).

#### Step 4 - Isolate the Problem Surface Area with Logging and/or Debugging

The findings in Step 1 made us all feel pretty miserable about the root cause,
but due to the failure point, we were at least pretty sure the issue lay
somewhere in the serial driver/peripheral configuration.

#### Step 5 - Keep an Eye on Your Stack

We found no evidence of stack overflows.

#### Step 6 - Keep an Eye on Your Heap

N/A, we weren't using a heap.

#### Step 7 - Vet Critical Peripherals:

Thus, a long and painful slog through our UART driver code started. We were
using the DMA to automatically transfer received bytes into a memory buffer on
reception in the UART. Then, we serviced said buffer in an RTOS task whenever
bytes were available. We couldn't get rid of these bad bytes causing CRC
failures no matter how closely we examined our peripheral configuration against
the datasheet. The breakthrough came when I finally remembered something: this
MCU has a cache. Turning off caching immediately fixed the problem. No more
erroneous bytes, and thus no more CRC failures. Which led us to…

#### Step 8 - MCU Errata and Application Notes:

Reading an
[application note](https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf)
on caching on our MCU, we quickly realized the DMA does not at all care about
the state of the cache. Once we fixed our cache management regarding the memory
buffer in which our UART bytes were stored, we could turn the cache back on
while eliminating the mysterious bad bytes. Because the cache was often out of
date before implementing cache management, whether or not the received bytes
were correct was almost entirely random, depending on other code execution and
cache hits/misses. Thus, changing unrelated bits of code changed cache behavior
and thus changed how often we got bad bytes.

### Case Study #4 - Memory Faults in the Depths of Hell

(figure: Doom 1 GIF)

This last one is the most painful yet satisfying bug I've ever dealt with. To
set the stage, I was in the process of porting DOOM to the display board on the
TK-02 coffee machine (I currently work as the lead firmware engineer at Terra
Kaffe). This was entirely a side project for the fun and the challenge. Porting
Doom to a "bare metal" system is a little spicier than for one with an actual
OS. For instance, I replaced all allocation calls in Doom's engine with an arena
allocator that made use of an external SDRAM IC we use. This will become
relevant later. Frustratingly, things were _almost_ working. I would
occasionally get the Doom splash screen to appear on the screen, but at
seemingly random times, shortly thereafter, everything would freeze.

#### Step 1 - See What Changed

I didn't have a baseline to diff against, as I was in the early stages of
getting the engine running at all.

#### Step 2 - Utilize All Compiler Error Reporting Capabilities

Done, and no findings.

#### Step 3 - Utilize All MCU Error Reporting Capabilities

Whenever the program would freeze up, I would get an MPU access violation that
told me I was trying to access an invalid address. The address always had the
form `0xFFXXXXXX`, which was indeed invalid.

#### Step 4 - Isolate the Problem Surface Area with Logging and/or Debugging

The code that kept throwing faults was in the section of the engine that
decompresses assets from the `.WAD` file (The DOOM engine's proprietary data
compression format that would generally be stored on a floppy disk or CD-ROM)
and stores them in RAM via the arena allocator I mentioned before.
Frustratingly, it wasn't always in the same place. Sometimes, it would get to
the splash screen, other times it would crash almost instantly. When it did make
it to the splash screen there were always lots of warnings from the engine about
bad assets, and some assets (character textures, etc.) were missing. Using a
debugger to walk up stack traces, it was clear that sometimes _when accessing
something in SDRAM_, a bogus address (beginning in `0xFF`) would be produced.

#### Step 5 - Keep an Eye on Your Stack

Values having bogus addresses did seem to point to a potential stack overflow,
but further investigation yielded no evidence the stack was getting anywhere
close to overflowing.

#### Step 6 - Keep an Eye on Your Heap

We weren't using the heap _per se_, however, the arena allocator functioned
essentially as a heap. Careful investigation and logging of the allocator
revealed we weren't getting close to any overflow situations regarding the heap.

#### Step 7 - Vet Critical Peripherals

While I spent many hours excitedly getting pieces of the DOOM engine working, I
never thought to double-check some of my initial MCU configurations. After all,
I had a "known good" production version of this configuration running the
_actual_ coffee machine firmware. But after many days and hours, convinced I had
somehow screwed something up in the engine implementation, I found the culprit:
a copy-paste error in a setup call that left one pin of the SDRAM IC
misconfigured, and electrically floating (only in the Doom project, the actual
production code was configured correctly). The pin that happened to be floating
controlled single-byte masking of the received data. Lo and behold, the single
byte it masked happened to be the most significant byte... So, I essentially
created a "random memory fault generator". When the misconfigured pin floated a
little too high, it masked the MSB, mangling the received data to be
`0xFFXXXXXX`. This explained the odd engine behavior. If the stars aligned and
the SDRAM read errors only happened on non-critical textures (and in a way that
didn't generate an MPU fault) the game would barely get to the splash screen. In
the end, it was all worth it to rip and tear on the TK-02:

(figure: Doom 2 GIF)
