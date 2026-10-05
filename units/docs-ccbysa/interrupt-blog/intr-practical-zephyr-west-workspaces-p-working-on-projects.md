---
id: "intr-practical-zephyr-west-workspaces-p-working-on-projects"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Working on projects"
summary: "Even though we mostly ignored the inner workings of West, there's one thing that you need to be aware of when working with West workspaces: Except for the manifest repository, West creates and controls a Git branch named …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#working-on-projects"
license: "CC-BY-SA-4.0"
mode: "V"
---

Even though we mostly ignored the inner workings of _West_, there's one thing that you need to be aware of when working with West workspaces: Except for the _manifest repository_, _West_ creates and controls a Git branch named `manifest-rev` in each _project_ and thus for all dependencies.

E.g., let's have a look at the `deps/zephyr` repository that we cloned using _West_ for the modified **Blinky** application in the section ["Zephyr with West"](#zephyr-with-west):

```bash
$ cd deps/zephyr
$ git status
HEAD detached at refs/heads/manifest-rev
nothing to commit, working tree clean
```

We're not on Zephyr's `main` branch nor are we on a detached head at a specific revision - we're on the `manifest-rev` branch that is maintained by _West_.

This is done for all _projects_ in a manifest. The manifest repository itself is not affected since - as we've seen before - West does not touch the manifest repository. This behavior is also explained in the [official documentation](https://docs.zephyrproject.org/latest/develop/west/workspaces.html#west-manifest-rev).

For all other _projects_, however, West creates and manages its own `manifest-rev` branch. It is important that you **do not modify the `manifest-rev` branch** and that you don't push it to your remote since West recreates and resets the `manifest-rev` branch on each execution of `west update` command. Any changes would be **lost**.

Being aware how West manages projects is especially important if you're using _West_ in a ["T3 forest topology"](https://docs.zephyrproject.org/latest/develop/west/workspaces.html#topologies-supported) or, e.g., if you're using a separate repository for shared code. E.g., we could add the following `shared/dummy` project to our workspace:

```bash
manifest:
  # --snip--
  projects:
    # --snip--
    - name: dummy
      revision: main
      url: git@github.com:lmapii/practical-zephyr-t2-dummy.git
      path: shared/dummy
```

In case you need to update such a shared dependency, make sure to push the changes to a new or existing branch, but **don't commit to the `manifest-rev` branch**. Also, after running `west update`, make sure to switch back to your working branch.

This sounds brittle, but it really isn't. It isn't that easy to lose changes to files with a `west update`. Let's see this in action. In case you want to follow along, add your own dummy repository to the manifest - I'll be using the above project in my `west.yml` - a dummy repository that contains an empty `test.txt` file:

```bash
# after adding the "dummy" project to west.yml, update the project
$ west update
$ tree --dirsfirst -a -L 4 --filelimit 10 -I hal
.
├── .west
│   └── config
├── app
├── deps
│   ├── modules
│   └── zephyr
└── shared
    └── dummy
        └── test.txt
```

West does not checkout the repository's `main` branch as specified in the with the `revision: main` entry in the manifest file, but instead uses the local `manifest-rev` branch mentioned before:

```bash
$ cd shared/dummy
$ git status
On branch manifest-rev
nothing to commit, working tree clean
$ cd ../../ # workspace root
```

Without checking out a new branch, I can modify the contents of `test.txt` and run `west update`. The changes won't be lost and `west update` succeeds since the changes are not in conflict with any incoming change:

```bash
$ echo 123-test >> shared/dummy/test.txt
$ west update
...
=== updating dummy (shared/dummy):
--- dummy: fetching, need revision main
From github.com:lmapii/practical-zephyr-t2-dummy
 * branch            main       -> FETCH_HEAD
M       test.txt
HEAD is now at c8deb58 initial commit
...

$ cat shared/dummy/test.txt
123-test
```

The output of `west update` shows me that I have in fact local changes to `test.txt`, but it doesn't reset the file. The changes are not lost.

Since we're using `main` as `revision` for this dependency (e.g., since we're still very much in development), it _could_ happen that someone else is writing to `test.txt`, e.g., the value `not-a-test.` (let's not discuss using development branches etc., I'm just showing _West's_ behavior). Trying to run `west update` with an incoming change leads to an error - the local changes are still not lost:

```bash
$ west update
...
=== updating dummy (shared/dummy):
--- dummy: fetching, need revision main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 229 bytes | 57.00 KiB/s, done.
From github.com:lmapii/practical-zephyr-t2-dummy
 * branch            main       -> FETCH_HEAD
error: Your local changes to the following files would be overwritten by checkout:
        test.txt
Please commit your changes or stash them before you switch branches.
Aborting
...
ERROR: update failed for project dummy
```

OK, time to really try and mess things up: Let's assume we had a long day and we simply forgot that we're changing things in a repository managed by West. We're changing things in `test.txt` and commit the changes to the local `manifest-rev` branch:

```bash
$ cd shared/dummy
$ git add test.txt
$ git commit -m "an honest mistake"
[detached HEAD 8de0853] an honest mistake
 1 file changed, 1 insertion(+)
```

Running `west update` we can indeed see that we're about to lose the commit:

```bash
cd ../../
$ west update
...
=== updating dummy (shared/dummy):
--- dummy: fetching, need revision main
From github.com:lmapii/practical-zephyr-t2-dummy
 * branch            main       -> FETCH_HEAD
Warning: you are leaving 1 commit behind, not connected to
any of your branches:

  8de0853 an honest mistake

If you want to keep it by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> 8de0853

HEAD is now at d22a413 updated test.txt
...
```

Whoops! Git is telling us that we're about to leave behind a commit and at the same time tells us that nothing is lost yet: We can recover the lost change in a new branch by using the proposed command:

```bash
$ cd shared/dummy
$ git branch recover-an-honest-mistake 8de0853
$ git checkout recover-an-honest-mistake
Previous HEAD position was c8deb58 initial commit
Switched to branch 'recover-an-honest-mistake'
$ cat test.txt
this-is-a-test.123-test%
```

Whew! A close call, but even after committing to our local `manifest-rev` branch the changes are not lost an can be restored as instructed by the command line output.

Keep in mind that all _projects_ in a West manifest are managed entirely by _West_. If you're working on those repositories, use dedicated branches. After **every** _West update_, double-check that you're still working on the correct branch and do **not** commit to the `manifest-rev` branch.

Have a look at the official documentation for [`west update`](https://docs.zephyrproject.org/latest/develop/west/built-in.html#west-update). There, you'll find a detailed description of the entire update procedure, including some options that allow you to selectively update projects.
