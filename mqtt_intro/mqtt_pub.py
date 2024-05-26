import sys
import time
import psutil

import paho.mqtt.client as paho

client = paho.Client()
topic = "mqtt-gbk"

while True:

    cpu_usage = psutil.cpu_percent(interval=10)
    pay_load = "Hi, paho mqtt client works fine! CPU_Usage=" + str(cpu_usage)

    client = paho.Client()
    print("\nmqtt_pub | Created client object at " + time.strftime("%H:%M:%S"))

    client.connect("localhost", 1883, 60)
    print("mqtt_pub | Connected to Mosquitto broker")

    try:
        client.publish(topic, pay_load)
        print("mqtt_pub | CPU usage percent = %.1f" % cpu_usage)
    except:
        print("mqtt_pub | Couldn't connect to the Mosquitto broker")
        sys.exit(1)
    else:
        client.disconnect()
        print("mqtt_pub | Disconnected from Mosquitto broker")
