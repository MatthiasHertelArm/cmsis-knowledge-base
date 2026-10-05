---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-capturing-a-trace"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: Capturing a Trace"
summary: "Now that we have the Saleae, let's trace a read transaction. The steps we will walk through below would work for any other type of transaction you want to investigate as well:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#capturing-a-trace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have the Saleae, let's trace a read transaction. The steps we will walk through below would work for any other type of transaction you want to investigate as well:

Let's read the `g_crash_config` variable and see what happens

First, we need to halt GDB by running `CTRL-C`, then "Start" a capture within the Saleae Logic App and run this in GDB:

```
(gdb) p/x g_crash_config
$1 = 0x0
```

We can determine the address and size of the read that needs to take place by inspecting the variable in gdb:

```
(gdb) p sizeof(g_crash_config)
$3 = 4
(gdb) p &g_crash_config
$4 = (int *) 0x20000108 <g_crash_config>
```

The first transaction we see over the wire gets decoded by the Saleae as follows:



We see it's an `ABORT` Debug Port write. This is a good operation to run before issuing any transactions because it will reset the state of the current `AP` and put the debugger into a known state. If you wanted to decode the transaction without the Saleae analyzer, the ADIv5 reference manual[^2] provides the information needed. The structure for a write operation looks like this:



### Saleae CSV Trace

The Saleae analyzer also lets us export the analysis as a CSV file. Let's walk through the transactions that we see. I've added some observation notes inline below:

```
Time [s], Analyzer Name, Decoded Protocol Result
//
// Write to the AP Abort Register (ABORT) to reset state
//
3.235528170000000,SWD,Request  DebugPort Write ABORT
3.235544810000000,SWD,Turnaround
3.235546840000000,SWD,ACK OK
3.235552900000000,SWD,Turnaround
3.235554950000000,SWD,WData 0x0000001E reg ABORT bits ORUNERRCLR=1, WDERRCLR=1, STKERRCLR=1, STKCMPCLR=1, DAPABORT=0
3.235621490000000,SWD,Data parityok
3.235623550000000,SWD,Trailing bits
//
// Write to the SELECT register. This is used to target the AP of
// interest. You can discover all the available APs by walking through
// the "ROM Table" (more details in the ADIv5 Specification). Per the
// Coresight specification, we know when APSEL=0x0, the AP selected
// is AHB-AP
//
3.235647510000000,SWD,Request  DebugPort Write SELECT
3.235664140000000,SWD,Turnaround
3.235666160000000,SWD,ACK OK
3.235672230000000,SWD,Turnaround
3.235675260000000,SWD,WData 0x00000000 reg SELECT bits APSEL=0x00, APBANKSEL=0x0, PRESCALER=0x0
3.235741780000000,SWD,Data parityok
3.235746540000000,SWD,Request  AccessPort Write CSW
3.235763170000000,SWD,Turnaround
3.235765200000000,SWD,ACK OK
3.235771260000000,SWD,Turnaround
//
// We are accessing a AHB-AP of type MEM-AP. The CSW register is
// written to in order to configure what type of access will be
// performed. One interesting setting is AddrInc which is used to
// control whether or not the access address is automatically
// incremented after a read.
//
3.235774290000000,SWD,WData 0x23000012 reg CSW bits DbgSwEnable=0, Prot=0x23, SPIDEN=0, Mode=0x0, TrInProg=0, DeviceEn=0, AddrInc=Increment single, Size=Word (32 bits)
3.235840750000000,SWD,Data parityok
//
// The Transfer Address Register (TAR) is now programmed with
// address of interest. It's close to the address we are trying to
// read (0x20000108) but interestingly does _not_ match
//
3.235844790000000,SWD,Request  AccessPort Write TAR
3.235861420000000,SWD,Turnaround
3.235863450000000,SWD,ACK OK
3.235869510000000,SWD,Turnaround
3.235872550000000,SWD,WData 0x20000100 reg TAR
3.235939040000000,SWD,Data parityok
//
// A request to read the data via the Data Read/Write Register (DRW)
// is finally issued. This will return the data at address 0x20000100
// and then increment the address in the TAR by 1 word so the next read
// would return 0x20000104
//
3.235943310000000,SWD,Request  AccessPort Read DRW
3.235959910000000,SWD,Turnaround
//
// Data is not ready yet so a ACK WAIT is returned
//
3.235961940000000,SWD,ACK WAIT
3.235971240000000,SWD,Request  AccessPort Read DRW
3.235987840000000,SWD,Turnaround
//
// Our read request has been ACKd. Per the ADIv5 documentation
// the read request has "posted" which means that
// "the result of the access is returned on the next transfer.
// This result can be another AP register read, or a DP register
// read of RDBUFF." This means the data in this transaction
// should be discarded
//
3.235989860000000,SWD,ACK OK
3.235995920000000,SWD,WData 0x00000000 reg DRW
3.236062190000000,SWD,Data parityok
3.236068440000000,SWD,Request  AccessPort Read DRW
3.236085030000000,SWD,Turnaround
3.236087060000000,SWD,ACK OK
//
// The actual value of the data at 0x20000100.
//
3.236093120000000,SWD,WData 0x00000000 reg DRW
3.236163440000000,SWD,Data parityok
3.236169630000000,SWD,Request  AccessPort Read DRW
3.236186220000000,SWD,Turnaround
3.236188250000000,SWD,ACK OK
//
// The actual value of the data at 0x20000104.
//
3.236194310000000,SWD,WData 0x00000000 reg DRW
3.236260570000000,SWD,Data parityok
3.236266750000000,SWD,Request  AccessPort Read DRW
3.236283360000000,SWD,Turnaround
3.236285380000000,SWD,ACK OK
//
// The actual value of the data at 0x20000108. (The address we
// wanted to read in the first place!)
//
3.236291450000000,SWD,WData 0x00000000 reg DRW
3.236357710000000,SWD,Data parityok
3.236363900000000,SWD,Request  AccessPort Read DRW
3.236380490000000,SWD,Turnaround
3.236382520000000,SWD,ACK OK
//
// The actual value of the data at 0x20000110.
//
3.236388580000000,SWD,WData 0x3910E7EF reg DRW
[...]
// In the actual trace we see another 12 reads performed
// bringing the total bytes read by the debugger to 16 bytes.
```

That's interesting, it seems like the debugger is caching 16 bytes of data. If we "Start" a trace while reading in this memory range we will see no SWD transactions get issued! To test it out, start the Saleae trace again and run

```
(gdb) p/x *(uint32_t[16]*)0x20000100
$10 = {0x0, 0x0, 0x0, 0x3910e7ef, 0xe0111c06, 0x1c26390c, 0x3908e00e, 0xe00b1c2e, 0xe0091f09, 0xd40d1e7f, 0x42b3680e, 0x1d09d104, 0xd1f71f12, 0xbdf22000, 0x60019806, 0x60069807}
```

This means the JLinkGDBServer must be caching results and not always issuing requests to the actual MCU.

If we try to read 17 bytes we will see a new transaction gets issued with `TAR` starting at `0x20000140`.

For reference, I've included trace [here](https://github.com/memfault/interrupt/blob/master/example/debugger-traces/17byte_read.logicdata). The original trace was in the same directory.
