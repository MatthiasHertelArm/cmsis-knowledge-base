---
id: "intr-beyond-error-codes-debugging-ill-d"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems"
summary: "It's Friday around 4 PM. You've been on a productivity tear and are getting to wrap up for the week when, all of a sudden, things go off the rails."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's Friday around 4 PM. You've been on a productivity tear and are getting to
wrap up for the week when, all of a sudden, things go off the rails. Logging has
stopped entirely with no clues to the problem, your LED has stopped blinking,
and even the debug CLI you painstakingly coded has stopped responding to any of
your commands. "But I wasn't even making a complicated change!" you yell into
the void. You've thoroughly bricked your firmware, and none of the usual safety
nets you've set for yourself are telling you why!

These types of problems can be extremely frustrating and intimidating when they
occur. They often undermine confidence in the codebase, making it seem as if
problems could jump out _at any time_ when you make _any change whatsoever._
I've encountered these sorts of problems many times in my career. Each one has
served as a painful lesson in debugging issues like this.

The good news is there has _always_ been an explanation for any issue I've
encountered. And they've yet to be
[caused by a rogue neutron](https://www.bbc.com/future/article/20221011-how-space-weather-causes-computer-errors),
despite how often I wish the culprit was someone other than myself.



The following guide serves as a prescriptive, step-by-step way of debugging
errors that on their face appear to be intangible.



> 🎬
> _[Listen to Hayden on Interrupt Live](https://www.youtube.com/watch?v=bgx4p-Voqkg)
> talk about the content and motivations behind writing this article._
