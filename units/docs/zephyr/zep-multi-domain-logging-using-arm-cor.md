---
id: "zep-multi-domain-logging-using-arm-cor"
type: "concept"
domain: "debug"
title: "Multi-domain logging using ARM Coresight STM"
summary: "The Arm CoreSight SoC-400 is a comprehensive library of components for the creation of debug and trace functionality within a system."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/cs_stm.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/cs_stm.rst"
license: "Apache-2.0"
mode: "V"
---

The Arm CoreSight SoC-400 is a comprehensive library of components for the creation of debug and
trace functionality within a system. The STM (System Trace Macrocell) is a trace source that
is integrated into a CoreSight system, designed primarily for high-bandwidth trace of
instrumentation embedded into software. This instrumentation is made up of memory-mapped writes to
the STMESP (STM Extended Stimulus Port) peripheral registers. Multiple cores can share and directly
access the STM without being aware of each other. Each core has 65536 stimulus ports (identical
register sets) which can be independently accessed thus there is no need for locking when various
contexts want to log the data.
