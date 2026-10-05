---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-diagnostic-output"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Diagnostic output"
summary: "In the library, the only functions that print messages (using printf()) are the self-test functions. These can be disabled at compilation time (MBEDTLS_SELF_TEST) without affecting the rest of the library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#diagnostic-output"
license: "Apache-2.0"
mode: "V"
---

In the library, the only functions that print messages (using `printf()`) are the self-test functions. These can be disabled at compilation time (`MBEDTLS_SELF_TEST`) without affecting the rest of the library.

Alternatively, `printf()` can easily be replaced with your own printing function, either by enabling `MBEDTLS_PLATFORM_PRINTF_ALT` at compilation time and then using `mbedtls_platform_set_printf()` at runtime, or by using `MBEDTLS_PLATFORM_PRINTF_MACRO` at compilation time.

### Platform setup and teardown

In some cases, the underlying hardware requires explicit initialization, before the hardware specific functions can operate properly.
Special deinitialization operations may be required afterwards as well.
To account for that, the `mbedtls_platform_setup()` and `mbedtls_platform_teardown()` functions are available in the Mbed TLS API.
By default they do not perform any actions.
However, you can provide your own implementation in order to give third parties integrating Mbed TLS into their own platforms a uniform way of initializing any underlying hardware or accelerators.
As such, to aid portability of application code that uses Mbed TLS across platforms, we recommend you to use these functions.
The code changes that are needed are discussed below.

For a target device to provide custom setup and teardown functions, you must define the macro `MBEDTLS_PLATFORM_SETUP_TEARDOWN_ALT` as shown below:
```
#define MBEDTLS_PLATFORM_SETUP_TEARDOWN_ALT
```
Then, you must provide a "platform_alt.h" header file, defining a platform context structure:
```
typedef struct {
    ...
}
mbedtls_platform_context;
```
Finally, you must provide implementations for the platform specific setup and teardown operations:
```
#if defined(MBEDTLS_PLATFORM_SETUP_TEARDOWN_ALT)
int mbedtls_platform_setup( mbedtls_platform_context *ctx )
{
    ...
}

void mbedtls_platform_teardown( mbedtls_platform_context *ctx )
{
    ...
}
#endif
```

Note that the setup and teardown functions must be called, respectively, before and after any other calls to the Mbed TLS API are made, as shown in the example:

```
 #include "mbedtls/platform.h"
...

int main()
{
    int ret;

#if defined(MBEDTLS_PLATFORM_C)
    mbedtls_platform_context platform_ctx;
#endif

    ...

#if defined(MBEDTLS_PLATFORM_C)
    if( ( ret = mbedtls_platform_setup( &platform_ctx ) ) != 0 )
    {
        // Error handling
    }
#endif

    // Your code goes here

    ...

#if defined(MBEDTLS_PLATFORM_C)
    mbedtls_platform_teardown( &platform_ctx );
#endif

    return( 0 );
}
```

<!---",how-do-i-port-mbed-tls-to-a-new-environment-OS,"How to port Mbed TLS to a new environment, architecture or OS",,"port, porting, environment, architecture, library, OS, system, network, timing, file system, entropy, platform",published,"2016-02-17 09:50:00",2,16866,"2017-04-23 14:37:00","Manuel PÃ©gouriÃ©-Gonnard"--->
