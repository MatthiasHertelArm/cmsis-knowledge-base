---
id: "x-start-zephyr-project-1"
type: "pattern"
domain: "project"
title: "GCC libc settings for a CMSIS Zephyr application"
status: "draft"
extracted_from: "proc-start-zephyr-project"
source: "project/start-zephyr-project/SKILL.md"
license: "Apache-2.0"
---

When selecting GCC, add the reference project's libc configuration to `blinky/prj.conf`:

CONFIG_NEWLIB_LIBC=y
CONFIG_PICOLIBC=n
CONFIG_PICOLIBC_USE_MODULE=n
CONFIG_MINIMAL_LIBC=n

Do not add these GCC-specific settings when selecting another compiler; retain that compiler's Zephyr libc configuration.
