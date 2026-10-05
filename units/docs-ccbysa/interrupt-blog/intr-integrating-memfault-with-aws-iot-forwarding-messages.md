---
id: "intr-integrating-memfault-with-aws-iot-forwarding-messages"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink: Forwarding Messages"
summary: "However, how does the MQTT broker forward the data to the Memfault API? This is where the Rules Engine in AWS IoT Core comes into play along with a custom AWS Lambda function for calling the Memfault API directly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink#forwarding-messages"
license: "CC-BY-SA-4.0"
mode: "V"
---

However, how does the MQTT broker forward the data
to the Memfault API? This is where the
[Rules Engine](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)
in AWS IoT Core comes into play along with a custom
[AWS Lambda](https://aws.amazon.com/lambda/) function for calling the
Memfault API directly. The
[Memfault docs](https://docs.memfault.com/docs/mcu/introduction/) provide
[an example](https://docs.memfault.com/docs/mcu/uploading-data-with-mqtt)
of the recommended rule setup which looks like this:

```
SELECT encode(\*,'base64') AS data, topic() AS topic FROM 'prod/+/+/memfault/\#'
```

Another example of this configuration and setup can be found
[here](https://github.com/NordicSemiconductor/asset-tracker-cloud-memfault-aws-js)
from Nordic Semiconductor as an asset tracking use case.
