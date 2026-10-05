---
id: "intr-a-shallow-dive-into-gnu-make-invoking-make"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Invoking Make"
summary: "Running make will load a file named Makefile from the current directory and attempt to update the default goal (more on goals later)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#invoking-make"
license: "CC-BY-SA-4.0"
mode: "V"
---

Running `make`  will load a file named `Makefile` from the current directory
and attempt to update the default **goal** (more on goals later).

> Make will search for files named `GNUmakefile`, `makefile`, and `Makefile`, in that
> order

You can specify a particular makefile with the `-f/--file` argument:

```bash
$ make -f foo.mk
```

You can specify any number of *goals* by listing them as positional arguments:

```bash
# typical goals
$ make clean all
```

You can pass Make a directory with the `-C` argument, and this will run Make as if it first `cd`'d into that directory.

```bash
$ make -C some/sub/directory
```

> Fun fact: `git` also can be run with `-C` for the same effect!

### Parallel Invocation

Make can run jobs in parallel if you provide the `-j` or `-l` options. A
guideline I've been told is to set the job limit to 1.5 times the number of
processor cores you have:

```bash
# a machine with 4 cores:
$ make -j 6
```

Anecdotally, I've seen slightly better CPU utilization with the `-l` "load
limit" option, vs. the `-j` "jobs" option. YMMV though!

There are a few ways to programmatically find the CPU count for the current
machine. One easy option is to use the python `multiprocessing.cpu_count()`
function to get the number of threads supported by the system (note on a system
with hyper-threading, this will use up a lot of your machine's resources,
but is probably preferable to letting Make spawn an unlimited number of jobs).

```bash
# call the python cpu_count() function in a subshell
$ make -l $(python -c "import multiprocessing; print(multiprocessing.cpu_count())")
```

{:.no_toc}

#### Output During Parallel Invocation

If you have a lot of output from the commands Make is executing in parallel, you
might see output interleaved on `stdout`. To handle this, Make has the option [`--output-sync`](https://www.gnu.org/software/make/manual/html_node/Parallel-Output.html).

I recommend using **`--output-sync=recurse`**, which will print the entire
output of each target's recipe when it completes, without interspersing other
recipe output.

It also will output an entire recursive Make's output together if your recipe
is using recursive make.
