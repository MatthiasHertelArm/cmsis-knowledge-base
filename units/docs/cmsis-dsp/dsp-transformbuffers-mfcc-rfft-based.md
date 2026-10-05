---
id: "dsp-transformbuffers-mfcc-rfft-based"
type: "concept"
domain: "optimization"
title: "transformbuffers: MFCC (RFFT based)"
summary: "transformbuffers: MFCC (RFFT based)"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/transformbuffers.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/transformbuffers.md#mfcc-rfft-based"
license: "Apache-2.0"
mode: "V"
---

MFCC of length N

### MFCC Temporary Buffer Size 1

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      | N        | N                | N        | N      |
| F32                      | N        | N                | N        | N      |
| F16                      | N        | N                | N        | N      |
| Q31                      | 2N       | 2N               | N+2      | N+2    |
| Q15                      | 2N       | 2N               | N+2      | N+2    |

### MFCC Temporary Buffer Size 2

| Datatype / Architecture  | SCALAR   | DSP EXTENSIONS   | HELIUM   | NEON   |
| :----------------------: | :------: | :--------------: | :------: | :----: |
| F64                      |          |                  |          |        |
| F32                      |          |                  |          | N      |
| F16                      |          |                  |          | N      |
| Q31                      |          |                  |          | 2N     |
| Q15                      |          |                  |          | 2N     |
