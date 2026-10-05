---
id: "ocp-pyts-install-for-development"
type: "concept"
domain: "trace"
title: "pyTS: Install for development"
summary: "Install pyTS itself and its runtime dependencies into the virtual environment in editable mode:"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/pyTS@3433343:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/pyTS/blob/3433343/README.md#install-for-development"
license: "Apache-2.0"
mode: "V"
---

Create a virtual environment for PyTS:

```sh
> python3 -m venv .venv
> source .venv/bin/activate
> which pip
.venv/bin/pip
```

Install pyTS itself and its runtime dependencies into the virtual environment in editable mode:

```sh
> pip install -e .
> which pyts
.venv/bin/pyts
```

Installing test tooling:

```sh
> pip install -e '.[test]'
```

Install type-check tooling:

```sh
> pip install -e '.[lint]'
```

Run tests and strict type checks:

```sh
> pytest -q
> pyright
> mypy
```

### Windows user

Run pip commands with double-quotes, e.g.

```cmd
> .venv/bin/activate.bat
> where pip
.venv/Scripts/pip.exe
> pip install -e ".[test]"
```
