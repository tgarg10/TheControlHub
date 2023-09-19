#from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from NanoWareControl.models import Logs, Moisture_Checker, Tomato_Plant_Height1, Tomato_Plant_Height2, Tomato_Plant_Height3, Greengram_Plant_Height1, Greengram_Plant_Height2, Greengram_Plant_Height3, Plants_Harvest, Seed_Type, Seeds_Sown, Water_Irrigated
#from django.views.decorators import gzip

from AWSIoTPythonSDK import MQTTLib as AWSIoTCam
#from PIL import Image
#import io, queue 
import json, boto3
from imgurpython import ImgurClient
from pytz import timezone
from datetime import datetime, date

imgur = ImgurClient('54cdaf3befe6f96','0e0f207bdcb319256df8189baeb5355f3e4d4753')

'''
CLIENT_ID1 = "esp32/cam_0"
CLIENT_ID2 = "esp32/cam_1"
CLIENT_ID3 = "esp32/cam_2"
CLIENT_ID4 = "esp32/cam_3"
image_queue1 = queue.Queue(maxsize=10)
image_queue2 = queue.Queue(maxsize=10)
image_queue3 = queue.Queue(maxsize=10)
image_queue4 = queue.Queue(maxsize=10)
'''
ENDPOINT = "a3611c7i1de58-ats.iot.ap-southeast-1.amazonaws.com"
PATH_TO_CERT = "esp_device_certificate.txt"
PATH_TO_KEY = "esp_private_key.txt"
PATH_TO_ROOT = "esp_root_credentials.txt"
'''
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
            AWS_IoT_Connect1() # recursion - trying to re-connect
    except:
        AWS_IoT_Connect1() #remove while debugging

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
            AWS_IoT_Connect2() # recursion - trying to re-connect
    except:
        AWS_IoT_Connect2() #remove while debugging

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
            AWS_IoT_Connect3() # recursion - trying to re-connect
    except:
        AWS_IoT_Connect3() #remove while debugging

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
            AWS_IoT_Connect4() # recursion - trying to re-connect
    except:
        AWS_IoT_Connect4() #remove while debugging

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
'''
def home(request):
    return redirect("http://thecontrolhub.com.s3-website-ap-southeast-1.amazonaws.com/")
'''
@gzip.gzip_page
def image_camera1_page(request, stream_path="video"):
    try:
        return StreamingHttpResponse(get_frame1(), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return HttpResponse("Error")

@gzip.gzip_page
def image_camera2_page(request, stream_path="video2"):
    try:
        return StreamingHttpResponse(get_frame2(), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return HttpResponse("Error")

@gzip.gzip_page
def image_camera3_page(request, stream_path="video3"):
    try:
        return StreamingHttpResponse(get_frame3(), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return HttpResponse("Error")

@gzip.gzip_page
def image_camera4_page(request, stream_path="video4"):
    try:
        return StreamingHttpResponse(get_frame4(), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return HttpResponse("Error")
'''
def livecameras(request):
    return redirect("https://s3.ap-southeast-1.amazonaws.com/thecontrolhub-livecamera.com/livecameras.html")

def S3toImgur(CamNum):
    try:
        session = boto3.Session(aws_access_key_id='AKIAZLP6QN2333L7NWOX', aws_secret_access_key='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')
        s3 = session.resource('s3')
        s3.Bucket('thecontrolhub-livecamera.com').download_file('cam%d.png' %CamNum, 'Log.png')
        if CamNum == 1:
            Camera = "Hub Camera 1"
        elif CamNum == 2:
            Camera = "Hub Camera 2"
        elif CamNum == 3:
            Camera = "Irrigator"
        else:
            Camera = "Harvester"
        logs_model = Logs()
        logs_model.image_link = imgur.upload_from_path('Log.png')['id']+'.jpeg'
        today = date.today()
        logs_model.camera = Camera
        logs_model.time = str(datetime.now(tz=timezone("Asia/Singapore")).time())[:8]
        logs_model.date = datetime.strptime(str(today),'%Y-%m-%d').strftime('%b %d')
        logs_model.save()

    except:
        pass

def camera1(request):
    '''
    CLIENT_ID = "cam1_publisher"
    IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
    IoTClient.configureEndpoint(ENDPOINT, 8883)
    IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    '''
    if request.method == 'POST':
        control = ""
        if 'log' in request.POST:
            #control = "log"
            S3toImgur(1)
        #IoTClient.publish("cam1_controls", json.dumps(control), 1) 
    return render(request, "camera1.html", {'prev':'', 'next':'camera2'})

def camera2(request):
    '''
    CLIENT_ID = "cam2_publisher"
    IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
    IoTClient.configureEndpoint(ENDPOINT, 8883)
    IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    '''
    if request.method == 'POST':
        control = ""
        if 'log' in request.POST:
            #control = "log"
            S3toImgur(2)
        #IoTClient.publish("cam2_controls", json.dumps(control), 1) 
    return render(request, "camera2.html", {'prev':'camera1', 'next':''})

def camera3(request):
    CLIENT_ID = "cam3_publisher"
    IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
    IoTClient.configureEndpoint(ENDPOINT, 8883)
    IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        IoTClient.connect()
    except:
        pass
    if request.method == 'POST':
        control = ""
        if 'forward' in request.POST:
            control = 'forward'
        elif 'left' in request.POST:
            control = 'left'
        elif 'stop' in request.POST:
            control = 'stop'
        elif 'right' in request.POST:
            control = 'right'
        elif 'backward' in request.POST:
            control = 'backward'
        elif 'log' in request.POST:
            #control = "log"
            S3toImgur(3)
        IoTClient.publish("cam3_controls", json.dumps(control), 1) 
    return render(request, "camera3.html", {'prev':'camera2', 'next':'camera4'})

def camera4(request):
    CLIENT_ID = "cam4_publisher"
    IoTClient = AWSIoTCam.AWSIoTMQTTClient(CLIENT_ID)
    IoTClient.configureEndpoint(ENDPOINT, 8883)
    IoTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    try:
        IoTClient.connect()
    except:
        pass
    if request.method == 'POST':
        control = ""
        if 'forward' in request.POST:
            control = 'forward'
        elif 'left' in request.POST:
            control = 'left'
        elif 'stop' in request.POST:
            control = 'stop'
        elif 'right' in request.POST:
            control = 'right'
        elif 'backward' in request.POST:
            control = 'backward'
        elif 'log' in request.POST:
            #control = "log"
            S3toImgur(4)
        IoTClient.publish("cam4_controls", json.dumps(control), 1) 
    return render(request, "camera4.html", {'prev':'camera3', 'next':''})

def monitor(request):
    ## new logs ##
    try:
        s3 = boto3.resource(service_name='s3', region_name='ap-southeast-1', aws_access_key_id='AKIAZLP6QN2333L7NWOX', aws_secret_access_key='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')
        s3_logs = s3.Bucket('moisture-bucket').objects.filter(Prefix="moisture_log/")
        logs_list = []
        for log in s3_logs:
            log_body = log.get()['Body'].read()
            log_dict = eval(log_body)
            last_modified = log.get()['LastModified'].replace(tzinfo=timezone('UTC'))
            timestamp = last_modified.astimezone(timezone('Asia/Singapore'))
            log_dict['date'] = timestamp.date()
            logs_list += [log_dict]
        s3_logs.delete()
        for log in logs_list:
            if log['name'] == 'moisture':
                logs_model = Moisture_Checker()
                logs_model.moisture_level = float(log['data'])
            elif log['name'] == 'harvest':
                logs_model = Plants_Harvest()
                logs_model.plants_harvested_count = float(log['data'])
            elif log['name'] == 'sown':
                logs_model = Seeds_Sown()
                logs_model.seed_sown_count = float(log['data'])
            else:
                logs_model = Water_Irrigated()
                logs_model.water_irrigated = float(log['data'])
            logs_model.date = datetime.strptime(str(log['date']),'%Y-%m-%d').strftime('%b %d')
            logs_model.save()
    except:
        pass

    ##### Water-Soil Moisture Line Graph #####
    Model_Moisture_Checker = list(Moisture_Checker.objects.values_list())
    MoistureReadings = []
    MoistureReadingsgraph_waterlabels = []
    IrrigationReadingsgraph_waterlabels = []
    graph_waterlabels = []
    Model_Water_Irrigated = list(Water_Irrigated.objects.all().values_list())
    IrrigationReadings = []

    # matching soil moisture check and water irrigated records by date
    if len(Model_Moisture_Checker) > 0 and len(Model_Water_Irrigated) > 0:
        MoistureReadNumber = -1
        while MoistureReadNumber >= -len(Model_Moisture_Checker) and MoistureReadNumber >= -11:
            MoistureReadings += [[MoistureReadNumber+1, float(Model_Moisture_Checker[MoistureReadNumber][1])]]
            MoistureReadingsgraph_waterlabels += [Model_Moisture_Checker[MoistureReadNumber][2]]       
            MoistureReadNumber -= 1 

        IrrigationReadNumber = -1
        while IrrigationReadNumber >= -len(Model_Water_Irrigated) and IrrigationReadNumber >= -11:
            IrrigationReadings += [[IrrigationReadNumber+1, float(Model_Water_Irrigated[IrrigationReadNumber][1])]]
            IrrigationReadingsgraph_waterlabels += [Model_Water_Irrigated[IrrigationReadNumber][2]]       
            IrrigationReadNumber -= 1 

        graphlabelnum = 0
        while graphlabelnum < len(MoistureReadingsgraph_waterlabels) and graphlabelnum < len(IrrigationReadingsgraph_waterlabels):
            if MoistureReadingsgraph_waterlabels[graphlabelnum] ==  IrrigationReadingsgraph_waterlabels[graphlabelnum]:
                graph_waterlabels += [MoistureReadingsgraph_waterlabels[graphlabelnum]]
            else:
                del MoistureReadings[graphlabelnum:]
                del IrrigationReadings[graphlabelnum:]
            graphlabelnum += 1
        else:
            if len(MoistureReadings) != len(IrrigationReadings):
                if len(MoistureReadings) > len(IrrigationReadings):
                    del MoistureReadings[len(IrrigationReadings):] 
                elif len(MoistureReadings) < len(IrrigationReadings):
                    del IrrigationReadings[len(MoistureReadings):] 
        
        MoistureReadings.reverse()
        IrrigationReadings.reverse()
        graph_waterlabels.reverse()
        graph_waterlabels = ",".join([i for i in graph_waterlabels])

    ##### Seed Type Donut Graph #####
    Model_Seed_Type = list(Seed_Type.objects.all().values_list())
    graph_typelabels = []
    SeedPieChartColors = []
    SeedTypeCount = []

    for SeedType in Model_Seed_Type:
        graph_typelabels += [SeedType[1]]
        SeedPieChartColors += [SeedType[2]]
        SeedTypeCount += [SeedType[3]]

    graph_typelabels = ",".join([i for i in graph_typelabels])
    SeedPieChartColors = ",".join([i for i in SeedPieChartColors])

    ##### Plant Height Bar Graph #####

    ## case 1 ##
    Tomato_Model_Plant_Height1 = list(Tomato_Plant_Height1.objects.all().values_list())
    Greengram_Model_Plant_Height1 = list(Greengram_Plant_Height1.objects.all().values_list())
    TomatoPlantHeightList1 = []
    GreengramPlantHeightList1 = []
    graph_heightlabels = []
    graph_heightlabels2 = []

    heightreading = -1
    while heightreading >= -len(Tomato_Model_Plant_Height1) and heightreading >= -11:
        TomatoPlantHeightList1 += [Tomato_Model_Plant_Height1[heightreading][1]]
        graph_heightlabels2 += [Tomato_Model_Plant_Height1[heightreading][2]]       
        heightreading -= 1 

    heightreading = -1
    while heightreading >= -len(Greengram_Model_Plant_Height1) and heightreading >= -11:
        GreengramPlantHeightList1 += [Greengram_Model_Plant_Height1[heightreading][1]]
        graph_heightlabels += [Greengram_Model_Plant_Height1[heightreading][2]]          
        heightreading -= 1 

    TomatoPlantHeightList1.reverse()
    GreengramPlantHeightList1.reverse()
    graph_heightlabels.reverse()
    graph_heightlabels = ",".join([i for i in graph_heightlabels])
    graph_heightlabels2.reverse()
    graph_heightlabels = ",".join([i for i in graph_heightlabels2])

## case 2 ##
    Tomato_Model_Plant_Height2 = list(Tomato_Plant_Height2.objects.all().values_list())
    Greengram_Model_Plant_Height2 = list(Greengram_Plant_Height2.objects.all().values_list())
    TomatoPlantHeightList2 = []
    GreengramPlantHeightList2 = []
    graph_heightlabels2 = []

    heightreading = -1
    while heightreading >= -len(Tomato_Model_Plant_Height2) and heightreading >= -11:
        TomatoPlantHeightList2 += [Tomato_Model_Plant_Height2[heightreading][1]]
        #graph_heightlabels2 += [Tomato_Model_Plant_Height2[heightreading][2]]       
        heightreading -= 1 

    heightreading = -1
    while heightreading >= -len(Greengram_Model_Plant_Height2) and heightreading >= -11:
        GreengramPlantHeightList2 += [Greengram_Model_Plant_Height2[heightreading][1]]       
        heightreading -= 1 

    TomatoPlantHeightList2.reverse()
    GreengramPlantHeightList2.reverse()
    #graph_heightlabels2.reverse()
    #graph_heightlabels2 = ",".join([i for i in graph_heightlabels2])

    ## case 3 ##
    Tomato_Model_Plant_Height3 = list(Tomato_Plant_Height3.objects.all().values_list())
    Greengram_Model_Plant_Height3 = list(Greengram_Plant_Height3.objects.all().values_list())
    TomatoPlantHeightList3 = []
    GreengramPlantHeightList3 = []
    #graph_heightlabels3 = []

    heightreading = -1
    while heightreading >= -len(Tomato_Model_Plant_Height3) and heightreading >= -11:
        TomatoPlantHeightList3 += [Tomato_Model_Plant_Height3[heightreading][1]]
        #graph_heightlabels3 += [Tomato_Model_Plant_Height3[heightreading][2]]       
        heightreading -= 1 

    heightreading = -1
    while heightreading >= -len(Greengram_Model_Plant_Height3) and heightreading >= -11:
        GreengramPlantHeightList3 += [Greengram_Model_Plant_Height3[heightreading][1]]       
        heightreading -= 1 

    TomatoPlantHeightList3.reverse()
    GreengramPlantHeightList3.reverse()
    #graph_heightlabels3.reverse()
    #graph_heightlabels3 = ",".join([i for i in graph_heightlabels3])

    ##### Yield Ratio #####
    Model_Seeds_Sown = list(Seeds_Sown.objects.all().values_list())
    Model_Plants_Harvested = list(Plants_Harvest.objects.all().values_list())
    Seeds_Sown_Count = []
    Plants_Harvested_Count = []
    graph_yieldlabels = []

    yieldreading = -1
    try:
        while yieldreading >= -len(Model_Plants_Harvested) and yieldreading >= -7:
            Seeds_Sown_Count += [Model_Seeds_Sown[yieldreading][1]]
            Plants_Harvested_Count += [Model_Plants_Harvested[yieldreading][1]]
            graph_yieldlabels += [Model_Seeds_Sown[yieldreading][2]+" - "+Model_Plants_Harvested[yieldreading][2]]       
            yieldreading -= 1 
    except:
        pass    

    Seeds_Sown_Count.reverse()
    Plants_Harvested_Count.reverse()
    graph_yieldlabels.reverse()
    graph_yieldlabels = ",".join([i for i in graph_yieldlabels])

    return render(request, "monitor.html", 
    {
        'soil_moisture':MoistureReadings, 'water_irrigated': IrrigationReadings, 'graph_waterlabels':graph_waterlabels, 
        'seed_types_count': SeedTypeCount, 'seed_pie_colours': SeedPieChartColors, 'graph_typelabels': graph_typelabels,
        'tomato_plant_height1':TomatoPlantHeightList1, 'tomato_plant_height2':TomatoPlantHeightList2, 'tomato_plant_height3':TomatoPlantHeightList3,
        'greengram_plant_height1':GreengramPlantHeightList1, 'greengram_plant_height2':GreengramPlantHeightList2, 'greengram_plant_height3':GreengramPlantHeightList3,
        'graph_heightlabels':graph_heightlabels, 'graph_heightlabels2':graph_heightlabels2,
        'seeds_sown_count':Seeds_Sown_Count, 'plants_harvested_count': Plants_Harvested_Count, 'graph_yieldlabels': graph_yieldlabels,
        'todaySoilMoisture':Model_Moisture_Checker[-1][1],
    })

def logs(request):
    try:
        s3 = boto3.resource(service_name='s3', region_name='ap-southeast-1', aws_access_key_id='AKIAZLP6QN2333L7NWOX', aws_secret_access_key='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')
        s3_logs = s3.Bucket('image-logs-bucket').objects.filter(Prefix="image_log/cam/")
        logs_list = []
        for log in s3_logs:
            log_body = log.get()['Body'].read()
            log_dict = eval(log_body)
            last_modified = log.get()['LastModified'].replace(tzinfo=timezone('UTC'))
            timestamp = last_modified.astimezone(timezone('Asia/Singapore'))
            log_dict['date'] = timestamp.date()
            log_dict['time'] = timestamp.time()
            logs_list += [log_dict]
        s3_logs.delete()
        for log in logs_list:   
            logs_model = Logs()
            logs_model.image_link = log['link'][18:]+'.jpeg'
            logs_model.camera = log['camera']
            logs_model.time = log['time']
            logs_model.date = datetime.strptime(str(log['date']),'%Y-%m-%d').strftime('%b %d')
            logs_model.save()
    except:
        pass

    LogsTuple = list(Logs.objects.all().values_list())
    id = 1
    for LogNum in range(len(LogsTuple)):
        LogsTuple[LogNum] += (id,)
        id += 1
    LogsTuple.reverse() # latest logs at top
    return render(request, "logs.html", {'logstuple':LogsTuple})

def log(request, logid):
    LogsTuple = list(Logs.objects.all().values_list())
    id = 1
    for LogNum in range(len(LogsTuple)):
        LogsTuple[LogNum] += (id,)
        id += 1
    if logid > 0 and logid <= len(LogsTuple): 
        Log = LogsTuple[logid-1] + (logid-1, logid+1)
        return render(request, "log.html", {'log':Log})
    else:
        LogsTuple.reverse() # latest logs at top
        return render(request, "logs.html", {'logstuple':LogsTuple})
