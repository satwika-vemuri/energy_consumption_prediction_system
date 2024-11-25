"""EE 250L Lab 04 Starter Code

REPO: https://github.com/usc-ee250-fall2024/mqtt-satwika-and-hansini/tree/master
Satwika Vemuri and Hansini Ramachandran

Run vm_publisher.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
import threading

def custom_callback(client, userdata, message):
    val = (message.payload).decode('utf-8')
    print("VM: " + val)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the temperature topic here
    client.subscribe("satwika-vemuri/temp")
    client.message_callback_add("satwika-vemuri/temp", custom_callback)

    #subscribe to topics of interest here

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_press():
    while True:
        sense = input("Sense? Y/N")
        if sense == 'Y':
            print("Requesting RPI")
            #request information from rpi
            client.publish("satwika-vemuri/temp", "True")


if __name__ == '__main__':
    #setup the keyboard event listener
    #lis = keyboard.Listener(on_press=on_press)
    #lis.start() # start to listen on a separate thread

    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    thread = threading.Thread(target=on_press)
    thread.daemon = True
    thread.start()

    while True:
         time.sleep(1)
            
