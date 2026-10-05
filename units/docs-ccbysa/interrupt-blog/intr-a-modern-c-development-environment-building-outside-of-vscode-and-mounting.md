---
id: "intr-a-modern-c-development-environment-building-outside-of-vscode-and-mounting"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Building outside of `vscode` and mounting volumes"
summary: "Not everyone is a friend of vscode."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#building-outside-of-vscode-and-mounting-volumes"
license: "CC-BY-SA-4.0"
mode: "V"
---

Not everyone is a friend of `vscode`. All the magic happening behind the scenes in an IDE is not everyone's favorite flavor and it is always good to know how to handle things without an IDE, so I'd like to provide an alternative setup that will also be important once we deal with the GitHub workflow, where we simply have to step out of the comforts of an IDE.

One such magic step that `vscode` does for you - and that we'll now need to do ourselves - is managing the files within the root container. We'll use a [volume](https://docs.docker.com/storage/volumes) to make all files available within the container. At the same time, this makes all modifications that happen *inside* the container also visible *outside* of it. We update our *Dockerfile* with the following commands:

```dockerfile
VOLUME ["/builder/mnt"]
WORKDIR /builder/mnt
```

This defines a volume that we can later use to mount our project directory when executing `docker run`, and the `workdir` instruction tells *Docker* to make this the default path for all future steps. Don't forget to rebuild the image, otherwise, the changes will not be available!

```bash
make builder-build
```

### A note on Docker volumes

As mentioned in the introduction, *Docker* does not behave the same way on all platforms. Only on Linux or when using Windows containers on Windows, containers run "natively" and thus without major penalties. If you're running a Linux container on macOS or Windows - in very simple words - they execute within a VM (though admittedly it is a bit more complicated than that).

The key takeaway is that since the container is executed in a VM, the I/O performance is significantly worse compared to a container that is run natively. For compiled languages or for any process that creates a lot of files, this impact can be significant since the overhead can be up to 100x of what you're experiencing natively. This can lead to longer build or generation times.

Thankfully, *Docker* has provided a good solution for macOS with the `VirtioFS` file-sharing implementation. All you need to do is enable it in your *Docker* configuration:



For Windows, at the time of writing, I don't know of a similar solution so you might have to dig a little deeper in case you run into performance problems. Personally, I've successfully used [docker-sync](https://docker-sync.io/) before, but it is a bit harder to handle.

### Running the development container manually

Now we can run the following command to spin up the container with our project folder mounted as a volume:

```bash
$ docker run \
    --rm \
    -it \
    --platform linux/amd64 \
    --workdir /builder/mnt \
    -v .:/builder/mnt \
    cproject-builder:latest \
    /bin/bash
```

The current directory "`.`" is now available within the container as `/builder/mnt`. And - just like in our development container - we're able to build the project:

```bash
$ rm -rf build

$ cmake -B build
-- The C compiler identification is GNU 10.2.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /builder/mnt/build

$ cmake --build build
Scanning dependencies of target Dummy
[ 50%] Building C object CMakeFiles/Dummy.dir/src/dummy.c.o
[100%] Linking C static library libDummy.a
[100%] Built target Dummy
```

Since the command to spin up the container is rather verbose, I tend to also use a `make` target in my `makefile` for that, such that all I need to type is `make builder-run`:

```makefile
builder-run :
  docker run \
    --rm \
    -it \
    --platform linux/amd64 \
    --workdir /builder/mnt \
    -v .:/builder/mnt \
    $(project_name)-builder:latest \
    /bin/bash
```
