import json
import time
import paho.mqtt.client as mqtt
from adafruit_crickit import crickit
from adafruit_motor import stepper

# MQTT Configuration
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "pythontest/sensors/mysensor"

# Motor Configuration
STEP_MOTOR = crickit.stepper_motor
INTERSTEP_DELAY = 0.01
STEPS_PER_REV = 200

# Callback when client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    try:
        # Decode the message payload
        data = json.loads(msg.payload.decode())
        temperature = float(data['temperature'])
        print(f"Temperature received: {temperature}")

        # Activate motor if temperature is above 24 degrees
        if temperature > 24:
            print("Temperature is above 24, activating motor.")
            for i in range(200):  # One full rotation forward
                STEP_MOTOR.onestep(direction=stepper.FORWARD)
                time.sleep(INTERSTEP_DELAY)
            for i in range(200):  # One full rotation backward
                STEP_MOTOR.onestep(direction=stepper.BACKWARD)
                time.sleep(INTERSTEP_DELAY)
    except Exception as e:
        print(f"Error handling message: {e}")

# Setup MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT Broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop on a new thread and continue executing the script
client.loop_start()

# Keep the script running
try:
    while True:
        time.sleep(1)  # Keep the script alive
except KeyboardInterrupt:
    print("Script interrupted by user, stopping MQTT client.")
    client.loop_stop()  # Stop the MQTT loop cleanly
    client.disconnect()  # Disconnect the MQTT client
