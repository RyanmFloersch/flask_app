import cv2

class VideoCamera(object):
    # start the video
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)

    # end the video
    def __del__(self):
        self.video.release()
    
    # retrieve frames and convert them into jpg and to bytes.
    def get_frame(self):
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
    