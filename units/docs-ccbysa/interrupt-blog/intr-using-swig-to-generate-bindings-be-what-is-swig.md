---
id: "intr-using-swig-to-generate-bindings-be-what-is-swig"
type: "concept"
domain: "debug"
title: "Using SWIG to generate bindings between C and Lua: What is SWIG?"
summary: "SWIG is a tool that generates a binding layer between C/C++ and higher-level programming languages."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-11-29-swig-for-c-and-lua.md"
doc_source: "https://interrupt.memfault.com/blog/swig-for-c-and-lua#what-is-swig"
license: "CC-BY-SA-4.0"
mode: "V"
---

[SWIG](https://www.swig.org/) is a tool that generates a binding layer between C/C++ and higher-level programming languages. The promise of SWIG is simple: write an interface file that annotates C/C++ headers with custom SWIG markers, and generates bindings to a given language, so that you can expose whatever functionality you want from C/C++ and use it in that language.

Let's explore generating bindings between applications written in C targeted for embedded hardware and Lua.
