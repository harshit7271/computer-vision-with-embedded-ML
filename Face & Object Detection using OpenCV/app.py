import cv2

face_cascade = cv2.CascadeClassifier(
    "Face & Object Detection using OpenCV/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    "Face & Object Detection using OpenCV/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(
    "Face & Object Detection using OpenCV/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)
    """"
    detectMultiScale() function detects objects of different sizes in the input image. 
    The detected objects are returned as a list of rectangles.

    """

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        """
        (x,y)- coordinates of the top-left corner of the rectangle
        (x+w, y+h) - coordinates of the bottom-right corner of the rectangle
        
        x - how far from left
        y - how far from top 
        w - width of the face
        h - heigth of the face
        """

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        """"
        assume :
        x = 100
        y = 150
        w = 80
        h = 80
    
        (100,150)
        w = 80 => 100 + 80 = 180
        h = 80 => 150 + 80 = 230
        so by this way we are cropping the face from the original image and storing it in roi_gray and roi_color variable.
        """

        # detect and draw eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # detect and draw smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

        # Lables on full frame
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile Detected", (x, y-30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
