from AWSIoTPythonSDK import MQTTLib
import json

CLIENT_ID = "publisher1"
ENDPOINT = "a3611c7i1de58-ats.iot.ap-southeast-1.amazonaws.com"
PATH_TO_CERT = "esp_device_certificate.txt"
PATH_TO_KEY = "esp_private_key.txt"
PATH_TO_ROOT = "esp_root_credentials.txt"

IoTClient = MQTTLib.AWSIoTMQTTClient(CLIENT_ID)
IoTClient.configureEndpoint(ENDPOINT, 8883)
IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
IoTClient.connect()
for i in range(20):
    IoTClient.publish("testboy", json.dumps("HALLO1"), 1) 
IoTClient.disconnect()
