import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *

temp_sensor = 0
flag = 0

def custom_callback2(client, userdata, message):
    global flag
    msg = (message.payload).decode('utf-8')
    if (msg == "True"):
        flag = 1

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    # subscribe to temp topic
    client.subscribe("satwika-vemuri/temp")
    client.message_callback_add("satwika-vemuri/temp", custom_callback2)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        if (flag==1):
            room_temperature_pin = 15 # this is equal to A1
            probe_temperature_pin = 14 # this is equal to A0
            # so you have to connect the sensor to A0 port

            # instatiate a HighTemperatureSensor object
            sensor = grovepi.HighTemperatureSensor(room_temperature_pin, probe_temperature_pin)
            total = 0
            average = 0
            # and do this indefinitely
            for i in range(1,11):
                # read the room temperature
                room_temperature = sensor.getRoomTemperature()
                total = total + room_temperature
                # and wait for 250 ms before taking another measurement - so we don't overflow the terminal
                time.sleep(0.25)

            average = total/10
            print("Indoor Temperature ", average)
            client.publish("satwika-vemuri/temp", average)
            flag = 0
        time.sleep(1)
            


