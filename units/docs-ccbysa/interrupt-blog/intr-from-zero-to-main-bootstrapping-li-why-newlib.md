---
id: "intr-from-zero-to-main-bootstrapping-li-why-newlib"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing Newlib / Why Newlib?"
summary: "There are several implementations of the C Standard Library, starting with the venerable glibc found on most GNU/Linux systems. Alternative implementations include Musl libc[^2], Bionic libc[^3], ucLibc[^4], and dietlibc[^5]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#why-newlib"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementing Newlib_

There are several implementations of the C Standard Library, starting with the
venerable `glibc` found on most GNU/Linux systems. Alternative implementations
include Musl libc[^2], Bionic libc[^3], ucLibc[^4], and dietlibc[^5].

Newlib is an implementation of the C Standard Library targeted at bare-metal
embedded systems that is maintained by RedHat. It has become the de-facto standard
in embedded software because it is complete, has optimizations for a wide range
of architectures, and produces relatively small code.

Today Newlib is bundled alongside toolchains and SDK provided by vendors such as ARM
(`arm-none-eabi-gcc`) and Espressif (ESP-IDF for ESP32).

> Note: when code-size constrained, you may choose to use
> a variant of newlib, called newlib-nano, which does away with some C99
> features, and some `printf` bells and whistles to deliver a more compact
> standard library. Newlib-nano is enabled with the `—specs=nano.specs` CFLAG.
> You can read more about it in our [code size blog
> post](https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#c-library)
