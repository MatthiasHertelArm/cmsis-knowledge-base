---
id: "intr-hunting-bugs-with-git-bisect-conclusion"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect: Conclusion"
summary: "I hope this article was a useful look into how git bisect works!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

I hope this article was a useful look into how git bisect works!

Bisecting is a pretty simple tool, but there’s a lot of ways to beef it up, and
this article highlighted just a few of those. In any case, it’s always a good
mentality to use when you’re hunting bugs. Even if you’re not using git, and
just manually testing releases of software, you can still gather some good
techniques from git bisect.

While it is a useful tool, git bisect is actually one of my last resorts in the
process of debugging. Compared to other methods of tracking down a bug,
bisecting can feel a bit too brute force-y sometimes. I tend to only use git
bisect when I have no idea where something could have gone wrong, and I need to
search through a lot of potentially unrelated changes to find where bad things
happened.

As a closing note, always watch out for your function return codes, and always
unit test your code along the way, so you can avoid the folly that I committed
in this article’s example.
