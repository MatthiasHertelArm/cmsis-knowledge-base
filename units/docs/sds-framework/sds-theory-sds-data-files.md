---
id: "sds-theory-sds-data-files"
type: "concept"
domain: "test"
title: "theory: SDS Data Files"
summary: "Each data stream is stored in a separate SDS data file. In the diagram below SCinput.0.sds is the input to Signal Conditioning, SCoutput.0.sds is the output of Signal Conditioning, and MLoutput.0.sds is the output of the ML Model."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#sds-data-files"
license: "Apache-2.0"
mode: "V"
---

Each data stream is stored in a separate SDS data file. In the diagram below `SCinput.0.sds` is the input to Signal Conditioning, `SCoutput.0.sds` is the output of Signal Conditioning, and `MLoutput.0.sds` is the output of the ML Model. Each execution of the algorithm is represented by a data block with a `timeslot`. The `timeslot` allows correlating blocks from different streams.

All data blocks of one algorithm execution have the same timeslot value as shown below:

(figure: SDS Files)

- Each call to the function `sdsWrite` writes one complete data block.
- Each call to the function `sdsRead` reads one complete data block.

### File Format

Each SDS file contains a sequence of variable-size data blocks. Every data block has the following information:

1. **timeslot**: data block timeslot measured at the `tick-frequency` rate (32-bit unsigned integer, little endian).
2. **block size**: number of bytes in the following data block (32-bit unsigned integer, little endian).
3. **data block**: SDS stream content (little endian, no padding) as described by the corresponding `*.sds.yml` [metadata file](#sds-metadata-format).

This structure supports recording and playback of multiple data streams that may have jitter. The timeslot information allows correlating data blocks from different data streams and enables sensor fusion applications where multiple data streams are combined as training input to one machine learning algorithm.

### Filenames

SDS data streams are stored in `*.sds` files with the following naming convention:

```txt
<stream-name>.<label>[.p].sds
```

The `.p` is added when the SDS data stream is recorded during playback.

The `sdsOpen` function takes `<stream-name>` for the stream and the opening mode as input parameters.
Opening a stream in `sdsModeRead` mode is used for playback and opening a stream in `sdsModeWrite` is used for recording.

The [`SDSIO-Server`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-server) adds `.<label>[.p].sds` to compose a filename as explained below:

**Recording:**

`<label>` is a sequential number starting at 0. The number is incremented until no file exists with the corresponding name, at which point a new file is created.

Each subsequent recording session uses the next `<label>` number in the sequence. If a file with the selected name already exists, it is preserved by renaming it with a `.bak` extension before a new file is created with the original name.

**Playback:**

When a [`*.sdsio.yml` control file](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-control-file-sdsioyml) is used and contains a [`play:`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#play) node, the `<label>` is specified in the corresponding [`step:`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#play).

When `*.sdsio.yml` control file is not used, the `<label>` is a sequential number starting at 0. If the corresponding file does not exist, the open operation fails.

!!! Note
    - Files recorded during playback include an additional `.p` before the `.sds` extension to
      distinguish them from originally recorded files (e.g., `ML_Out.0.p.sds`).
    - If a recording filename already exists, any existing `.bak` file with the same name is deleted,
      the current file is renamed by appending `.bak`.

### Timeslot

The timeslot is a 32-bit unsigned value and is used for:

- Alignment of different data streams that have the same timeslot value.
- Order of the SDS data files captured during execution.
- Combining multiple SDS file records with the same timeslot value.

The same timeslot connects different SDS file data blocks. It is useful to
use the same timeslot for the recording of data blocks in different data streams for one iteration of a DSP or ML algorithm.
In most cases the granularity of an RTOS tick (typically 1ms) is a good choice for a timeslot resolution.
