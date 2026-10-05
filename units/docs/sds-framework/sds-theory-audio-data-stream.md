---
id: "sds-theory-audio-data-stream"
type: "concept"
domain: "test"
title: "theory: SDS Metadata Format / Audio data stream"
summary: "Describes audio data format, typically used for a microphone data stream."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#audio-data-stream"
license: "Apache-2.0"
mode: "V"
---

_Part of: SDS Metadata Format_

Describes audio data format, typically used for a microphone data stream.

`content:`                                               | Audio metadata for `content:` node
:--------------------------------------------------------|:---------------------------------------------------
`- audio:`                                               | Audio format specification
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `bit-depth:`        | Bits per audio sample (required)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `channels:`         | Number of interleaved audio channels (required)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `format:`           | Audio format used (optional), currently only `pcm` is supported

**Example:**

```yml
sds:
  name: Mono
  description: Mono 16-bit PCM microphone
  sample-frequency: 16000
  content:
    - audio:
        bit-depth: 16
        channels: 1
        format: pcm
```
