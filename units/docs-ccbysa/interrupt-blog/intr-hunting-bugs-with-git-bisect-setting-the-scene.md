---
id: "intr-hunting-bugs-with-git-bisect-setting-the-scene"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect: Setting the Scene"
summary: "To start, let’s introduce the system we’re using:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect#setting-the-scene"
license: "CC-BY-SA-4.0"
mode: "V"
---

### The System

To start, let’s introduce the system we’re using:

- A microcontroller with internal RAM
- A NOR flash chip with 4MiB of memory

In this particular instance, I was trying to bring up a new system where the
NOR flash would be the boot medium. I could not memory map it, and
therefore I needed to create a way of passing data through the system’s
internal RAM into NOR flash.

Doesn’t sound hard, right? I could use a debugger to write internal RAM, and
then use a small bit of firmware to write out data chunks to the flash chip.
Sounds reasonable enough. So the system would look something like this:

- A small firmware binary that can receive commands, and use various locations
  in memory for the data to be read/written, as well as any relevant metadata
- A python script that could interface with the debugger to read and write
  these memory locations in the chip.

Using this system involves 5 main steps:

1. Load the firmware
2. Format the NOR flash
3. Write the data from the file to RAM
4. Write the data from RAM to NOR flash
5. Verify the data in NOR flash matches the file

### The Problem

Somewhere between version 1.0 and the current head of the repository, my
teammates started reporting that the verify step (Step 5) from above was
failing unexpectedly. The python script was reporting failures where there was
no issue before. Although there were few commits, such issues can be very
difficult to find if not approached methodically. Trying to
find issues by testing commits one by one tends to look like this:


  
  Your life without git bisect (Source: Giphy)


Thankfully, git bisect was there to come to the rescue. Come along and join me
in re-living this bug-hunting adventure!
