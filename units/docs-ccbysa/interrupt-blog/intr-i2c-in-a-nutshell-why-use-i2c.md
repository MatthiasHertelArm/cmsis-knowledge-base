---
id: "intr-i2c-in-a-nutshell-why-use-i2c"
type: "concept"
domain: "debug"
title: "I2C in a Nutshell: Why use I2C"
summary: "I2C has many advantages: 1. It is cheaper to implement than comparable low-power buses, with fewer pins than SPI[^5], and a simpler physical layer than CAN[^6] (no differential signalling). 2."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-22-i2c-in-a-nutshell.md"
doc_source: "https://interrupt.memfault.com/blog/i2c-in-a-nutshell#why-use-i2c"
license: "CC-BY-SA-4.0"
mode: "V"
---

I2C has many advantages:
1. It is cheaper to implement than comparable low-power buses, with fewer pins
   than SPI[^5], and a simpler physical layer than CAN[^6] (no differential
signalling).
2. It supports up to 127 devices on a bus with only two pins.
3. It has transfer rates up to 400Kbps, which is fast enough for many human
   interfaces as well as fan control, temperature sensing and other low-speed
control loops.
4. Historically, it has been less onerous for manufacturers to include than
   competing protocols like Maxim's 1-wire protocol[^4].

Many of the sensors and actuators in devices all around us use I2C:
temperature sensors, accelerometers, gyroscopes, fans, video bridging chips,
GPIO expanders, EEPROMs, ...etc.

I2C is not appropriate for all applications however:
1. When higher bandwidth is required, SPI may be the right choice and can be found
   in many NOR-flash chips. MIPI can go even faster, and is often used in
displays and cameras.
2. If reliability is a must, CAN is the bus of choice. It is found in cars and
   other vehicles.
3. When a single device is on the bus, UART may work just as well.
