---
id: "intr-visualizing-real-time-data-with-st-i-m-already-using-stmstudio-cubemonitor"
type: "concept"
domain: "debug"
title: "Visualizing Real-time Data With STMViewer: I'm already using STMStudio/CubeMonitor. Why create a new tool?"
summary: "Let's begin with the most commonly asked question: Why bother creating a tool when ST provides existing options? There are several reasons:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-15-stm-viewer-debug.md"
doc_source: "https://interrupt.memfault.com/blog/stm-viewer-debug#i-m-already-using-stmstudio-cubemonitor-why-create-a-new-tool"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's begin with the most commonly asked question: Why bother creating a tool when ST provides existing options? There are several reasons:

STMStudio is deprecated, and while it was a helpful tool, it became challenging to work with due to persistent bugs. It also lacks support for mangled C++ names and is exclusively available for Windows.

CubeMonitor, on the other hand, is often considered too much overhead for debugging purposes. It's primarily designed for creating dashboards, and during debugging, the focus tends to be on functionality rather than aesthetics. Manipulating plot data and writing values to logged variables can be inconvenient. Furthermore, setting up a basic logger configuration can require some time to familiarize with NodeRED's setup.

Last but not least, none of the available hobby-level software tools include a trace data visualizer. STMViewer's trace data visualizer is the most intriguing module, enabling users to visualize variables synchronously and profile functions or interrupts within minutes.
