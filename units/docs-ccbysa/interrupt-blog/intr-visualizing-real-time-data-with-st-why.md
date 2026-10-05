---
id: "intr-visualizing-real-time-data-with-st-why"
type: "concept"
domain: "debug"
title: "Visualizing Real-time Data With STMViewer: Why"
summary: "Visualizing process data in the debugging stage of firmware development offers several advantages - consider a scenario where an embedded controller is responsible for monitoring a physical quantity with a sensor."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-15-stm-viewer-debug.md"
doc_source: "https://interrupt.memfault.com/blog/stm-viewer-debug#why"
license: "CC-BY-SA-4.0"
mode: "V"
---

Visualizing process data in the debugging stage of firmware development offers several advantages - consider a scenario where an embedded controller is responsible for monitoring a physical quantity with a sensor. Plotting the data allows us to validate the accuracy of the recorded measurements and identify any sporadic outliers that may occur. Observing data trends over time can detect other issues, such as excessive noise or deviations in readings, especially those arising under specific conditions. Visualizing can lead to a better understanding of a complex control system's behavior, as all variables and their interactions can be easily monitored. Additionally, representing specific software actions' durations and sequences in a digital plot (aka logic analyzer view) can be beneficial when profiling hot code paths or validating the order of asynchronous events.
