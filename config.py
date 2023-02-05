import os

CURRENT_DIR = os.getcwd()

CLIENT_ID = 'python_pub_script'

SSL_MODE = bool(os.environ.get("SSL_MODE", True))
MQTT_HOST = os.environ.get("MQTT_BROKER", "192.168.11.29")
MQTT_PORT = int(os.environ.get("BROKER_PORT", 1883))
MQTT_USERNAME = os.environ.get("MQTT_USERNAME", "")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD", "")

AWS_HOST = "a31dvipl38h049-ats.iot.ap-southeast-1.amazonaws.com"
AWS_PORT = 8883
CA_PATH = os.path.join(CURRENT_DIR, "cert", os.environ.get("CA_PATH", "AmazonRootCA1.pem"))
CERT_PATH = os.path.join(CURRENT_DIR, "cert", os.environ.get("CERT_PATH", "iot-core-certificate.pem.crt"))
KEY_PATH = os.path.join(CURRENT_DIR, "cert", os.environ.get("KEY_PATH", "iot-core-private.pem.key"))

DEBUG = bool(os.environ.get("DEBUG", True))
