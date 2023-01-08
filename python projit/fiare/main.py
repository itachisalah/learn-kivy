
from playsound import playsound
import cv2


fiare_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)
while (True):

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fiare_cascade.detectMultiScale(frame,1.2,5)
    for (x,y,w,h)in fire:
        roi_gray =gray[y:y+h,x:x+w]
        foi_color= frame[y:y+h ,x:x+w]
        print('FIRE IS detected')
        Playsound('audio.mp3')


    cv2.imshow('Salah', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
