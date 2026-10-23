---
id: "mcuboot-serial-recovery-transport-encoding"
type: "concept"
domain: "boot-update"
title: "Serial recovery: Transport encoding"
summary: "By default, SMP packets are exchanged using the SMP over console encoding: each packet is prefixed with a two-byte length, protected with a CRC16, base64-encoded and split into \\n-terminated frames marked with start and continuation markers."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/serial_recovery.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/serial_recovery.md#transport-encoding"
license: "Apache-2.0"
mode: "V"
---

By default, SMP packets are exchanged using the *SMP over console* encoding:
each packet is prefixed with a two-byte length, protected with a CRC16,
base64-encoded and split into ``\n``-terminated frames marked with start and
continuation markers.

When the ``MCUBOOT_SERIAL_RAW_PROTOCOL`` option is enabled (on Zephyr,
``CONFIG_BOOT_SERIAL_RAW_PROTOCOL``), the *raw* encoding is used instead.
The SMP packet (header directly followed by the payload) is transferred as
binary without base64 encoding, length prefix, CRC or console framing. Packet
boundaries are derived from the length field of the SMP header.

Compared to SMP over console, the raw encoding uses less flash and RAM and
allows faster transfers, at the cost of requiring a binary-capable serial link.
The two encodings are mutually exclusive and selected at build time; the mcumgr
client must be configured to use a matching raw transport (for example a Zephyr
application built with ``CONFIG_UART_MCUMGR_RAW_PROTOCOL``).

Because the raw encoding has no CRC or framing to detect a truncated packet, a
stalled or malformed transfer would otherwise wedge serial recovery. To prevent
this, ``BOOT_SERIAL_RAW_PROTOCOL_INPUT_TIMEOUT`` (Zephyr:
``CONFIG_BOOT_SERIAL_RAW_PROTOCOL_INPUT_TIMEOUT``) discards a partially received
packet after ``BOOT_SERIAL_RAW_PROTOCOL_INPUT_TIMEOUT_MS`` milliseconds without
new data and awaits a fresh command. It is enabled by default whenever the raw encoding is used, and
mirrors Zephyr's ``CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT``.

Because the raw encoding has no per-line delimiter, each receive interrupt is
delivered as its own fragment, so the ``BOOT_LINE_BUFS`` receive buffers are
consumed faster than with the console encoding. If a link can deliver data
faster than recovery drains it (received bytes are dropped when the buffers are
exhausted), increase ``BOOT_LINE_BUFS``.
