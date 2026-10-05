---
id: "x-start-zephyr-project-3"
type: "concept"
domain: "project"
title: "First west-integrated cbuild run can take several minutes"
status: "draft"
extracted_from: "proc-start-zephyr-project"
source: "project/start-zephyr-project/SKILL.md"
---

Pack installation, initial RTE generation, Zephyr toolchain-cache creation, and the first build can take several minutes, especially on slower computers. Treat limited output as normal while the process remains active. Continue monitoring and do not terminate the process or report a timeout prematurely. Subsequent builds are usually faster because they reuse cached data.
