---
id: "dsp-transformbuffers-cfft"
type: "concept"
domain: "optimization"
title: "transformbuffers: CFFT"
summary: "transformbuffers: CFFT"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/transformbuffers.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/transformbuffers.md#cfft"
license: "Apache-2.0"
mode: "V"
---

CFFT of length N

### CFFT Temporary Buffer Size

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      |          |                  |          |        |
| F32                      |          |                  |          | 2N     |
| F16                      |          |                  |          | 2N     |
| Q31                      |          |                  |          | 2N     |
| Q15                      |          |                  |          | 2N     |

### CFFT Output Buffer Size

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      | 2N       | 2N               | 2N       | 2N     |
| F32                      | 2N       | 2N               | 2N       | 2N     |
| F16                      | 2N       | 2N               | 2N       | 2N     |
| Q31                      | 2N       | 2N               | 2N       | 2N     |
| Q15                      | 2N       | 2N               | 2N       | 2N     |

### CIFFT Output Buffer Size

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      | 2N       | 2N               | 2N       | 2N     |
| F32                      | 2N       | 2N               | 2N       | 2N     |
| F16                      | 2N       | 2N               | 2N       | 2N     |
| Q31                      | 2N       | 2N               | 2N       | 2N     |
| Q15                      | 2N       | 2N               | 2N       | 2N     |
