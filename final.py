import cv2,time

face_cascade = cv2.CascadeClassifier("faceFrontal.txt")
video = cv2.VideoCapture(0)


while True:
    check,frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    
    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 3)
    cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
    cv2.imshow("Capturing Video" , frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
try:
    cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    print("Number of faces detected: " + str(faces.shape[0]))
except:
    a = 0
    print("No faces detected.")

video.release()
cv2.destroyAllWindows()
