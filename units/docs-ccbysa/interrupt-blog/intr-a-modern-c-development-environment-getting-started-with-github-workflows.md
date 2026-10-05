---
id: "intr-a-modern-c-development-environment-getting-started-with-github-workflows"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Getting started with GitHub workflows"
summary: "We've gotten quite far already, and this setup is way beyond the \"works on my machine\" type of environment. All of your contributors can now build a development container and execute all steps to build or test your project."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#getting-started-with-github-workflows"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've gotten quite far already, and this setup is way beyond the "works on my machine" type of environment. All of your contributors can now build a development container and execute all steps to build or test your project. There is one more thing that we should do to keep the project stable even if we're not actively working on it: setting up a pipeline that periodically ensures that the environment still works.

Continuously testing and checking your code is important. Pipelines are now available on all major platforms such as [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [Bitbucket](https://bitbucket.org/). In this article, we'll set up a [GitHub action](https://github.com/features/actions) which periodically builds our image and tests our code.

There's yet another catch though: Ensuring that your Docker images build and using those Docker images in your pipeline can sometimes be a bit tedious. At the time of writing, GitHub has support for so-called [container actions](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action) that allow executing pipeline steps inside a Docker container. These steps, however, assume that the image exists on some registry, e.g., [dockerhub](https://hub.docker.com/), and is not built within the action itself.

Since nowadays [dockerhub](https://hub.docker.com/) is no longer entirely free to use, we will still try to execute all steps within a Docker image that is built as part of the pipeline. This makes the pipeline steps less elegant and very verbose, but I'll choose this approach over having to use multiple actions or a container registry.

### Adding a GitHub action

GitHub actions are added `.yml` workflow files in the `.github/workflows` directory of the repository. We'll name our workflow file [`ci.yml`](https://github.com/lmapii/cproject/blob/main/.github/workflows/ci.yml):

```yml
name: ci
on:
  push:
    branches:
    - main
  schedule:
    - cron: '0 1 * * 0'
jobs:
  # empty
```

With the above configuration, the jobs in this action are executed [at 01:00 every Sunday](https://crontab.guru/#0_1_*_*_0) and on every push to the `main` branch.

### Building an image in a GitHub action

Building a Docker image in your pipeline is quite straightforward due to the existing GitHub actions:

```yml
jobs:
  docker-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
        name: Build builder-image
        with:
          context: .
          file: builder.Dockerfile
          tags: cproject-builder:latest
  build-and-test:
    needs: docker-build
    # TODO: needs cproject-builder:latest
```

The problem is that all jobs are isolated and that data *including Docker images* must be shared explicitly between jobs. Without sharing, `cproject-builder:latest` is not available in the next job `build-and-test`.

### Using caches to share images between jobs

The [proposed solution by Docker](https://docs.docker.com/build/ci/github-actions/share-image-jobs/) is to share an image using *artifacts*. Artifacts are files that can be stored in steps in a GitHub action and thus be downloaded in a subsequent step. For our builder image this is very problematic since the builder image is very large:

- Uploading the image takes a very long time.
- Artifact count towards the storage limit in your GitHub plan. A free plan only has 500 MB of storage.
- Downloading the image in subsequent steps also takes a very long time.

My favorite solution for this problem is using [cache dependencies](https://github.com/actions/cache). Similar to the proposed solution by Docker, we build the image and store it in a file, which is then accessible using a *cache*. Another benefit of this approach is, that for subsequent actions and if the *Dockerfile* did not change, the image is not rebuilt!



```yml
jobs:
  docker-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      -
        name: Create docker cache folder
        run: mkdir -p /tmp/docker
      -
        name: Restore docker image
        id: cache-docker
        uses: actions/cache@v4
        with:
          path: /tmp/docker
          key: ${{ runner.os }}-docker-${{ hashFiles('builder.Dockerfile') }}
      -
        name: Build docker builder-image
        if: steps.cache-docker.outputs.cache-hit != 'true'
        uses: docker/build-push-action@v5
        with:
          context: .
          file: builder.Dockerfile
          tags: cproject-builder:latest
          outputs: type=docker,dest=/tmp/docker/${{ runner.os }}-builder-image.tar
```



At the time of writing caches do **not** count towards the storage limit of your GitHub account. The only downside that I've encountered, is that caches are not shared between actions of different branches and that you'll need to manage your caches in case you have too many branches using images.

### Using the cached image to build the project

In the next job, we load the builder image and execute our actions. As mentioned before, the image is not available yet and therefore we cannot use the much more elegant GitHub actions for containers. It does, however, do its job and does so efficiently since restoring a cache takes much less time than downloading an artifact:



```yml
jobs:
  docker-build:
    # <snip>
  build-and-test:
    runs-on: ubuntu-latest
    needs: docker-build
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      -
        name: Restore docker image
        id: cache-docker
        uses: actions/cache@v4
        with:
          path: /tmp/docker
          key: ${{ runner.os }}-docker-${{ hashFiles('builder.Dockerfile') }}
      -
        name: Load image
        run: |
          docker load --input /tmp/docker/${{ runner.os }}-builder-image.tar
          docker image ls -a
      -
        name: Build library
        run: |
          docker run \
            --rm \
            --platform linux/amd64 \
            --workdir /builder/mnt \
            -v ${{ github.workspace }}:/builder/mnt \
            cproject-builder:latest \
            /bin/bash -c "rm -rf build; cmake -B build; cmake --build build"
```



This job needs the previous `docker-build` to pass, then restores the docker image from the cache and builds the project within the image using `cmake`. Here the downside of this approach is visible: We always need to use the entire `docker run` command to execute our steps.

### Running the tests and storing the coverage report as an artifact

We can now run the same commands that we used previously to run the unit tests with coverage and generate our coverage report. In addition, we can store this coverage report as an artifact in our pipeline such that we can download it after any successful run.



```yml
jobs:
  docker-build:
    # <snip>
  build-and-test:
    runs-on: ubuntu-latest
    needs: docker-build
    steps:
      # <snip>
      -
        name: Test library
        run: |
          docker run \
            --rm \
            --platform linux/amd64 \
            --workdir /builder/mnt/tests/unittest \
            -v ${{ github.workspace }}:/builder/mnt \
            cproject-builder:latest \
            /bin/bash -c "ceedling clobber; ceedling gcov:all; ceedling utils:gcov"
      -
        name: Archive coverage results
        shell: bash
        run: |
          staging="reports-${{github.run_number}}"
          mkdir -p "$staging"
          cp -r tests/unittest/build/artifacts/gcov "$staging"
          tar czf "$staging.tar.gz" "$staging"
          echo "ASSET=$staging.tar.gz" >> $GITHUB_ENV
      -
        name: Archive artifacts
        uses: actions/upload-artifact@v4
        with:
          name: reports-${{github.run_number}}
          path: ${{ env.ASSET }}
          retention-days: 3
```



Never forget to specify a retention period for your artifacts, since otherwise, it is very easy to hit the storage limit of your GitHub plan.
