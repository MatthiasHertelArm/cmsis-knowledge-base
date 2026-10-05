---
id: "intr-building-a-tiny-cli-shell-for-tiny"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware"
summary: "The most common and simplest interface to a computer and operating system is a command-line shell. It allows for quick operations, the ability to automate operations through scripting, and is light on bandwidth usage."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell"
license: "CC-BY-SA-4.0"
mode: "V"
---

The most common and simplest interface to a computer and operating system is a
command-line shell. It allows for quick operations, the ability to automate
operations through scripting, and is light on bandwidth usage.

A class of devices which makes heavy use of command-line shells are low-power
embedded devices running bare-metal or with an RTOS. They are
resource-constrained and have limited bandwidth, so a text-based interface is
ideal.



In this post, we go over why an embedded firmware should include a command-line
shell interface, common use cases for it, how to build and extend one, and cover
common issues that developers run into while build and maintaining one. The
shell we will build will work over a UART serial port, which should make it
applicable to most embedded systems.
