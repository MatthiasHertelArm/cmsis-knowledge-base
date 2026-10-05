---
id: "intr-embedded-open-source-summit-2024-r-engineering-secure-ssh-access-for-engine"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Engineering Secure SSH Access for Engineers"
summary: "Colin (Garmin) goes through the challenges for enabling SSH access to devices in production. Passwords and secret keys are not great solutions: if you share one across all your devices then a leak would be catastrophic."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#engineering-secure-ssh-access-for-engineers"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=M8RTsz0I5bM&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=60&pp=iAQB)
- Recommended by: Thomas

Colin (Garmin) goes through the challenges for enabling SSH access to devices in
production. Passwords and secret keys are not great solutions: if you share one
across all your devices then a leak would be catastrophic. And a leak is hard to
protect against because the engineers need the keys with them when doing
maintenance work. So instead, he recommends using certificates to create keys
that are only valid for one hour or one day. The device SSH daemon validates
that the engineer key has been signed by the proper certificate, and that we are
still within the correct validity period. This way, the only real secret (the
private key used to sign the keys) can be stored in a very safe storage,
engineers are only granted access for a few hours (so an ex-employee will not
have access anymore).

The talk goes in much more details on how to actually implement this.
Demonstrates the commands to create certificates, options available in SSH to
restrict permissions of the key, mentions a few tools that can be used to manage
the certificate and sign the keys for the engineers, etc. He also discusses some
challenges that are specific to embedded devices such as how to deal with devices
that may not have the correct time set (he also reminds us that NTP is not a
safe protocol and time attacks are possible).

A great talk from someone who has obviously gone pretty far into the
implications of keeping SSH open on production device. Another one that I will
be recommending for years to come!
