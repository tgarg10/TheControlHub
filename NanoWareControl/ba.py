CLIENT_ID1 = "esp32/cam_0"
CLIENT_ID2 = "esp32/cam_1"
CLIENT_ID3 = "esp32/cam_2"
CLIENT_ID4 = "esp32/cam_3"
image_queue1 = queue.Queue(maxsize=10)
image_queue2 = queue.Queue(maxsize=10)
image_queue3 = queue.Queue(maxsize=10)
image_queue4 = queue.Queue(maxsize=10)
ENDPOINT = "a3611c7i1de58-ats.iot.ap-southeast-1.amazonaws.com"
PATH_TO_CERT = "esp_device_certificate.txt"
PATH_TO_KEY = "esp_private_key.txt"
PATH_TO_ROOT = "esp_root_credentials.txt"
#################### CAM 1 ####################
#recursive
def AWS_IoT_Connect1():
    global IoTClient1
    IoTClient1 = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID1)
    IoTClient1.configureEndpoint(ENDPOINT, 8883)
    IoTClient1.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        if IoTClient1.connect():
            MQTT_Subscriber1(CLIENT_ID1)
        else:
            AWS_IoT_Connect1(CLIENT_ID1) # recursion - trying to re-connect
    except:
        AWS_IoT_Connect1(CLIENT_ID1) #remove while debugging

#recursive
def MQTT_Subscriber1(topic):
    if IoTClient1.subscribe(topic, 0, lambda client, userdata, message: {
        image_queue1.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                              "Image": Camera_Image_to_Bytes(message)})
    }):
        pass
    else:
        MQTT_Subscriber1(topic) #recursion - trying to subscribe again

def get_frame1():
    AWS_IoT_Connect1()
    while True:    
        try:     
            message = image_queue1.get()
            cam_image = message.get("Image") #returns image
            #target_cam = message.get("Target_UI") #returns camera name/number
            yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + cam_image + b'\r\n')
        except:
            pass

#################### CAM 2 ####################
#recursive
def AWS_IoT_Connect2():
    global IoTClient2
    IoTClient2 = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID2)
    IoTClient2.configureEndpoint(ENDPOINT, 8883)
    IoTClient2.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        if IoTClient2.connect():
            MQTT_Subscriber2(CLIENT_ID2)
        else:
            AWS_IoT_Connect2(CLIENT_ID2) # recursion - trying to re-connect
    except:
        AWS_IoT_Connect2(CLIENT_ID2) #remove while debugging

#recursive
def MQTT_Subscriber2(topic):
    if IoTClient2.subscribe(topic, 0, lambda client, userdata, message: {
        image_queue2.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                              "Image": Camera_Image_to_Bytes(message)})
    }):
        pass
    else:
        MQTT_Subscriber2(topic) #recursion - trying to subscribe again

def get_frame2():
    AWS_IoT_Connect2()
    while True:    
        try:     
            message = image_queue2.get()
            cam_image = message.get("Image") #returns image
            #target_cam = message.get("Target_UI") #returns camera name/number
            yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + cam_image + b'\r\n')
        except:
            pass

#################### CAM 3 ####################
#recursive
def AWS_IoT_Connect3():
    global IoTClient3
    IoTClient3 = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID3)
    IoTClient3.configureEndpoint(ENDPOINT, 8883)
    IoTClient3.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        if IoTClient3.connect():
            MQTT_Subscriber3(CLIENT_ID3)
        else:
            AWS_IoT_Connect3(CLIENT_ID3) # recursion - trying to re-connect
    except:
        AWS_IoT_Connect3(CLIENT_ID3) #remove while debugging

#recursive
def MQTT_Subscriber3(topic):
    if IoTClient3.subscribe(topic, 0, lambda client, userdata, message: {
        image_queue3.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                              "Image": Camera_Image_to_Bytes(message)})
    }):
        pass
    else:
        MQTT_Subscriber3(topic) #recursion - trying to subscribe again

def get_frame3():
    AWS_IoT_Connect3()
    while True:    
        try:     
            message = image_queue3.get()
            cam_image = message.get("Image") #returns image
            #target_cam = message.get("Target_UI") #returns camera name/number
            yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + cam_image + b'\r\n')
        except:
            pass

#################### CAM 4 ####################
#recursive
def AWS_IoT_Connect4():
    global IoTClient4
    IoTClient4 = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID4)
    IoTClient4.configureEndpoint(ENDPOINT, 8884)
    IoTClient4.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        if IoTClient4.connect():
            MQTT_Subscriber4(CLIENT_ID4)
        else:
            AWS_IoT_Connect4(CLIENT_ID4) # recursion - trying to re-connect
    except:
        AWS_IoT_Connect4(CLIENT_ID4) #remove while debugging

#recursive
def MQTT_Subscriber4(topic):
    if IoTClient4.subscribe(topic, 0, lambda client, userdata, message: {
        image_queue4.put({"Target_UI": "_{}_".format(str(message.topic).upper()),
                              "Image": Camera_Image_to_Bytes(message)})
    }):
        pass
    else:
        MQTT_Subscriber4(topic) #recursion - trying to subscribe again

def get_frame4():
    AWS_IoT_Connect4()
    while True:    
        try:     
            message = image_queue4.get()
            cam_image = message.get("Image") #returns image
            #target_cam = message.get("Target_UI") #returns camera name/number
            yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n' + cam_image + b'\r\n')
        except:
            pass

def Camera_Image_to_Bytes(ImageBytes):
    try:                
        bytes_image = io.BytesIO(ImageBytes.payload)
        Image.LOAD_TRUNCATED_IMAGES = True
        cam_image = Image.open(bytes_image)
        image_byte = io.BytesIO()
        cam_image.save(image_byte, "PNG")
        return image_byte.getvalue() 
    except:
        return None
