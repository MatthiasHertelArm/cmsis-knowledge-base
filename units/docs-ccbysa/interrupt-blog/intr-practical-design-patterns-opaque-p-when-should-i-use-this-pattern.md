---
id: "intr-practical-design-patterns-opaque-p-when-should-i-use-this-pattern"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: When Should I Use This Pattern?"
summary: "Opaque pointers are a good fit if you need multiple instances. They are also a good fit for general-purpose libraries, like cJSON."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#when-should-i-use-this-pattern"
license: "CC-BY-SA-4.0"
mode: "V"
---

Opaque pointers are a good fit if you need multiple instances. They are also
a good fit for general-purpose libraries, like
[cJSON](https://github.com/DaveGamble/cJSON).

If you only ever need one of something (e.g. a state machine),
then the pattern can be overkill. Since there's just one instance (in OOP, a singleton),
there's no need for handles. The opaque pointer would just be useless overhead.

In my experience, a large portion of C modules do not need multiple instances,
so I use this pattern sparingly.

Once you are comfortable with the pattern, you may be tempted to apply it to every C module
in the system ("We must objectify all the things!"), but this would be a mistake. APIs which
don't have opaque pointers are easier to use than ones that do, so default to not using them.
The less "stuff" that's in the header file, the better.
