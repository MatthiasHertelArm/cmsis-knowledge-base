---
id: "intr-managing-developer-environments-wi-creating-your-own-conda-packages"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: Creating Your Own Conda Packages"
summary: "There is a high chance that all packages required by your project, team, or developers are not yet built for Conda and hosted on the Conda Forge repository. Fret not, as building and publishing Conda packages is relatively simple."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#creating-your-own-conda-packages"
license: "CC-BY-SA-4.0"
mode: "V"
---

There is a high chance that all packages required by your project, team, or
developers are not yet built for Conda and hosted on the Conda Forge repository.
Fret not, as building and publishing Conda packages is relatively simple. We'll
quickly walk through how I built and published the `gcc-arm-none-eabi` package
that is hosted [here](https://anaconda.org/memfault/gcc-arm-none-eabi) and built

[ARM GNU Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).

Creating a package for this toolchain is straight-forward since the binaries are
already built for each platform. All we need to do is download the tarball,
extract it, and copy the contents into a Conda package.

> If you want to jump ahead and look at the final recipe, it is hosted in
> Memfault's
> [conda-recipes Github repo](https://github.com/memfault/conda-recipes/tree/master/gcc-arm-none-eabi).

### Creating the Build Environment

The first thing we need to do is create an environment which has `conda-build`
and `anaconda-client` installed, both of which will be used to build and publish
our package.

```
# Create the Conda Environment we'll use for building
$ conda create -n build

# Activate the environment called `build`
$ conda activate build

# Install the necessary packages to build and publish Conda packages
(build)
$ conda install conda-build anaconda-client
```

Now we'll want to create an empty directory, with a single `meta.yaml` file
within it.

```
$ mkdir /tmp/arm-none-eabi-gcc && cd /tmp/arm-none-eabi-gcc
$ touch meta.yaml
```

### Defining the `meta.yaml` File

Next, we'll set up our `meta.yaml` file with the following information, with
each field described below. The definition is small because we are merely
repackaging binaries.

```yaml
package:
  name: gcc-arm-none-eabi
  version: 8.2019.q3.update

source:
  url: https://developer.arm.com/-/media/Files/downloads/gnu-rm/8-2019q3/RC1.1/gcc-arm-none-eabi-8-2019-q3-update-mac.tar.bz2 # [osx]
  sha256: fc235ce853bf3bceba46eff4b95764c5935ca07fc4998762ef5e5b7d05f37085 # [osx]

build:
  string: "0"

test:
  commands:
    - arm-none-eabi-gcc --version
```

- `package`: This is the Name and Version of the Conda package that we are
  building. e.g. if we are building Make 4.2.1 for Conda, then Name would be
  "Make" and Version would be "4.2.1".
- `source`: This is either the fields `url` and `sha256` which points to a Zip
  or Tarball containing the source code or binaries, or it can also reference a
  Git repository using the `git_url` and `git_rev` fields.
- `build`: This is the build identifier. If a user publishes a package but it
  was built incorrectly, they would use a new version of this identifier when
  they re-publish the package. A monotonically increasing integer or a random
  hash is appropriate.
- `test`: These are test commands to run against the package once it is build.
  In our example above, we have the package print out the version.

For information about all the fields in the `meta.yaml` file, reference
[this documentation page](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html)

### Writing the build script `build.sh`

The last thing we need is to define a `build.sh` file. This script will be run
after the build completes, and is responsible for building and moving the
necessary binaries and supporting files to the directory that will be packaged
up.

If we download and extract the toolchain from the ARM website, the folder
structure is as follows:

```
gcc-arm-none-eabi-8-2019-q3-update
├── arm-none-eabi
├── bin
├── lib
└── share
```

We'll want to copy **all** of these directories into our Conda package, so our
script is simply

```
#!/usr/bin/env bash
cp -R $SRC_DIR/* $PREFIX
```

`SRC_DIR` is the directory where the source files were extracted to, and
`PREFIX` is the build prefix to which the build script should install the
resulting files. For more variables exported during the build process, reference
[this page](https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html#environment-variables-set-during-the-build-process).

### Building and Publishing the Package

We've finished setting up our package metadata, so now it's time to build and
publish it. To build the package, we run

```
(build)
$ conda build .
```

This will download our source tarball from the ARM website, verify the checksum,
extract the contents, and then, using the `build.sh` script, copy the contents
to the package working directory, which it will then compress back into a
tarball into a Conda package!

After the build finishes, the command will output another command starting with
`anaconda upload ...` which you can use to publish this new Conda package under
your own personal repository.

However, before publishing a package, I generally like to confirm it works in a
clean Conda environment on my local machine. We can do this by pointing to our
`build` environments local repository and specifying the package name
`gcc-arm-none-eabi` when installing the package.

```
(build)
$ conda deactivate
$ conda create -n test
$ conda activate test
(test)
$ conda install -c $HOME/miniconda3/envs/build/conda-bld/ gcc-arm-none-eabi
```

After the package is installed, we can verify it's in our new Conda environment
and can run the `--version` command

```
$ which arm-none-eabi-gcc
/Users/tyler/miniconda3/envs/test/bin/arm-none-eabi-gcc
(test)
$ arm-none-eabi-gcc --version
arm-none-eabi-gcc (GNU Tools for Arm Embedded Processors 8-2019-q3-update) ...
```

It works! Now we can publish it using the `anaconda upload ...` command printed
previously in the terminal.

> NOTE: It is also possible to automate this test procedure by adding test
> scripts. The
> [Conda docs](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#test-section)
> are a great place to start and
> [here](https://github.com/memfault/conda-recipes/blob/master/gcc-arm-none-eabi/meta.yaml#L16-L18)
> is an example which performs the steps above.

This was by no means a comprehensive tutorial of how to build a Conda package,
so I suggest reading the following references if you want to learn more.

- [Building conda packages from scratch](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html)
- [Defining metadata (meta.yaml)](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html)
- [Build scripts (build.sh, bld.bat)](https://docs.conda.io/projects/conda-build/en/latest/resources/build-scripts.html)

If you want to look at a more detailed recipe, I've also published a Conda
recipe that builds and packages the popular C++ unit testing framework
CppUTest[^4]
[on Github](https://github.com/memfault/conda-recipes/tree/master/cpputest)

{:.no_toc}
