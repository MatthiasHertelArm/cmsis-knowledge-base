---
id: "intr-i2c-in-a-nutshell"
type: "concept"
domain: "debug"
title: "I2C in a Nutshell"
summary: "<style> div[id^=\"WaveDrom\"] { text-align: center; } </style>"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-22-i2c-in-a-nutshell.md"
doc_source: "https://interrupt.memfault.com/blog/i2c-in-a-nutshell"
license: "CC-BY-SA-4.0"
mode: "V"
---

`<style>`
div[id^="WaveDrom_"] {
    text-align: center;
}
`</style>`


I2C is perhaps the most commonly used bus to connect ICs together. As such,
firmware engineers encounter it on most projects. In this post, we explain how I2C
works, explore common bugs and investigate how to debug these issues.
