---
id: "mlek-noise-reduction-code-sample-post-processing"
type: "concept"
domain: "edge-ai"
title: "Noise Reduction Code Sample: Post-processing"
summary: "After each inference the output of the model is passed to post-processing code which uses the gain values the model produced to generate audio with the noise removed from it."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/noise_reduction.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/noise_reduction.md#post-processing"
license: "Apache-2.0"
mode: "V"
---

After each inference the output of the model is passed to post-processing code which uses the gain values the model
produced to generate audio with the noise removed from it.

For you to verify the outputs of the model after post-processing, you will have manually use an [offline script](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../scripts/py/rnnoise_dump_extractor.py)
to convert the post-processed outputs into a wav file.
This offline script takes a dump file as the input and saves the denoised WAV file to disk. The following is an example
of how to call the script from the command line after running the use-case and
[selecting to dump memory contents](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#dumping-post_processed-results-for-all-inferences).

```commandline
python scripts/py/rnnoise_dump_extractor.py --dump_file <path_to_dump_file.bin> --output_dir <path_to_output_folder>
```

The application for this use case has been written to dump the post-processed output to the address pointed to by
the CMake parameter `noise_reduction_MEM_DUMP_BASE_ADDR`. The default value is set to `0x80000000`.

### Dumping of memory contents from the Fixed Virtual Platform

The fixed virtual platform supports dumping of memory contents to a file. This can be done by
specifying command-line arguments when starting the FVP executable. For example, the argument:

```commandline
$ FVP_Corstone_SSE-300_Ethos-U55 -a ./bin/mlek_noise_reduction.axf \
    --dump cpu0=output.bin@Memory:0x80000000,0x100000
```

Dumps 1 MiB worth of data from address `0x80000000` to the file `output.bin`.

### Dumping post-processed results for all inferences

The Noise Reduction application uses the memory address specified by
`noise_reduction_MEM_DUMP_BASE_ADDR` as a buffer to store post-processed results from all inferences.
The maximum size of this buffer is set by the parameter
`noise_reduction_MEM_DUMP_LEN` which defaults to 1 MiB.

Logging information is generated for every inference run performed. Each line corresponds to the post-processed
result of that inference being written to a certain location in memory.

For example:

```log
INFO - Audio Clip dump header info (20 bytes) written to 0x80000000
INFO - Inference 1/136
INFO - Copied 960 bytes to 0x80000014
...
INFO - Inference 136/136
INFO - Copied 960 bytes to 0x8001fa54
```

In the preceding output we can see that it starts at the default address of
`0x80000000` where some header information is dumped. Then, after the first inference 960 bytes
(480 INT16 values) are written to the first address after the dumped header `0x80000014`.
Each inference afterward will then write another 960 bytes to the next address and so on until all inferences
are complete.

When consolidating all inference outputs for an entire audio clip, the application output should report:

```log
INFO - Output memory dump of 130580 bytes written at address 0x80000000
```

The application output log states that there are 130580 bytes worth of valid data ready to be read
from `0x80000000`. If the FVP was started with the `--dump` option, then the output file is created
when the FVP instance exits.
