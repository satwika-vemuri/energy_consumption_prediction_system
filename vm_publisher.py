"""EE 250L Lab 04 Starter Code

REPO: https://github.com/usc-ee250-fall2024/mqtt-satwika-and-hansini/tree/master
Satwika Vemuri and Hansini Ramachandran

Run vm_publisher.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
import threading


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_press():
    print("in on press")
    #try: 
       # k = key.char # single-char keys
    #except: 
        #k = key.name # other keys
    while True:
        k = input("")
        if k == 'w':
            print("w")
            #send "w" character to rpi
            client.publish("satwika-vemuri/lcd", "w")

        elif k == 'a':
            print("a")
            # send "a" character to rpi
            client.publish("satwika-vemuri/lcd", "a")
            #send "LED_ON"
            client.publish("satwika-vemuri/led", "LED_ON")

        elif k == 's':
            print("s")
            # send "s" character to rpi
            client.publish("satwika-vemuri/lcd", "s")

        elif k == 'd':
            print("d")
            # send "d" character to rpi
            client.publish("satwika-vemuri/lcd", "d")
            # send "LED_OFF"
            client.publish("satwika-vemuri/led", "LED_OFF")



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
            
