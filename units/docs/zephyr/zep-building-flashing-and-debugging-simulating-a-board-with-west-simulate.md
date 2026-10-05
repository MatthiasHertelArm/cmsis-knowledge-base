---
id: "zep-building-flashing-and-debugging-simulating-a-board-with-west-simulate"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Simulating a board with: `west simulate`"
summary: "Currently the command supports only one runner which is using Renode, but can be easily extended by adding other runners."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

### Basics


Currently the command supports only one runner which is using Renode,
but can be easily extended by adding other runners.

From a Zephyr build directory, to run the built binary::
```
west simulate --runner=renode
```
This will start Renode and configure simulation based on a default `.resc` script
for the current platform with the zephyr.elf file loaded by default. The simulation
then can be started by typing "start" or "s" in Renode's Monitor. This can also be
done by passing a command to Renode, using an argument provided by the runner:

  west simulate --runner=renode --renode-command start

To pass an argument to Renode itself, for example to start Renode in console mode
instead of a separate window:

  west simulate --runner=renode --renode-arg="--console"

From that point on Renode can be used normally in both console and window modes.
For details on using Renode see Renode - documentation.


### Runner-Specific Overrides


To view all of the available options supported by the runners, as well
as their usage information, use `--context` (or `-H`)::
```
west simulate --runner=renode --context
```
To view all available options Renode supports, use::
```
west simulate --runner=renode --renode-help
```
