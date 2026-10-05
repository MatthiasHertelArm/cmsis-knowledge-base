---
id: "intr-practical-zephyr-west-workspaces-p-zephyr-as-dependency"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr as dependency"
summary: "When browsing allowed imports, we've seen that Zephyr has dependencies."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#zephyr-as-dependency"
license: "CC-BY-SA-4.0"
mode: "V"
---

When browsing allowed imports, we've seen that Zephyr has dependencies. What we haven't seen yet, is that Zephyr itself can be a dependency: Depending on your application, you might make use of some frameworks or SDKs that in turn depend on Zephyr and thus list it as _project_ in their own `west.yml` file.

E.g., looking at the [GitHub repository the _nRF Connect SDK_](https://github.com/nrfconnect/sdk-nrf/), we find that Nordic uses their own fork of the official Zephyr repository and has it listed as a _project_ in the SDK's [`west.yml`](https://github.com/nrfconnect/sdk-nrf/blob/e464540b74daca7f4a660f04fee0886b04365f70/west.yml#L62) file:

[`https://github.com/nrfconnect/sdk-nrf/blob/main/west.yml`](https://github.com/nrfconnect/sdk-nrf/blob/main/west.yml)

```yaml
manifest:
  projects:
    - name: zephyr
      repo-path: sdk-zephyr
      revision: 90a72daae2c8715d760d974a7d294aa2eb6b38c4
      import:
        name-allowlist:
          - TraceRecorderSource
          - canopennode
          - chre
          - ...
```

Another example is the [Golioth Zephyr SDK](https://docs.golioth.io/firmware/zephyr-device-sdk/), which lists the official Zephyr repository as a project in their [`west-zephyr.yml`](https://github.com/golioth/golioth-zephyr-sdk/blob/4f0fcea1370bfec84f6754caaca8b3f35bbc3573/west-zephyr.yml#L3) manifest:

[`https://github.com/golioth/golioth-zephyr-sdk/blob/main/west-zephyr.yml`](https://github.com/golioth/golioth-zephyr-sdk/blob/main/west-zephyr.yml)

```yaml
manifest:
  projects:
    - name: zephyr
      revision: v3.5.0
      url: https://github.com/zephyrproject-rtos/zephyr
      import: true
```

> **Note:** The _Golioth Zephyr SDK_ is now deprecated in favor of the [Golioth Firmware SDK](https://github.com/golioth/golioth-firmware-sdk), which is a Zephyr _module_ - something we won't discuss in this article series.

These dependencies are something that you need to handle yourself since [_West_ ignores projects that have already been defined in other files](https://docs.zephyrproject.org/latest/develop/west/manifest.html#manifest-imports). E.g., if you define _Zephyr_ as a project in your manifest file, and _after_ add [Golioth's Zephyr SDK](https://docs.golioth.io/firmware/zephyr-device-sdk/), then the _Zephyr_ project in the `west-zephyr.yml` file of the Golioth SDK is _ignored_.

It is your responsibility to ensure that the projects are **compatible** - or deal with resolving differences in case they are **not**. _West_ doesn't do that for you.

For some applications, it can therefore be beneficial to maintain multiple manifest files: E.g., when building for devices from Nordic, you may want to use the [`sdk-nrf`](https://github.com/nrfconnect/sdk-nrf) as a _project_ in your manifest file instead of adding "vanilla" _Zephyr_.

This may be tedious but is necessary and not a downside of using Zephyr: If you were to switch MCUs or if you'd be including a big SDK in any other firmware project, you'd also have to ensure compatibility. West manifests simply make this explicit, reproducible, and manageable.
