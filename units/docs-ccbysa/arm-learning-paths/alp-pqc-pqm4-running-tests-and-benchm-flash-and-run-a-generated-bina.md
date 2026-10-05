---
id: "alp-pqc-pqm4-running-tests-and-benchm-flash-and-run-a-generated-bina"
type: "concept"
domain: "edge-ai"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Run pqm4 tests and benchmarks: Flash and run a generated binary"
summary: "How you run a binary depends on whether you are using a physical board or QEMU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/running-tests-and-benchmarks/#flash-and-run-a-generated-binary"
license: "CC-BY-SA-4.0"
mode: "V"
---

How you run a binary depends on whether you are using a physical board or QEMU.

#### Physical board

Flash the binary and read the serial output.

Flash the binary:

```bash
st-flash write bin/<binary_name>.bin 0x8000000
```

Read the output from the board:

```bash
python3 hostside/host_unidirectional.py
```

Press the RESET button on the board to trigger execution and see the output.

#### QEMU

Run the corresponding ELF file directly.

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/<binary_name>.elf
```

To exit QEMU, press `Ctrl+A` then `X`.

### Run a test binary

The test binary verifies that a scheme works correctly end to end.

#### Physical board

Flash the ML-KEM-768 test binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_test.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 test binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_test.elf
```

It generates a keypair, performs encapsulation and decapsulation, and checks that both sides derive the same shared secret. It also tests failure cases such as an invalid secret key or invalid ciphertext.

The output after running the binary is similar to:

```output
==========================
DONE key pair generation!
DONE encapsulation!
DONE decapsulation!
OK KEYS

+
...
OK invalid sk_a

+
OK invalid ciphertext

+
#
```

### Run a speed binary

The speed binary measures execution time in CPU cycles for each operation.

#### Physical board

Flash the ML-KEM-768 speed binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_speed.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 speed binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_speed.elf
```

The output after running the binary is similar to:

```output
==========================
keypair cycles:
123456

encaps cycles:
234567

decaps cycles:
210000
=
```

### Run a hashing binary

The hashing binary measures how many cycles are spent in symmetric primitives such as SHA-2, SHA-3, and AES. The number of cycles shows how much of the overall algorithm cost comes from hashing.

#### Physical board

Flash the ML-KEM-768 hashing binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_hashing.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 hashing binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_hashing.elf
```

The output after running the binary is similar to:

```output
==========================
keypair hash cycles:
50000

encaps hash cycles:
80000

decaps hash cycles:
75000
=
```

### Run a stack binary

The stack binary measures peak stack memory usage for each operation.

#### Physical board

Flash the ML-KEM-768 stack binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_stack.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 stack binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_stack.elf
```

The output after running the binary is similar to:

```output
==========================
keypair stack usage:
2048

encaps stack usage:
3072

decaps stack usage:
2800
#
```

**Note:**
Stack measurement might not work correctly on some boards due to platform-specific memory layout. Memory allocated outside functions, such as public keys and ciphertexts, is not included in these measurements.


### Run a test vectors binary

The test vectors binary generates deterministic test vectors using a fixed random seed. These are used to validate correctness and compare different implementations against each other.

#### Physical board

Flash the ML-KEM-768 test vectors binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_testvectors.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 test vectors binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_testvectors.elf
```

To compare the on-device vectors against host-generated reference vectors, use the `testvectors.py` script described in the automated testing section.
