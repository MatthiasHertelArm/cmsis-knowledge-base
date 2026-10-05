---
id: "intr-the-android-developer-s-journey-in-introduction-to-android-hardware-observa"
type: "concept"
domain: "debug"
title: "The Android Developer's Journey into Hardware Observability: Introduction to Android hardware observability"
summary: "With the popularity of mobile app development over the last decade, many developers are at least vague familiar with what's involved with shipping and maintaining an Android app."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-28-aosp-observability.md"
doc_source: "https://interrupt.memfault.com/blog/aosp-observability#introduction-to-android-hardware-observability"
license: "CC-BY-SA-4.0"
mode: "V"
---

With the popularity of mobile app development over the last decade, many
developers are at least vague familiar with what's involved with shipping and
maintaining an Android app. But if your only experience is with Android apps and
you are suddenly thrown into a project developing on Android hardware, it can be
surprising how the single mobile app is just a tiny fraction of the complexity
involved.

When you ship an Android app to Google's Play Store so users can install it on
Android smartphones from Google, Samsung, Motorola, or some other manufacturer,
you're only responsible for delivering a single Android app. But when you
deliver Android hardware, there are tens (hundreds?) of Android apps on the
device to think about — like Status Bar, Settings, Software Updater,
Dialer, Messaging, Documents, Keyboard, and more. And there are even more native
services that run as part of the core Android OS. Each custom Android device is
also usually ordered from an ODM (Original Design Manufacturer), which
customizes the base version of the Android Open Source Project (AOSP) with
ODM-specific changes to support that specific SoC (system-on-a-chip) by
providing drivers for hardware components. So at the end of the day, at the bare
minimum, you're responsible for a device that's running parts of your own
Android apps, parts of your ODM's customizations, and the whole of AOSP, which
is also running a customized version of Linux.

(figure: AOSP Component Stack)

To make things even more complicated, if your team ordered the Android hardware
from an ODM, you might not contractually have access to the source code of the
OS (since the ODM would rather not let you see the types and quality of changes
to AOSP), which significantly limits your ability to dig into and understand the
operation of the device, instead relying on the terms of support in your
contract.

This web of complexity might not seem like a big issue, but it is the nature of
all software and hardware today that there are bugs, and the more complicated
the system, the more complicated the bugs that can arise. It's unrealistic to
expect to catch all bugs during development, so what we need is a variety of
tools to help diagnose and fix problems when the hardware is in the field and in
our customer's hands.
