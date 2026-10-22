---
id: "sds-theory-sds-metadata-format"
type: "concept"
domain: "test"
title: "theory: SDS Metadata Format"
summary: "The content of each data stream may be described in an SDS metadata file in YAML format that is created by the user. Data conversion utilities and data viewers use this metadata to interpret the binary stream content."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#sds-metadata-format"
license: "Apache-2.0"
mode: "V"
---

The content of each data stream may be described in an SDS metadata file in [YAML format](https://en.wikipedia.org/wiki/YAML) that is created by the user. Data conversion utilities and data viewers use this metadata to interpret the binary stream content. For example, a data stream named `sensorX` (stored in files `sensorX.0.sds`, `sensorX.1.sds`, ...) can be described with a corresponding metadata file `sensorX.sds.yml` as shown below.

(figure: SDS Metadata Format)

The following section defines the YAML format of this metadata file. The file [`schema/sds.schema.json`](https://github.com/ARM-software/SDS-Framework/blob/main/schema/sds.schema.json) is a schema description of the SDS metadata format.

`sds:`                                | Start of the SDS format description
:-------------------------------------|---------------------------------------------------
    `name:`            | Name of the Synchronous Data Stream (required)
    `description:`     | Additional descriptive text (optional)
    `block-frequency:` | Frequency in Hz (interval) of data blocks within a data stream (optional, see note)
    `sample-frequency:`| Frequency in Hz (sample rate) of samples within a data block (optional, see note)
    `tick-frequency:`  | Tick frequency in Hz of the timeslot value (optional); default: 1000 Hz
    `content:`         | List of values captured (required, see below)

!!! Note
    - `block-frequency:` is optional as it can be derived from the timeslot value in combination with `tick-frequency:`.
    - `sample-frequency:` is required when a data block contains a temporal sequence sampled at a fixed rate. Omit it when all records share the block timeslot.
    - SDS v3.0 used `frequency:` to indicate a sample rate. In SDS v3.1 this is renamed to `sample-frequency:` to clarify the information.

The picture below shows how `sample-frequency:` and `block-frequency:` are applied. When data streams from different sources are combined, data blocks may vary in size.

(figure: Data Block Size and Sample Frequency)

The `content:` list describes the binary layout of one data block. Depending on the stream type, it uses these nodes:

- [`value:`](#value-list-data-stream) list entries to describe discrete values, such as sensor channels or algorithm outputs. A data block can contain multiple samples, so the `block size` is a multiple of the sample size. A `block size` of 0 indicates that no sample is available in that timeslot.
- [`audio:`](#audio-data-stream) entry to describe audio channel parameters.
- [`image:`](#image-data-stream) entry to describe a camera stream with frame layout parameters.
