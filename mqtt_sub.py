import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import sys
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

while True:
    randNumber = uniform(20.0, 21.0)
    client.subscribe("TEMPERATURE")
    time.sleep(10)
    
    