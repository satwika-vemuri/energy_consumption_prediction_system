import paho.mqtt.client as mqtt
import time
import threading
from flask import Flask, flash, redirect, render_template, request, session, abort
import weather
import machine_learning
import math

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
    <br>
    <div id="text"></div>
<form>
 
</body>

</html>
"""

updated = False
consumption = -1

app = Flask(__name__)
succeeded = set()

@app.route("/")
def setup():
    return main_page

@app.route('/getWeather')
def getWeather():
    global updated
    client.publish("satwika-vemuri/temp", "True")
    while(updated == False):
        time.sleep(1)
    updated = True
    print("hello")    
    return render_template('result.html', value=consumption)

def custom_callback(client, userdata, message):
    global consumption, updated

    indoor_temp = (message.payload).decode('utf-8')
    print("VM: " + indoor_temp)

    weather_data = weather.get_weather(request.args.get("city"))
    if(weather_data[0] == 200): # status code successful
        # Call ML model w/indoor and outdoor temp
        outdoor_temp = weather_data[1] 
        consumption = machine_learning.predict(math.abs(outdoor_temp-indoor_temp))
        updated = True
    else:
        print("Data retrieval not successful")


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the temperature topic here
    client.subscribe("satwika-vemuri/temp")
    client.message_callback_add("satwika-vemuri/temp", custom_callback)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


if __name__ == '__main__':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    app.run()
    
    #while True:
         #time.sleep(1)
            
