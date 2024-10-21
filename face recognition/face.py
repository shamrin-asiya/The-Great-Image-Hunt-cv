import cv2 
#to open and access the web cam 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0) # 0 indicates the number of web cam we allow or present in the system
while True:
    _,img = webcam.read() 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.6,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Face Detection",img)
    key = cv2.waitKey(10) #10millieseconds are given 
    if key == 27:
        break
webcam.release() 
cv2.destroyAllWindows() # alrightt all the windows are closed when we press esc
