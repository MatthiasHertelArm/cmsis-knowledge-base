---
id: "mbedtls-how-to-tune-elliptic-curves-resour-mbedtls-ecp-window-size"
type: "concept"
domain: "security"
title: "How to tune Elliptic Curves resource usage: MBEDTLS_ECP_WINDOW_SIZE"
summary: "The main operation on elliptic curves is multiplication of a point by an integer, which is performed using additions and doubling. This is similar to fast exponentiation algorithms you may be familiar with."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md#mbedtls-ecp-window-size"
license: "Apache-2.0"
mode: "V"
---

The main operation on elliptic curves is multiplication of a point by an integer, which is performed using additions and doubling. This is similar to fast exponentiation algorithms you may be familiar with. It is possible to boost performance by pre-computing some well-chosen multiples of the input point just before you multiply it by the chosen integer. This is the [comb method](https://eprint.iacr.org/2004/342.pdf).)

RAM usage increases with the number of multiples you compute and store before performing the actual multiplication. However, while pre-computing a few multiples gives better performance than pre-computing none, you don't want to compute too many either. The optimal size of the pre-computation table depends on the size of the curve.

By default, our multiplication function will select the table size that gives the best performance for the curve used. However, you might want to set an upper bound for the table size: this is what `MBEDTLS_ECP_WINDOW_SIZE` does. More specifically the value of this macro is the log of the maximum number of points that will be precomputed.

For example, for NIST P-256, the performance and RAM figures for various values of this parameter (with fixed point optimization disabled, see next section) are as follows:

|Window Size|2|3|4|5|6|
| --- | --- | --- | --- | --- | --- |    
|ECDHE/s|44|50|53|53|53|
|Heap bytes|2064|2448|3592|3624|3680|

As you can see, when moving from 2 to 4, performance increases with RAM usage; larger values aren't helpful for performance. The code selects 4 as the effective value, and doesn't change RAM usage as much.
