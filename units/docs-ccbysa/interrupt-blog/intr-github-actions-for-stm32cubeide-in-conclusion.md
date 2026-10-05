---
id: "intr-github-actions-for-stm32cubeide-in-conclusion"
type: "concept"
domain: "debug"
title: "GitHub Actions for STM32CubeIDE: In Conclusion"
summary: "I hope you enjoyed this article! It's always a fun challenge to coax some of the less cooperative tools into working in a CI environment, and STM32CubeIDE was no exception."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-01-github-actions-for-stm32cubeide.md"
doc_source: "https://interrupt.memfault.com/blog/github-actions-for-stm32cubeide#in-conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

I hope you enjoyed this article! It's always a fun challenge to coax some of the
less cooperative tools into working in a CI environment, and STM32CubeIDE was no
exception.

You could use a similar process for other Eclipse-based IDEs since most support
the `-build` command line argument.

One last note- this example is saving the build artifacts (`.elf` and `.bin`
files, etc.) as GitHub Actions artifacts, but you could also upload them to a
cloud storage service, or even use the GitHub API to create a release with the
artifacts attached. One simple approach is to push the artifacts into AWS S3
storage under a folder named after the commit hash so you can easily find the
artifacts for a given commit.

Thanks for reading!









{:.no_toc}
