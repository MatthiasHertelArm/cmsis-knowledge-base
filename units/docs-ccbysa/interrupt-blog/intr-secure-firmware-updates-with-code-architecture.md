---
id: "intr-secure-firmware-updates-with-code-architecture"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Firmware Signing Implementation / Architecture"
summary: "Part of: Firmware Signing Implementation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Firmware Signing Implementation_

As a reminder, this is what our device firmware update architecture looks like:

`<style>`
.diag4 {
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}
`</style>`

blockdiag {
    span_width = 100;
    // Set labels to nodes.
    C [label = "Bootloader"];
    A [label = "App Loader"];
    B [label = "Application"];
    C -> A [label = "Loads", fontsize=8];
    A -> B [label = "Ld, Updt", fontsize=8];

    E [label = "Updater"];
    A -> E [label = "Ld, Updt", fontsize=8];
    E -> A [label = "Updates", fontsize=8];
    C -> E [label = "Loads", style=dashed, fontsize=8];

    group {
        label = "Slot 0";
        color = "PaleGreen";
        C;
    }
    group {
        label = "Slot 1";
        color = "LightPink";
        A;
    }
    group {
        label = "Slot 2";
        color = "LemonChiffon";
        B; E;
    }
}
{:.diag4}

With the following functionality for each block:

1. Bootloader: a simple program whose sole job is to load the Loader, and fallback
   to another image if the Loader is invalid.
2. Loader: a program that can verify our Application image, load it, and update
   it.
3. Application: our main code, which does not do any updates itself
4. Updater: a program that temporarily replaces the Application and can update
   the Loader.

The Loader, the Application, and the Updater all need to be signed since they
can be updated. Components that update other components need to implement our
signature verification algorithm, in our case that's the Loader and the Updater.
