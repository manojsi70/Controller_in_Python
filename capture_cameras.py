import cv2

def capture_from_cameras():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    if not cap1.isOpened() or not cap2.isOpened():
        return "Error: Could not open one or both cameras."

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            return "Error: Could not read frames from one or both cameras."
            break

        frame1 = cv2.resize(frame1, (640, 480))
        frame2 = cv2.resize(frame2, (640, 480))
        combined_frame = cv2.hconcat([frame1, frame2])
        cv2.imshow('Combined Frame', combined_frame)

        if cv2.waitKey(1) == 13:
            break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
    return "Success: Captured from both cameras."
