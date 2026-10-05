---
id: "intr-secure-firmware-updates-with-code"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing"
summary: "Previously, we wrote about implementing firmware update for our devices. One important detail we did not cover is firmware update security."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Previously](https://interrupt.memfault.com/blog/device-firmware-update-cookbook), we
wrote about implementing firmware update for our devices. One important detail
we did not cover is firmware update security.

Much can be done - and written - about firmware update security, but perhaps the
most important bit is firmware signing. Other security measures are not much use
if we cannot verify the authenticity of a firmware update!


In this post, we explain why firmware signing is important, how it works, and
what algorithm should be used to implement it. We also detail a full
implementation built with open source, cross platform libraries.


> If you'd rather listen to me present this information and see some demos in action, watch
> [this webinar recording](https://hubs.la/Q02hgRrk0)
