#importing cv2 and time
import cv2
import time
import numpy

#enabling access to camera for capture
cap=cv2.VideoCapture(0)

#capturing images at an interval of 0.5 seconds
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]

#converting images to grayscale
gr1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gr2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gr3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#finding difference between images
def image_diff(x,y,z):
    dif1=cv2.absdiff(x,y)
    dif2=cv2.absdiff(y,z)
    dif=cv2.bitwise_and(dif1,dif2)
    return dif

while cap.isOpened():
    status,frame=cap.read()
    image=image_diff(gr1,gr2,gr3)
    gr1=gr2
    gr2=gr3
    gr3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('motion',frame)
    cv2.imshow('difference',image)
    print(image)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

    



    

