# SonicSync System Architecture

## Architecture style

SonicSync can be represented as a master-client distributed mobile architecture operating over a shared local Wi-Fi network.

```text
+----------------------------+
| Master Android Device      |
| - Select audio             |
| - Discover/register peers  |
| - Send control messages    |
| - Coordinate start time    |
+-------------+--------------+
              |
              | Local Wi-Fi network
              |
      +-------+--------+----------------+
      |                |                |
+-----v------+   +-----v------+   +-----v------+
| Client 1   |   | Client 2   |   | Client n   |
| Buffer     |   | Buffer     |   | Buffer     |
| Prepare    |   | Prepare    |   | Prepare    |
| Play audio |   | Play audio |   | Play audio |
+------------+   +------------+   +------------+
```

## Main components

### 1. User interface

Provides controls for selecting a master or client role, discovering devices, connecting to a session, selecting audio and managing playback.

### 2. Device discovery and session management

Finds devices on the local network, records participating clients and maintains the session state.

### 3. Network communication layer

Transfers connection requests, acknowledgements, timing information and playback commands between the master and clients.

### 4. Audio control layer

Prepares the selected media and responds to start, pause, resume and stop commands.

### 5. Synchronisation controller

Coordinates a common playback start time. A practical implementation may use buffering, clock-offset estimation and scheduled playback to reduce audible delay between devices.

## Expected sequence

1. All devices connect to the same Wi-Fi network.
2. One device starts a session as the master.
3. Other devices discover or join the session as clients.
4. The master selects the audio and sends preparation information.
5. Clients acknowledge readiness after buffering.
6. The master sends a scheduled start command.
7. Devices start playback at the agreed time.
8. The master sends further playback-control commands as required.

## Technical risks

- Unequal network latency
- Different device clocks
- Different audio hardware and processing delay
- Wi-Fi congestion or packet loss
- Android background-execution restrictions
- File availability and codec compatibility

## Scope note

This architecture is a retrospective engineering interpretation of the recovered project description. It should not be presented as a verbatim copy of the missing original report.