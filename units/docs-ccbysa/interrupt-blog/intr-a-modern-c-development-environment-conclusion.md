---
id: "intr-a-modern-c-development-environment-conclusion"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Conclusion"
summary: "If you've managed to bear with me until this point, thank you for reading! Our job is done here, the library builds, the report is available as an artifact, and all of this without clogging our computer with tools."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you've managed to bear with me until this point, thank you for reading! Our job is done here, the library builds, the report is available as an artifact, and all of this without clogging our computer with tools.



But are we really ever done? A development environment grows with the project, and so will your base image. Even at this point, it grew fairly large, and if that is a problem for you or your contributors, you should look into some of the [strategies to reduce your image size](https://www.docker.com/blog/reduce-your-image-size-with-the-dive-in-docker-extension/). Another strategy is to split images based on their usage, e.g., use a different image for building and another one for testing. This can greatly reduce your image size and allows you to use already stripped-down base images.

One last thing that is worth mentioning, is that with [Docker Desktop](https://www.docker.com/products/docker-desktop/) you can now comfortably inspect your image for vulnerabilities, and also check the size impact of each step in your Dockerfile and even its base image:



This is a great starting point in case you want to reduce the image size or update packages. E.g., you could uninstall unused packages using `apt remove` as a last step in your *Dockerfile*, or install a more recent version of `ruby` using the [Ruby Version Manager](https://rvm.io/) instead of relying on the outdated version that comes with `apt`. This discussion, however, is far beyond the scope of this article.

As mentioned throughout the article, the [example project is available on GitHub](https://github.com/lmapii/cproject). Feel free to point out my mistakes or add some improvements to the project yourself!

You have now all the skills to set up a containerized C/C++ project with a CI on GitHub. With this at hand, it should be easy to add a specific compiler to your *Dockerfile* or to clean up all the mistakes that I did when setting up the CI.







{:.no_toc}
