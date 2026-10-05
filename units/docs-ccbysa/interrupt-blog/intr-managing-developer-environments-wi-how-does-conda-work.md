---
id: "intr-managing-developer-environments-wi-how-does-conda-work"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: How Does Conda Work?"
summary: "When a developer installs Conda on their computer, a command-line tool called conda becomes available. conda is used to install, manage, and activate the Conda virtual environments."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#how-does-conda-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

When a developer installs Conda on their computer, a command-line tool called
`conda` becomes available. `conda` is used to install, manage, and activate the
Conda virtual environments.

The local Conda environment is kept in sync with a manifest file, typically
called `environment.yml` and revision controlled. It works similarly to a
`requirements.txt` file in Python or `package.json` in the JavaScript world.
This enables a developer to check out **any revision** from the past and
immediately have the proper tools installed to build and debug.

There are also public repositories which host packages built by Anaconda, Inc.
and the community. The two most popular are the self-named Anaconda and
[Conda Forge](https://conda-forge.org/) repositories. Conda Forge is supported
by the community and developers contribute packages through Github, after which
they are built and released for all platforms through their CI/CD system.

When a package, Python or binary, is installed through Conda to a particular
environment, it is placed in a separate "environment" directory (e.g.
`~/miniconda3/envs/example`). To activate these virtual environments, Conda will
edit the shell's `$PATH` variable, prepending it with the directory of the
desired environment. For example, if we activate the `example` environment, the
`$PATH` variable becomes

```
# Activate environment
$ conda activate example

(example)
$ echo $PATH
/Users/tyler/miniconda3/envs/example/bin:...
```

This forces the current shell to look within the above directory _first_ before
searching the default package paths, such as `/usr/bin` or `/usr/local/bin`. For
example, below we print which `make` binary and version is used by the shell,
before and after activating a Conda environment.

```
$ which make && make --version
/usr/bin/make
GNU Make 3.81

# Activate our Conda environment
$ conda activate example

(example)
$ which make && make --version
/Users/tyler/miniconda3/envs/example/bin/make
GNU Make 4.2.1
```

### Common Developer Environment Alternatives

I have found Conda to be the least restrictive and easiest way for firmware
teams to manage developer environments, but let's go through the most popular
alternatives.

#### Docker

Docker is the best way to create developer environments from scratch and for
temporary purposes (such as in continuous integration). A `Dockerfile`, which
commonly lives in a project's repo, defines any and all setup command, such as
downloading and install system packages, installing Python requirements, and
setting up permissions and volumes.

Despite the numerous benefits, Docker is not a great fit for local developer
environments.

- By using Docker, you'll have two file systems, one on the host machine and one
  within the container. Without a large investment in up-front tooling to help
  developers manage the code, build artifacts, debugging tools, and volume
  mounts, it is cumbersome and slow.
- On macOS or Windows, shared volumes have file-sharing performance issues,
  which can cause build times to increase between 2-10x depending on where the
  files live.[^3]
- For developers that like the use of IDE's and other visual tools, a virtual
  machine using VMWare or VirtualBox may be more appropriate.

With all that said, using Docker in your CI system is a no-brainer. Conda and
Docker can even be used _together_, where Docker manages the system image and
low-level setup, and Conda manages all of the packages required to build and
test the firmware.

Check out [this previous Interrupt
post](https://interrupt.memfault.com/blog/continuous-integration-for-firmware) for how to
get up and running quickly with Docker and continuous integration.

#### Included System Package Managers

System package managers, such as Brew, Apt, MinGW, etc., are very good at
installing packages and managing dependencies between them. They are also great
at ensuring that the modern software you use everyday works correctly, safely,
and is kept up-to-date. They are not good at ensuring that the software or
firmware that **you** build continues to work correctly. They are also not good
at juggling multiple versions of packages that aren't the default ones.

It is not uncommon for firmware consultancies or companies to have multiple
different firmware projects in flight. This could be a legacy project and a
newer one. I imagine the following wouldn't be far off:

**Old Project Dependencies:** GNU Make 4.1, GCC 5.4.1, GDB 7.11, Python
3.5

**New Project Dependencies:** GNU Make 4.2.1, GCC 8.3.1, GDB 8.3,
Python 3.6

In the above example, to be able to go back and forth between these two
projects, we'd have to uninstall and reinstall these four packages and their
dependencies. We'd also be taking the risky bet that doing so wouldn't affect
other packages that we have installed.

In an ideal world, you should be able to use `brew upgrade` or
`apt update && apt upgrade` anytime and it wouldn't affect anything related to
the project's firmware build. This is **not possible** when using system package
managers and I strongly advise against using this approach.

#### Virtualenv

Virtualenv works well for managing Python environments and packages, but it
doesn't manage system binaries. It also requires that each Python version be
installed prior to being used in a virtual environment, such as with `pyenv` or
the system package manager.

You can use Virtualenv alongside Conda as well if that is necessary, but it is
not required. Conda is a full replacement for Virtualenv.

#### Virtual Machine

Using a virtual machine is a great way to isolate the environment even more so
that every developer uses a similar environment and is provided with a GUI
and/or IDE. It's also especially useful if everyone has a Linux machine and the
build requires Windows, or vice-versa. However, I still find issues with this
approach.

- Sharing file systems between the host and image has performance issues.
- Using the UI within a virtual machine is generally slower.
- One still would need some sort of environment management with the VM, as
  packages will inevitably change every couple of months.

If a VM is chosen, I suggest using Conda **within it** to help manage the
packages that are used within the VM. Otherwise, the team would have to package
and distribute a new VM image each time a dependency changes, or hope that
everyone knows when and how to update the system (and does it).
