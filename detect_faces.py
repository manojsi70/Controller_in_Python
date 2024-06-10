import cv2

def detect_faces():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error: Could not open the camera."

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()

        if not ret:
            return "Error: Could not read frame from the camera."
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cropped_face = frame[y:y+h, x:x+w]
            cv2.imshow('Cropped Face', cropped_face)

        cv2.imshow('Main Frame', frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Success: Detected faces."
