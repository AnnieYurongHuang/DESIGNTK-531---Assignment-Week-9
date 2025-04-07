# Stepper Motor Control via MQTT

## Project Overview
This README.md demonstrates how to control a stepper motor using a Raspberry Pi based on temperature data received through MQTT messages. The system uses two main components:
1. An MQTT publisher that sends temperature data.
2. An MQTT subscriber that listens to this data and controls a stepper motor connected to a Crickit Hat when the temperature exceeds a threshold.

## How It Works

### Publisher
The `motorpub.py` script generates random temperature data and sends it over MQTT. It continually publishes this data to the topic `"pythontest/sensors/mysensor"`, which includes temperature values along with humidity and timestamp information.

### Subscriber
The `run_stepper.py` script listens for MQTT messages on the specified topic. When it receives a message, it decodes the data and extracts the temperature value. If the temperature exceeds 24 degrees Celsius, the script activates the stepper motor. The motor control logic triggers the stepper motor to make one full rotation forward and then backward, demonstrating how IoT devices can respond to data in real-time.

### Messaging Logic to Motor Control Connection
The core of this project lies in the integration of MQTT messaging with physical device control:

- **MQTT Messaging**: Provides a lightweight method of carrying data (temperature readings in this case) using a publish-subscribe model. This is ideal for IoT applications like this where data needs to be transferred from one point (the publisher) to others (subscribers) over a network.

- **Motor Control**: Upon receiving the correct conditions (temperature > 24°C), the subscriber script engages the motor's hardware control through the Crickit Hat's motor driver libraries. This direct control of hardware based on data received over MQTT showcases a practical IoT application.

## Hardware Requirements
- Raspberry Pi (tested on Raspberry Pi 4)
- Adafruit Crickit Hat
- Stepper motor (e.g., NEMA-17)
- Power supply for Raspberry Pi and Crickit Hat
- Internet connection for the Raspberry Pi

## Software Requirements
- Mosquitto MQTT broker
- Python 3.x
- Paho-MQTT Python library
- Adafruit libraries for motor control

## Setup Instructions

### Setting Up the Raspberry Pi
1. **Install the Raspbian OS**: Download and install the Raspberry Pi OS onto your Raspberry Pi.
2. **Enable SSH** (optional): Enable SSH on your Raspberry Pi for remote access.
3. **Connect to the Internet**: Ensure your Raspberry Pi is connected to the internet via WiFi or Ethernet.

### Installing Required Software
1. **Install Mosquitto MQTT Broker**:
   ```bash
   sudo apt update
   sudo apt install -y mosquitto mosquitto-clients
   sudo systemctl enable mosquitto
   sudo systemctl start mosquitto

## Hardware Connections
- **Connect the Stepper Motor to the Crickit Hat** according to the Crickit Hat documentation.
- **Power the Raspberry Pi and Crickit Hat**.

## Setting Up the Development Environment in VSC
1. **Install Visual Studio Code** on your computer.
2. **Install the Python extension** for Visual Studio Code.
3. **Connect to your Raspberry Pi** via SSH or directly use the terminal in VSC if you are coding on the Raspberry Pi.

