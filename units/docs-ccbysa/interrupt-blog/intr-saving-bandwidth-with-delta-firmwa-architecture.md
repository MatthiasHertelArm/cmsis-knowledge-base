---
id: "intr-saving-bandwidth-with-delta-firmwa-architecture"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Implementation / Architecture"
summary: "As a reminder, this is what our device firmware update architecture looks like:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Delta Updates Implementation_

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

1. Bootloader: a simple program whose sole job is to load the Loader, and fall back
   to another image if the Loader is invalid.
2. Loader: a program that can verify our Application image, load it, and update
   it.
3. Application: our main code, which does not do any updates itself
4. Updater: a program that temporarily replaces the Application and can update
   the Loader.

The Loader and the Updater both may want to implement delta updates, while the
Application or the Bootloader would be mostly untouched.
