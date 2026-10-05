---
id: "intr-gophyr-building-a-gopher-client-fo-history-lesson-the-gopher-protocol"
type: "concept"
domain: "debug"
title: "Gophyr: Building a Gopher Client for Zephyr with Claude: History Lesson: The Gopher Protocol"
summary: "About the time Sir Berners-Lee was doing his thing, some folks at the University of Minnesota brought us a more spartan vision of hypertext#Origins>)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-05-16-gophyr-gopher-for-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/gophyr-gopher-for-zephyr#history-lesson-the-gopher-protocol"
license: "CC-BY-SA-4.0"
mode: "V"
---

About the time Sir Berners-Lee was
[doing his thing](https://en.wikipedia.org/wiki/Tim_Berners-Lee), some folks at
the University of Minnesota brought us a more _spartan_
[vision of hypertext](https://interrupt.memfault.com/blog/<https://en.wikipedia.org/wiki/Gopher_(protocol)#Origins>).
Gopher, as defined in RFC1436 [^rfc1436], offers a simple menu-oriented
interface for navigating content (resources) across servers.

(figure: An example Gopher menu displayed in Firefox 1.5)

What makes Gopher particularly interesting for embedded systems:

1. Minimal protocol overhead
2. Text-based responses ideal for serial terminals
3. Simple parsing requirements
4. Low memory footprint

This simplicity makes it a perfect candidate for implementation on
resource-constrained systems like modern microcontrollers running Zephyr.

### Protocol Specification Simplified

At its core, the Gopher protocol is refreshingly minimal:

```plaintext
                   GOPHER PROTOCOL FLOW
                   --------------------
│ CLIENT                                            SERVER │
│                                                          │
│  1. Open TCP connection to server (port 70)              │
│     ----------------------------------------------->     │
│                                                          │
│  2. Send selector string + CRLF                          │
│     (empty for root menu)                                │
│     ----------------------------------------------->     │
│                                                          │
│                      3. Server processes selector...     │
│                                                          │
│  4. Receive response data (text, binary, menu...)        │
│     <-----------------------------------------------     │
│                                                          │
│     For MENU response:                                   │
│     Each line has format:                                │
│     [Type][Description]\t[Selector]\t[Host]\t[Port]\r\n  │
│                                                          │
│     Where Type is a single character:                    │
│     0 = Text file    1 = Directory                       │
│     7 = Search       h = HTML document                   │
│     i = Info message                                     │
│                                                          │
│     Response ends with single "." line                   │
│                                                          │
│  5. Close connection when done                           │
│     <------------------------------------------->        │
```

That's it - no cookies, no sessions, no headers, no complex state management.
Just a simple selector string sent to the server, and a straightforward response
back. When you want to navigate to another resource, you make a new connection
with a new selector. This elegant simplicity makes Gopher perfect for
constrained environments like embedded systems.
