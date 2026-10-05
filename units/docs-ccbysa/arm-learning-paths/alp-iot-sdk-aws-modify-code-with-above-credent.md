---
id: "alp-iot-sdk-aws-modify-code-with-above-credent"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Enable AWS connectivity: Modify code with above credentials"
summary: "The example applications need to be modified to add the credentials."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/aws.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/aws/#modify-code-with-above-credentials"
license: "CC-BY-SA-4.0"
mode: "V"
---

The example applications need to be modified to add the credentials.

Return to your Virtual Hardware terminal.

Modify the 2 `.h` files to add your information.

### bsp/default_credentials/aws_clientcredential.h

Use a text editor to modify these macros with the unique values for your AWS thing.


```C
#define clientcredentialMQTT_BROKER_ENDPOINT         "endpointid.amazonaws.com"
```

where `endpointid.amazonaws.com` is unique to you, and is given in `IoT Core` > `Settings` > `Endpoint` on your AWS console.

```C
#define clientcredentialIOT_THING_NAME               "thingname"
```

where `thingname` is the `thing` created [above](#thing).

Save the file when done.

### bsp/default_credentials/aws_clientcredential_keys.h

Use a text editor to modify these macros with the unique values for your AWS thing.

```C
#define keyCLIENT_CERTIFICATE_PEM \
...
```

with the contents of the `.crt` certificate file downloaded [above](#thing). You will need to start and end each line of the certificate with quotations and escape commands:

```output
"-----BEGIN CERTIFICATE-----\n"\
"1234123412341234123412341234123412341234123412341234123412341234\n"\
"5678567856785678567856785678567856785678567856785678567856785678\n"\
...
"-----END CERTIFICATE-----"
```

Similarly add the public and private keys (`.pem.key`), modified as above.

```C
#define keyCLIENT_PRIVATE_KEY_PEM \
...
#define keyCLIENT_PUBLIC_KEY_PEM \
...
```

Save the file when done.
