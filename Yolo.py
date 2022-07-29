import cv2
import numpy as np
import picamera
from picamera import PiCamera
from time import sleep


# This function uses the PiCamera to take a photo and stores it in the current directory while returning the filename of the photo taken
def take_pic():
    
    #Open the camera and request access to the MMU
    with PiCamera() as camera:

        camera.resolution = (320,320) #Resolution needed for YOLO model
        
        file_name = 'sample.jpg'
        camera.start_preview()
        sleep(5)
        
        camera.capture(file_name)
        camera.stop_preview()

        return file_name


# This function sets the classes to identify with the yolo model and returns a list of classes names as strings
def SetClasses():
    
    class_file = 'coco.names' #file containing all names
    classes = []

    with open(class_file, 'rt') as f:
        
        classes = f.read().rstrip('\n').split('\n')
        f.close()

    return classes


# Helper function to find the objects in the image that outputs a list of output layers from the YOLO model and returns the Element found, "None" otherwise.
def FindObjects(outputs, img, classes):
    
    #Extract the attributes of the image (which is a numpy array)
    height_target, width_target, channels = img.shape
    
    #Contains width and height
    bounding_box = [] 

    #Contains class IDs
    class_IDs = [] 

    #contains confidence values
    confidences = [] 
    
    #Hpyer parameter to make a determination
    confidence_threshold = 0.5 
    
    #the lower this hyper param. the higher the accuracy
    nms_threshold = 0.3 
    
    #Finds the maximum value of every output from the DNN output layers
    for out in outputs:

        for detection in out:
            
            scores = detection[5:]
            class_ID = np.argmax(scores)
            confidence = scores[class_ID]

            #If model is at least 50% confident
            if confidence > confidence_threshold:
                
                #Save location of object in the image
                w, h = int(detection[2] * width_target),
                int(detection[3] * height_target)

                #Coordinates of center of bounding box
                x, y = int((detection[0]*width_target)-(width_target/2)),
                int((detection[1]*height_target)-(height_target/2))

                bounding_box.append([x,y,w,h])
                class_IDs.append(class_ID)
                confidences.append(float(confidence))

    #Produce bounding boxes and label confidences for detected object
    indices = cv2.dnn.NMSBoxes(bounding_box, confidences, confidence_threshold, nms_threshold)

    #For all detected objects, create the bounding boxes
    for i in indices:
       
        box = bounding_box[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x ,y), (x + w, y + h), (255,0,0), 2)

        detected_classes = []
        detected_classes.append(classes[class_IDs[i]].upper())
        cv2.putText(img, f'{classes[class_IDs[i]].upper()} {int(confidences[i]*100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    try:
        return detected_classes

    except UnboundLocalError:
        return ['None']


# This function initializes the YOLO model for the object recognition and returns the Object found.
def SetModel():

    #Take the picture to pass into ML model
    file_name = take_pic()
    
    #Since we are working with reg. Yolo model, dimensions are 320x320
    width_height_target = 320
    model_config = 'yolov3.cfg'
    model_weights = 'yolov3.weights'
    
    #Add parameters and weights for Neural Network, set computation to be done by CPU
    net = cv2.dnn.readNetFromDarknet(model_config, model_weights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    
    classes = SetClasses()
    img = cv2.imread('sample.jpg')
    
    cv2.imshow('sample', img)
    cv2.waitKey(1)
    
    #Image is a numpy array but model works with Blob object
    blob = cv2.dnn.blobFromImage(img, 1 /255, (width_height_target, width_height_target), [0,0,0], 1, crop = False)
    net.setInput(blob)

    #from the network, obtain the output layers
    layer_names = net.getLayerNames()
    output_names = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(output_names)
    found = FindObjects(outputs, img, classes)
    
    cv2.destroyAllWindows()
    
    return found