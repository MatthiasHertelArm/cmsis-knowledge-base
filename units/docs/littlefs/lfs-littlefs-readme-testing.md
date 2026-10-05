---
id: "lfs-littlefs-readme-testing"
type: "concept"
domain: "project"
title: "littlefs README: Testing"
summary: "The littlefs comes with a test suite designed to run on a PC using the emulated block device found in the bd directory. The tests assume a Linux environment and can be started with make:"
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#testing"
license: "BSD-3-Clause"
mode: "V"
---

The littlefs comes with a test suite designed to run on a PC using the
[emulated block device](https://github.com/littlefs-project/littlefs/blob/6cb4e86/bd/lfs_emubd.h) found in the `bd` directory.
The tests assume a Linux environment and can be started with make:

``` bash
make test
```

Tests are implemented in C in the .toml files found in the `tests` directory.
When developing a feature or fixing a bug, it is frequently useful to run a
single test case or suite of tests:

``` bash
./scripts/test.py -l runners/test_runner  # list available test suites
./scripts/test.py -L runners/test_runner test_dirs  # list available test cases
./scripts/test.py runners/test_runner test_dirs  # run a specific test suite
```

If an assert fails in a test, test.py will try to print information about the
failure:

``` bash
tests/test_dirs.toml:1:failure: test_dirs_root:1g12gg2 (PROG_SIZE=16, ERASE_SIZE=512) failed
tests/test_dirs.toml:5:assert: assert failed with 0, expected eq 42
    lfs_mount(&lfs, cfg) => 42;
```

This includes the test id, which can be passed to test.py to run only that
specific test permutation:

``` bash
./scripts/test.py runners/test_runner test_dirs_root:1g12gg2  # run a specific test permutation
./scripts/test.py runners/test_runner test_dirs_root:1g12gg2 --gdb  # drop into gdb on failure
```

Some other flags that may be useful:

```bash
./scripts/test.py runners/test_runner -b -j  # run tests in parallel
./scripts/test.py runners/test_runner -v -O-  # redirect stdout to stdout
./scripts/test.py runners/test_runner -ddisk  # capture resulting disk image
```

See `-h/--help` for a full list of available flags:

``` bash
./scripts/test.py --help
```
