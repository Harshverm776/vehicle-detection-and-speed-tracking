import cv2
import time


def Speed_Cal(time):
    # The 9.144 is distance of free space between two lines
    # Found in https://news.osu.edu/slow-down----those-lines-on-the-road-are-longer-than-you-think/
    # We know that the 9.144 is an standard and our video may not be that but its like guess and its need Field research
    try:
        Speed = (9.144 * 3600)/(time * 1000)
        return Speed
    except ZeroDivisionError:
        print (5)

cascade_src = 'dataset/cars1.xml'
video_src = 'dataset/video3.mp4'

# Line a
ax1 = 70
ay = 90
ax2 = 230

# Line b
bx1 = 15
by = 125
bx2 = 225

# Car Number
i = 1
start_time = time.time()

# Video ....
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)   


while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    # Bluring to have exacter detection
    blurred = cv2.blur(img, ksize = (15, 15))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)
    
    # Line a # I know road has got 
    cv2.line(img, (ax1, ay), (ax2, ay), (255, 0, 0), 2)
    # Line b
    cv2.line(img, (bx1, by), (bx2, by), (255, 0, 0), 2)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)   
        cv2.circle(img, (int((x + x + w)/2), int((y + y + h)/2)), 1, (0, 255, 0), -1)
        
        while int(ay) == int((y + y + h)/2):
            start_time = time.time()
            break
            
        while int(ay) <= int((y + y + h)/2):
            if int(by) <= int((y + y + h)/2) & int(by + 10) >= int((y + y + h)/2):
                cv2.line(img, (bx1, by), (bx2, by), (0, 255, 0), 2)
                Speed = Speed_Cal(time.time() - start_time)
                print("Car Number " + str(i) + " Speed: " + str(Speed))
                i = i + 1
                cv2.putText(img, "Speed: " + str(Speed) + "KM/H", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                break
            else :
                cv2.putText(img, "Calcuting", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                break
                
                
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
