---
id: "dsp-transformbuffers-rfft"
type: "concept"
domain: "optimization"
title: "transformbuffers: RFFT"
summary: "transformbuffers: RFFT"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/transformbuffers.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/transformbuffers.md#rfft"
license: "Apache-2.0"
mode: "V"
---

RFFT of length N

### RFFT/RIFFT Temporary Buffer Size

Apply to both RFFT and RIFFT

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      |          |                  |          |        |
| F32                      |          |                  |          | N      |
| F16                      |          |                  |          | N      |
| Q31                      |          |                  |          | 2N     |
| Q15                      |          |                  |          | 2N     |

### RFFT Output Buffer Size

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      | N        | N                | N        | N      |
| F32                      | N        | N                | N        | N      |
| F16                      | N        | N                | N        | N      |
| Q31                      | 2N       | 2N               | N+2      | N+2    |
| Q15                      | 2N       | 2N               | N+2      | N+2    |

### RIFFT Input Buffer Size

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      | N        | N                | N        | N      |
| F32                      | N        | N                | N        | N      |
| F16                      | N        | N                | N        | N      |
| Q31                      | N+2      | N+2              | N+2      | N+2    |
| Q15                      | N+2      | N+2              | N+2      | N+2    |
