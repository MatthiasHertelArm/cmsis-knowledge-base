---
id: "sds-theory-value-list-data-stream"
type: "concept"
domain: "test"
title: "theory: SDS Metadata Format / Value-list data stream"
summary: "Typically describes the sample layout of a sensor data stream or the output of ML algorithms. A data block may contain several samples as shown in the picture above."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#value-list-data-stream"
license: "Apache-2.0"
mode: "V"
---

_Part of: SDS Metadata Format_

Typically describes the sample layout of a sensor data stream or the output of ML algorithms. A data block may contain several samples as shown in the picture above. The `sample-frequency:` should be specified when the data stream uses a discrete sample rate.

With `dim-x:` and `dim-y:` arrays can be composed. The equivalent representation in C is "*type name[dim-y][dim-x]*".

`content:`                           | Value list in the order stored in the data block
:------------------------------------|---------------------------------------------------
`- value:`                           | Name of the value (required)
    `type:`           | Data type of the value (required)
    `dim-x:`          | Array size x (optional); default: 1
    `dim-y:`          | Array size y (optional); default: 1
    `offset:`         | Offset of the value (optional); default: 0
    `scale:`          | Scale factor of the value (optional); default: 1.0
    `unit:`           | Physical unit of the value (optional)

The following examples show metadata files for several value-list data streams.

#### Example: Gyroscope data

The following `sensorX.sds.yml` describes the binary layout of the `sensorX` data stream:

```yml
sds:                   # describes a synchronous data stream
  name: sensorX        # user defined name
  description: Gyroscope stream with 1KHz sample rate, plus additional user data
  sample-frequency: 1000
  content:
    - value: x         # Value name is 'x'
      type:  uint16_t  # stored using a 16-bit unsigned int
      scale: 0.2       # value is scaled by 0.2
      unit: dps        # base unit of the value
    - value: y
      type: uint16_t
      scale: 0.2
      unit: dps
    - value: z
      type: uint16_t
      unit: dps        # scale 1.0 is default
    - value: temp
      type: float
      unit: degree Celsius
    - value: raw
      type: uint16_t   # raw data, no scale or unit given
    - value: flag
      type: uint32_t:1 # a single bit stored in a 32-bit int
```

#### Example: Time-of-Flight data

The following `ToF.sds.yml` metadata describes data from a Time-of-Flight sensor:

```yml
sds:                   # describes a synchronous data stream
  name: ToF            # user defined name
  description: Time-of-Flight sensor with 8x8 matrix
  content:
    - value: distance  # Value name is 'distance'
      type:  uint16_t  # stored using a 16-bit unsigned int
      dim-x: 8
      dim-y: 8
```

#### Example: Motion-inference input

The following `Motion.sds.yml` metadata describes motion samples used together as the input to one inference:

```yml
sds:
  name: motion
  description: Motion samples used for one inference
  sample-frequency: 1000
  content:
    - value: x
      type: float
    - value: y
      type: float
    - value: z
      type: float
```

One record contains the three values `x`, `y`, and `z` and has a size of 12 bytes. A data block containing 125 records has a block size of 1500 bytes. The records form a temporal sequence sampled at 1 kHz, while the complete block is processed by one inference and has one timeslot.

#### Example: Object-detection output

The following `Object.sds.yml` metadata describes a variable-size collection of objects produced by one inference:

```yml
sds:
  name: detections
  description: 0 - n objects detected in one inference
  content:
    - value: class_id
      type: uint32_t
    - value: confidence
      type: float
    - value: x
      type: uint32_t
    - value: y
      type: uint32_t
    - value: width
      type: uint32_t
    - value: height
      type: uint32_t
```

One detection record has a size of 24 bytes. For example, a block size of 240 bytes contains 10 object detections. The number of detections may vary between blocks and is calculated by dividing the block size by 24. `sample-frequency:` is omitted because all detections are results of the same inference and share the block timeslot.

!!! Note
    - The current `sdsWrite` implementation does not accept a zero-byte data block. An application must therefore omit the block or define an application-specific non-empty representation when an inference produces no detections.
    - A variable-size segmentation mask cannot be described as a fixed-size detection record. It may be stored in a separate image or mask stream and correlated with the detection stream using the same timeslot.
