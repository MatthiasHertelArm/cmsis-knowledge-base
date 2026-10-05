---
id: "intr-practical-zephyr-west-workspaces-p-installing-west"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Creating a workspace from scratch / Installing west"
summary: "Part of: Creating a workspace from scratch"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#installing-west"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Creating a workspace from scratch_

We've been using [West](https://docs.zephyrproject.org/latest/develop/west/index.html) a lot now to build, debug and flash our project. It comes bundled with the [nRF Connect SDK](https://www.nordicsemi.com/Products/Development-software/nrf-connect-sdk), so until now, we didn't have to install it at all. Without sourcing any paths, e.g., from a `setup.sh` script that we created at the very beginning of this article series, I don't have _West_ installed:

```bash
$ west --version
zsh: command not found: west
```

The first thing to even get started is therefore installing West, which is available as a `python` package. Instead of following the [official documentation](https://docs.zephyrproject.org/latest/develop/west/install.html) and installing _West_ globally, I'll be using `pipenv` to manage an environment for me:

```bash
$ pwd
$ path/to/workspace
$ touch Pipfile
```

In my `Pipfile`, I can simply add `west` as a `dev-package`, since I won't be needing it for any `python` application or extension:

```ini
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[dev-packages]
autopep8 = "*"
pylint = "*"
west = "1.5"

[requires]
python_version = "3.11"
```

All that's left to do is to install the environment and activate the shell, and we have _West_ available:

```bash
workspace $ pip install pipenv
workspace $ pipenv install --dev
workspace $ pipenv shell
(workspace) workspace $ west --version
West version: v1.5.0
```

In the remainder of this article, I won't explicitly refer to the `python` environment or _West_ installation anymore. It is up to you to decide which approach to use, e.g., installing _West_ globally, using [`pipenv`](https://pipenv.pypa.io/), [`venv`](https://docs.python.org/3/library/venv.html), [`poetry`](https://python-poetry.org/), or maybe you're using one Zephyr's [docker images](https://github.com/zephyrproject-rtos/docker-image) - whatever works best for you!
