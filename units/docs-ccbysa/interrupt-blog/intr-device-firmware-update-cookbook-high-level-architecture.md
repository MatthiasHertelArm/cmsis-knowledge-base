---
id: "intr-device-firmware-update-cookbook-high-level-architecture"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: High-Level Architecture"
summary: "Over the years, I've come up with a set of basic requirements most DFU systems should fulfill. Let's walk through these one by one and iteratively design our system."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#high-level-architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

Over the years, I've come up with a set of basic requirements most DFU systems
should fulfill. Let's walk through these one by one and iteratively design our
system.

We start with the simplest possible description of what we want to achieve with
DFU: an application that updates itself.

`<style>`
.diag1 {
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
}
`</style>`

blockdiag {
   // Set labels to nodes.
   A [label = "Application"];
   A -> A [label = "Updates", fontsize=8];
}
{:.diag1}

This is not a practical design. For one, self-modifying code is easy
to mess up. Let's see how we might modify this architecture to get to something
we're happy with.

### DFU should be separate from the application

The only time I ever broke DFU on a device, I did it without changing a line of
code related to DFU. Unbeknownst to me, our DFU processes accidentally depended on an
uninitialized variable which up until then had always ended up being `0`.
Inevitably a new version reshuffled the content of the stack, and all of a
sudden our uninitialized variable held a "1". This prevented DFU from taking
place.[^chris-dfu-debug]

The moral to this story: keep your DFU process and your application code
separate. Firmware update code is critical and should not be changed unless
absolutely necessary. Separating application code from firmware update code
allows us to update our application code without risking problems with DFU.

How do we modify our architecture to meet this requirement? We simply split the
firmware into a "Loader" and an "Application". The loader verifies the
application, runs it, and can update it.

`<style>`
.diag2 {
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
`</style>`
{:.diag2}

### DFU code should be updatable

While we want to update our DFU code as little as possible, updating it should
still be *possible*. Inevitably we will find a bug in our firmware update code
which we must fix. We may want to change our memory map to allocate more code
space to our app, or to rotate a security key baked into our Loader.

But where should the code that updates our Loader live? It cannot be in the
application, or else we would violate the previous principle. It cannot be in
the Loader itself either. That leaves one option: a third program tasked with
updating the loader. We'll call it the "Updater".

The Updater is loaded by the Loader, perhaps when a specific input is received.
All it knows how to do is update the Loader.

`<style>`
.diag3 {
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
`</style>`
{:.diag3}

### DFU should use minimal code space

Every firmware project I've ever worked on has run out of code space. At Pebble,
we spent months porting our 3.0 firmware to the original watch; most of that
time was spent slimming down the code so it could fit within the 512KB of Flash
available on that device[^pebble-3].

With that in mind, we should make sure our Loader and Updater do not take more
code space than absolutely necessary. Are there ways we can update our design to
use less code space? Absolutely!

The key insight here is that the Updater needs to run very rarely and that it
never needs to coexist with the application. We can, therefore, use the same
"slot" in flash for both the Updater and the Application. The main tradeoff here
is that our Loader update flow becomes more complicated as we need to do a DFU
to get the Updater, then another to update the loader, then a third to load the
application back. In other words:

Go to Loader → DFU Updater in the Application's place → Load Updater →
DFU the new Loader → Reboot into Loader → DFU the Application back in its slot

We can tolerate this complexity because it should not be used often.

{:.diag3}

### DFU failures should not brick the device

This one should be obvious. Whether there is a bug in our DFU process, or a power loss event while we are
writing firmware, the device should be able to recover. It may operate in a
degraded mode for a bit, but it should at least be able to update itself back to
a good state.

Our design already does a reasonable job of this: if we lose power in the middle
of an Application update, we can reboot into our Loader and start our update
again. There are however two failure modes we must deal with.

First, in the event we lose power while updating the Loader, we could find
ourselves with no valid image at the address the chip boots from (`0x0` by
default for Cortex-M, but aliased to `0x80000000` on STM32). The solution is to
add a small, immutable bootloader whose sole job is to sit at the start address
and load our Loader.

Second, what happens if we find ourselves without a functional Loader? We would
want to fall back to the Updater. Here again, the small bootloader is the
solution. In the event no valid Loader is found, it should try to load whatever
is found in the "Application" slot.

`<style>`
.diag4 {
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}
`</style>`

blockdiag {
    span_width = 100;
    // Set labels to nodes.
    C [label = "Bootloader"];
    A [label = "App Loader"];
    B [label = "Application"];
    C -> A [label = "Loads", fontsize=8];
    A -> B [label = "Ld, Updt", fontsize=8];

    E [label = "Updater"];
    A -> E [label = "Ld, Updt", fontsize=8];
    E -> A [label = "Updates", fontsize=8];
    C -> E [label = "Loads", style=dashed, fontsize=8];

    group {
        label = "Slot 0";
        color = "PaleGreen";
        C;
    }
    group {
        label = "Slot 1";
        color = "LightPink";
        A;
    }
    group {
        label = "Slot 2";
        color = "LemonChiffon";
        B; E;
    }
}
{:.diag4}

In summary, we end up with four programs:

1. An immutable Bootloader whose sole job is to load the Loader, and fallback to
   another image if the Loader is invalid.
2. A Loader that can verify our Application image, load it, and update it.
3. An Application which does not do any updates itself
4. An Updater that temporarily replaces the Application and can update the
   Loader.

This is not the only valid firmware update architecture, but it avoids many of
the pitfalls of DFU without consuming too much code space.
