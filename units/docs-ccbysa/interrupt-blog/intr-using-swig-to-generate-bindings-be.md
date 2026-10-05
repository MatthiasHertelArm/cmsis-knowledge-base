---
id: "intr-using-swig-to-generate-bindings-be"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua"
summary: "Lua is one of the many great interpreters that can be run on embedded devices. It's fast, uses little memory, is written in ANSI C, and is known by plenty of developers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua"
license: "CC-BY-SA-4.0"
mode: "V"
---

Lua is one of the many great interpreters that can be run on embedded devices. It's fast, uses little memory, is written in ANSI C, and is known by plenty of developers. For these reasons, many great teams are choosing to include a Lua interpreter in their embedded project (e.g. Panic with [their Playdate device](https://play.date/dev/)). You can think of Lua as an alternative to the MicroPython (Python) or JerryScript (Javascript) interpreters. However, there's a problem. Many of the libraries today for embedded devices are written in C, not Lua!

There are ways to make Lua and C work together and share data structures, but it requires a lot of boilerplate and complex code. The result is writing a lot of wrapper code integrating the two languages together that then must be maintained as the application evolves.

Thankfully, there is a project which helps automate the generation of this boilerplate code called SWIG.



This article covers how to write a C program that launches a Lua interpreter and then how to use SWIG to generate the necessary wrapper code to allow Lua scripts to access the functions and data inside of the C runtime.
