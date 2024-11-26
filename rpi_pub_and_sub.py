"""EE 250L Lab 04 Starter Code

REPO: https://github.com/usc-ee250-fall2024/mqtt-satwika-and-hansini/tree/master
Satwika Vemuri and Hansini Ramachandran

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
#from grovepi import *
#from grove_rgb_lcd import *

temp_sensor = 0
#global flag
flag = 0

#def custom_callback(client, userdata, message):
    #print("received")
    #led_msg = (message.payload).decode('utf-8')
    #if(led_msg == "LED_ON"):
        #digitalWrite(led,1)
    #elif(led_msg == "LED_OFF"):
        #digitalWrite(led,0)

def custom_callback2(client, userdata, message):
    global flag
    msg = (message.payload).decode('utf-8')
    #print("incallback")
    if (msg == "True"):
        #print("received")
        flag = 1
        #client.publish("satwika-vemuri/temp", 10)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("satwika-vemuri/temp")
    client.message_callback_add("satwika-vemuri/temp", custom_callback2)
    #client.subscribe("satwika-vemuri/lcd")
    #client.message_callback_add("satwika-vemuri/lcd", custom_callback2)

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
        #val = ultrasonicRead(ultrasonic_ranger)
        #print(flag)
        if (flag==1):
            #print("Flag is true")
            val = 10
            client.publish("satwika-vemuri/temp", val)
            flag = 0
       # client.publish("satwika-vemuri/temp", 10)
        #b = digitalRead(button)
        #client.publish("satwika-vemuri/button", b)
        time.sleep(1)
            
