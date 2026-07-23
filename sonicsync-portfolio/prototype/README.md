# SonicSync Modern Demonstration Prototype

This folder is reserved for a new demonstration of the SonicSync concept.

## Authenticity notice

Any code added here will be a **modern reconstruction** created after the original undergraduate project. It must not be described as recovered original source code.

## Suggested minimum viable prototype

- Android master mode
- Android client mode
- Local-network session discovery
- Client connection and readiness acknowledgement
- Shared test audio file
- Scheduled start command
- Logging of requested and actual start times
- Simple latency summary

## Suggested implementation stages

1. Build static master/client interfaces.
2. Implement local-network communication.
3. Add session join and device-list management.
4. Add shared audio preparation.
5. Add scheduled playback.
6. Record timing differences between devices.
7. Document results and limitations.

## Suggested repository structure

```text
prototype/
├── android-app/
├── diagrams/
├── test-results/
└── screenshots/
```

## Evaluation metrics

- Connection success rate
- Time required to join a session
- Playback start-time difference between devices
- Command-delivery delay
- Stability during a complete audio track
- User task-completion rate

No test result should be reported until it has been measured on an implemented prototype.