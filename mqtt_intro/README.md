# MQTT Intro

Install Mosquitto MQTT broker

```shell
brew install mosquitto
```

The install script finishes by providing the instructions to start the MQTT server on startup.

```shell
ln -sfv /usr/local/opt/mosquitto/*.plist ~/Library/LaunchAgents
```
Finally, to save a restart, the server can be started now by running

```shell
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mosquitto.plist
```

Create a virtual environment

```shell
python3 -m venv .env
```

Activate the virtual environment

```shell
source .env/bin/activate
```

Install Paho client in the virtual environment

```shell
pip install paho-mqtt
```

Install psutil Package in the virtual environment

```shell
pip install psutil
```

Run Mosquitto Broker in the first virtual environment

```shell
/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
```

[broker](mqtt_intro/images/mosquitto.png)

Run mqtt_sub.py in the second virtual environment

```shell
python3 mqtt_sub.py
```

[pub](mqtt_intro/images/mqtt_sub.png)

Run mqtt_pub.py in the third virtual environment

```shell
python3 mqtt_pub.py
```

[broksuber](mqtt_intro/images/mqtt_pub.png)

Kill running port

```shell
lsof -i tcp:1883
kill -9 <port-id>
```

### References

https://medium.com/@potekh.anastasia/a-beginners-guide-to-mqtt-understanding-mqtt-mosquitto-broker-and-paho-python-mqtt-client-990822274923