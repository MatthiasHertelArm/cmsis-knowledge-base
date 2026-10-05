---
id: "intr-hunting-bugs-with-git-bisect-let-s-go-hunting-a-real-example-of-bisec"
type: "concept"
domain: "debug"
title: "Hunting Bugs with Git Bisect: Let's Go Hunting! A Real Example of Bisecting"
summary: "Time to actually bisect through my code and figure out why my flashing script isn’t working. Let’s go through this bisect and see what happened."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-21-git-bisect.md"
doc_source: "https://interrupt.memfault.com/blog/git-bisect#let-s-go-hunting-a-real-example-of-bisecting"
license: "CC-BY-SA-4.0"
mode: "V"
---

Time to actually bisect through my code and figure out why my flashing script
isn’t working. Let’s go through this bisect and see what happened.

### Setting Up the Bisect

Let’s look at my commit history first. I know this was good at v1.0, and bad at
HEAD (AKA, my latest commit), so let’s get a shortlist of everything in
between.

```
>>> git log --pretty=oneline v1.0~1..HEAD
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
```

Cool, not too much here, just 15 commits. Let’s set up the bisect using the
commands we just learned

```
git bisect start
git bisect bad HEAD (same as git bisect e1952a1c)
git bisect good v1.0 (same as git bisect acf78303)
```

### Running the Bisect

Now we see this output:

```
Bisecting: 6 revisions left to test after this (roughly 3 steps)
[26338040b292e110c2086de6bc42d1c232005a58] Refactor python script with classes
```

In a very helpful output, git is telling us how many different commits we still
need to run through, and is counting down about how many test steps we have
left. The view of our bisect looks something like this right now:







`
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
`




Git has now checked out commit 26338040 for us to test. This commit is
effectively the midpoint between v1.0 and the head of our repo. Let’s run our
python script to see what’s happening.

```
>>> python update.py
Verification failed!
```

We now know things were still bad at commit 26338040. Let’s tell git about that:

```
>>> git bisect bad
Bisecting: 3 revisions left to test after this (roughly 2 steps)
[a2b8a742e16e0f63d47a003bf9ad9b55ab912633] More misc. changes
```

At this point, as expected from a binary search, we’ve knocked out half our
commits, and have one less step to test. Now that we know our midpoint is bad,
git considers everything between our midpoint and HEAD to be bad, looking
something like this:







`
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
`




Future’s already looking brighter. Let’s test it again and tell git the result.

```
>>> python update.py
Verification failed!
>>> git bisect bad
Bisecting: 0 revisions left to test after this (roughly 1 step)
[e0c258c05343202c53a294ba59704bb02565c9d5] Misc. Changes
```

Things were _still_ bad at commit a2b8a742. We’re getting there.

Side note- it’s always great to go through your own git history and see how
incredibly helpful your commit messages were.

Now our view of the world looks like this. As I trudged along through this
bisect, I couldn’t help but feel a particular form of shame at how long things
had been broken...







`
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
`




Self-pity aside, let’s keep going.

```
>>> python update.py
Verification failed!
>>> git bisect bad
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[cecc054a35be79b84241b275253cc0a3a5287dc3] Integrate all the things
```

Just about there... One more step left, and our world will be crystal clear







`
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
`




Now, at long last, let’s test our last commit and tell git.

```
>>> python update.py
Flashing successful!
>>> git bisect good
e0c258c05343202c53a294ba59704bb02565c9d5 is the first bad commit
```

Cool, we found the bad commit, and if we look at our world one last time, we
see exactly where things went bad.







`
e1952a1c Comment flasher files
51ed84b6 Comment main.c
b3a10580 Helpful python error message and traceback
f21a4c55 (tag v1.2) Add comments and static-ize flasher.c
47a89108 Actually improved performance
0afd538f Reverting performance improvements that made things slower
84c98ac9 Performance improvements
26338040 Refactor python script with classes
54526f51 (tag v1.1) Note the work that still needs to be done in the readme
9f0d9a91 Move flash driver to non-memory-mapped
e717c312 Repo linting changes
a2b8a742 More misc. changes
e0c258c0 Misc. Changes
cecc054a Integrate all the things
acf78303 (tag v1.0) Add initialization procedure
`




### Fixing the Bug

As we saw at the end of the last section, our bug seems to have been introduced
with commit e0c258c0. Let’s check that changeset for verification changes...

```diff
/* @brief
 * Verify the given data from NOR flash
 * Return 0 if contents match
 */
static int prv_flasher_verify(void) {
[...]
+ uint8_t readback_data[size];
+ nor_flash_dev->operations.read(sector_to_compare, readback_data, size);
+ int return_code = memcmp((void *) DATA_PAYLOAD_ADDR, readback_data, size);
+ return (return_code == 0)
}
```

Ah, of course! This is an improper checking of `memcmp`’s return code. No wonder
the verification was failing. Looking at the reference for `memcmp`, we should
get 0 as the return code if the contents are the same. We capture this, but
instead of returning that directly, we return a boolean. The boolean value
`true` is usually nonzero under the hood, and thus, this function would return
a nonzero value if the memory matched. Our python script only considers our
verification successful if we return a zero return code.


  
  There is not enough facepalm for a bug like this (Source: Giphy)


Now that we know what the error is, let’s exit git bisect so we can get back to
work. This is the easiest step of the bisect.

```
>>> git bisect reset
```

One quick modification, and we should be all set.

```diff
- int return_code = memcmp((void *) DATA_PAYLOAD_ADDR, readback_data, size);
- return (return_code == 0)
+ return memcmp((void *) DATA_PAYLOAD_ADDR, readback_data, size);
```

With this committed, problem solved!
