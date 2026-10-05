---
id: "intr-integrating-memfault-with-aws-iot"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink"
summary: "In the dynamic realm of embedded systems, the right combination of hardware and software components can transform the development process and empower engineers to build robust and efficient solutions."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the dynamic realm of embedded systems, the right combination of hardware
and software components can transform the development process and empower
engineers to build robust and efficient solutions. This article explores
a streamlined device-to-cloud embedded design utilizing the [STM32G0
Nucleo board](https://www.st.com/en/evaluation-tools/nucleo-g071rb.html)
from [STMicroelectronics](https://www.st.com/content/st_com/en.html),
an [AWS IoT ExpressLink](https://aws.amazon.com/iot-expresslink/)
module from [Espressif](https://www.espressif.com/en),
[AWS IoT Core](https://aws.amazon.com/iot-core/) for secure MQTT
communication, and [Memfault](https://memfault.com/) for remote debugging.
We will delve into the seamless integration of these technologies and
highlight the benefits they offer in the context of IoT applications.



To ensure the reliability and stability of IoT applications, effective
debugging and error monitoring are crucial. Memfault comes to the rescue
with its comprehensive set of tools for remote debugging, crash
reporting, and real-time error monitoring.
