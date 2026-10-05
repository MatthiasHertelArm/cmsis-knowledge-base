---
id: "intr-hunting-bugs-with-git-bisect-going-further"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect: Going Further"
summary: "This was a fairly simple bisect example, with a search space of only 15 commits. As you can imagine, this complexity can increase fast when you're working on a larger project with more contributors."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect#going-further"
license: "CC-BY-SA-4.0"
mode: "V"
---

This was a fairly simple bisect example, with a search space of only 15 commits.
As you can imagine, this complexity can increase fast when you're working on a
larger project with more contributors. This section includes some strategies on
making your search go faster and making you a true bisect ninja.

### Narrowing the Search Space

As the complexity and size of a project increases, the number of commits will
likely grow as well. However, for a given issue, many of those commits may have
a low likelihood of causing the problem. It would make a bisect much faster if
we could throw out some of these commits based on what we know.

#### Searching Specific Directories/Files

Although you may not know where the behavior changed in the repo’s history, you
might know which folders/files are likely candidates. Git bisect makes it
trivially easy to narrow down the bisect to only commits that affected those
folders/files, using the following syntax.

```
git bisect start -- <dir1> <dir2>
```

Let’s assume in our test case that we knew the python script wasn’t to blame,
rather just the mini-firmware that operates on-target, located in the
`c_flasher` folder. We could run this from the root of our repo, and git will
now only bisect commits that affected that folder.

```
git bisect start -- c_flasher/
```

You can also specify specific files to investigate if you have an idea where
the bug might be.

#### Choosing the Correct Types of Commits

In your project, if you are working with multiple people and using pull requests
to get your changes in, you might be using the non-fast forward merge strategy
(as opposed to rebase). Atlassian has a great write-up[^atlassian_merge] about
merge commits if you are not familiar.

Using a merge strategy works just fine for a project, but when it comes to git
bisect, it can be a bit problematic. Your master branch could look something
like the following:


  
  (Source: Medium- @haydar_ai)


Unfortunately, if you’re trying to track down when the main branch (develop,
in this case) went bad, you’re in for a world of hurt here. Git bisect sees all
of these commits, including those on the feature branches, as fair game for a
bisect. If you’re just looking for when develop broke, these extraneous commits
are only going to cause you pain, as you only want to see the “merge commits”,
which are what git creates whenever develop is changed.

In this case, after you have started your bisect, you’ll want to tell git to
skip anything that isn’t a merge commit. That can be accomplished using this
short bit of shell script, replacing the good commit and bad commit references
with your own good and bad commits.

```
for rev in $(git rev-list <bad commit>..<good commit> --merges --first-parent);
do
  git rev-list $rev^2 --not $rev^
done | xargs git bisect skip
```

(Source: Quantic)

### Automating git bisect

One thing you might have wondered through the entire manual bisect we did
earlier was “Isn’t there an easier way to automate this?” After all, we were
just running the same script every time, looking for a success or failure
message, telling git, and then repeating the procedure until we were done.


  
  Automation can help you find bugs at the speed of Forrest
(Source: Giphy)


#### Scripting the Testing

Git bisect has a very useful feature called `git bisect run`. You can pass in a
script or any program that returns exit codes for this. Git will interpret a
nonzero code as a failure/bad commit, and zero code as successful/good. There
are some nuances to this command that you should keep in mind, but rather than
explaining them, I’ll point you to the very helpful git bisect help reference.

In our case, every time we want to test something, we need to build our firmware
code, and then run our python script. Our python script already returns 1 for an
error case, and 0 for a successful case, so let’s construct a little shell
script to do this for us.

```
$ cat ~/test.sh
#!/bin/sh

# Compile the FW code, exit with a nonzero code if we fail
make || exit 1
# Run the python script, exit with nonzero code if we fail
python update.py || exit 2
```

In essence, this will run `make` and our python script, and if either fails, we
will return a nonzero error code to indicate this is a bad commit.

#### Run the Automated Bisect

Now that we have our shell script, let’s tell git bisect to run it.

```
>>> git bisect start
>>> git bisect good v1.0
>>> git bisect bad HEAD
>>> git bisect run ./test.sh
e0c258c05343202c53a294ba59704bb02565c9d5 is the first bad commit
>>> git bisect reset
```

Well that was easy. By scripting away our problems, git is now able to save you
a lot of time and effort in finding your issue. Yay!
