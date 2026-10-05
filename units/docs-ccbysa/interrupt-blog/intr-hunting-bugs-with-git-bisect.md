---
id: "intr-hunting-bugs-with-git-bisect"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect"
summary: "It’s one of those nights- your project has been moving along at breakneck pace, with all of its contributors committing refactors, improvements, and bugfixes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect"
license: "CC-BY-SA-4.0"
mode: "V"
---

It’s one of those nights- your project has been moving along at breakneck
pace, with all of its contributors committing refactors, improvements, and
bugfixes. You’ve been using git commands so much recently that you
can rely on your fingers’ muscle memory to do all of your git operations for
you. All of a sudden, you get that dreaded message from a teammate:

> The firmware flasher is broken, and we don’t know when it broke

If you’re anything like me, your reaction looks something like this.


  
  Donald Glover hates bugs too, probably (Source: Tenor Gif)


Your brain starts swirling. “How did this break? What could’ve possibly caused
that? Am I that far off my game that I somehow goofed this?”

You start to look around at the codebase, and nothing’s popping out to you as
an obvious cause of the bug. You run `git log --oneline` to look through the
recent commit history, but your heart starts to sink because you actually don’t
know when the bug might’ve been introduced. You ask your team in Slack “Does
anyone know when this broke?” You get more desperate and start checking out
random commits to see if it works. No luck.

What do you do now? If only there was a tool you could use to find where things
broke in an organized fashion...

This is where the concept of bisecting comes to the rescue. Regardless of
what version control system you are using there are options for
bisecting. In this article, we will be using git, since it has a bisect
feature built-in. If you use a different system, check the References section
for bisecting solutions for Mercurial[^mercurial_bisect], CVS[^cvs_bisect], or
SVN[^svn_bisect].



This article is a personal story of a time I had to run a bisect on a repository,
and the thoughts that went through my mind as it happened.
I touch on how to find a bug using git’s bisect feature and go over some easy strategies
to narrow your search space as much as possible. Lastly, I detail some ways of speeding up that
search through git bisect’s automation options.
