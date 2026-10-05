---
id: "sds-theory"
type: "concept"
domain: "test"
title: "theory"
summary: "The SDS Framework enables recording and playback of one or more data streams for an application under development, as shown in the diagram below. With the SDSIO interface, the data streams are connected to SDS data files."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md"
license: "Apache-2.0"
mode: "V"
---

﻿# Theory of Operation

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->
<!-- markdownlint-disable MD060 -->

The SDS Framework enables recording and playback of one or more data streams for an application under development, as shown in the diagram below. With the SDSIO interface, the data streams are connected to SDS data files. The file storage can be either embedded within the system and accessed via a file system, or external (on a host computer) and accessed via a communication interface such as Ethernet or USB.

The DSP or ML algorithms under test operate on blocks and are executed periodically. This documentation uses the term **Data Block** to refer to a block of input or output data that is processed in one step by a DSP or ML compute node.

(figure: SDSIO Interface for Player and Recorder)

Using the SDS Stream Interface functions (`sds.c/h`), the data stream under development may read and write as shown above. The Stream Interface functions store data streams in a circular buffer (`sds_buffer.c/h`). This circular buffer is the I/O queue for the SDSIO-Client (`sdsio_x.c/h`).

(figure: Implementation Files of SDS)
