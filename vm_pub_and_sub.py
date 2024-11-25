"""EE 250L Lab 04 Starter Code

REPO: https://github.com/usc-ee250-fall2024/mqtt-satwika-and-hansini/tree/master
Satwika Vemuri and Hansini Ramachandran

Run vm_publisher.py in a separate terminal on your VM."""

#import paho.mqtt.client as mqtt
import time
import threading
from flask import Flask, flash, redirect, render_template, request, session, abort
import weather

main_page = """
<!DOCTYPE html>
<html>

<body>
<h2>Welcome to the Energy Consumption Calculator</h2>
In the textbox below, enter the name of the city you are located in. Then, click the button to get an estimate of your building's energy consumption.
<br>

<form action="getWeather">
    <input type="text" name="city" placeholder="City Name">
    <button type="submit">Retrieve Weather!</button>
<form>
 
</body>

</html>
"""

app = Flask(__name__)
succeeded = set()

@app.route("/")
def setup():
    return main_page

@app.route('/getWeather')
def getWeather():
    #client.publish("satwika-vemuri/temp", "True")
    return main_page


def custom_callback(client, userdata, message):
    indoor_temp = (message.payload).decode('utf-8')
    print("VM: " + indoor_temp)

    weather_data = weather.get_weather(request.args.get("city"))
    if(weather_data[0] == 200): # status code successful
        outdoor_temp = weather_data[1] 
        # TODO: Call ML model w/indoor and outdoor temp
    else:
        print("Data retrieval not successful")


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the temperature topic here
    client.subscribe("satwika-vemuri/temp")
    client.message_callback_add("satwika-vemuri/temp", custom_callback)

    #subscribe to topics of interest here

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


if __name__ == '__main__':
    #setup the keyboard event listener
    #lis = keyboard.Listener(on_press=on_press)
    #lis.start() # start to listen on a separate thread

    #this section is covered in publisher_and_subscriber_example.py
    # client = mqtt.Client()
    # client.on_message = on_message
    # client.on_connect = on_connect
    # client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    # client.loop_start()

    # thread = threading.Thread(target=on_press)
    # thread.daemon = True
    # thread.start()
    app.run()
    
    #while True:
         #time.sleep(1)
            
