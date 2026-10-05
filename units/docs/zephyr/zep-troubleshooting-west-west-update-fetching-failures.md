---
id: "zep-troubleshooting-west-west-update-fetching-failures"
type: "concept"
domain: "project"
title: "Troubleshooting West: `west update` fetching failures"
summary: "One good way to troubleshoot fetching issues is to run west update in verbose mode, like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

One good way to troubleshoot fetching issues is to run `west update` in
verbose mode, like this:

```shell

west -v update
```
The output includes Git commands run by west and their outputs. Look for
something like this:

```none

=== updating your_project (path/to/your/project):
west.manifest: your_project: checking if cloned
[...other west.manifest logs...]
--- your_project: fetching, need revision SOME_SHA
west.manifest: running 'git fetch ... https://github.com/your-username/your_project ...' in /some/directory
```
The `git fetch` command example in the last line above is what needs to
succeed.

One strategy is to go to `/path/to/your/project`, copy/paste and run the entire
`git fetch` command, then debug from there using the documentation for your
credential storage helper.

If you're behind a corporate firewall and may have proxy or other issues,
`curl -v FETCH_URL` (for HTTPS URLs) or `ssh -v FETCH_URL` (for SSH URLs)
may be helpful.

If you can get the `git fetch` command to run successfully without prompting
for a password when you run it directly, you will be able to run ``west
update`` without entering your password in that same shell.
