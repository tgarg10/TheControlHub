from AWSIoTPythonSDK import MQTTLib as AWSIoTCam
from PIL import Image
import io
import queue 
    
AWSIoTClient = None
image_queue = queue.Queue()
CLIENT_ID = "esp32/cam_0"

#recursive
def AWS_IoT_Connect(CLIENT_ID):
    global IoTClient
    ENDPOINT = "a3611c7i1de58-ats.iot.ap-southeast-1.amazonaws.com"
    PATH_TO_CERT = "D:\TheControlHub\esp_device_certificate.txt"
    PATH_TO_KEY = "D:\TheControlHub\esp_private_key.txt"
    PATH_TO_ROOT = "D:\TheControlHub\esp_root_credentials.txt"

    IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
    IoTClient.configureEndpoint(ENDPOINT, 8883)
    IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        if IoTClient.connect():
            MQTT_Subscriber(CLIENT_ID)
        else:
            AWS_IoT_Connect(CLIENT_ID) # recursion - trying to re-connect
    except:
        AWS_IoT_Connect(CLIENT_ID) #remove while debugging

#recursive
def MQTT_Subscriber(topic):
    if IoTClient.subscribe(topic, 0, lambda client, userdata, message: {
        image_queue.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                              "Image": Camera_Image_to_Bytes(message)})
    }):
        pass
    else:
        MQTT_Subscriber(topic) #recursion - trying to subscribe again

def Camera_Image_to_Bytes(ImageBytes):
    try:                
        bytes_image = io.BytesIO(ImageBytes.payload)
        Image.LOAD_TRUNCATED_IMAGES = True
        cam_image = Image.open(bytes_image)
        image_byte = io.BytesIO()
        cam_image.save(image_byte, "PNG")
        #print(image_byte.getvalue())
        print(ImageBytes.payload)
        #return image_byte.getvalue() 
    except:
        return None

def get_frame():
    CLIENT_ID = "esp32/cam_0"
    while True:
        AWS_IoT_Connect(CLIENT_ID)
        try:
            message = image_queue.get_nowait()
        except:
            message = None
        if message is not None:
            target_cam = message.get("Target_UI") #returns camera name/number
            cam_image = message.get("Image") #returns image
            #return cam_image
            #return (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + cam_image + b'\r\n')
            break
        return None

print(get_frame())
'''
from AWSIoTPythonSDK import MQTTLib as AWSIoTCam
from PIL import Image

import io
import queue 

class ESP32_CAM_STREAM():
    
    def __init__(self):
        self.AWSIoTClient = None
        self.image_queue = queue.Queue()
        self.CLIENT_ID = "esp32/cam_0"

    def get_frame(self):
        while True:
            self.AWS_IoT_Connect(self.CLIENT_ID)
            try:
                message = self.image_queue.get_nowait()
            except:
                message = None
            if message is not None:
                target_cam = message.get("Target_UI") #returns camera name/number
                cam_image = message.get("Image") #returns image
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + cam_image + b'\r\n')

    #recursive
    def AWS_IoT_Connect(self, CLIENT_ID):
        ENDPOINT = "a3611c7i1de58-ats.iot.ap-southeast-1.amazonaws.com"
        PATH_TO_CERT = "D:\TheControlHub\IoT_Cameras_Certificates\esp_device_certificate.txt"
        PATH_TO_KEY = "D:\TheControlHub\IoT_Cameras_Certificates\esp_private_key.txt"
        PATH_TO_ROOT = "D:\TheControlHub\IoT_Cameras_Certificates\esp_root_credentials.txt"

        self.IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
        self.IoTClient.configureEndpoint(ENDPOINT, 8883)
        self.IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
        try:
            if self.IoTClient.connect():
                self.MQTT_Subscriber(CLIENT_ID)
            else:
                self.AWS_IoT_Connect(CLIENT_ID) # recursion - trying to re-connect
        except:
            self.AWS_IoT_Connect(CLIENT_ID) #remove while debugging

    #recursive
    def MQTT_Subscriber(self, topic):
        if self.IoTClient.subscribe(topic, 0, lambda client, userdata, message: {
            self.image_queue.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                                  "Image": self.Camera_Image_to_Bytes(message)})
        }):
            pass
        else:
            self.MQTT_Subscriber(topic) #recursion - trying to subscribe again

    def Camera_Image_to_Bytes(self, ImageBytes):
        try:                
            bytes_image = io.BytesIO(ImageBytes.payload)
            Image.LOAD_TRUNCATED_IMAGES = True
            cam_image = Image.open(bytes_image)
            image_byte = io.BytesIO()
            cam_image.save(image_byte, "PNG")
            return image_byte.getvalue() 
        except:
            return None

if __name__ == "__main__":
    cam0 =  ESP32_CAM_STREAM()
'''