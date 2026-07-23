# SonicSync Modern Demonstration Prototype

This folder contains the modern demonstration work for the SonicSync concept.

## Authenticity notice

All material in this folder is a **modern retrospective reconstruction** created after the original undergraduate project. It must not be described as recovered original source code.

## Completed: interactive mobile interface mockup

The `web-mockup/` folder now contains a responsive, interactive mobile application prototype with:

- Home, Devices and Player screens
- Create-room and join-room flows
- Generated room codes
- Simulated local Wi-Fi device discovery
- Host and client device cards
- Connected-device and estimated-latency indicators
- Synchronized playback controls
- Status messages and user feedback

### Run the mockup

Open `web-mockup/index.html` in a modern web browser.

## Remaining Android implementation stages

1. Create a native Java/XML Android Studio project.
2. Implement host and client operating modes.
3. Add Wi-Fi Direct, network service discovery or socket-based communication.
4. Add session joining and readiness acknowledgements.
5. Add shared audio preparation and buffering.
6. Add scheduled playback commands and clock-offset estimation.
7. Measure playback-start differences on physical Android devices.
8. Document measured results and limitations.

## Current structure

```text
prototype/
├── README.md
└── web-mockup/
    ├── index.html
    ├── styles.css
    ├── app.js
    └── README.md
```

## Planned evaluation metrics

- Connection success rate
- Time required to join a session
- Playback start-time difference between devices
- Command-delivery delay
- Stability during a complete audio track
- User task-completion rate

No networking or synchronization performance result is claimed because the current version is an interface demonstration rather than an implemented distributed-audio system.
