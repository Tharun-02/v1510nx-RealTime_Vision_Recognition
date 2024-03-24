import cv2
import cvlib as cv
import urllib.request
import numpy as np
from ultralytics import YOLO
import threading

url='http://192.168.113.75/cam-hi.jpg'
im=None
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key != -1 and key==ord('q'):
            break

            
    cv2.destroyAllWindows()
    
def run2():

    stream_url = url
    cap = cv2.VideoCapture (stream_url)
    #get video dimensions
    frame_width = int (cap.get (cv2.CAP_PROP_FRAME_WIDTH)) 
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Define the codec and create VideoWriter object 
    fourcc= cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter ('output.mp4', fourcc, 30.0, (frame_width, frame_height))
    #initialize the YOLOV8 model here
    model = YOLO('yolov8n.pt')
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        
        results = model(frame, save=True) #working 
        print (results)
        cv2.waitKey(1)
        res_plotted = results[0].plot()
        cv2.imshow("result", res_plotted)

        out.write(res_plotted)
        
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
    
    
def run3():
    cv2.namedWindow("results", cv2.WINDOW_AUTOSIZE)
    model = YOLO('yolov8n.pt')
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        
        results = model(im) #working 
        print (results)
        cv2.waitKey(1)
        res_plotted = results[0].plot()
        cv2.imshow("result", res_plotted)
        
 
        #cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key != -1 and key==ord('q'):
            break

            
    cv2.destroyAllWindows()


if __name__=="__main__":
    run3()
"""     t1 = threading.Thread(target=run1)
    t2 = threading.Thread(target=run3)

    t1.start()
    t2.start() """