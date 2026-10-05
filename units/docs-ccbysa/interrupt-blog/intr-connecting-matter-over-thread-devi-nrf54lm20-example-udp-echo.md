---
id: "intr-connecting-matter-over-thread-devi-nrf54lm20-example-udp-echo"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: nRF54LM20 Example: UDP Echo"
summary: "Let's put this into practice. We will send a UDP message from an nRF54LM20 DK through a HomePod Border Router to Nordic Semiconductor's public echo server found at udp-echo.nordicsemi.academy:2444, and receive the response."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#nrf54lm20-example-udp-echo"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's put this into practice. We will send a UDP message from an nRF54LM20 DK through a HomePod Border Router to Nordic Semiconductor's public echo server found at `udp-echo.nordicsemi.academy:2444`, and receive the response.

The nRF54LM20[^nrf54lm20] is a good fit for Matter. It has an ARM Cortex-M33
at 128 MHz, 2 MB of NVM (it's actually RRAM, not flash, which is pretty cool) and 512 KB of RAM, which is plenty of headroom for the Matter stack, OpenThread, and application code. It supports both BLE (for commissioning) and 802.15.4 (for Thread).

Let's grab a nRF54LM20 Dev Kit[^lm20dk], the latest of the nRF Connect SDK[^ncs] and start writing some code!

### Project Setup

We set up NCS and started from the Matter template sample (`samples/matter/template`). You can learn more about setting up NCS in [Nordic's excellent documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/installation/install_ncs.html).

We need to toggle a few KConfig to get things working in our example:

```
# prj.conf

# Enable Matter
CONFIG_CHIP=y

# OpenThread DNS client (for resolving hostnames via Thread network)
CONFIG_OPENTHREAD_DNS_CLIENT=y

# Shell support (for our echo commands)
CONFIG_CHIP_LIB_SHELL=y
CONFIG_OPENTHREAD_SHELL=y
```

`CONFIG_OPENTHREAD_DNS_CLIENT=y` is the important one. It enables the DNS client
in the OpenThread stack, which allows us to resolve hostnames using the Border
Router's DNS proxy. Without it, you would have to hardcode IP addresses.

### DNS Resolution

Before we can send a UDP packet, we need to resolve the echo server's address.
OpenThread provides a DNS client API that sends queries through the Border
Router's DNS proxy.

For NAT64, we resolve the A record (IPv4) using `otDnsClientResolveIp4Address`.
The OpenThread DNS client automatically synthesizes a NAT64 IPv6 address from
the result:

```c
#include <openthread/dns_client.h>
#include <openthread/nat64.h>

#define ECHO_SERVER_HOST "udp-echo.nordicsemi.academy"

static K_SEM_DEFINE(dns_sem, 0, 1);
static otIp6Address resolved_addr;
static bool dns_resolved_ok;

static void dns_resolve_cb(otError aError,
                           const otDnsAddressResponse *aResponse,
                           void *aContext)
{
    if (aError != OT_ERROR_NONE) {
        dns_resolved_ok = false;
        k_sem_give(&dns_sem);
        return;
    }

    uint32_t ttl;
    otError err = otDnsAddressResponseGetAddress(aResponse, 0,
                                                  &resolved_addr, &ttl);
    dns_resolved_ok = (err == OT_ERROR_NONE);
    k_sem_give(&dns_sem);
}

static bool resolve_echo_server(otInstance *instance)
{
    k_sem_reset(&dns_sem);
    dns_resolved_ok = false;

    openthread_mutex_lock();
    otError err = otDnsClientResolveIp4Address(
        instance, ECHO_SERVER_HOST, dns_resolve_cb, NULL, NULL);
    openthread_mutex_unlock();

    if (err != OT_ERROR_NONE) {
        return false;
    }

    if (k_sem_take(&dns_sem, K_SECONDS(10)) != 0) {
        return false;
    }

    return dns_resolved_ok;
}
```

The DNS resolution is asynchronous. We use a semaphore to block until the
callback fires. On success, `resolved_addr` contains a synthesized IPv6 address
that embeds the server's IPv4 address with the Border Router's NAT64 prefix.

> **Note:** In my testing with a HomePod mini, the DNS proxy could not follow
> CNAME chains for certain hostnames. If DNS resolution fails, you can fall back
> to a hardcoded IPv4 address and synthesize the NAT64 address manually using
> `otNat64SynthesizeIp6Address`.

### Sending and Receiving UDP

With the address resolved, we can open a UDP socket and send a message. We use
the OpenThread native UDP API rather than Zephyr's socket API. The OpenThread stack is already quite large, so we save some code space by not having to pull the full Zephyr networking stack alongside it.

Here's what it looks like:

```c
#include <openthread/udp.h>
#include <openthread/message.h>

#define ECHO_SERVER_PORT 2444
#define RECV_TIMEOUT_MS  5000

static K_SEM_DEFINE(udp_recv_sem, 0, 1);
static char udp_recv_buf[256];
static int udp_recv_len;

static void udp_receive_cb(void *aContext, otMessage *aMessage,
                            const otMessageInfo *aMessageInfo)
{
    uint16_t offset = otMessageGetOffset(aMessage);
    uint16_t length = otMessageGetLength(aMessage) - offset;

    if (length > sizeof(udp_recv_buf) - 1) {
        length = sizeof(udp_recv_buf) - 1;
    }

    udp_recv_len = otMessageRead(aMessage, offset,
                                  udp_recv_buf, length);
    udp_recv_buf[udp_recv_len] = '\0';
    k_sem_give(&udp_recv_sem);
}

static int send_udp(otInstance *instance,
                     const otIp6Address *addr,
                     const char *msg)
{
    otUdpSocket socket;
    otSockAddr bind_addr;
    otMessageInfo msg_info;
    otMessage *ot_msg;
    otError err;

    /* Open and bind a UDP socket */
    memset(&socket, 0, sizeof(socket));
    openthread_mutex_lock();

    err = otUdpOpen(instance, &socket, udp_receive_cb, NULL);
    if (err != OT_ERROR_NONE) {
        openthread_mutex_unlock();
        return -1;
    }

    memset(&bind_addr, 0, sizeof(bind_addr));
    otUdpBind(instance, &socket, &bind_addr, OT_NETIF_THREAD);

    /* Allocate and populate a message buffer */
    ot_msg = otUdpNewMessage(instance, NULL);
    if (!ot_msg) {
        otUdpClose(instance, &socket);
        openthread_mutex_unlock();
        return -1;
    }

    otMessageAppend(ot_msg, msg, (uint16_t)strlen(msg));

    /* Set destination and send */
    memset(&msg_info, 0, sizeof(msg_info));
    msg_info.mPeerAddr = *addr;
    msg_info.mPeerPort = ECHO_SERVER_PORT;

    k_sem_reset(&udp_recv_sem);
    err = otUdpSend(instance, &socket, ot_msg, &msg_info);
    openthread_mutex_unlock();

    if (err != OT_ERROR_NONE) {
        return -1;
    }

    /* Wait for the echo response */
    if (k_sem_take(&udp_recv_sem, K_MSEC(RECV_TIMEOUT_MS)) == 0) {
        printk("Received: %s\n", udp_recv_buf);
    } else {
        printk("Timeout, no response\n");
    }

    openthread_mutex_lock();
    otUdpClose(instance, &socket);
    openthread_mutex_unlock();

    return 0;
}
```

A few things to note about the OpenThread UDP API:

- **Mutex discipline.** OpenThread is not thread-safe. You must hold the
  `openthread_mutex` when calling OT APIs. We release it before blocking on the
  receive semaphore so the OT thread can process incoming packets.
- **Message buffers.** OpenThread uses its own message pool (`otMessage`), not
  flat byte arrays. You allocate with `otUdpNewMessage` and append data with
  `otMessageAppend`. The stack takes ownership of the message on `otUdpSend`,
  so do not free it yourself.
- **Bind to Thread.** The `OT_NETIF_THREAD` parameter in `otUdpBind` ensures
  the socket is bound to the Thread network interface.

### Trying It Out

After building and flashing with `west`, commission the device into your Thread network using a Matter controller. Look for this log line:

```
00:00:00.140,606] <inf> chip: [SVR]https://project-chip.github.io/connectedhomeip/qrcode.html?data=xxxxxx
```

Copy the URL in your browser, and scan the resulting QR code with your favorite Matter ecosystem app (I used Apple Home).


Once commissioned, connect to the UART console and first check that everything is working as expected:

```
uart:~$ echo status
Thread role: router
  IPv6: fdd7:c450:969a:0:0:ff:fe00:a000
  IPv6: fd7e:67af:9049:1:4ed0:80d4:5675:8326
  IPv6: fdd7:c450:969a:0:76a:9a56:214b:b9dd
  IPv6: fe80:0:0:0:a01c:abda:791a:e404
```

Next, let's run our UDP echo test:

```
uart:~$ echo nat64 "hello from Matter"
Resolving udp-echo.nordicsemi.academy (A via NAT64)...
Sending to [64:ff9b::1452:10a4]:2444
Sent 17 bytes: "hello from Matter"
Received 44 bytes: "1742480123: hello from Matter"
```

The echo server prepends a timestamp and sends the message back. The address
`64:ff9b::1452:10a4` is the NAT64-synthesized IPv6 address, where `1452:10a4` is
`20.82.16.164` encoded in hex.

That is a UDP packet originating from a Thread device, traversing the mesh to a
HomePod, getting NAT64-translated to IPv4, hitting a server in the cloud, and
coming back. All in under a second.
