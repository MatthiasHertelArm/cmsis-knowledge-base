---
id: "sds-sdsio-interface-layer-sdsio-fs"
type: "concept"
domain: "test"
title: "SDSIO Interface: Layer: sdsio_fs"
summary: "The layer/sdsio/filesystem/sdsiofs.clayer.yml is configured for recording to a Memory Card. It uses the MDK-Middleware File System component."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio-fs"
license: "Apache-2.0"
mode: "V"
---

The [`layer/sdsio/filesystem/sdsio_fs.clayer.yml`](https://github.com/ARM-software/SDS-Framework/tree/main/layer/sdsio/filesystem) is configured for recording to a Memory Card. It uses the MDK-Middleware File System component.

### Using File System Interface

The file system interface, used together with a template, enables recording of [SDS data files](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sds-data-files) to the SD card on the embedded board.

Recording can be started and stopped using the on-board user button.

Once the desired number of recordings has been captured, the SD card can be removed and transferred to a PC for review, copying, or labeling of the recorded data.

!!! Note
    The template-based file system implementation natively supports recording mode only.
    Playback mode can be enabled by adapting the provided template code.
    For example, an additional button on the board can be used to toggle between recording and playback modes.
