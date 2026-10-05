---
id: "intr-a-practical-guide-to-ble-throughpu-examples"
type: "concept"
domain: "debug"
title: "A Practical Guide to BLE Throughput: Examples"
summary: "For iOS 10 and above, most iOS devices support a 185 byte MTU and 7 packets per connection interval. The lowest connection interval which can be negotiated for normal applications is 15ms."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-24-ble-throughput-primer.md"
doc_source: "https://interrupt.memfault.com/blog/ble-throughput-primer#examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

{:.no_toc}

### iPhone SE BLE Throughput Analysis

For iOS 10 and above, most iOS devices support a 185 byte MTU and 7 packets per connection interval. The lowest connection interval which can be negotiated for normal applications is 15ms. Let's take a look at the realistic throughput which can be achieved!

First let's make sure we can transmit 7 packets in 15ms:

`7 * (328μs Data + 150μs + 80μs ACK + 150μs) = 4.956ms`

Now that we know the packets fit, we can take the duty cycle we are achieving and multiply it by the ATT throughput maximums tabulated above.

`Data Rate = (4.956ms / 15ms) * 36.7 kBytes/Sec = 12.2 kBytes/sec = 0.10 Mbps`

{:.no_toc}

{: #optimal-connection-interval-example}

### Optimizing throughput Example

Let's figure out if we can improve the throughput for the following application:

- the connection parameter being used is 11.25ms (minimum supported for the device we are using)
- data packet length extension is being used with 251 byte packets being sent
- both devices will send as much data they can fit in a connection interval
- 1 MB PHY is being used

From the examples above, we know it takes 2500μs to exchange a 251 byte data payload. This means we can fit 4 transfers in a 11.25ms connection interval. No data will be sent in the last 1.25ms of the window since it does not fit. This gives us a throughput of:

`(251 bytes * 4 packets) / 11.25 ms = 89kBytes/sec = 0.713Mbps`

If we chose a slightly larger connection interval that is a multiple of our transfer duration
(2500μs) we can fill the connection interval without any gap where no data is sent. For example, in
a 12.5ms window, we can fit 5 packets perfectly. This gives us a ~13% improvement in overall throughput:

`(251 bytes * 5 packets) / 12.5 ms = 100.4kBytes/sec = 0.803Mbps`

The important takeaway here is that in some scenarios a slower connection interval can actually yield faster throughput!
