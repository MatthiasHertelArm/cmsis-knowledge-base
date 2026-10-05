---
id: "sds-theory-data-blocks-records-and-values"
type: "concept"
domain: "test"
title: "theory: SDS Metadata Format / Data blocks, records, and values"
summary: "An SDS stream contains data blocks. One data block represents one application operation, typically one DSP processing step or ML inference."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#data-blocks-records-and-values"
license: "Apache-2.0"
mode: "V"
---

_Part of: SDS Metadata Format_

An SDS stream contains data blocks. One data block represents one application operation, typically one DSP processing step or ML inference. A data block contains zero or more records, and each record contains the values listed under `content:` in the specified order. For temporal data, these records are also called samples.

For a `value:` list, the data block repeats the described record layout. The number of records is calculated as:

```txt
record count = block size / record size
```

The meaning of multiple records depends on the stream:

- **Temporal sequence:** Records were acquired consecutively. `sample-frequency:` specifies their rate and therefore the time interval between them. For example, one motion-inference block may contain 125 consecutive accelerometer samples.
- **Result collection:** Records were produced by the same operation and share the block timeslot. `sample-frequency:` is omitted because the records are not a temporal sequence. For example, one object-detection block may contain a variable number of detected objects.

The timeslot identifies the complete data block or application operation. It does not provide an individual acquisition time for every record. When exact per-record times are required, include a timestamp as another value in each record.
