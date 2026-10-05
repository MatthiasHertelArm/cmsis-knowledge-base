---
id: "intr-standout-exhibits-at-embedded-worl-exciting-new-startups-are-sprouting"
type: "concept"
domain: "debug"
title: "Standout Exhibits at Embedded World 2024: Exciting new startups are sprouting"
summary: "Exein[^exein] is a new startup in the embedded security space. They have built an agent for embedded Linux devices which collects security signal from the device as it is used and uploads it to their cloud for analysis and alerting."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-25-embedded-world-2024.md"
doc_source: "https://interrupt.memfault.com/blog/embedded-world-2024#exciting-new-startups-are-sprouting"
license: "CC-BY-SA-4.0"
mode: "V"
---



Exein[^exein] is a new startup in the embedded security space. They have built
an agent for embedded Linux devices which collects security signal from the
device as it is used and uploads it to their cloud for analysis and alerting.
And yes, their agent is written in Rust! I think we’ve done too little for too
long to secure IoT devices, and am glad to see startups like Exein take up the
challenge of IoT security.



Another security startup, Emproof[^emproof] provides firmware hardening services
to device makers. Their clever solution scans and rewrites firmware binaries to
obfuscate it (preventing reverse engineering) and add security features such as
stack guards.

I've always been suspicious of security-by-obscurity, the idea that obfuscation
will make you safer. But I think the approach of automatically adding security
features such as stack guards, address randomization, and others to firmware has
a lot of potential.



I was surprised by the number of Embedded GUI solutions (they call themselves
“Human Machine Interface” - HMI platforms) that exist. Qt of course had a large
booth, but so did Embedded Wizards and a long list of others.

One startup in the space stood out to me: Incari[^incari]. They have built a GUI
editor for hardware (Incari Studio) and an embedded rendering engine which can
render those GUIs on limited devices. Incari Studio even has a Figma integration
so you can drop a Figma design into its studio, then compile your design
directly for your device. That’s a pretty cool workflow! Unlike Qt it won’t work
on your MCU, however, as it requires 256MB and a higher level OS (QNX, Linux,
…).



Last but not least, I had a chance to chat with Michael at Embedd[^embedd]. They
have built an AI system that can parse a data sheet provided as PDF and spit out
a fully functional driver in C. This feels like a task perfectly suited for AI
techniques, and I look forward to trying it out when it goes into general
availability. I would be thrilled if I never had to write a driver again!
