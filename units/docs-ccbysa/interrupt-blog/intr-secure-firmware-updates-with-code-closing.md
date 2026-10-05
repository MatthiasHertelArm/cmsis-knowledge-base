---
id: "intr-secure-firmware-updates-with-code-closing"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Closing"
summary: "Hope this post has convinced you that firmware signing can be implemented relatively simply, and that there are important benefits to doing so."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

Hope this post has convinced you that firmware signing can be implemented
relatively simply, and that there are important benefits to doing so.

There is much more we could do to secure our firmware update process. For
example, we should make sure we lock our flash when our application is running
to avoid an bug in our firmware being used to modify it. We also should consider
a more robust mechanism to "unlock" than our special Loader with development
keys.

These will perhaps be topics for future blog posts :-).

As always, we'd love to hear from you. How do you secure your firmware update
process? Let us know! And if you see anything you'd like to change, don't
hesitate to submit a pull request or open an issue on
[Github](https://github.com/memfault/interrupt)

> Interested in learning more device firmware update best practices? [Watch this webinar recording](https://hubs.la/Q02hgRrk0)









{:.no_toc}
