---
id: "intr-firmware-testing-with-renode-and-g-github-actions-ci-renode"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: GitHub Actions CI & Renode"
summary: "It's now time to plug things into a continuous integration system for automated testing! In a previous post, we wrote about building firmware in CircleCI."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#github-actions-ci-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's now time to plug things into a continuous integration system for automated
testing! In a previous post, we wrote about [building firmware in
CircleCI](https://interrupt.memfault.com/blog/continuous-integration-for-firmware). This
time, we are going to use GitHub Actions to build and test our firmware, as it's
likely the easiest for most people to get up and running.

To start, we'll want to start by creating a file `.github/workflows/main.yml` in
our repo. The `blank` example from GitHub's
[starter-workflows](https://github.com/actions/starter-workflows/blob/master/ci/blank.yml)
gives a quick introduction to how the system works. I've copied it down below
for easy reference.

```yaml
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.
```

### Building Firmware in CI

It's time to adapt the sample above to make it build our firmware. First, we'll
need to make sure that the `checkout` routine clones submodules as well, since
our example repo has a couple of them.

```yaml
jobs:
  build_and_test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
        with: #
          submodules: true # CHANGED
```

Next, we'll want to download and configure the ARM embedded toolchain since it
isn't installed by default. Thankfully, there is already an Action,
[`fiam/arm-none-eabi-gcc`](https://github.com/fiam/arm-none-eabi-gcc), that we
can use to install the toolchain for us.

```yaml
    steps:
    [...]

    # Get the arm-non-eabi-gcc toolchain
    - name: Install arm-none-eabi-gcc
      uses: fiam/arm-none-eabi-gcc@v1
      with:
          release: '9-2019-q4'
```

The last thing we need to do is to invoke `make` itself to start the build.

```yaml
    steps:
    [...]

    - name: Build Firmware
      run: make -j4
```

### Running Renode in CI

The next thing we need to do is to get Renode working in CI. The GitHub Action
runners are standard Linux boxes running Ubuntu. They also have many common
tools installed that you may need, such as Docker, Make, and many more can be
installed using `apt-get`.

For our particular use case, we want to be able to run Renode exactly the same
way locally as we do in GitHub Actions. The easiest way to accomplish this is to
use Docker.

I found a
[small script](https://github.com/tensorflow/tensorflow/blob/eefeac0e116b02dbf2c8de171d5ad9fcb700fccb/tensorflow/lite/micro/testing/test_stm32f4_binary.sh)
in the TensorFlow Micro project which does exactly what I was looking for. This
script builds and runs the official Renode Docker image, the mounts the local
project folder, starts the Renode Robot Framework tests, and outputs the results
to the mounted folder.

I adapted the above file and saved it as
[docker-test.sh](https://github.com/memfault/interrupt-renode-test-automation/blob/master/docker-test.sh).
The beauty of this script is that it can be run locally _or_ in a CI runner!
Therefore, all we need to do in our `main.yml` file is call it.

```yaml
    steps:
    [...]

    - name: Renode Tests
      run: ./docker-test.sh
```

Since the script `docker-test.sh` was configured to output the test artifacts to
the folder `test_results/`, we will want to capture that directory and save it
as an artifact in the CI build.

```yaml
    steps:
    [...]

    - name: Upload Output Directory
      uses: actions/upload-artifact@v2
      with:
        name: Renode Test Results
        path: test_results/
```

### Complete GitHub Action `main.yml`

```yaml
name: Renode Automated Tests

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build_and_test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true

      # Get the arm-non-eabi-gcc toolchain
      - name: Install arm-none-eabi-gcc
        uses: fiam/arm-none-eabi-gcc@v1
        with:
          # The arm-none-eabi-gcc release to use.
          release: "9-2019-q4"

      - name: Build Firmware
        run: make -j4

      - name: Upload ELF
        uses: actions/upload-artifact@v2
        with:
          name: renode-example.elf
          path: build/renode-example.elf

      - name: Renode Tests
        run: ./docker-test.sh

      - name: Upload Output Dir
        uses: actions/upload-artifact@v2
        with:
          name: Renode Test Results
          path: test_results/
```

Now, when we publish a pull-request on GitHub, we'll immediately see that the
build is triggered and our job starts.



  


If we click on "Details", we can watch each job complete in real time! Below we
see that all jobs are successful and that we have two artifacts. One is the ELF
file that was built during the job, and the other is a ZIP archive of the Robot
Framework test results.



  


The best part about using the Robot Framework integration of Renode is that it
generates pretty HTML-based reports, as we saw in the [Introduction to Renode
post](https://interrupt.memfault.com/blog/intro-to-renode#renode--integration-tests).

> I've included the HTML report for the above test.
> [Click here to view it](https://interrupt.memfault.com/misc/test-automation-renode/log.html).
