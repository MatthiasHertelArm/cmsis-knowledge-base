---
id: "intr-saving-bandwidth-with-delta-firmwa-conclusion"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Conclusion"
summary: "With the help of some great open source software, implementing delta updates in our Loader turned out to be relatively easy."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

With the help of some great open source software, implementing delta updates in
our Loader turned out to be relatively easy. A huge thanks especially to Jan
Jongboom for his reverse engineering of the jojodiff format and implementation
of an embedded-friendly patch library.

A separate post could be written about how to wrangle those updates on the
cloud side. Getting the right binary to the right device becomes more
complicated as we roll out features like Delta Updates. Perhaps we will tackle
this topic next time.

As always, we'd love to hear from you. Do you use a different approach to delta
updates? Let us know! And if you see anything you'd like to change, don't
hesitate to submit a pull request or open an issue on
[Github](https://github.com/memfault/interrupt)

> Interested in learning more device firmware update best practices? [Watch this webinar recording](https://hubs.la/Q02hgRrk0)







{:.no_toc}
