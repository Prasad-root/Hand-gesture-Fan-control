# Gesture-Controlled Smart Fan

This project creates a gesture-controlled fan system that allows users to control fan speed and on/off functionality using hand gestures. By capturing and interpreting gestures through image processing, the system communicates wirelessly with a fan motor.

## Project Overview

The Gesture-Controlled Smart Fan uses a **NodeMCU**, **L295D motor driver**, **12V DC motor**, and additional components to control fan speed and power. The system utilizes **Mediapipe** for gesture recognition and **OpenCV** for image processing, transmitting commands to the NodeMCU via Wi-Fi.

## Features

- **Gesture Recognition**: Uses hand gestures to control fan speed and power.
- **Wireless Control**: Commands are transmitted to the NodeMCU via Wi-Fi.
- **Image Processing**: OpenCV handles video feed processing.
- **Real-Time Response**: Detects gestures and adjusts fan settings instantaneously.

## Components, Modules, and IDEs Used

- **NodeMCU**: Microcontroller for Wi-Fi communication and motor control.
- **L295D Motor Driver**: Manages the 12V DC motor.
- **12V DC Motor**: Drives the fan.
- **Two AAA Batteries**
- **3 LEDs**: For status indication of command changes.
- **Mediapipe**: Library for real-time hand gesture detection.
- **OpenCV**: Processes captured video.
- **Arduino IDE**: For programming the NodeMCU.
- **VS Code**: For Python programming and debugging.

## How It Works

1. **Gesture Detection**: Video footage from a webcam is analyzed to detect hand gestures.
2. **Command Selection**: Pre-defined commands are triggered based on recognized gestures.
3. **Command Transmission**: The command is sent to the NodeMCU over a Wi-Fi connection.
4. **Motor Control**: The NodeMCU receives the command and controls the fan speed accordingly.

## Hardware Setup

Refer to the [hardware setup guide](link-to-hardware-setup) for detailed instructions.

### Installation and Setup

1. **Clone this repository**:
   ```bash
   git clone <[repository-link](https://github.com/Prasad-root/Hand-gesture-Fan-control.git)>
