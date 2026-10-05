---
id: "intr-separating-unique-parameters-from-generating-parameter-files"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries: Generating Parameter Files"
summary: "With that done, we need to generate a file that contains our unique parameters. We need that file to contain the data as well as the address at which it should be written."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters#generating-parameter-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

With that done, we need to generate a file that contains our unique parameters.
We need that file to contain the data as well as the address at which it should
be written.

One option would be to create C files containing the parameters before compiling
them to binaries that can be flashed to the correct addresses. Instead, we
settled on creating IHEX files since they exactly meet our requirements, are
simple to generate and come with lots of great tooling.

### Building HEX File Programmatically

Hex files consist of lines of hexadecimal data, called records, that specify
both an address and the data to write at this address. The
[Wikipedia entry](https://en.wikipedia.org/wiki/Intel_HEX) on the Intel HEX
format explains the file format quite clearly.

Based on this we can create a Python script that generates our HEX files with
the given parameters at the desired addresses. The Python code below does just
that:

```python
#!/usr/bin/env python3

# generateHexFile.py
# usage: ./generateHexFile.py <DevEUI> <AppEUI> <AppKey> <NodeName>"
import sys
# The hex format puts data at (baseAddr << 4) +  addr, which is why we shift
baseAddr = 0x18000
baseAddr = baseAddr >> 4

hexOut = ""

# Probably not working for all record types.
#  I use it for data, end of file, and extended segment address
def getRecordLine(address, nBytes, recordType, dataString):
   record = "%02X%04X%02X%s"%(nBytes, address, recordType, dataString)
   data = int(record, 16)
   checksum = 0
   for i in range(nBytes + 4):
       checksum += (data >> i*8) & 0xff
   checksum = (~checksum +1) & 0xff
   record = ":%s%02X"%(record,checksum)
   return record

# Write a line setting a base address for subsequent lines
hexOut += getRecordLine(0, 2, 2, "{:04X}".format(baseAddr)) + "\n"

# Write lines placing parameters at desired positions in flash
hexOut += getRecordLine(0     ,  8, 0, str(sys.argv[1])) + "\n"
hexOut += getRecordLine(0 + 8 ,  8, 0, str(sys.argv[2])) + "\n"
hexOut += getRecordLine(0 + 16, 16, 0, str(sys.argv[3])) + "\n"

# End of file record
hexOut += getRecordLine(0, 0, 1, "")

#print to stdout
print(hexOut)
```

### Automating File Generation

Now that we have a file format and a script to generate it, let's create some
provisioning files!

Since we are registering our devices with TTN, we will use the TTN CLI
(ttnctl)[^ttnctl] to register a new device in our selected TTN application and
return the parameters that we want. This is done by calling `ttnctl devices
register [node_name]` where `node_name` is a unique string we use to identify
that node, oftentimes this is simply the serial number of the device.

While the generation of the files and the registration of new devices could be
done just in time when programming new devices, I believe it is better to
generate a bunch of files ahead of time. This makes the production setup more
robust since it would not depend on some external service which may not be
reachable from the factory floor.

To keep things organized, we will store all of our generated artifacts in folders
based on the node name and keep track of which are used and which are free. The
free parameters are stored in `keys/free/<node_name>` and used parameters
in `keys/used/<node_name>`.

In addition to the hex file, we also generate a human-readable file containing
the unique parameters and store it in the same folder. It might come in
handy!

The shell script below registers a device, generates a human-readable file, and
finally calls the Python script to generate a corresponding HEX file. There is a
lot of sed commands here to get hold of the parameters we need, but the general
idea is what's important.

```shell
#!/usr/bin/env bash

# Usage: ./registerNode.sh <node-name>.
# Files ../keys/free/node-name/node-name.key and
#  ../keys/free/node-name/node-name.hex will be created

# The sed command below removes ANSI color formatting
output="$(ttnctl devices register "$1" | sed 's/\x1b\[[0-9;]*m//g')"

AppEUI=$(echo "$output" | sed -n -r '0,/.*AppEUI=([0-9A-F]{16})\s{1,}.*/s//\1/p')
DevEUI=$(echo "$output" | sed -n -r '/.*DevEUI=([0-9A-F]{16})\s{1,}.*/s//\1/p')
AppKey=$(echo "$output" | sed -n -r '/.*AppKey=([0-9A-F]{32})\s{1,}.*/s//\1/p')
DevID=$(echo "$output" | sed -n -r '0,/.*DevID=(.*)/s//\1/p')

# Store keys in a human readable file
mkdir ../keys/free/$DevID
printf "DevID: $DevID\nDevEUI: $DevEUI\nAppEUI: $AppEUI\nAppKey: $AppKey\n" > ../keys/free/$DevID/$DevID.key
# Create hex file with keys
./generateHexFile.py $DevEUI $AppEUI $AppKey $DevID > ../keys/free/$DevID/$DevID.hex
```

Here is an example of the resulting human-readable file
(`keys/free/node_id/node_id.key`), generated by the script:

```
DevID: node_id
DevEUI: 8899AABBCCDDEEFF
AppEUI: 0011223344556677
AppKey: 00112233445566778899AABBCCDDEEFF
```

The content of the corresponding HEX file `keys/free/node_id/node_id.hex` is
below. Although the same data is somewhat readable, you hopefully agree that it
was a good idea to also generate the more easily readable version of the file.

```
:020000021800E4
:080000008899AABBCCDDEEFFDC
:08000800001122334455667714
:1000100000112233445566778899AABBCCDDEEFFE8
:00000001FF
```

> The shell script in this section lets TTN come up with a DevEUI for
> simplicity. Check out
> [this link](https://www.thethingsnetwork.org/forum/t/deveui-for-non-hardware-assigned-values/2093/23)
> to see why you should not do that in production.
