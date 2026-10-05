---
id: "mbedtls-mbed-tls-ci-failure-faq-reproducing-failures-locally"
type: "concept"
domain: "security"
title: "Mbed TLS CI failure FAQ: Reproducing failures locally"
summary: "First, determine which component(s) failed. See the CI guide for an overview of component names."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/understanding-ci-failures.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/understanding-ci-failures.md#reproducing-failures-locally"
license: "Apache-2.0"
mode: "V"
---

### How do I reproduce an `all.sh` failure locally?

First, [determine which component(s) failed](#pr-tests-failed-which-components-failed). See the [CI guide](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#high-level-overview-of-the-pr-tests) for an overview of component names.

Suppose that the CI status for PR tests is
```
Failures: all_u16-full_without_ecdhe_ecdsa all_u16-test_tls1_2_ccm_psk_dtls
```

You can run these `all.sh` components as follows:
```
tests/scripts/all.sh -k full_without_ecdhe_ecdsa test_tls1_2_ccm_psk_dtls
```

Note that this may or may not run successfully outside the [official Docker image](https://github.com/Mbed-TLS/mbedtls-test/tree/main/resources/docker_files). See the [CI tooling guide](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#tooling-for-allsh) for more information.

### Almost all tests fail in the full config

When `MBEDTLS_ENTROPY_NV_SEED` is enabled, any code that calls `mbedtls_entropy_init()` or `psa_crypto_init()`, which includes most tests other than low-level crypto tests, requires a seed file. For test purposes, the seed file can have any content, it just needs to be large enough (at least 64 bytes). The seed file is called `seedfile` and must be in the working directory where the test program runs, which is normally `tests`.

You can use one of the following commands to create a seed file:
```
head -c 64 </dev/urandom >tests/seedfile
truncate -s 64 tests/seedfile
```

If you run tests in different configurations successively in the same directory, you may end up with a smaller seed file. The seed file can be larger than required, but not smaller. If needed, just re-create a 64-byte seed file.

### How do I reproduce an `all.sh` failure in a debugger?

Most builds in `all.sh` have optimization enabled, and sometimes with sanitizers that might cause noise or incompatibilities with debuggers. If you want to look at the failure in a debugger, you'll need to look at the code of the component. The code of components is located in `tests/scripts/components-*.sh` (or within `tests/scripts/all.sh` itself in older branches).

Here are a few tips if you want to use `all.sh` directly:

* For builds that use CMake, run `cmake -D CMAKE_BUILD_TYPE=Debug` instead of the build type used in the test script. Alternatively, edit the lines that set `CMAKE_C_FLAGS_ASAN` in your local copy of `tests/scripts/all.sh` to give it the value `"-O0 -g3"` (don't commit the result).
* For builds that use plain make, pass `CFLAGS='-O0 -g3'`. If you're doing that a lot, edit the line that sets `ASAN_CFLAGS` in your local copy of `tests/scripts/all.sh` to be `ASAN_CFLAGS='-O0 -g3 -Werror'` (don't commit the result).
* `all.sh` will stop at the first failure, with the result of the partial build and any modified files, if you don't pass the `-k` (`--keep-going`) option.
* If you want to get the build products of a passing build by running `all.sh`, add `exit 1` in the component where you want to stop, then run `tests/scripts/all.sh component_name`.

### How do I reproduce driver builds with debug symbols?

The tips in [“How do I reproduce an `all.sh` failure in a debugger?”](#how-do-i-reproduce-an-allsh-failure-in-a-debugger) can help you get a debug build instead of an optimized+Asan build.

### How do I get multiple build trees with different configurations?

The provided `Makefile` does not support out-of-tree builds.

CMake supports out-of-tree builds. You can have a different configuration in different build trees as follows:

* Copy `mbedtls_config.h` under a different name, e.g.
    ```
    cp include/mbedtls/mbedtls_config.h include/foo-mbedtls_config.h
    ```
* Run `scripts/config.py -f include/foo-mbedtls_config.h` so that the file contains the desired configuration.
* If needed, do the same for `include/psa/crypto_config.h`.
* Create a build tree and run CMake with `CFLAGS` including `-DMBEDTLS_CONFIG_FILE="foo-mbedtls_config.h"` and if applicable `-DPSA_CRYPTO_CONFIG_FILE="foo-crypto_config.h"`. Pay attention to quoting in the shell! For example:
    ```
    mkdir build-foo
    cd build-foo-debug
    CFLAGS='-DMBEDTLS_CONFIG_FILE="foo-mbedtls_config.h" -DPSA_CRYPTO_CONFIG_FILE="foo-crypto_config.h"' cmake -DCMAKE_BUILD_TYPE=Debug
    make lib tests
    ```

Alternatively, the unofficial build tool [`mbedtls-prepare-build`](https://github.com/gilles-peskine-arm/mbedtls-docs/blob/mbedtls-prepare-build-3.4/tools/bin/mbedtls-prepare-build) is designed to support multiple build trees easily. For example:

```
mbedtls-prepare-build -p full-debug
mbedtls-prepare-build -d build-default-debug -p debug
mbedtls-prepare-build -d build-nosha1-debug -p debug --config-unset=MBEDTLS_SHA1_C
mbedtls-prepare-build -d build-norsa-debug -p full-debug --config-unset=MBEDTLS_PSA_CRYPTO_CONFIG,MBEDTLS_RSA_C,MBEDTLS_PKCS1_V15,MBEDTLS_PKCS1_V21,MBEDTLS_GENPRIME,MBEDTLS_X509_RSASSA_PSS_SUPPORT,MBEDTLS_KEY_EXCHANGE_DHE_RSA_ENABLED,MBEDTLS_KEY_EXCHANGE_RSA_PSK_ENABLED,MBEDTLS_KEY_EXCHANGE_ECDHE_RSA_ENABLED,MBEDTLS_KEY_EXCHANGE_ECDH_RSA_ENABLED,MBEDTLS_KEY_EXCHANGE_RSA_ENABLED
mbedtls-prepare-build -d build-suiteb-debug --config-file=configs/config-suite-b.h --config-set=MBEDTLS_DEBUG_C,MBEDTLS_ERROR_C
mbedtls-prepare-build -d build-accel-ecdsa-debug -p debug --config-set=MBEDTLS_PSA_CRYPTO_CONFIG --config-unset=MBEDTLS_PSA_CRYPTO_SE_C --accel-list=ALG_ECDSA,ALG_DETERMINISTIC_ECDSA,KEY_TYPE_ECC_PUBLIC_KEY,KEY_TYPE_ECC_KEY_PAIR_BASIC,KEY_TYPE_ECC_KEY_PAIR_IMPORT,KEY_TYPE_ECC_KEY_PAIR_EXPORT,KEY_TYPE_ECC_KEY_PAIR_GENERATE,KEY_TYPE_ECC_KEY_PAIR_DERIVE,ECC_SECP_R1_192,ECC_SECP_R1_224,ECC_SECP_R1_256,ECC_SECP_R1_384,ECC_SECP_R1_521,ECC_SECP_K1_192,ECC_SECP_K1_224,ECC_SECP_K1_256,ECC_BRAINPOOL_P_R1_256,ECC_BRAINPOOL_P_R1_384 -accel-list=ECC_BRAINPOOL_P_R1_512,ECC_MONTGOMERY_255,ECC_MONTGOMERY_448 --config-unset=MBEDTLS_ECDSA_C,MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED,MBEDTLS_KEY_EXCHANGE_ECDH_ECDSA_ENABLED --libtestdriver1-extra-list=ALG_SHA_224,ALG_SHA_256,ALG_SHA_384,ALG_SHA_512,ALG_SHA3_224,ALG_SHA3_256,ALG_SHA3_384,ALG_SHA3_512
```
