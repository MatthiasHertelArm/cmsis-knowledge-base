---
id: "intr-how-to-build-drivers-for-zephyr-dependency-management"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Dependency Management"
summary: "There are a few different ways of handling dependencies in firmware land. I've used Git submodules as my dependency \"manager\" of choice. Zephyr though, is very opinionated on how you should work with your dependencies."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#dependency-management"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are a few different ways of handling dependencies in firmware land. I've used Git submodules as my dependency "manager" of choice. Zephyr though, is very opinionated on how you should work with your dependencies. Let's look into how we do that with `west` and a `west.yml` file.

`west.yml` is a manifest file much like a `Cargo.toml` in rust or `package.json` for Node. You initialize a Zephyr repository using `west init` command. This does a shallow `git` clone for each dependency and puts them into place.

Here's what a `west.yml` file may look like. This was for a personal project that uses [NanoPB](https://github.com/nanopb/nanopb) and also the nRF Connect SDK.

```yaml
manifest:
  remotes:
    - name: nrfconnect
      url-base: https://github.com/nrfconnect
    - name: nanopb
      url-base: https://github.com/nanopb
  projects:
    - name: nrf
      remote: nrfconnect
      revision: v1.3.0
      import: true
    - name: nanopb
      repo-path: nanopb
      revision: 0.3.9
      path: pyrinas/ext/nanopb
      remote: nanopb
  self:
    # This repository should be cloned to ncs/nrf.
    path: pyrinas
```

The `west.yml` file doesn't affect driver operation. If you're going to include your drivers as a separate repo though, this is where you would add it! You can learn more though by going to the Zephyr documentation on [West Manifests](https://docs.zephyrproject.org/1.14.1/guides/west/manifest.html). (complete with crazy dependency diagrams and more!)
