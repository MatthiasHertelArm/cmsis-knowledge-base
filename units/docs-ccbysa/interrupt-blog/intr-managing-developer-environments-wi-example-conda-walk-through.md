---
id: "intr-managing-developer-environments-wi-example-conda-walk-through"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: Example Conda Walk-through"
summary: "In this part of the post, we will set up Conda on our local machine and set up an environment that is able to build, flash, and debug an nRF52 device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#example-conda-walk-through"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this part of the post, we will set up Conda on our local machine and set up
an environment that is able to build, flash, and debug an nRF52 device.

If you'd like to follow along, you may download the Interrupt repo and navigate
to the example directory.

```
$ git clone git@github.com:memfault/interrupt.git
$ cd interrupt/example/conda-developer-environments/
```

> Before we begin, I want to bring comfort to anyone skeptical about installing
> yet another tool. Conda is the opposite of invasive, and everything is
> installed into a single directory, `$HOME/miniconda3` by default. If you want
> to uninstall Conda, deleting that directory will be all that is necessary.

### Installing Conda

To install the `conda` client on a machine, the recommended way is to download
the interactive
[Miniconda installer](https://docs.conda.io/en/latest/miniconda.html) and run it
through `bash`. The following steps apply to both Linux and macOS. If you are
using Windows, there is a Miniconda installer that can be downloaded from the
same page.

```bash
# Download for Mac:
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# Download for Linux:
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# install it
$ bash Miniconda3-latest-*-x86_64.sh
```

The final step in the installer is to make sure the
`$HOME/miniconda3/etc/profile.d/conda.sh` script is loaded in the shell. When
the following prompt is given:

```
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
```

If you'd like Conda to edit your `.bashrc` or `.zshrc` file automatically, you
can say `yes` here. If you do, I suggest running the following command after the
installation is complete so that the base Conda environment won't automatically
activate.

```
$ conda config --set auto_activate_base false
```

If you would rather edit the startup file yourself, add the following line:

```
. "$HOME/miniconda3/etc/profile.d/conda.sh"
```

If everything was successful, after reloading our shell, we can now run the
`conda` command in the shell.

```
$ conda --version
conda 4.7.12
```

### Creating the Environment

The next step is to create an isolated environment in which we can install
packages into. We will create an environment called `example` using Conda's
[`create` command](https://docs.conda.io/projects/conda/en/latest/commands/create.html)

```
$ conda create -n example
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/tyler/miniconda3/envs/example

Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate example
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```

Now, we are able to load up our environment using:

```
$ conda activate example
```

Our current environment has zero packages installed. We can double check this by
running `conda list`.

```
(example)
$ conda list
# packages in environment at /Users/tyler/miniconda3/envs/example:
#
# Name                    Version                   Build  Channel

```

### Configuring the Environment

We want to install the following packages:

- ARM GCC Toolchain (8-2019-q3-update)
- Make (4.2.1)
- Python (3.6)
- nrfutil (6.0.0)

There are two ways to install packages. The first is by installing them directly
with the CLI (e.g. `conda install make`), and the second is by defining them in
a `environment.yml` file, generally placed in the root of the project. We will
use the second method.

There are also multiple repositories to install packages from. The two most
popular ones are "Anaconda" and "Conda Forge". We will use Conda Forge as our
primary repository, since it has more mainstream packages that we as firmware
developers use. We will also add Memfault's Conda repository (memfault), as it
has the ARM GCC package.

To search for packages that can be installed, you can navigate to the
[Conda Forge](https://anaconda.org/conda-forge) repository and browse around. It
is also possible to install community packages built by others, but mileage may
vary.

Below is the `environment.yml` file that contains all of our dependencies.

```yaml
channels:
  - memfault
  - conda-forge
  - defaults
dependencies:
  - make=4.2.1
  - gcc-arm-none-eabi=8.2019.q3.update
  - python=3.6.9
  - pip
  - pip:
      - nrfutil==6.0.0
```

If you'd rather manage your `pip` packages in a separate `requirements.txt`
file, the following should work for the `pip:` section.

```
  - pip:
    - -r requirements.txt
```

### Populating the Environment

With our `environment.yml` file set with all the dependencies, we are ready to
install them! This is done using the `conda env update` command.

```
conda env update -f environment.yml
```

If successful, we'll now have all the packages we defined available on our
`$PATH` and stored within the `~/miniconda3/envs/example` environment directory.

```
$ which make
/Users/tyler/miniconda3/envs/example/bin/make

$ which arm-none-eabi-gdb-py
/Users/tyler/miniconda3/envs/example/bin/arm-none-eabi-gdb-py
```

We are now able to build, flash, and debug as any developer should using `make`,
`arm-none-eabi-gcc`, and `nrfjprog`.

> If any developer joins the team and needs to set up an environment, the only
> two things they would need to do is install Conda and run
> `conda create -n my_env -f environment.yml` in the project. Easy, right!?

### Adding Another Package

Let's assume we have 10 engineers working on our project distributed across the
globe. We also have a problem where our firmware builds are slowing down, and
we'd like to speed them up. A clever engineer realized that we could be using
`ccache` to locally cache built object files between subsequent builds. This
speeds up our firmware build by 50%, which is a huge win!

We want _everyone_ to have `ccache` installed and to use it with every build. We
could send out an email to the team, mention it in Slack, and maybe even error
out in the Makefile if we see the developer does not have it installed. All
these methods are tedious and not 100% reliable.

Since every developer on the project is using Conda at this point, we can add an
entry for `ccache` in our `environment.yml` and this becomes trivial.

```yaml
dependencies:
  # System Packages
  ...
  - ccache
```

The next time a developer runs `conda env update`, they'll have `ccache`
available on their `PATH` and can start using it immediately.

```
$ conda env update -f environment.yml
$ which ccache
/Users/tyler/miniconda3/envs/test/bin/ccache
```
