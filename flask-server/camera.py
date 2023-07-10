import cv2
import cvlib as cv
# Drawbox draws a box around detected objects
from cvlib.object_detection import draw_bbox


class VideoCamera(object):
    # start the video
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)

    # end the video
    def __del__(self):
        self.video.release()
    
    # retrieve frames and convert them into jpg and to bytes.
    def get_frame(self):
        # read from VideoCameras instance video the frame.
        ret, frame = self.video.read()
            
                
        # detect objects in the frame.
        # bbox sets up border around object.
        # label is the label for the object
        # conf is decimal numbers for object identification
        bbox, label, conf = cv.detect_common_objects(frame)

        # Applies a box to the frame where the detected object is
        output_image = draw_bbox(frame, bbox, label, conf)

        # convert the output_image format to jpg
        ret, jpeg = cv2.imencode('.jpg', output_image)
        # convert jpeg frame to bytes for easier transfer
        return jpeg.tobytes()
    