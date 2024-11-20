"""EE 250L Lab 04 Starter Code

REPO: https://github.com/usc-ee250-fall2024/mqtt-satwika-and-hansini/tree/master
Satwika Vemuri and Hansini Ramachandran

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

def custom_callback(client, userdata, message):
    print("VM: " + (message.payload).decode('utf-8') + " cm")
    #print("VM: " + (message.payload, "utf-8") + " cm")

def custom_callback2(client, userdata, message):
    val = (message.payload).decode('utf-8')
    if(val == 1):
        print("Button pressed!")
    
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("satwika-vemuri/ultrasonicRanger")
    client.subscribe("satwika-vemuri/button")
    client.message_callback_add("satwika-vemuri/customCallback", custom_callback)
    client.message_callback_add("satwika-vemuri/customCallback", custom_callback2)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
            
