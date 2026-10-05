---
id: "intr-device-firmware-update-cookbook-closing"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Closing"
summary: "I hope this post will prove useful next time you need to implement DFU on a device! While there are plenty of good reasons to stray from this design, it is a solid base upon which to build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

I hope this post will prove useful next time you need to implement DFU on a
device! While there are plenty of good reasons to stray from this design, it is
a solid base upon which to build.

In systems where code space isn't a challenge, I would have made different
choices. For example, I would have allocated a slot to the Updater. I would also
recommend allocating two slots to the Application so A/B updates can be
implemented.

One topic we did not cover at all is security. In 2020, firmware security is an
important topic and DFU is a key component in the security architecture of a
device. We will cover this in a post next month.

As always, we'd love to hear from you. Do you have design rules of thumb for
firmware update that we did not cover? Let us know! And if you see anything
you'd like to change, don't hesitate to submit a pull request or open an issue
on [Github](https://github.com/memfault/interrupt)

> Interested in learning more device firmware update best practices? [Watch this webinar recording](https://hubs.la/Q02hgRrk0)



{:.no_toc}
