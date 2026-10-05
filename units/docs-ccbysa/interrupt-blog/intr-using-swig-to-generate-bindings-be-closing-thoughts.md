---
id: "intr-using-swig-to-generate-bindings-be-closing-thoughts"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua: Closing thoughts"
summary: "After choosing Lua for an embedded project it quickly became clear how much time we’ll need to spend binding two different worlds of Lua and C together."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua#closing-thoughts"
license: "CC-BY-SA-4.0"
mode: "V"
---

After choosing Lua for an embedded project it quickly became clear how much time we’ll need to spend binding two different worlds of Lua and C together. Looking at an inspiring example of [nodemcu firmware](https://github.com/nodemcu/nodemcu-firmware), which provides a Lua-based firmware for Espressif processors, it became clear we’ll have lots of code that glues functions and data structures for both languages to understand each other.

As we started to write wrapper code, translating C arrays into Lua tables and naming structure fields manually, we found out about SWIG which promised to help with this task. At first, things were smooth as we were learning how to write a SWIG interface file, and getting simple examples to work. However, foreseeing what we’ll need to do in our application in the future and demoing passing of structures with arrays of custom types, the magic of SWIG quickly disappeared and we realized we’ll still have to write all that boilerplate code anyways, just in a SWIG interface file.

We also noticed that SWIG sneakily added dynamic memory allocation like `calloc` calls, which we want to have full control over in the embedded domain. To address this issue the solution is, again, to extend the interface file and take control of the object creation. Instead, we would have hoped one could just specify a custom memory allocator to configure SWIG with.

To sum up, there’s no doubt SWIG is a useful tool that aids with code generation, but it didn’t fill our needs in an embedded application, and we would rather take control over the whole boilerplate code than use a tool that still needs to be helped with.









{:.no_toc}
