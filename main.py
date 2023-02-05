import json
import random
import time
import ssl
from paho.mqtt import client as mqtt_client

from config import *

DEVICE_TOPIC = "control/807D3AC722E8"

class MQTT(mqtt_client.Client):
    host = AWS_HOST if SSL_MODE else MQTT_HOST
    port = AWS_PORT if SSL_MODE else MQTT_PORT
    topic = []
    client_id = CLIENT_ID
    username = ""
    password = ""
    keepalive=120
    
    def __init__(self, host=host, port=port, listen_topic=[], ssl_connect=SSL_MODE,
                client_id=client_id, username="", password="", keepalive=keepalive):

        self.host, self.port = host, port, 
        self.client_id, self.username, self.password = client_id, username, password
        self.listen_topic = listen_topic
        self.keepalive=keepalive

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(f'publish on {DEVICE_TOPIC} message on')
                self.publish(DEVICE_TOPIC, payload="on")
            else:
                print("Fail to connect mq")
        
        super().__init__(client_id)
        self.username_pw_set(username, password)
        self.on_connect = on_connect
        
        if ssl_connect:
            self.tls_set(ca_certs=CA_PATH, certfile=CERT_PATH, keyfile=KEY_PATH, 
                        cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, 
                        ciphers=None)

        self.connect(self.host, self.port, self.keepalive)
        print(f'Connect mqtt')

    def __del__(self):
        self.disconnect()

if __name__ == "__main__":
    mq_client = MQTT()
    while True:
        print(f'main thread sleep every 30 sec')
        mq_client.publish(DEVICE_TOPIC, payload="on")
        time.sleep(30)
        mq_client.publish(DEVICE_TOPIC, payload="off")
        time.sleep(30)