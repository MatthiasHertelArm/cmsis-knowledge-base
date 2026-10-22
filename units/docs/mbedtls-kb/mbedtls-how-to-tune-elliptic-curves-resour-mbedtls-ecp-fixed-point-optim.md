---
id: "mbedtls-how-to-tune-elliptic-curves-resour-mbedtls-ecp-fixed-point-optim"
type: "concept"
domain: "security"
title: "How to tune Elliptic Curves resource usage: `MBEDTLS_ECP_FIXED_POINT_OPTIM`"
summary: "The first paragraph of the previous section said some multiples are precomputed just before computation, suggesting that they are discarded once the operation is done, and computed again for the next operation. This is true, but incomplete."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md#mbedtls-ecp-fixed-point-optim"
license: "Apache-2.0"
mode: "V"
---

The first paragraph of the previous section said some multiples are precomputed just before computation, suggesting that they are discarded once the operation is done, and computed again for the next operation. This is true, but incomplete.

Elliptic curves each come with a standard "base point" (also know as generator, and usually denoted by the letter `G`), for when the protocol requires a point known by all parties. For example, in ECDHE, one party generates a secret exponent `a`, computes `aG`, send the result to its peer, receives the peer's public share `Q` then computes the shared secret `aQ`.

Notice that for the first part (but not the second), the point to be multiplied is known in advance: `G`. When you first multiply a `G` by an integer, you pre-compute well-chosen multiples of `G` as usual. After that step, you may want to store those multiples in order to speed up subsequent multiplications of `G` by other integers. Keeping this information, however, uses RAM. There is a performance-memory trade-off.

* Set `MBEDTLS_ECP_FIXED_POINT_OPTIM` to 1 in order to keep the table, and 0 to discard it.

For example, the performance and RAM figures for NIST P-256 without and with fixed point optimization (with max window size set to 4, see previous section) are as follows:


||0|1|
|---|---|---|
|ECDHE/s|53|76|
|Heap bytes|3592|5360|

### Conclusion

The ECC implementation in Mbed TLS uses some memory-performance trade-offs. The defaults values are chosen with performance in mind, but you can adjust them to reduce RAM usage for the trade-off that best fits your particular needs.

It should be noted that newer curves like Curve25519, with a simpler implementation that doesn't use any trade-offs, manage to deliver superior performance while using less RAM compared to NIST curves.

<!---",how-do-i-tune-elliptic-curves-resource-usage,"How-to guide on reducing resource usage of elliptic curves with Mbed TLS",,"elliptic curves, resources, configuration",published,"2016-02-10 12:59:00",2,3399,"2016-02-22 16:19:00","Manuel PÃ©gouriÃ©-Gonnard"--->
