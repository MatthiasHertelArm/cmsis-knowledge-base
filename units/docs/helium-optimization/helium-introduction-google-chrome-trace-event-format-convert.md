---
id: "helium-introduction-google-chrome-trace-event-format-convert"
type: "concept"
domain: "optimization"
title: "Introduction: FVP/AVH/IPX model TARMAC Trace post-processing / Google Chrome Trace Event Format converter"
summary: "Part of: FVP/AVH/IPX model TARMAC Trace post-processing"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#google-chrome-trace-event-format-converter"
license: "Apache-2.0"
mode: "V"
---

_Part of: FVP/AVH/IPX model TARMAC Trace post-processing_

Google Chrome embeds a trace viewer, accessed via
chrome://tracing URL, which allows interactive navigation through
a profiling trace enabling easy understanding of cycle repartition and
hot-spots identification.

Trace format is a JSON file with contains basic information regarding
function start, end and duration and can be amended with additional side
information like markers, counters, and others. It can also contain
several trace sources which can be presented in the same timeline
provided these are using a similar time base. This can be useful to
track optimization iterations and confirm performance gains using the
same timeline.

The format documentation can be found in:

[Trace Event Format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview#heading=h.yr4qxyxotyw)

*Note:*
The Chrome Trace Event Profiling Format and Tool, originaly part of the Catapult performance tools, is considered as end of life and there is no more active development on it.
It has been superseded by https://ui.perfetto.dev/, which still accept original JSON format.


By processing TARMAC trace in correlating program counter with function
name, a JSON output containing function name, function start timestamp
and duration can be generated.

A utility python script can be found in [arm_tarmac_2_chrometracing.py](https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/tools/arm_tarmac_2_chrometracing.py).
This one consumes a symbol file allowing to correlate TARMAC program counter and local function, and TARMAC log.

Example:
```shell
# symbol file extraction
fromelf -s audiomark_app.axf > audiomark_app_sse300.sym
# conversion
python arm_tarmac_2_chrometracing.py audiomark_app_sse300.sym audiomark_app_sse300.tarmac audiomark_app_sse300.json
```


An extract of such JSON trace can be found below:

```json
{"name": "__aeabi_memclr8           ", "cat": "arm", "ph": "X", "ts": 36316968.000, "dur": 8992.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_mult_f32              ", "cat": "arm", "ph": "X", "ts": 36329964.000, "dur": 3612.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_copy_f32              ", "cat": "arm", "ph": "X", "ts": 36333632.000, "dur": 2588.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_cfft_f32              ", "cat": "arm", "ph": "X", "ts": 36336320.000, "dur": 19720.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_rfft_fast_f32         ", "cat": "arm", "ph": "X", "ts": 36336240.000, "dur": 28268.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_scale_f32             ", "cat": "arm", "ph": "X", "ts": 36364576.000, "dur": 2600.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "spx_fft                   ", "cat": "arm", "ph": "X", "ts": 36333588.000, "dur": 33588.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_cmplx_mag_squared_f32 ", "cat": "arm", "ph": "X", "ts": 36367200.000, "dur": 2376.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "filterbank_compute_bank32 ", "cat": "arm", "ph": "X", "ts": 36369600.000, "dur": 5616.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "preprocess_analysis       ", "cat": "arm", "ph": "X", "ts": 36325980.000, "dur": 49236.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "update_noise_prob         ", "cat": "arm", "ph": "X", "ts": 36375224.000, "dur": 9212.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "filterbank_compute_bank32 ", "cat": "arm", "ph": "X", "ts": 36390148.000, "dur": 5616.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "expf                      ", "cat": "arm", "ph": "X", "ts": 36428904.000, "dur": 288.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "filterbank_compute_psd16  ", "cat": "arm", "ph": "X", "ts": 36440180.000, "dur": 5420.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "filterbank_compute_psd16  ", "cat": "arm", "ph": "X", "ts": 36445616.000, "dur": 5420.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "filterbank_compute_psd16  ", "cat": "arm", "ph": "X", "ts": 36451052.000, "dur": 5420.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_cmplx_mult_real_f32   ", "cat": "arm", "ph": "X", "ts": 36510512.000, "dur": 4644.000, "pid": 1, "tid": 1,  "args": {}},
{"name": "arm_cfft_f32              ", "cat": "arm", "ph": "X", "ts": 36548388.000, "dur": 20244.000, "pid": 1, "tid": 1,  "args": {}},
...
```

An additional tool, [arm_json_merge.py](https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/tools/arm_json_merge.py), allows to merge multiple JSON trace logs and align timestamps in a single timeline to ease comparison.
This can be used to compare several optimized code bases, visualize effects of NPU acceleration or to compare behaviour on different platforms.

As an example, this command allows to merge 2 JSON traces with Audiomark running with Ethos U55-128 acceleration and Audiomark running on CM55 only,

```shell
# capture 2nd occurence of the ee_audiomark symbol inside audiomark_cm55_only and audiomark_cm55_with_u55 traces
python arm_json_merge.py ee_audiomark 2 audiomark_sse300_vs_sse310.json audiomark_cm55_only.json  audiomark_cm55_with_u55.json
```

Here is the extract of the resulting JSON merged trace:

```json
 {"name": "ethosu_mutex_lock         ", "cat": "arm", "ph": "X", "ts": 525127.0, "dur": 4.001, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "ethosu_semaphore_give     ", "cat": "arm", "ph": "X", "ts": 525181.0, "dur": 6.9999999996, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "ethosu_mutex_unlock       ", "cat": "arm", "ph": "X", "ts": 525192.0, "dur": 4.001, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "ethosu_release_driver     ", "cat": "arm", "ph": "X", "ts": 525123.009, "dur": 83.9999999991, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "_ZN6tflite26SingleArenaBufferAllocator20IsAllTempDeallocatedEv", "cat": "arm", "ph": "X", "ts": 525295.0, "dur": 8.002, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "_ZN6tflite26SingleArenaBufferAllocator20ResetTempAllocationsEv", "cat": "arm", "ph": "X", "ts": 525276.0, "dur": 46.002, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "_ZN6tflite14MicroAllocator20ResetTempAllocationsEv", "cat": "arm", "ph": "X", "ts": 525257.0, "dur": 65.002, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "_ZN6tflite19GetCurrentTimeTicksEv", "cat": "arm", "ph": "X", "ts": 525350.0, "dur": 59.0, "pid": 1, "tid": "m55_u55_128.json", "args": {}},
 {"name": "_ZN6tflite5micro12GetEvalInputEPK13TfLiteContextPK10TfLiteNodei", "cat": "arm", "ph": "X", "ts": 412093.99999999953, "dur": 37.005, "pid": 1, "tid": "m55_only.json", "args": {}},
 {"name": "_ZN6tflite12MicroContext13GetEvalTensorEi", "cat": "arm", "ph": "X", "ts": 412160.99999999953, "dur": 5.001, "pid": 1, "tid": "m55_only.json", "args": {}},
 {"name": "_ZN6tflite25MicroContextGetEvalTensorEPK13TfLiteContexti", "cat": "arm", "ph": "X", "ts": 412148.99999999953, "dur": 16.9999999999, "pid": 1, "tid": "m55_only.json", "args": {}},
 {"name": "_ZN6tflite5micro13GetEvalOutputEPK13TfLiteContextPK10TfLiteNodei", "cat": "arm", "ph": "X", "ts": 412138.99999999953, "dur": 27.002, "pid": 1, "tid": "m55_only.json", "args": {}},
 {"name": "_ZN6tflite16TfLiteTypeSizeOfE10TfLiteTypePj", "cat": "arm", "ph": "X", "ts": 412169.99999999953, "dur": 19.0, "pid": 1, "tid": "m55_only.json", "args": {}},
 {"name": "_ZN6tflite12ElementCountERK14TfLiteIntArray", "cat": "arm", "ph": "X", "ts": 412195.99999999953, "dur": 40.0, "pid": 1, "tid": "m55_only.json", "args": {}},
```

The trace analyzer can access cycle repartition over a selected region
(interactive with the mouse) and allows determine complexity breakdown
over this region for example DSP front-end, or individual component like
ABF.






Another interesting transform consists of grouping adjacent PC
instructions into bins and generating histogram. Histogram samples
are assigned not to functions, but to individual instructions or block
of instructions (containing cumulated duration). Relating program
counter to source code (addr2line) allows to generate gprof-like
line-by-line profiling.
