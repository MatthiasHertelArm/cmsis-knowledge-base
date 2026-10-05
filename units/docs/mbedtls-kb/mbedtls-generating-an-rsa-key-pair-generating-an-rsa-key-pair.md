---
id: "mbedtls-generating-an-rsa-key-pair-generating-an-rsa-key-pair"
type: "concept"
domain: "security"
title: "Generating an RSA key pair: Generating an RSA key pair"
summary: "To actually generate an RSA key pair, you have to decide which size your RSA key should be."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/rsa-key-pair-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/rsa-key-pair-generator.md#generating-an-rsa-key-pair"
license: "Apache-2.0"
mode: "V"
---

To actually generate an RSA key pair, you have to decide which size your RSA key should be. Depending on your need for security, we advise you to use at least **2048** bits, and use **4096** bits or higher if you have very high security requirements.

To use the RSA key pair generator to generate a 4096 bits RSA key and save that key in PEM format in private.key, use:

    ./gen_key type=rsa rsa_keysize=4096 filename=private.key format=pem
    
The larger the requested keysize, the longer it will take to generate the key itself. You also need to take into account the performance of the system.

The key generator also outputs the key in **human readable** format in addition to writing the key to the requested keyfile in the requested format.

The output for a 1024-bit RSA key looks something like this:

      . Seeding the random number generator...
      . Generating the private key ... ok
      . Key information:
    N:  8C3A0BE5B196E6CAAEB18B53C654B59FD1F4D1B62CA3C17B4BD094582A4D94BBA9FB3A93E61B4ED0108021A6DFDB2FE89E855030310A7653DC595259501ADC48C4E8C87D78DE750FC44A3069B4F71107C50CDF2E0BD26229297C31D2CBD9C31009736D0D6503ED16D148AF3894770E084BCF56FD6290E1FF28632CB9620B105
    E:  010001
    D:  1F3728C0D818AC85BFFFBBF1493C403634A9D82942A4AD8481EB0BAAD8B7EE7D1C28D5F0688FF9AA6D91E86BDA7753A1E7EFEB5ADEFFE23966DAE76F045B0660407392B3C07DB8F1200EF70D9CA46DFD3631F455C97F087B8F678DB890AC601FD812C7A435D6826811474BDFACAB2D6AEC9C95809D28AC85DA067B9DA5E005C1
    P:  FF96AC7E4E47FC4F153C6C5D3FE7EFC01ECDBBFC6AC861089C675191987281E18E33A731BE939B80C566199E98FDDC9F764AA5283E43FFBA260650B6E9C650D5
    Q:  8C73D538DBEA066F00161DCFB69921374ABBD20A96C2693E5072A0890728FE79E881EC532C8918C486C6061987EAED3350F5C6F79E30721C55E3ED72FFF47771
    DP: B93FEF6458BECA3C53AB08EC099EC5621DB186786CB931C3790155D8CE82E86AA09405B2036C9F4015536C6C4C7D6BC4548BC3EB483E270337FE49D059DEB8C5
    DQ:  61360AEE3FC7CA8C2953256F0EC30DEA671F78513BE773505DFDF87EDF25D07C30213CA094C28F11F6F63862936056AC9DEC7EBA041323E7D8CAD91E2F69D501
    QP:  A945E282018B46EFFA11030152A42AD977FAAD439D6C482134A8BC5716F082808904C2001F9D5BBF8B1A6CF98C30FD66BA00EA86F8790552F160929CF10BF8F6
