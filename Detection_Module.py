import cv2
import time

cascade_src = 'dataset/cars1.xml'
video_src = 'dataset/video3.mp4'


#video ....
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)   


while True:
    ret, img = cap.read()
    cv2.imshow('Original', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)
    if (type(img) == type(None)):
        break
    #bluring to have exacter detection
    blurred = cv2.blur(img,ksize=(15,15))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   
        cv2.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),1,(0,255,0),-1)
                        
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
