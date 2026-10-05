---
id: "sds-theory-sdsio-message-sequence"
type: "concept"
domain: "test"
title: "theory: SDSIO Message Sequence"
summary: "This section describes the states and the message sequence of the SDS framework when using the SDSIO-Server. It contains the following threads that execute on the target."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sdsio-message-sequence"
license: "Apache-2.0"
mode: "V"
---

This section describes the states and the message sequence of the SDS framework when using the [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-server).
It contains the following threads that execute on the target.

- **sdsControlThread**: Control thread that organizes the overall execution.
- **AlgorithmThread**: Executes the algorithm under test.
- **sdsThread**: SDS worker thread.
- **SDSIO-Server**: SDSIO-Server running on the host computer.

!!! Note
    - The command `SDSIO_CMD_FLAGS` is sent asynchronously by the SDSIO-Server.

The `sdsControlThread` handles a state machine with the following states:

States                   | Description
:------------------------|:------------
SDS_STATE_INACTIVE       | Streaming is not active; waiting for flag info from SDSIO-Server
SDS_STATE_CONNECTED      | Device (client) is connected to SDSIO-Server (host), but streaming is not active
SDS_STATE_START          | Request to start streaming, open streams and get ready for read/write operations
SDS_STATE_ACTIVE         | Streaming is active
SDS_STATE_STOP_REQ       | Request to stop streaming and close open streams
SDS_STATE_STOP_DONE      | Streaming has stopped
SDS_STATE_END            | Request to end streaming (e.g., no more playback data is available)
SDS_STATE_RESET          | Request to reset the device

The following flowcharts show the state transition in context with the messages that are exchanged with the `SDSIO-Server`.

**Connect flowchart**

```mermaid
sequenceDiagram
    participant sdsControlThread
    activate sdsControlThread

    participant Server as SDSIO-Server<br/>(host)

    Note over sdsControlThread: sdsInit
    Note right of sdsControlThread: SDS_STATE_INACTIVE 
    loop every 100 ms
      Note over sdsControlThread: sdsExchange
      activate Server
      Server-->>sdsControlThread: SDSIO_CMD_FLAGS: set SDS_FLAG_ALIVE
      sdsControlThread-->>Server: SDSIO_CMD_INFO
    end
    Note right of sdsControlThread: SDS_STATE_CONNECTED 
    deactivate sdsControlThread
    deactivate Server
```

!!! Note
    - When the command `SDSIO_CMD_FLAGS` sets SDS_FLAG_ALIVE, the `sdsControlThread` transitions to SDS_STATE_CONNECTED.
    - When `SDSIO_CMD_INFO` is sent more than 10 times without a `SDSIO_CMD_FLAGS` response, the `sdsControlThread` transitions into the SDS_STATE_INACTIVE.

**Recording start flowchart**

```mermaid
sequenceDiagram
    participant sdsControlThread
    activate sdsControlThread
    participant AlgorithmThread
    activate AlgorithmThread
    participant SDSIO as sdsThread
    activate SDSIO
    participant Server as SDSIO-Server<br/>(host)
    activate Server

    Note right of sdsControlThread: SDS_STATE_CONNECTED 

    loop every 100 ms
      Note over sdsControlThread: sdsExchange
      Server->>sdsControlThread: SDSIO_CMD_FLAGS
      sdsControlThread->>Server: SDSIO_CMD_INFO
    end

    Server-->>sdsControlThread: SDSIO_CMD_FLAGS: set SDS_FLAG_START
    Note right of sdsControlThread: SDS_STATE_START

    Note over sdsControlThread: sdsOpen<br/>(all streams)
    sdsControlThread->>Server: SDSIO_CMD_OPEN
    Server->>sdsControlThread: Response

    Note right of sdsControlThread: SDS_STATE_ACTIVE

    loop periodic
        Note over AlgorithmThread: sdsWrite
        AlgorithmThread->>SDSIO: Buffered data reached or crossed threshold
        loop send all data from buffer
            SDSIO->>Server: SDSIO_CMD_WRITE
        end
    end

    deactivate sdsControlThread
    deactivate AlgorithmThread
    deactivate SDSIO
    deactivate Server
```

**Recording stop flowchart**

```mermaid
sequenceDiagram
    participant sdsControlThread
    activate sdsControlThread

    participant AlgorithmThread
    activate AlgorithmThread
    participant SDSIO as sdsThread
    activate SDSIO
    participant Server as SDSIO-Server<br/>(host)
    activate Server

    Note right of sdsControlThread: SDS_STATE_ACTIVE 

    loop every 100 ms
      Note over sdsControlThread: sdsExchange
      Server->>sdsControlThread: SDSIO_CMD_FLAGS
      sdsControlThread->>Server: SDSIO_CMD_INFO
    end

    Server-->>sdsControlThread: SDSIO_CMD_FLAGS: clear SDS_FLAG_START
    Note right of sdsControlThread: SDS_STATE_STOP_REQ
    loop send all data from buffer
        SDSIO->>Server: SDSIO_CMD_WRITE
    end
    Note right of sdsControlThread: SDS_STATE_STOP_DONE

    Note over sdsControlThread: sdsClose<br/>(all streams)
    sdsControlThread->>Server: SDSIO_CMD_CLOSE
    Note right of sdsControlThread: SDS_STATE_CONNECTED

    deactivate AlgorithmThread
    deactivate SDSIO
    deactivate Server
    deactivate sdsControlThread
```

**Playback flowchart**

```mermaid
sequenceDiagram
    participant sdsControlThread
    activate sdsControlThread
    participant AlgorithmThread
    activate AlgorithmThread
    participant SDSIO as sdsThread
    activate SDSIO
    participant Server as SDSIO-Server<br/>(host)
    activate Server

    Note right of sdsControlThread: SDS_STATE_CONNECTED 

    loop every 100 ms
      Note over sdsControlThread: sdsExchange
      Server->>sdsControlThread: SDSIO_CMD_FLAGS
      sdsControlThread->>Server: SDSIO_CMD_INFO
    end

    Server-->>sdsControlThread: SDSIO_CMD_FLAGS: set SDS_FLAG_START and SDS_FLAG_PLAYBACK
    Note right of sdsControlThread: SDS_STATE_START

    Note over sdsControlThread: sdsOpen<br/>(all streams)
    sdsControlThread->>Server: SDSIO_CMD_OPEN
    Server->>sdsControlThread: Response

    loop read data until threshold is reached
        sdsControlThread->>Server: SDSIO_CMD_READ
        Server->>sdsControlThread: Data
    end
  
    Note right of sdsControlThread: SDS_STATE_ACTIVE

    loop periodic
        Note over AlgorithmThread: sdsRead
        AlgorithmThread->>SDSIO: Buffer data falls below threshold
        loop read data to fill the buffer
            SDSIO->>Server: SDSIO_CMD_READ
            Server-->>SDSIO: Data
        end
    end

    Server-->>SDSIO: No more data

    Server->>AlgorithmThread: End of Stream (EOS)
    Note over AlgorithmThread: sdsRead = SDS_EOS

    AlgorithmThread->>sdsControlThread: End of Stream (EOS)
    Note right of sdsControlThread: SDS_STATE_STOP_REQ
    Note right of sdsControlThread: SDS_STATE_STOP_DONE

    Note over sdsControlThread: sdsClose<br/>(all streams)
    sdsControlThread->>Server: SDSIO_CMD_CLOSE
    Note right of sdsControlThread: SDS_STATE_CONNECTED

    deactivate sdsControlThread
    deactivate AlgorithmThread
    deactivate SDSIO
    deactivate Server
```
