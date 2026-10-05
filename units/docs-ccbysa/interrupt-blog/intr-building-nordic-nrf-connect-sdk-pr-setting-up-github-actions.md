---
id: "intr-building-nordic-nrf-connect-sdk-pr-setting-up-github-actions"
type: "concept"
domain: "debug"
title: "Building Nordic nRF-Connect SDK Projects with GitHub Actions: Setting up GitHub Actions"
summary: "The first thing we'll need to do is create a new GitHub Actions workflow file:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-18-ncs-github-actions.md"
doc_source: "https://interrupt.memfault.com/blog/ncs-github-actions#setting-up-github-actions"
license: "CC-BY-SA-4.0"
mode: "V"
---

> Note: this quickstart guide is helpful for some guidance on setting up GitHub
> Actions. We'll assume a little familiarity with the basics of GitHub Actions
> going forward: <https://docs.github.com/en/actions/quickstart>

The first thing we'll need to do is create a new GitHub Actions workflow file:

```bash
# from within our memfault-nrfconnect-ci-app project directory
$ mkdir -p .github/workflows
$ touch .github/workflows/ci.yml
```

All we'll put in the file for now is a basic workflow that runs on every push
and pull request targeting the `main` branch, and just clones our repository:

```yaml
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

The last thing we'll do here is make it possible to manually trigger our
workflow, by adding the `workflow_dispatch` event trigger:

```yaml
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main
  workflow_dispatch:
```

This can be useful for testing changes without requiring a commit, for example
if we're iterating on a custom Docker image used by the workflow. You can
manually trigger the run from the GitHub Actions UI (instructions
[here](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow)), or the `gh` cli also supports triggering the workflow:

```bash
$ gh workflow run ci.yml
```

After pushing `ci.yml`, we can go to the "Actions" tab in our GitHub repository, and we should see our
workflow successfully run:


