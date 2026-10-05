---
id: "intr-tracking-firmware-code-size-keeping-the-code-size-to-a-minimum"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: Keeping the Code Size to a Minimum"
summary: "Up until now, the code sizes we've analyzed had all already been committed to master. If our firmware is out of space today, we'd have to retro-actively refactor or revert these changes, both of which are difficult and time-consuming."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#keeping-the-code-size-to-a-minimum"
license: "CC-BY-SA-4.0"
mode: "V"
---

Up until now, the code sizes we've analyzed had all already been committed to
master. If our firmware is out of space today, we'd have to retro-actively
refactor or revert these changes, both of which are difficult and
time-consuming.

However, if you haven't run out of space yet, or you are looking to keep the
future code space bloat to a minimum, you need to ensure that every new commit
and its code size impact is validated.

The best way I've found to keep code size in check is to calculate how much each
pull-request contributes (or removes!) from the total. Now that we have most of
the data we need, this is possible!

### Code Size Deltas on Pull Requests

To get deltas on pull requests, we'll need CI to run a script whenever one is
published or updated. This script will take the built binary, compute its code
size, and compare it against a given revision or the
`git-merge-base`[^git_merge_base] of the "master" branch. `git-merge-base` takes
both revisions given and finds the most recent common ancestor between the two.
In the case of the Zephyr Project, this is the common ancestor between the base
of a pull-request and the `origin/master` branch.

In our
[example code](https://github.com/memfault/interrupt/tree/master/example/code-size-deltas/codesizes.py),
we have a command, `diff` which will do exactly this.

```python
@cli.command()
@click.argument("binary")
@click.option("--build", default="default")
@click.option("--revision")
def diff(binary, build, revision):
    """
    Calculate the size of the BINARY given, and compare it
    to either the REVISION provided or the "merge-base" of the
    current branch and master for the given BUILD.
    """
    text, data, bss = _calculate_codesize(binary)
    if not revision:
        click.echo("Using `git merge-base` against master branch")
        # git merge-base HEAD master
        revision = _get_merge_base("HEAD", "master")

    codesize = _fetch_codesize(build, revision)
    if not codesize:
        click.echo("No code size for build: {}, revision: {}".format(
            build, revision))
        return

    text_delta = text - codesize.text
    data_delta = data - codesize.data
    bss_delta = bss - codesize.bss

    click.echo("Comparing current binary against: {}".format(revision))
    click.echo(dict(text=text_delta, data=data_delta, bss=bss_delta))
```

Let's try it out! I went digging into the Zephyr Github Pull Requests page for a
large changeset, and found a good candidate:
[Timeout API rework #23382](https://github.com/zephyrproject-rtos/zephyr/pull/23382).

We'll check out the branch and build the firmware first.

```
# Check out the branch for #23382
$ cd zephyrproject/zephyr
$ git remote add pr git@github.com:andyross/zephyr.git
$ git fetch pr
$ git checkout pr/timeout-take-2

# Build the firmware
$ west build -b cc3220sf_launchxl samples/net/lwm2m_client --pristine
```

Next, let's sanity check and ensure that the pull-request is based against a
commit in the last 2,500, which would mean we had uploaded the size.

```
$ git merge-base master HEAD
7c5db4b755f73ab5f93a6456abaa5b97bd6aff7a

$ python ~/codesizes.py fetch 7c5db4b755f73ab5f93a6456abaa5b97bd6aff7a --build lwm2m_client
{'text': 146334, 'data': 4220, 'bss': 41735}
```

Perfect! We have the commit's code size in our database. Let's get the delta.

```
$ python ~/codesizes.py diff build/zephyr/zephyr.elf --build lwm2m_client
Using `git merge-base` against master branch
Comparing code size of current .elf against: 7c5db4b755f73ab5f93a6456abaa5b97bd6aff7a
+---------+--------+-------+-------+
|  Region |  .text | .data |  .bss |
+---------+--------+-------+-------+
|   Local | 146582 |  4220 | 41735 |
| Against | 146334 |  4220 | 41735 |
|   Delta |    248 |     0 |     0 |
+---------+--------+-------+-------+
```

It turns out this pull-request adds roughly 250B to the master branch for our
example firmware build! With this information in hand, the maintainers of the
Zephyr Project can then decide whether the change is worth the bump in the
firmware size. (I'd ✅)

### The Last Mile

This is the end of the tutorial, but I wanted to share with you what I found
works best at the previous companies I've worked for.

- Using Github Actions or the Github API, post a comment on each pull request.
  Something like: 
- Automatically add a firmware lead if the code size delta crosses a set
  threshold.
- Start tracking now. When you run out, it's too late to make changes quickly.

{:.no_toc}
