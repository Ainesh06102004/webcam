import cv2

def takesnapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("NewPic1.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


takesnapshot()