---
id: "zep-building-flashing-and-debugging-running-robot-framework-tests-west-robot"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Running Robot Framework tests: `west robot`"
summary: "Currently the command supports only one runner which is using renode-test, (essentially a wrapper for running Robot tests in Renode), but can be easily extended by adding other runners."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

**Tip:** Run `west robot -h` for additional help.


### Basics


Currently the command supports only one runner which is using `renode-test`,
(essentially a wrapper for running Robot tests in Renode), but can be
easily extended by adding other runners.

From a Zephyr build directory, to run a Robot test suite::
```
west robot --runner=renode-robot --testsuite path/to/testsuite.robot
```
This will run all tests from testsuite.robot and print output provided
by Robot Framework.

To pass additional parameters to Renode use `--renode-robot-args` switch.
For example to show Renode logs in addition to Robot Framework's output:

  west robot --runner=renode-robot --testsuite path/to/testsuite.robot --renode-robot-arg="--show-log"


### Runner-Specific Overrides


To view all of the available options for the Robot runners your board
supports, as well as their usage information, use `--context` (or
`-H`)::
```
west robot --runner=renode-robot --context
```
To view all available options "renode-test" runner supports, use::
```
west robot --runner=renode-robot --renode-robot-help
```
