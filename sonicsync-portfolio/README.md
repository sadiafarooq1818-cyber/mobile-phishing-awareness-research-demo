# SonicSync: The Legit Sound System

## Undergraduate Capstone Portfolio

**Student:** Sadia Farooq  
**Institution:** University of Central Punjab (UCP), Lahore, Pakistan  
**Project advisor:** Mr Nabeel Ahsan  
**Status:** Completed  
**Project type:** Final Year Project / software-development capstone

## Project overview

SonicSync was an Android mobile application concept designed to transform multiple Android smartphones into a synchronized wireless multi-speaker system. A master audio-source device would control playback, while additional phones connected through the same local Wi-Fi network would function as wireless speakers and reproduce the same audio simultaneously.

The recovered UCP project-office record identifies the project as **"SONICSYNC: THE LEGIT SOUND SYSTEM,"** lists **Mr Nabeel Ahsan** as the project advisor, and records its status as **Completed**. The record also identifies Java, XML, Android Studio and networking as the principal technologies and development environment.

## Core objectives

- Convert Android smartphones into a wireless multi-speaker audio system.
- Connect secondary devices to a master audio-source device over a local network.
- Coordinate audio playback across connected devices.
- Provide a simple mobile interface for device discovery, connection and playback control.

## Technology stack documented in the recovered record

- Java
- XML
- Android Studio
- Local Wi-Fi networking

## Proposed architecture

1. A master Android device selects and controls the audio source.
2. Secondary Android devices join the same local Wi-Fi network.
3. The master discovers or registers available client devices.
4. Control messages coordinate preparation, start, pause and stop actions.
5. Client devices buffer audio and begin playback according to the master's timing signal.

## Completed interactive mockup

A high-fidelity browser-based mobile mockup is available in:

`prototype/web-mockup/`

The mockup includes:

- Home, Devices and Player screens
- Room creation and join-room interactions
- Simulated local-network scanning
- Host and client device management
- Device-count and latency indicators
- Synchronized play and pause controls
- Responsive phone interface

Open `prototype/web-mockup/index.html` to run it locally.

## Important evidence statement

This repository is a **retrospective technical portfolio** reconstructed from an official UCP project-office listing and the student's recollection. It is not presented as the original submitted source code or original university report. The interactive mockup is a modern demonstration of the original concept. Local-network discovery, audio streaming and synchronization are simulated and are not presented as measured implementation results.

## Portfolio structure

- `docs/project-summary.md` - concise professional summary
- `docs/technical-report-outline.md` - report structure aligned with UCP's traditional-project category
- `docs/system-architecture.md` - architecture and component description
- `docs/evidence-register.md` - verified facts and missing evidence
- `prototype/README.md` - prototype status and development roadmap
- `prototype/web-mockup/` - completed interactive mobile interface mockup

## Current status

Documentation portfolio and interactive mobile mockup completed. A future native Android demonstration may implement real local-network communication, audio buffering and synchronized playback testing.
