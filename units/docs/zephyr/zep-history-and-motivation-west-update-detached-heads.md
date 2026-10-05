---
id: "zep-history-and-motivation-west-update-detached-heads"
type: "concept"
domain: "project"
title: "History and Motivation: `west update` detached HEADs"
summary: "The use of detached git HEAD revisions documented in the :ref:update procedure <west-update-procedure> confuses and even frustrates some users."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/why.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/why.rst"
license: "Apache-2.0"
mode: "V"
---

The use of detached git `HEAD` revisions documented in the :ref:`update
procedure <west-update-procedure>` confuses and even frustrates some users.

Specifically, users often ask why `west update` doesn't leave existing local
branches checked out by default.

This section explains why `west update` behaves the way it does by default,
and mentions some other options you have for managing projects that you
modified locally.

Two core requirements for `west update` are:

#. safety: the command should not lose any of the user's work
#. determinism: two users running `west update` on the same manifest should
   get the exact same workspace contents

Using detached HEADs helps preserve safety. As documented in the update
procedure, using `git checkout --detach` on the updated project to get a
detached `HEAD` is a generally safe operation that won't lose the user's
work:

- if your work is all safely committed in a local git branch, that branch
  will be left as-is (see the `git help checkout` output for details)

- if you have uncommitted work, it will be safely kept in your working tree by
  git if that's possible

- if that's not possible, the entire command will fail, and you can decide what
  to do with your work before re-running `west update`

Detached HEADs also help ensure determinism:

- Checking out exactly the project revision that's specified in your manifest
  file is needed to make sure your workspace's files match what's specified in
  the main manifest. If west did not check out the manifest revision by
  default, your workspace could be invisibly different from what you would
  expect given the contents of the manifest files in your working copy. Even
  worse, the way it was different would depend on exactly what was in your
  branch before you ran `west update`.

- There is a subtle interaction with west-manifest-import. If your
  project itself has one or more manifest files that are being imported by
  `west update`, then west needs to check out those files into the working
  tree so it can resolve the entire imported manifest. If `west update` left
  a branch checked out in your project, the manifest files in your working tree
  could be out of date. If west then used those out-of-date files to finish the
  import, the process could fail unexpectedly or produce other nondeterministic
  results.

West does not check out the manifest-rev branch
directly for reasons explained in the documentation for that branch.

This default behavior was chosen a long time ago and it's too late to change it
now, since users are depending on it. However, there are other ways to run
`west update` if this default doesn't work for you. To learn more, run ``west
help update` and read the `checked out branch behavior`` option group text.
For example:

- if you're actively writing some code in your project and you want
  to keep it up to date after potential changes in the upstream manifest,
  use `west update --rebase`

- if you've got some local code you'd like to keep around as long as the
  upstream revision for your project hasn't moved on to something newer, use
  `west update --keep-descendants`

You can use west-aliases if you want to set up a shorter way to type one
of these commands in your workspace. You can also contribute new options to
this option group by sending a pull request to:

https://github.com/zephyrproject-rtos/west
