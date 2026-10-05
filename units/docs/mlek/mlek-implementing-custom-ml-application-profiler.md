---
id: "mlek-implementing-custom-ml-application-profiler"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Profiler"
summary: "The profiler is a helper class that assists with the collection of timings and Ethos-U cycle counts for operations. It uses platform timer to get system timing information."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#profiler"
license: "Apache-2.0"
mode: "V"
---

The profiler is a helper class that assists with the collection of timings and *Ethos-U* cycle counts for operations.
It uses platform timer to get system timing information.

| Method name             | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| `StartProfiling`        | Starts profiling and records the starting timing data.         |
| `StopProfiling`         | Stops profiling and records the ending timing data.            |
| `StopProfilingAndReset` | Stops the profiling and internally resets the platform timers. |
| `Reset`                 | Resets the profiler and clears all collected data.             |
| `GetAllResultsAndReset` | Gets all the results as string and resets the profiler.        |
| `PrintProfilingResult`  | Prints collected profiling results and resets the profiler.    |
| `SetName`               | Set the profiler name.                                         |

An example of it in use:

```C++
/* A named profiler instance */
Profiler profiler{"Inference"};

profiler.StartProfiling();
// Code running inference to profile
profiler.StopProfiling();

profiler.PrintProfilingResult();
```
