---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tosa-specific-op"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 TOSA Specific Operator Constraints"
summary: "This is a list of constraints that the ARITHMETIC_RIGHT_SHIFT operator must satisfy in order to be scheduled on the NPU."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tosa-specific-operator-constraints"
license: "Apache-2.0"
mode: "V"
---

### Ethos-U55 and Ethos-U65 TOSA ARITHMETIC_RIGHT_SHIFT Constraints

This is a list of constraints that the ARITHMETIC_RIGHT_SHIFT operator must satisfy in order to be scheduled on the NPU.

- DataTypes: int32 only (IFM and OFM must be 32-bit)
- Round: true only

### Ethos-U55 and Ethos-U65 TOSA LOGICAL_LEFT_SHIFT Constraints

This is a list of constraints that the LOGICAL_LEFT_SHIFT operator must satisfy in order to be scheduled on the NPU.

- DataTypes: int32 only (IFM and OFM must be 32-bit)

### Ethos-U55 and Ethos-U65 TOSA TABLE Constraints

This is a list of constraints that the TABLE operator must satisfy in order to be scheduled on the NPU.

- DataTypes: int8 only
- EXT-INT16 is not supported

### Ethos-U55 and Ethos-U65 TOSA AVG_POOL2D Constraints

This is a list of constraints that the AVG_POOL2D operator must satisfy in order to be scheduled on the NPU.

- Tensor axis: N=1 and HWC in range 1..65536
- IF padding is used: 1 <= kernel_x <= 8 and 1 <= kernel_y <= 8
- ELSE: 1 <= kernel_x*kernel_y <= 65536 and 1 <= kernel_y <= 256
- Kernel stride: 1 <= stride <= 3

### Ethos-U55 and Ethos-U65 TOSA MAX_POOL2D Constraints

This is a list of constraints that the MAX_POOL2D operator must satisfy in order to be scheduled on the NPU.

- Tensor axis: N any, HWC in range 1..65536
- Kernel size: 1 <= kernel_x*kernel_y <= 65536 and 1 <= kernel_y <= 256
- Kernel stride: 1 <= stride <= 3

### Ethos-U55 and Ethos-U65 TOSA ARGMAX Constraints

This is a list of constraints that the ARGMAX operator must satisfy in order to be scheduled on the NPU.

- Tensor axis: N=1, C in range 1..127, and W*H in range 1..65536
- Rank must be in range 1..4
- Reduction axis must be channel

### Ethos-U55 and Ethos-U65 TOSA CONV2D Constraints

This is a list of constraints that the CONV2D operator must satisfy in order to be scheduled on the NPU.

- DataTypes (IFM, Weights, OFM): (i8_t,i8_t,i32_t), (i8_t,i4_t,i32_t), (i16_t,i8_t,i48_t)
- EXT-INT16 is only supported if followed by RESCALE to i8_t, i16_t or i32_t
- Tensor axis: NHW any, C in range 1..65536
- Kernel size: 1 <= kernel_x*kernel_y <= 4096 and 1 <= kernel_y <= 64
- Kernel stride: 1 <= stride <= 3
- Sum of absolute weights must not exceed 127*65536
- Bias must fit in signed int40: -549755813888..549755813887

### Ethos-U55 and Ethos-U65 TOSA CONV3D Constraints

This is a list of constraints that the CONV3D operator must satisfy in order to be scheduled on the NPU.

- DataTypes (IFM, Weights, OFM): (i8_t,i8_t,i32_t), (i8_t,i4_t,i32_t), (i16_t,i8_t,i48_t)
- EXT-INT16 is only supported if followed by RESCALE to i8_t, i16_t or i32_t
- Tensor axis: NDHW any, C in range 1..65536
- Kernel size: 1 <= kernel_x*kernel_y <= 4096 and 1 <= kernel_y <= 64 and kernel_z==1
- Kernel stride: 1 <= stride_x <= 3, 1 <= stride_y <= 3, 1 <= stride_z
- Sum of absolute weights must not exceed 127*65536

### Ethos-U55 and Ethos-U65 TOSA TRANSPOSE_CONV2D Constraints

This is a list of constraints that the TRANSPOSE_CONV2D operator must satisfy in order to be scheduled on the NPU.

- DataTypes (IFM, Weights, OFM): (i8_t,i8_t,i32_t), (i8_t,i4_t,i32_t), (i16_t,i8_t,i48_t)
- EXT-INT16 is only supported if followed by RESCALE to i8_t, i16_t or i32_t
- Tensor axis: N any, HWC in range 1..65536
- Kernel size: 1 <= kernel_x*kernel_y <= 4096 and 1 <= kernel_y <= 64
- Stride combinations:
  - (1,1), (2,2)
  - (1,2) only if IFM height and kernel height are 1
  - (2,1) only if IFM width and kernel width are 1

### Ethos-U55 and Ethos-U65 TOSA MATMUL Constraints

This is a list of constraints that the MATMUL operator must satisfy in order to be scheduled on the NPU.

- DataTypes (IFM, IFM2, OFM): (i8_t, i8_t, i32_t)
- Tensor axis: WC in range 1..65536, NH any

### Ethos-U55 and Ethos-U65 TOSA RESIZE Constraints

This is a list of constraints that the RESIZE operator must satisfy in order to be scheduled on the NPU.

- Upscale must be power-of-two in range 2x..8x
- Bilinear mode must be followed by RESCALE with shift=log2(upscale_x*upscale_y) and scale=1

### Ethos-U55 and Ethos-U65 TOSA TRANSPOSE Constraints

This is a list of constraints that the TRANSPOSE operator must satisfy in order to be scheduled on the NPU.

- DataTypes: int8, int16, int32 (bool is not supported)
- Rank: int8/int16 support 1..MAX_RANK, int32 support 1..4
- Permutation and tensor-axis constraints:
  - IF IFM is Int32:
    - Rank must be <= 4
    - NHWC: C <= 2^15
    - NWHC: N == 1, H <= 2^16, W <= 2^16, C <= 2^14
    - NHCW: N*H <= 2^16, W <= 2^16, C <= 2^16
    - NCWH: N == 1, H <= 2^16, W <= 2^16, C <= 2^14
    - Any other permutation vector is unsupported
  - IF IFM is Int8 or Int16:
    - NHWC: no shape constraints
  - ELSE IF permutation is: NWHC/NHCW/NCWH/NWCH/NCHW and the tensor is 3D, or higher-rank with all axes outside H/W/C equal to 1:
    - (H, W, C) <= (2^16, 2^16, 2^16)
  - ELSE:
    - Product of any N-2 axes in a rank N tensor must be less than or equal to 2^16. For example, for rank 4: N*H <= 2^16, N*W <= 2^16, N*C <= 2^16, H*W <= 2^16, H*C <= 2^16, W*C <= 2^16.

### Ethos-U55 and Ethos-U65 TOSA REDUCE_SUM Constraints

This is a list of constraints that the REDUCE_SUM operator must satisfy in order to be scheduled on the NPU.

- Reduced axis must be in range 1..65536
- IF reduction is over channel: other axes can be any size
- ELSE: product of axes before and after the reduced axis respectively must be in range 1..65536
- Reduction is native over depth only; otherwise Vela inserts transpose (lower performance)

### Ethos-U55 and Ethos-U65 TOSA REDUCE_MAX Constraints

This is a list of constraints that the REDUCE_MAX operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8->INT8 and INT16->INT16

### Ethos-U55 and Ethos-U65 TOSA REDUCE_MIN Constraints

This is a list of constraints that the REDUCE_MIN operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8->INT8 and INT16->INT16

### Ethos-U55 and Ethos-U65 TOSA CONCAT Constraints

This is a list of constraints that the CONCAT operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8, INT16, INT32

### Ethos-U55 and Ethos-U65 TOSA RESHAPE Constraints

This is a list of constraints that the RESHAPE operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8, INT16, INT32

### Ethos-U55 and Ethos-U65 TOSA SLICE Constraints

This is a list of constraints that the SLICE operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8, INT16, INT32

### Ethos-U55 and Ethos-U65 TOSA TILE Constraints

This is a list of constraints that the TILE operator must satisfy in order to be scheduled on the NPU.

- DataTypes: INT8, INT16, INT32

### Ethos-U55 and Ethos-U65 TOSA CAST Constraints

This is a list of constraints that the CAST operator must satisfy in order to be scheduled on the NPU.

- Any PRO-INT combination is supported if bool is not used
- Down-casting from int32 is not supported

### Ethos-U55 and Ethos-U65 TOSA RESCALE Constraints

This is a list of constraints that the RESCALE operator must satisfy in order to be scheduled on the NPU.

- EXT-INT16 (INT48 types) are not supported standalone, but might be supported if the compiler can fuse them. See EXT-INT16 constraints on other operators for more details.

### Ethos-U55 and Ethos-U65 TOSA IDENTITY Constraints

This is a list of constraints that the IDENTITY operator must satisfy in order to be scheduled on the NPU.

- Supported pairs: INT8->INT8, INT16->INT16, INT32->INT32, INT48->INT48

### Ethos-U55 and Ethos-U65 TOSA PAD Constraints

This is a list of constraints that the PAD operator must satisfy in order to be scheduled on the NPU.

- Supported pairs: INT8->INT8, INT16->INT16, INT32->INT32
- Bool is not supported

### Ethos-U55 and Ethos-U65 TOSA REVERSE Constraints

This is a list of constraints that the REVERSE operator must satisfy in order to be scheduled on the NPU.

- Supported pairs: INT8->INT8 and INT16->INT16
- Only W-axis and H-axis reverse are supported
- INT32 is not supported

### Ethos-U55 and Ethos-U65 TOSA Not Supported Operators

This is a list of TOSA operators that are not supported on Ethos-U55 and Ethos-U65.

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
- INTDIV
- LOGICAL_AND
- LOGICAL_RIGHT_SHIFT
- LOGICAL_OR
- LOGICAL_XOR
- LOGICAL_NOT
- SELECT
- EQUAL
- GREATER
- GREATER_EQUAL
- REDUCE_ALL
- REDUCE_ANY
- GATHER
- SCATTER
