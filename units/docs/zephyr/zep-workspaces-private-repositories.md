---
id: "zep-workspaces-private-repositories"
type: "concept"
domain: "project"
title: "Workspaces: Private repositories"
summary: "You can use west to fetch from private repositories. There is nothing west-specific about this."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/workspaces.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/workspaces.rst"
license: "Apache-2.0"
mode: "V"
---

You can use west to fetch from private repositories. There is nothing
west-specific about this.

The `west update` command essentially runs `git fetch YOUR_PROJECT_URL`
when a project's `manifest-rev` branch must be updated to a newly fetched
commit. It's up to your environment to make sure the fetch succeeds.

You can either enter the password manually or use any of the `credential
helpers built in to Git`_. Since Git has credential storage built in, there is
no need for a west-specific feature.

The following sections cover common cases for running `west update` without
having to enter your password, as well as how to troubleshoot issues.


### Fetching via HTTPS


On Windows when fetching from GitHub, recent versions of Git prompt you for
your GitHub password in a graphical window once, then store it for future use
(in a default installation). Passwordless fetching from GitHub should therefore
work "out of the box" on Windows after you have done it once.

In general, you can store your credentials on disk using the "store" git
credential helper. See the git-credential-store manual page for details.

To use this helper for all the repositories in your workspace, run:

```shell

west forall -c "git config credential.helper store"
```
To use this helper on just the projects `foo` and `bar`, run:

```shell

west forall -c "git config credential.helper store" foo bar
```
To use this helper by default on your computer, run:

```shell

git config --global credential.helper store
```
On GitHub, you can set up a personal access token to use in place of your
account password. (This may be required if your account has two-factor
authentication enabled, and may be preferable to storing your account password
in plain text even if two-factor authentication is disabled.)

You can use the Git credential store to authenticate with a GitHub PAT
(Personal Access Token) like so:

```shell

echo "https://x-access-token:$GH_TOKEN@github.com" >> ~/.git-credentials
```
If you don't want to store any credentials on the file system, you can store
them in memory temporarily using git-credential-cache instead.

If you setup fetching via SSH, you can use Git URL rewrite feature. The following
command instructs Git to use SSH URLs for GitHub instead of HTTPS ones:

```shell

git config --global url."git@github.com:".insteadOf "https://github.com/"
```

### Fetching via SSH


If your SSH key has no password, fetching should just work. If it does have a
password, you can avoid entering it manually every time using ssh-agent.

On GitHub, see Connecting to GitHub with SSH for details on configuration
and key creation.
