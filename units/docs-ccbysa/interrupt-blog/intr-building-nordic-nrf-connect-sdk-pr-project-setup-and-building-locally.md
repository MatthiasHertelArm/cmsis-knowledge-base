---
id: "intr-building-nordic-nrf-connect-sdk-pr-project-setup-and-building-locally"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Project Setup and Building Locally"
summary: "To get started, first we need to set up an nRF-Connect SDK project. We'll use the samples/debug/memfault project, because it's one I'm familiar with (I work for Memfault, after all, when I'm not writing Interrupt articles!)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#project-setup-and-building-locally"
license: "CC-BY-SA-4.0"
mode: "V"
---

> Note: This article assumes some familiarity with the nRF-Connect SDK and
> Zephyr build setup. If you're new to the nRF-Connect SDK, check out the
> [Nordic
> documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/2.5.1/nrf/installation.html)
> for details on how to set up a local build environment.

To get started, first we need to set up an nRF-Connect SDK project. We'll use
the
[`samples/debug/memfault`](https://github.com/nrfconnect/sdk-nrf/tree/v2.5.1/samples/debug/memfault)
project, because it's one I'm familiar with (I work for Memfault, after all,
when I'm not writing Interrupt articles!). The same principles apply to any
nRF-Connect SDK-based project, though.

The first thing we'll do is clone the nRF-Connect SDK and initialize the Zephyr
workspace, and confirm we can build this project with our local build
environment (I'm currently using the Zephyr SDK v0.16.4, installed following
these instructions:
<https://docs.zephyrproject.org/latest/getting_started/index.html#set-up-a-development-system>).

> Note: I'm using a Ubuntu Linux host for these examples.

```bash
# create a directory for our project
$ mkdir memfault-nrfconnect-ci
$ cd memfault-nrfconnect-ci
# clone the nRF-Connect SDK. note that we're using the v2.5.1 tag here
$ git clone https://github.com/nrfconnect/sdk-nrf.git nrf -b v2.5.1
# initialize the Zephyr workspace
$ west init -l nrf
# update the Zephyr workspace, downloading all projects selected by the
# manifest. this takes a while!
$ west update
```

Now that we've fetched the nRF-Connect SDK and initialized the Zephyr workspace,
let's build the `memfault` sample project. I'm going to target the
`nrf7002dk_nrf5340_cpuapp` board, because I've got it handy on my desk.

```bash
# running from the root of the Zephyr workspace
$ west build \
  --board nrf7002dk_nrf5340_cpuapp \
  --pristine=always \
  nrf/samples/debug/memfault \
  -- \
  -DCONFIG_MEMFAULT_NCS_PROJECT_KEY=\"DUMMY\"
```

A couple of notes:

- The target project is `nrf/samples/debug/memfault`. This is the path to the
  project relative to the root of the Zephyr workspace.
- We're using the `--pristine=always` option to ensure that we startt with a
  clean build.
- We're passing the `CONFIG_MEMFAULT_NCS_PROJECT_KEY` option to the build
  command, which is a required option for this project that's unset by default.
  Just provide a dummy value here for building the project.

Once we've confirmed the project builds locally, we're almost ready to start
setting up our GitHub Actions workflow.
