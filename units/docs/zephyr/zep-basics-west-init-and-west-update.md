---
id: "zep-basics-west-init-and-west-update"
type: "concept"
domain: "project"
title: "Basics: west init and west update"
summary: "The two most important workspace-related commands are west init and west update."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/basics.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/basics.rst"
license: "Apache-2.0"
mode: "V"
---

The two most important workspace-related commands are `west init` and ``west
update``.


### `west init` basics


This command creates a west workspace.


**Important:** West doesn't change your manifest repository contents after `west init` is run. Use ordinary Git commands to pull new versions, etc.

You will typically run it once, like this:

```shell

west init -m https://github.com/zephyrproject-rtos/zephyr --mr v2.5.0 zephyrproject
```
This will:

#. Create the topdir, `zephyrproject`, along with
   `.west` and `.west/config` inside it
#. Clone the manifest repository from
   https://github.com/zephyrproject-rtos/zephyr, placing it into
   `zephyrproject/zephyr`
#. Check out the `v2.5.0` git tag in your local zephyr clone
#. Set `manifest.path` to `zephyr` in `.west/config`
#. Set `manifest.file` to `west.yml`

Your workspace is now almost ready to use; you just need to run `west update`
to clone the rest of the projects into the workspace to finish.

For more details, see west-init.


### `west update` basics


This command makes sure your workspace contains Git repositories matching the
projects in the manifest file.


**Important:** Whenever you check out a different revision in your manifest repository, you should run `west update` to make sure your workspace contains the project repositories the new revision expects.

The `west update` command reads the manifest file's contents by:

#. Finding the topdir. In the `west init` example above, that
   means finding `zephyrproject`.
#. Loading `.west/config` in the topdir to read the `manifest.path`
   (e.g. `zephyr`) and `manifest.file` (e.g. `west.yml`) options.
#. Loading the manifest file given by these options (e.g.
   `zephyrproject/zephyr/west.yml`).

It then uses the manifest file to decide where missing projects should be
placed within the workspace, what URLs to clone them from, and what Git
revisions should be checked out locally. Project repositories which already
exist are updated in place by fetching and checking out their respective Git
revisions in the manifest file.

For more details, see west-update.
