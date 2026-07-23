# SonicSync Interactive Mobile Mockup

This folder contains a high-fidelity, browser-based mobile interface mockup for **SonicSync: The Legit Sound System**.

## Purpose

The mockup demonstrates the intended user flow of the documented Final Year Project concept:

1. Create or join a SonicSync room.
2. Discover Android devices on the same local Wi-Fi network.
3. Connect client phones to a host phone.
4. Select and control audio playback.
5. Display synchronization and estimated latency status.

## Run locally

Open `index.html` in a modern browser. No installation or server is required.

## Interactive features

- Home, Devices and Player screens
- Room creation with a generated room code
- Join-room demonstration
- Simulated local-network device discovery
- Connected-device and latency indicators
- Synchronized play/pause controls
- Toast messages and status feedback
- Responsive mobile-phone presentation

## Technology

- HTML5
- CSS3
- Vanilla JavaScript

## Evidence statement

This is a **modern retrospective prototype** created to demonstrate the original SonicSync concept described in the recovered UCP project record. It is not represented as the original application submitted to UCP. Network discovery, device connection, audio streaming and timing synchronization are simulated in this interface mockup.

## Future Android implementation

A production Android prototype could use Java and XML in Android Studio, with Wi-Fi Direct, network service discovery or socket-based local communication. Audio timing would require buffering, clock-offset estimation and scheduled playback commands.
