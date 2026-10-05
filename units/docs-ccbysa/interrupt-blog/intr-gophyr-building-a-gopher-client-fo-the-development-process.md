---
id: "intr-gophyr-building-a-gopher-client-fo-the-development-process"
type: "concept"
domain: "debug"
title: "Gophyr: Building a Gopher Client for Zephyr with Claude: The Development Process"
summary: "The inspiration for this project struck one evening after working with my nRF7002-DK. It dawned on me that building a Gopher client for Zephyr would be a great test for my new acquaintance, Claude (3.7)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-05-16-gophyr-gopher-for-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/gophyr-gopher-for-zephyr#the-development-process"
license: "CC-BY-SA-4.0"
mode: "V"
---

The inspiration for this project struck one evening after working with my
[nRF7002-DK](https://www.nordicsemi.com/Products/Development-hardware/nRF7002-DK).
It dawned on me that building a Gopher client for Zephyr would be a great test
for my new acquaintance, Claude (3.7). Now, I understand the mention of AI may
illicit a certain negative response, and frankly, that may be entirely deserved.
I don't know that my own thoughts are even now resolved on this topic. Still,
I've been encouraged by my coworkers to give it a chance, so I decided to take
the opportunity to learn about agent-assisted coding as applied to
retrocomputing and embedded systems.

### An efficient project kick-off

I began by asking Claude to create a new Zephyr shell application project,
creating the essential build files according to convention. Claude understood
the assignment. The serial shell [^zephyr_shell] provides a constrained but
perfectly suitable CLI interface for a Gopher client. I regularly use CLI-driven
Gopher clients on desktop systems ([cgo](https://github.com/kieselsteini/cgo) is
a favorite), and in this case, we have to engage our Gopher client functions
through the `gopher` command prefix. (I later improved the ergonomics slightly
by introducing `g` as an alias)

Once I confirmed a working project template, I simply asked Claude to add a
Gopher (RFC1436-compliant) client. The Gopher protocol is refreshingly
straightforward - TCP-based client-server communication with a simple
line-oriented text format. Each menu item is marked with a single-character
code, and server responses need minimal parsing. Claude was able to grok the
standard immediately.

### Iterative Development (So _this_ is "vibe coding"...)

This turned out to be my first "vibe coding" session (cringe-worthy term
notwithstanding), and I found myself falling naturally into a collaborative
rhythm with Claude. Despite initial skepticism, I was impressed by how quickly
it grasped the task from minimal prompts, delivering immediately useful code.
Claude even showed surprising initiative - when I vaguely suggested "improve the
rendering output," it implemented a series of enhancements, including ANSI color
codes I hadn't considered.

For this initial session, I just used Anthropic's Claude web UI (this seemed
like a good place to start) and developed a simple file-copy flow for the
outputs from the browser. This was only slightly cumbersome and allowed me to
maintain a greater sense of control over the flow of information from the AI
into my new codebase. (I have since let my guard down and discovered the
benefits (and frustrations) of tighter agent integration ala Cursor -- and more
recently, the new Claude CLI)

The only real hiccups came from API changes. Claude wasn't familiar with the
latest Zephyr APIs in my pre-release branch, requiring updates to networking
calls and shell command registration patterns. I took a bit of a daft approach,
feeding compiler errors back directly, but the compiler was eventually satisfied
-- the familiar edit-compile-run loop is preserved!

What struck me most from this initial session was how implementation details
faded into the background. Instead of syntax and API minutiae, our conversation
focused on capabilities and features. I found myself thinking at a higher level
of abstraction - "we need a menu rendering system" rather than "let's loop
through these structs." This shift created a fluid creative process where
technical constraints didn't dominate. The unexpected benefit wasn't just
productivity, but a more enjoyable, conceptual approach to problem-solving.

After about three hours, (and only 15 prompts!) I had a very serviceable Gopher
client capable of rendering Gopher menus and displaying ASCII text resources.
There were bugs aplenty (responses being truncated, mostly), but it worked! I've
since fixed several bugs and begun work on new functionality, testing it on my
ESP32-S3 hardware along the way. Maybe this will become my preferred Gopher
client as I chip away at the `TODO` list one credit at a time?

### Claude's own recollection of that initial conversation

In preparing this article, I went back and found this open tab and asked Claude
about the conversation. This was the response:

```plaintext
In this chat, you've sent 16 prompts/messages:

Initial request to create a Zephyr RTOS application with serial shell interface
Feedback about compilation failure
Message saying "awesome, thanks!" and request to add WiFi connectivity
Report about compilation failure with specific error
Message about code compiling and request to add a Gopher client
Message about compilation issues with struct fields
Message with errors from paste.txt
Feedback about display functions not connecting properly
Message with the paste.txt document about gopher_shell.c failing to compile
Message with new compiler errors
Note that the latest changes weren't in the file
Message with compiler errors about "size_t" and other issues
Message with more errors about "struct net_if_addr_ipv4"
Message with link error for "net_if_ipv4_addr_get"
Message saying "That did the trick!" and request to add support for non-canonical Gopher item types
Current message asking how many prompts were used

This has been a detailed troubleshooting and development conversation with multiple iterations to get everything working correctly.
```

Yeah, this sounds right. I didn't experience any hallucinations, really, or any
of the kinds of circular thinking I've encountered in later sessions.
