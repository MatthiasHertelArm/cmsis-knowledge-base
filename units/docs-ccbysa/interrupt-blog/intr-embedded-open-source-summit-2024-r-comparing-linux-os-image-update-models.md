---
id: "intr-embedded-open-source-summit-2024-r-comparing-linux-os-image-update-models"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Comparing Linux OS Image Update Models"
summary: "Drew Moseley, from Toradex and ex-Mender engineer, did some great research to compare different strategies to update Linux systems."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#comparing-linux-os-image-update-models"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=enejawJmb5k&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=11&pp=iAQB)
- Recommended by: Thomas

Drew Moseley, from Toradex and ex-Mender engineer, did some great research to
compare different strategies to update Linux systems. He starts with a little
explanation of what delta updates can look like for an A/B system: he covers
SWUpdate with ZChunks, Rauc, and Mender proprietary delta-update. Of course, he
also includes Toradex and starts with a little refresher of how it works
differently using libostree (a git like approach to your entire filesystem).

Then he devised a few “update scenarios”, including one very small change in a
configuration file, installing a big package, removing a big package. The choice
of scenarios seemed very relevant to me and I was glad to see someone take the
time to “run the numbers” and compare the number of bytes downloaded for each
scenario and each solution.

As always, the perfect solution will depend on your use-case. This talk gives a
solid methodology and some solid starting numbers to compare different
approaches. Thank you Drew for taking the time to do this and share it with the
community!
