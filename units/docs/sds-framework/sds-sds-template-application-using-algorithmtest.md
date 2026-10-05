---
id: "sds-sds-template-application-using-algorithmtest"
type: "concept"
domain: "test"
title: "SDS Template Application: Using AlgorithmTest"
summary: "The AlgorithmTest project allows you to add custom algorithms for testing. It is prepared for recording and playback of SDS data files."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/template.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/template.md#using-algorithmtest"
license: "Apache-2.0"
mode: "V"
---

The **AlgorithmTest** project allows you to add custom algorithms for testing. It is prepared for recording and playback of SDS data files.

### Add User Algorithm

In the SDS template application, these files must be modified to integrate the DSP/ML algorithm under test:

- `algorithm/algorithm_config.h` configures the block size of data streams.
- `algorithm/algorithm_user.c` is the interface to the DSP/ML algorithm under test.
- `algorithm/data_in_user.c` is the interface to the physical data source.
