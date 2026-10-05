---
id: "intr-hunting-bugs-with-git-bisect-starting-with-git-bisect"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect: Starting With git bisect"
summary: "Put simply, git bisect is a “divide-and-conquer” approach to finding where something changed in your codebase, and is most useful during those mysterious times when the search space is large and the root cause of a change in …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect#starting-with-git-bisect"
license: "CC-BY-SA-4.0"
mode: "V"
---

Put simply, git bisect is a “divide-and-conquer” approach to finding where
something changed in your codebase, and is most useful during those mysterious
times when the search space is large and the root cause of a change in behavior
is not clear.


  
  Gordon Ramsay’s advice doesn’t just apply to the kitchen (Source:
Giphy)


### What's the Idea?

I’ll start by explaining the concept theoretically, and later on, we’ll apply
it to a real-world example of bisecting my flasher example further down in this
article. This is one of those concepts that I found far easier to learn and
understand by example, so if my theoretical description is lackluster,
hopefully going through a real-life example will help

Git bisect works by taking in the two most important pieces of information that
you might have in such a situation: when did you know things were good, and
where did you know things were bad? Once you input the “good” commit and the
“bad” commit, the tool performs a binary search on the commits that lie in
between, starting with the midpoint between the “good” and “bad” commits. The
concept of a binary search is nothing new:


  
  Finding a G using a binary search (Source: TutorialsPoint)


A git bisect is very similar to this visual, if you imagine letter A is your
good commit, and letter R is your bad commit. At each point in the binary
search, git will checkout the commit, and wait for you to run whatever tests
you need to run. In this case, we checkout commit "I" and test it. Once you have
determined if the commit is good or bad, you tell git as such. Now, git knows
the following:

- If the midpoint commit was good, you know the commit that introduced the
  change is between your midpoint and the initial “bad” commit.
- If the midpoint commit was bad, you know the commit that introduced the change
  is between your midpoint and the initial “good” commit.

As a result, you have now effectively cut the whole search space in half, and
can continue to the midpoint of the remaining search space. This procedure
repeats on to commit E, to commit G, and finally to either F or H depending on
whether G is good or bad. Once you’ve finished searching, you have isolated the
commit that introduced the undesired behavior and can finally see what
happened.

### Typical/Important Commands

There are quite a few commands within the git bisect world, but here is the bare
minimum you would need for a bisect.

- `git bisect start`: puts git into bisect mode, awaiting further bisect
  commands
- `git bisect bad <commit hash or tag>`: Informs bisect which commit is known
  to be bad
- `git bisect good <commit hash or tag>`: Informs bisect which commit is known
  to be good
- `git bisect reset`: exits bisect mode, returns you to normal git mode.
