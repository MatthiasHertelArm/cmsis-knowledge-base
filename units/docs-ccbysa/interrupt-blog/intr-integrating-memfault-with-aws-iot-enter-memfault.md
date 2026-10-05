---
id: "intr-integrating-memfault-with-aws-iot-enter-memfault"
type: "concept"
domain: "debug"
title: "Integrating Memfault With AWS IoT Core and ExpressLink: Enter Memfault"
summary: "To ensure the reliability and stability of IoT applications, effective debugging and error monitoring are crucial. Memfault comes to the rescue with its comprehensive set of tools for remote debugging, crash reporting, and real-time error monitoring."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-30-memfault-aws-iot-expresslink.md"
doc_source: "https://interrupt.memfault.com/blog/memfault-aws-iot-expresslink#enter-memfault"
license: "CC-BY-SA-4.0"
mode: "V"
---

To ensure the reliability and stability of IoT applications, effective
debugging and error monitoring are crucial. Memfault comes to the rescue
with its comprehensive set of tools for remote debugging, crash
reporting, and real-time error monitoring. By integrating Memfault into
the STM32G0 Nucleo and AWS IoT ExpressLink combination, developers gain
valuable insights into application crashes, exceptions, and faults. This
integration enables proactive error detection, efficient bug fixing, and
improved system performance, resulting in more robust and reliable IoT
applications. You can get started with a
[free Memfault account](https://app.memfault.com/register).

On the device side, the
[Memfault SDK](https://github.com/memfault/memfault-firmware-sdk) can be
used to incorporate Memfault into the firmware code to enable the remote
debugging capabilities. When an application encounters an error, the Memfault
SDK captures relevant information and splits it into smaller chunks. These
chunks are then sent securely to the Memfault API via AWS IoT Core and
MQTT. By dividing the data into manageable chunks, developers can ensure
efficient and reliable transmission, even in resource-constrained
environments. This approach enables comprehensive error reporting,
aiding in quicker issue resolution and enhancing the overall stability
of IoT applications.
