---
id: "intr-github-actions-for-stm32cubeide-creating-a-github-actions-workflow"
type: "concept"
domain: "debug"
title: "GitHub Actions for STM32CubeIDE: Creating a GitHub Actions Workflow"
summary: "For those unfamiliar with GitHub Actions, a quick overview can be found at the GitHub Actions documentation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-01-github-actions-for-stm32cubeide.md"
doc_source: "https://interrupt.memfault.com/blog/github-actions-for-stm32cubeide#creating-a-github-actions-workflow"
license: "CC-BY-SA-4.0"
mode: "V"
---

For those unfamiliar with GitHub Actions, a quick overview can be found at the
[GitHub Actions documentation](https://docs.github.com/en/actions).

We're going to create a workflow that does the following:

1. clone the project code
2. run the STM32CubeIDE build commands
3. upload the build artifacts

Before we can start, let's first upload our Docker image to the GitHub Container
Registry. Uploading to the registry will allow us to use the image in our GitHub
Actions workflow.

Pushing the image to the GitHub container registry requires logging in
(instructions
[here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)),
then doing the normal docker push command:

```bash
$ docker push ghcr.io/noahp/stm32wba55-example:2024-08-01
```

Next, we'll open the container URL in our browser
(<https://ghcr.io/noahp/stm32wba55-example>) and set the image to public so our
GitHub Actions workflow can use it without logging in.

Now we're ready to write our GitHub Actions workflow.

### Implementing the Workflow

Our workflow is pretty simple- using the Docker image we just pushed, we'll go
through the steps outlined above.

Here's the workflow file:

```yaml
name: Build STM32 Project

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

  # enable manual triggering
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/noahp/stm32wba55-example:2025-02-24

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          # submodules too
          submodules: recursive

      - name: Build project
        run: |
          /opt/st/stm32cubeide_1.17.0/stm32cubeide --launcher.suppressErrors -nosplash \
            -application org.eclipse.cdt.managedbuilder.core.headlessbuild \
            -data /tmp/stm-workspace \
            -import "STM32CubeIDE"

          /opt/st/stm32cubeide_1.17.0/stm32cubeide --launcher.suppressErrors -nosplash \
            -application org.eclipse.cdt.managedbuilder.core.headlessbuild \
            -data /tmp/stm-workspace \
            -build BLE_p2pServer/Debug

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: BLE_p2pServer.artifacts
          # The output artifacts are BLE_p2pServer.elf, BLE_p2pServer.map, etc.
          # Use a wildcard pattern to get them all
          path: STM32CubeIDE/Debug/BLE_p2pServer.*
```

And that's it! We'll check that into our test project, push it to a branch, and
open a test pull request to see it in action.

(figure: Screenshot of the GitHub Actions workflow running)

We can also download the artifacts from the GitHub Actions UI and confirm the
uploaded files are correct ✅.
